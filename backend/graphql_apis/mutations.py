import strawberry
from .inputs import CreateUserInput,HandleRequestInput, SubmitApplicationInput,UpdateInfo,InventoryInput, OrderInput, CancelOrderInput,AddToCartInput, BecomeSellerInput, PaymentInput, LoginInput, OrderInput
from .gql_types import AuthPayload, SignUpResponse, StandardResponse, ListApplications, ProductType
from .resolvers import login_resolver, sumbit_app,del_application,get_product,seller_application, handle_application, product_filter_resolver,get_applications, order_resolver, signup_resolver, upload_product, update_product, delete_product
from .decorators import required_role

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, data: CreateUserInput) -> SignUpResponse:
        return signup_resolver(info, data)
    
    @strawberry.mutation
    def login(self, info, data: LoginInput) -> AuthPayload:
        return login_resolver(info, data)
    
    @strawberry.mutation
    @required_role("seller")
    def upload_product(self, info, data: InventoryInput) -> StandardResponse:
        return upload_product(info, data)

    @strawberry.mutation
    @required_role("seller")
    def update_product(self, info, product_id: int, data: InventoryInput) -> StandardResponse:
        return update_product(info, product_id, data)

    @strawberry.mutation
    @required_role("seller")
    def delete_product(self, info, product_id: int) -> StandardResponse:
        return delete_product(info, product_id)

    @strawberry.mutation
    @required_role("seller", "user")
    def update_profile(self,info,data: UpdateInfo)->StandardResponse:
        user_id = info.context["user"]["sub"]
        return update_info_resolver(info, user_id, data)

    @strawberry.mutation
    @required_role("user")
    def add_to_cart(self,info,data: AddToCartInput) -> StandardResponse:
        user_id = info.context["user"]["sub"]
        return add_to_cart_resolver(info, user_id, data)

    @strawberry.mutation
    @required_role("user")
    def place_order(self,info,data: OrderInput) -> StandardResponse:
        user_id = info.context["user"]["sub"]
        return order_resolver(info, user_id, data)

    @strawberry.mutation
    @required_role("user")
    def start_selling(self, info,data: BecomeSellerInput)-> StandardResponse:
        user_id = info.context["user"]["sub"]
        return seller_application(info, user_id, data)

    @strawberry.mutation
    @required_role("admin")
    def handle_requests(self, info, data:HandleRequestInput)->StandardResponse:
        user_id = info.context["user"]["sub"]
        return handle_application(info, user_id, data)  
    
    @strawberry.mutation
    @required_role("user")
    def cancel_order(self, info, data: CancelOrderInput) -> StandardResponse:
        user_id = info.context["user"]["sub"]
        return cancel_order_resolver(info, user_id, data)
    
    @strawberry.mutation
    @required_role("user")
    def submit_application(self, info, data: SubmitApplicationInput) -> StandardResponse:
        user_id = info.context["user"]["sub"]
        return submit_app(info, user_id, data)
    
    @strawberry.mutation
    @required_role("user","admin")
    def delete_application(self, info, applicant_id: int) -> StandardResponse:
        user_id = info.context["user"]["sub"]
        return del_application(info, user_id, applicant_id)


    
