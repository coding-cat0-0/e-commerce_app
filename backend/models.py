from datetime import datetime, date
from sqlmodel import SQLModel, Field, Relationship
from pydantic import field_validator 
import re
from typing import Optional, List
from enum import Enum

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    email: str = Field(index=True, nullable=False, unique=True)
    password: str = Field(nullable=False)
    role: str = Field(default="user")
    address: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    seller_id:int = Field(foreign_key="user.id", nullable=False)
    name: str = Field(nullable=False)
    description: Optional[str] = None
    type: str = Field(nullable=False)
    price: float = Field(nullable=False)
    quantity: int = Field(default=0, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    order: List["Order"] = Relationship(back_populates="product")
    
class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    product_id: str = Field(foreign_key="product.id",nullable=False)
    total_amount: float = Field(nullable=False)
    is_cancelled: bool = Field(default=False)
    address: str = Field(nullable=False)
    phone_number: str | None = Field(
        default=None,
        max_length=20,
        unique=False,
        index=True
        )
    payment_method: str = Field(foreign_key="payment.payment_method", nullable=False)
    is_payed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    product: "Product" = Relationship(back_populates="order")
    
    @field_validator("phone_number")
    @classmethod
    def validate_phone(cls, ph):
        if ph is None:
            return ph
        if not re.match(r"^\+?[1-9]\d{7,14}$", ph):
            raise ValueError("Invalid phone number format")
        return ph
    
class AddToCart(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)    
    user_id: int = Field(foreign_key="user.id", nullable=False)
    product_id: int = Field(foreign_key="product.id", nullable=False)
    quantity: int = Field(default=1, nullable=False)

class Payment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id", nullable=False)
    amount: float = Field(nullable=False)
    payment_method: str = Field(nullable=False)
    amount_paid: float = Field(nullable=False)
    payment_status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Help(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    email: str = Field(nullable=False)
    message: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow) 

class ApplicationStatus(str,Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    
class SellerApplication(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    business_name: str = Field(nullable=False)
    business_details: str = Field(nullable=False)
    business_address: str = Field(nullable=False)
    contact_email: str = Field(nullable=False)
    contact_phone: str = Field(nullable=False)
    status:str = Field(default=ApplicationStatus.PENDING, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
"""    def request_handler(self):
        if self.status not in ("rejected", "accepted"):
            raise ValueError(f"Invalid status")
        return 
        """
    