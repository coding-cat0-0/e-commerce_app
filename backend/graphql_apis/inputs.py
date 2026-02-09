import strawberry
from typing import Optional
from dataclasses import dataclass
import re
from datetime import date

@strawberry.input
class CreateUserInput:
    email:str
    password:str
    name:str
    address:str| None = None
    
    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e
        
    @classmethod
    def password_must_be_strong(cls, p):
             if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*^_-])[A-Za-z\d!@#$%^&_*-]{8,}$",p):
                 raise ValueError("Invalid Password")
             else:
                    return p
                
                
@strawberry.input
class InventoryInput:
    name: str
    description: Optional[str] = None
    price: float = 0.0
    quantity: int = 0
    
    @classmethod
    def validate_phone(cls, ph):
        if ph is None:
            return ph
        if not re.match(r"^\+?[1-9]\d{7,14}$", ph):
            raise ValueError("Invalid phone number format")
        return ph
    
@strawberry.input
class AddToCartInput:
    quantity: int
    
@strawberry.input
class PaymentInput:
    method: str
    amount: float
    status: str
    amountPaid: float
    
    def __post_init__(self):
        if self.amountPaid > self.amount:
            raise ValueError("Amount paid cannot exceed total amount")

    @classmethod
    def method_must_be_valid(cls, m):
        valid_methods = ["credit_card", "debit_card", "paypal", "bank_transfer"]
        if m not in valid_methods:
            raise ValueError(f"Invalid payment method. Choose from {valid_methods}")
        return m    
        
@strawberry.input
class LoginInput:
    email: str
    password: str


    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e

    @classmethod
    def password_must_be_strong(cls, p):
             if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*^_-])[A-Za-z\d!@#$%^&_*-]{8,}$",p):
                 raise ValueError("Invalid Password")
             else:
                    return p
                
    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e

    @classmethod
    def password_must_be_strong(cls, p):
             if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*^_-])[A-Za-z\d!@#$%^&_*-]{8,}$",p):
                 raise ValueError("Invalid Password")
             else:
                    return p
@strawberry.input
class HelpInput:
    name: str
    email: str
    message: str      
    
@strawberry.input
class UpdateInfo:
    name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    

    @classmethod
    def email_must_be_valid(cls, e):    
        if e is not None and not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e
              
@strawberry.input
class AddCartInput:
    product_id: int
    quantity: int 
                 
@strawberry.input
class OrderInput:
    product_id: int
    total_amount: float
    address: str
    phone_number: str
    payment_method: str
    is_cancelled: bool = False
    is_payed: bool
    

    @classmethod
    def validate_phone(cls, ph):
        if ph is None:
            return ph
        if not re.match(r"^\+?[1-9]\d{7,14}$", ph):
            raise ValueError("Invalid phone number format")
        return ph                 
    
@strawberry.input
class BecomeSellerInput:
    business_name: str
    business_details: str
    business_address: str
    contact_email: str
    contact_phone: str
    

    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e    
        
    @classmethod
    def validate_phone(cls, ph):
        if not re.match(r"^\+?[1-9]\d{7,14}$", ph):
            raise ValueError("Invalid phone number format")
        return ph    
    
@strawberry.input
class HandleRequestInput:
    application_id: int
    action: str  # "accept" or "reject"
    
    @classmethod
    def action_must_be_valid(cls, a):
        valid_actions = ["accepted", "rejected"]
        if a not in valid_actions:
            raise ValueError(f"Invalid action. Choose from {valid_actions}")
        return a
    
@strawberry.input
class ProductFilterInput:
    filter_by: str 
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    category: Optional[str] = None
    latest: Optional[date] = None
    popular: Optional[bool] = False
    oldest: Optional[date] = None
    
    @classmethod
    def validate_prices(cls, min_p, max_p):
        if min_p is not None and max_p is not None and min_p > max_p:
            raise ValueError("min_price cannot be greater than max_price")
        if min_p is not None and min_p < 0:
            raise ValueError("min_price cannot be negative")
        if max_p is not None and max_p < 0:
            raise ValueError("max_price cannot be negative")
        return min_p, max_p
    
    @classmethod
    def validate_filter_by(cls, f):
        valid_filters = ["price_range", "category", "by_date", "popular",]
        if f not in valid_filters:
            raise ValueError(f"Invalid filter_by. Choose from {valid_filters}")
        return f
    @classmethod
    def validate_dates(cls, latest, oldest):
        if latest is not None and oldest is not None and latest < oldest:
            raise ValueError("latest date cannot be earlier than oldest date")
        if latest > date.today():
            raise ValueError("latest date cannot be in the future")
        
        return latest, oldest

    
@strawberry.input
class CancelOrderInput:
    order_id: int       
    
@strawberry.input
class SubmitApplicationInput:
    business_name: str
    business_details: str
    business_address: str
    contact_email: str
    contact_phone: str
    

    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e