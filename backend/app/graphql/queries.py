import strawberry
from .types import ProductType, ListApplications
from .resolvers import get_product, list_products, get_applications, get_product_by_type
from .decorators import required_role


@strawberry.type
class Query:

    @required_role("seller", "user", "admin")
    @strawberry.field
    def get_product(self, info, product_id: int) -> ProductType:
        return get_product(info, product_id)

    @required_role("seller", "user", "admin")
    @strawberry.field
    def all_products(self, info) -> list[ProductType]:
        return list_products(info)


    @strawberry.mutation
    @required_role("seller","user","admin")
    def get_type(self, info, data):
        return get_product_by_type(info, data)
    
    @required_role("admin")
    @strawberry.field
    def get_all_applications(self, info) -> list[ListApplications]:
        return get_applications(info)
