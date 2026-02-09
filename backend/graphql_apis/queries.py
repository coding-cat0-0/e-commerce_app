import strawberry
from .gql_types import ProductType, ListApplications
from .resolvers import get_product, list_products, get_applications, search_products ,get_apps ,view_orders,get_product_by_type, product_filter_resolver
from .decorators import required_role
from .inputs import ProductFilterInput

@strawberry.type
class Query:

    @strawberry.field
    @required_role("seller", "user", "admin")
    def get_product(self, info, product_id: int) -> ProductType:
        return get_product(info, product_id)

    @strawberry.field
    @required_role("seller", "user", "admin")
    def all_products(self, info) -> list[ProductType]:
        return list_products(info)

    @strawberry.field
    @required_role("seller","user","admin")
    def get_type(self, info, data:str)-> ProductType:
        return get_product_by_type(info, data)
    
    @strawberry.field
    @required_role("admin")
    def get_all_applications(self, info) -> list[ListApplications]:
        return get_applications(info)
    
    @strawberry.field
    @required_role("user","seller","admin")
    def filter_products(self, info, data: ProductFilterInput) -> list[ProductType]:
        return product_filter_resolver(info, data)

    @strawberry.field
    @required_role("user","seller","admin")
    def view_orders(self, info) -> list[ProductType]:
        return view_orders(info)

    @strawberry.field
    @required_role("user")
    def get_applications(self, info) -> list[ListApplications]:
        user_id = info.context["user"]["sub"]
        return get_apps(info, user_id)
    @strawberry.field
    @required_role("user")
    def search_for_products(self, info, prod_type: str) -> list[ProductType]:
        return search_products(info, prod_type)