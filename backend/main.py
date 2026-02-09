from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from core.logging import logging_middleware
from graphql_apis.schema import schema
from graphql_apis.context import get_context
from database import engine
from sqlmodel import SQLModel
from fastapi import Request
app = FastAPI()
# CORS (same as REST)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# GraphQL router
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    graphql_ide="apollo-sandbox",
)

app.include_router(graphql_app, prefix="/graphql")

@app.on_event("startup")
def on_startup() -> None:
    SQLModel.metadata.create_all(engine)
    
@app.middleware("http")
async def log_requests(request: Request, call_next):
    return await logging_middleware(request, call_next)

@app.middleware("http")
async def debug_body(request: Request, call_next):
    body = await request.body()
    if body:
        print(f"DEBUG BODY: {body.decode()}")
    # Recreate the request with the original body for downstream
    async def receive():
        return {"type": "http.request", "body": body}
    request._receive = receive
    return await call_next(request)

