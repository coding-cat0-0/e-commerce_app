from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from .graphql.schema import schema
from .graphql.context import get_context

app = FastAPI()

# CORS (same as REST)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GraphQL router
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context
)

@app.middleware("http")
async def log_requests(request, call_next):
    return await logging_middleware(request, call_next)

app.include_router(graphql_app, prefix="/graphql")
