import strawberry

from .inputs import SignupInput, UpdateInfo,InventoryInput, OrderInput, AddToCartInput, BecomeSellerInput, PaymentInput, LoginInput, OrderInput
from .types import AuthPayload, SignUpResponse, StandardResponse, ListApplications, ProductType
from .resolvers import login_resolver, get_product,seller_application, handle_application, get_applications, order_resolver, signup_resolver, upload_product, update_product, delete_product
from .decorators import required_role

@strawberry.type
class Mutation:
    @strawberry.mutation
    def signup(self, info, data: SignupInput) -> SignUpResponse:
        return signup_resolver(info, data)
    
    @strawberry.mutation
    def login(self, info, data: LoginInput) -> AuthPayload:
        return login_resolver(info, data)
    
    @strawberry.mutation
    @required_role("seller")
    def upload_product(self, info, data: InventoryInput) -> UploadProductResponse:
        return upload_product(info, data)

    @strawberry.mutation
    @required_role("seller")
    def update_product(self, info, product_id: int, data: InventoryInput) -> UploadProductResponse:
        return update_product(info, product_id, data)

    @strawberry.mutation
    @required_role("seller")
    def delete_product(self, info, product_id: int) -> UploadProductResponse:
        return delete_product(info, product_id)

    @strawberry.mutation
    @required_role("seller", "user")
    def update_profile(self,info,data: UpdateInfo)->UpdateInfoResponse:
        user_id = info.context["user"]["sub"]
        return update_info_resolver(info, user_id, data)

    @strawberry.mutation
    @required_role("user")
    def add_to_cart(self,info,data: AddToCartInput):
        user_id = info.context["user"]["sub"]
        return add_to_cart_resolver(info, user_id, data)


    @strawberry.mutation
    @required_role("user")
    def place_order(self,info,data: OrderInput):
        user_id = info.context["user"]["sub"]
        return order_resolver(info, user_id, data)

    @strawberry.mutation
    @required_role("user")
    def start_selling(self, info,data: BecomeSellerInput):
        user_id = info.context["user"]["sub"]
        return seller_application(user_id, data)

    @strawberry.mutation
    @required_role("admin")
    def handle_requests(self, info, data)->StandardResponse:
        user_id = info.context["user"]["sub"]
        return handle_application(info, user_id, data)
