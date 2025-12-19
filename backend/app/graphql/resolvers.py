from auth.auth_handler import create_access_token
from .types import AuthPayload, SignUpResponse, StandardResponse, ProductType, ListApplications, ListUserOrders
from auth.jwt_auth import check_hashed_password
from models import User, Product, Order, AddToCart, Payment, SellerApplication
from sqlmodel import select


def signup_resolver(info,data):
    session = info.context["session"]
    user = session.exec(select(User).where(User.email == data.email)).first()
    if user:
        raise Exception("User already exists")
    hashed_password = hash_password(data.password)
    new_user = User(name = data.name, email=data.email, password=hashed_password, address=data.address)
    session.add(new_user)
    session.commit()
 
    return SignUpResponse(message = "User created successfully")

def login_resolver(info, data) -> AuthPayload:
    session = info.context["session"]
    user = session.exec(select(User).where(User.email == data.email)).first()
    
    if not user or not check_hashed_password(data.password, user.password):
        raise Exception("Invalid credentials")

    token = create_access_token(user_id=user.id, role = user.role, expiretime=60)
    return AuthPayload(access_token=token)

def upload_product(info, data):
    session = info.context["session"]
    new_product = Product(
        name=data.name,
        description=data.description,
        type=data.type,
        price=data.price,
        quantity=data.quantity
    )
    session.add(new_product)
    session.commit()
    return StandardResponse( message="Product uploaded successfully")

def update_product(info, product_id, data):
    session = info.context["session"]
    product = session.get(Product, product_id)
    if not product:
        raise Exception("Product not found")
    
    product.name = data.name
    product.description = data.description
    product.type = data.type
    product.price = data.price
    product.quantity = data.quantity
    
    session.commit()
    return StandardResponse(message="Product updated successfully")

def delete_product(info, product_id):
    session = info.context["session"]
    product = session.get(Product, product_id)
    if not product:
        raise Exception("Product not found")
    
    session.delete(product)
    session.commit()
    return StandardResponse( message="Product deleted successfully")

def list_products(info):
    session = info.context["session"]
    products = session.exec(select(Product)).all()
    return [ProductType(
        id=product.id,
        name=product.name,
        description=product.description,
        product_type=product.type,
        price=product.price,
        quantity=product.quantity
    ) for product in products]

def get_product(info, product_id):
    session = info.context["session"]
    product = session.get(Product, product_id)
    if not product:
        raise Exception("Product not found")
    
    return ProductType(
        id=product.id,
        name=product.name,
        description=product.description,
        product_type=product.type,
        price=product.price,
        quantity=product.quantity
    )    
def get_product_by_type(info, data):
    session = info.context["session"]
    products = session.exec(select(Product).where(Product.type == data.type)).all()
    return [ProductType(
        id=product.id,
        name=product.name,
        description=product.description,
        product_type=product.type,
        price=product.price,
        quantity=product.quantity
    ) for product in products]
    
def update_info_resolver(info, user_id, data):
    session = info.context["session"]
    user = session.get(User, user_id)
    if not user:
        raise Exception("User not found")
    
    user.name = data.name
    user.address = data.address
    user.email = data.email
    session.commit()
    return UpdateInfoResponse(message = "User information updated successfully")

def add_to_cart(info, user_id, product_id, data):
    session = info.context["session"]
    product = session.get(Product, product_id)
    if not product:
        raise Exception("Product not found")
    
    cart_item = session.exec(
        select(AddToCart).where(
            (AddToCart.user_id == user_id) & (AddToCart.product_id == product_id)
        )
    ).first()
    
    if cart_item:
        cart_item.quantity += data.quantity
    else:
        cart_item = AddToCart(
            user_id=user_id,
            product_id=product_id,
            quantity=data.quantity
        )
        session.add(cart_item)
    
    session.commit()
    return CartUpdateResponse(
        message="Product added to cart successfully"
        )

def order_resolver(info, user_id, data):
    session = info.context["session"]
    product = session.get(Product, data.product_id)
    if not product:
        raise Exception("Product not found")
    
    if product.quantity < data.quantity:
        raise Exception("Insufficient product quantity")
    
    total_amount = product.price * data.quantity
    new_order = Order(
        user_id=user_id,
        product_id=data.product_id,
        total_amount=total_amount,
        address=data.address,
        phone_number=data.phone_number
    )
    method = Payment(
        order_id=new_order.id,
        payment_method=data.payment_method,
        amount=total_amount,
        amount_paid=data.amount_paid
    )
    if method.payment_method == "Cash on Delivery":
        new_order.is_payed = False
        method.status = "pending"
    else:
        # functionality for other payment methods can be added here
        new_order.is_payed = True
        method.status = "completed"
        
    product.quantity -= data.quantity
    session.add(new_order)
    session.commit()

    return OrderResponse(order_id=new_order.id, message="Order placed successfully")

def seller_application(info,user_id, data):
    session = info.context["session"]
    user = session.get(User, user_id)
    if not user:
        raise Exception("User not found")
    
    application = SellerApplication(
        user_id=user_id,
        business_name=data.business_name,
        business_details=data.business_details,
        business_address=data.business_address,
        contact_email=data.contact_email,
        contact_phone=data.contact_phone
    )
    session.add(application)
    session.commit()
    return StandardResponse(message="Seller application submitted successfully. We will respond to your application shortly")

def handle_application(info, applicant_id, data):
    
    session = info.context["session"]
    application = session.exec(select(SellerApplication).where(user_id == applicant_id)).first()
    if not applicant:
        raise Exception("The application is no longer available maybe the applicant deleted it")
    if data.status == "rejected":
        application.status = "rejected"
    else:
        application.status = "accepted"
    
    return  StandardResponse(f"You have approved application of applicant ID: {applicant_id}")

def get_applications(info):
    session = info.context["session"]
    applications = session.exec(select(SellerApplication)).all()

    
    if not applications:
        return Exception("No applications yet")
    
    return [ListApplications(
    user_id = applications.user_id,
    business_name = applications.business_name,
    address= applications.business_address,
    email= applications.contact_email,
    number = applications.contact_phone
    ) for application in applications]
    
def view_orders(info):
    
    role = info.context["user"]["role"]
    user_id = info.context["user"]["sub"]
    
    if role == "user":
        orders = session.exec(select(Order).where(user_id == user_id)).all()
        p = session.exec(select(Product).where(id = orders.product_id)).first()
        return [ListUserOrders(product= p.name,
                t_amount = orders.total_amount,
                is_cancelled = orders.is_cancelled,
                address = orders.address,
                number = orders.phone_number,
                payed=orders.is_payed)for order in orders]
    
    elif role == "seller":
        orders = session.exec(select(Order).where(user_id == user_id)).all()
        p = session.exec(select(Product).where(id = orders.product_id)).first()
        return [ListUserOrders(product= p.name,
                t_amount = orders.total_amount,
                is_cancelled = orders.is_cancelled,
                address = orders.address,
                number = orders.phone_number,
                payed=orders.is_payed)for order in orders]
    
    
    
    
    
