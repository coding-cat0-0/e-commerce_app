from strawberry.exceptions import GraphQLError
from functools import wraps
def required_role(info, *req_role):
        def decorator(resolver):
            @wraps(resolver)
            def wrapper(*args, **kwargs):
                info = args[1]
                user = info.context.get("user")
                if not user:
                    raise GraphQLError("User not found")
                
                if user["role"] not in req_role:
                    raise GraphQLError("User Unauthorized")
                return resolver(*args, **kwargs)
            return wrapper
        return decorator 