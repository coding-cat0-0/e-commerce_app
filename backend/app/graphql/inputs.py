import strawberry
from typing import Optional
from dataclasses import dataclass
import re

@strawberry.input
class CreateUserInput:
    email:str
    password:str
    name:str
    address:str| None = None
    
    @strawberry.validator("email")
    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e
    @strawberry.validator("password")
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
    
    
    @strawberry.validator("phoneNumber")
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
        
    @strawberry.validator("method")
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

    @strawberry.validator("email")
    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e
    @strawberry.validator("password")
    @classmethod
    def password_must_be_strong(cls, p):
             if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*^_-])[A-Za-z\d!@#$%^&_*-]{8,}$",p):
                 raise ValueError("Invalid Password")
             else:
                    return p

@strawberry.input
class SignupInput:
    email: str
    password: str
    name: str
    address: str | None = None
    
    @strawberry.validator("email")
    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e
    @strawberry.validator("password")
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
    
    @strawberry.validator("email")
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
    
    @strawberry.validator("phone_number")
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
    
    @strawberry.validator("contact_email")
    @classmethod
    def email_must_be_valid(cls, e):    
        if not re.search(r"\w+@(\w+\.)?\w+\.(com)$",e, re.IGNORECASE):
            raise ValueError("Invalid email format")
        else:
            return e    
        
    @strawberry.validator("contact_phone")
    @classmethod
    def validate_phone(cls, ph):
        if not re.match(r"^\+?[1-9]\d{7,14}$", ph):
            raise ValueError("Invalid phone number format")
        return ph    