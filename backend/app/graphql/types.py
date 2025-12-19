import strawberry
from typing import Optional

@strawberry.type
class SignUpResponse:
    message: str

@strawberry.type
class AuthPayload:
    access_token: str
    token_type: str = "bearer"
    
@strawberry.type
class ProductType:
    id: int
    name: str
    description: Optional[str]
    product_type: str
    price: float
    quantity: int
    
"""@strawberry.type
class UploadProductResponse:
    product: ProductType
    message: str    
    
@strawberry.type
class UpdateInfoResponse:
    message: str    
    
@strawberry.type
class CartUpdateResponse:
    message: str    
    
@strawberry.type
class OrderResponse:    
    order_id: int
    message: str """
@strawberry.type
class StandardResponse:
    message:str
@strawberry.type
class ListApplications:
    user_id:int
    business_name:str
    address: str
    email:str
    number:str
    
@strawberry.type
class ListUserOrders:
    product=str
    t_amount = float
    is_cancelled = bool
    address = str
    number = str
    payed=bool
    
        
        