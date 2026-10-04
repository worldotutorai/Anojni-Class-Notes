import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from fastapi import FastAPI,HTTPException
from pydantic import Field,EmailStr,BaseModel
from typing import List,Optional

load_dotenv()
neondb_url=os.getenv("NEON_ECOMMERCE_DATABASE_URL")


if not neondb_url:
    raise "Database URL Not found"

engine= create_engine(neondb_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# users table
'''
CREATE TABLE users (
id SERIAL PRIMARY KEY,
user_name VARCHAR(100) NOT NULL,
email VARCHAR(150) UNIQUE NOT NULL,
phone_number VARCHAR(20) CHECK (phone_number ~ '^\+?[0-9\s\-()]+$'),
address VARCHAR(255),
created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''

app= FastAPI()
class CreateUser(BaseModel):
    user_name:str
    email:EmailStr
    phone_number:str
    address: str


@app.post("/create_user")
def create_user(user:CreateUser):
    session=SessionLocal()
    try:
        query=text("INSERT INTO users (user_name,email,phone_number,address) VALUES (:user_name,:email,:phone_number,:address)")
        session.execute(query,{"user_name":user.user_name,"email":user.email,"phone_number":user.phone_number,"address":user.address})
        session.commit()
        return {"message":f"user {user.user_name} name is added successfully to database","user":user}
    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }
    finally:
        session.close()

@app.get("/get_all_user")
def get_all_user():
    session= SessionLocal()
    try:
        users_list=[]
        query = text("SELECT *from users")
        result= session.execute(query)
        users=result.fetchall()
        if not users:
            raise HTTPException(
                status_code=404,
                detail="users not found"
            )
        for users in users:
            users_list.append({
            "user_id":  users.id,
            "name":  users.user_name,
            "email": users.email,
            "phone_number":users.phone_number,
            "address": users.address
            })
        return {
            "message": "User information",
            "students":users_list
        }
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()


# get user based on userid
@app.get("/users/{user_id}")
def get_user(user_id:int):
    session=SessionLocal()
    try:
        query= text("SELECT * FROM users WHERE id = :id")
        result= session.execute(query,{"id":user_id})
        user = result.fetchone()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="user not found"
            )
        return {
            "message": "User info",
            "user": dict(user._mapping)
        }
    finally:
        session.close()

class UserUpdate(BaseModel):   
    user_name: str | None = Field(default=None)
    email: EmailStr | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    address: str | None = Field(default=None)     

    
@app.patch("/update_user/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM users WHERE id = :id")
        result = session.execute(query, {"id": user_id})
        user = result.fetchone()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        
        update_data =user_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(
                status_code=400,
                detail="No fields provided for update"
            )

        # update the field provided by the user
        set_clause=", ".join([f"{field} = :{field}" for field in update_data.keys()])
        update_query = text(f"""
            UPDATE users
            SET {set_clause}
            WHERE id = :id
        """)
        
        session.execute(update_query, {**update_data, "id": user_id})
        session.commit()
        
        return {
            "message": f"User with ID {user_id} updated successfully",
            "updated_fields": update_data
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }
    finally:
        session.close()

# delete user based on user id
@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM users WHERE id = :id")
        result = session.execute(query, {"id": user_id})
        user = result.fetchone()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        
        delete_query = text("DELETE FROM users WHERE id = :id")
        session.execute(delete_query, {"id": user_id})
        session.commit()
        
        return {
            "message": f"User with ID {user_id} deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }
    finally:
        session.close()



# products table
'''
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  product_name VARCHAR(100) NOT NULL,
  category VARCHAR(50) NOT NULL,
  is_available BOOLEAN NOT NULL DEFAULT TRUE,
  quantity INT NOT NULL CHECK (quantity >= 0),
  price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''

class CreateProduct(BaseModel):
    product_name: str
    category: str
    is_available: bool = True
    quantity: int
    price: float
    description: str | None = None

# add product to the database
@app.post("/create_product")
def create_product(product: CreateProduct):
    session = SessionLocal()
    try:
        query = text("""
            INSERT INTO products (product_name, category, is_available, quantity, price, description)
            VALUES (:product_name, :category, :is_available, :quantity, :price, :description)
        """)
        session.execute(query, {
            "product_name": product.product_name,
            "category": product.category,
            "is_available": product.is_available,
            "quantity": product.quantity,
            "price": product.price,
            "description": product.description
        })
        session.commit()
        return {"message": f"Product {product.product_name} added successfully", "product": product}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()

# get all products from the database
@app.get("/get_all_products")
def get_all_products():
    session = SessionLocal()
    try:
        products_list = []
        query = text("SELECT * FROM products")
        result = session.execute(query)
        products = result.fetchall()
        if not products:
            raise HTTPException(
                status_code=404,
                detail="No products found"
            )
        for product in products:
            products_list.append({
                "product_id": product.id,
                "product_name": product.product_name,
                "category": product.category,
                "is_available": product.is_available,
                "quantity": product.quantity,
                "price": float(product.price),
                "description": product.description
            })
        return {
            "message": "Product information",
            "products": products_list
        }
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()

# get product based on product id
@app.get("/products/{product_id}")
def get_product(product_id: int):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM products WHERE id = :id")
        result = session.execute(query, {"id": product_id})
        product = result.fetchone()
        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        return {
            "message": "Product info",
            "product": dict(product._mapping)
        }
    finally:
        session.close()


# update product based on product id
class ProductUpdate(BaseModel):
    product_name: str=Field(default=None)
    category: str= Field(default=None)
    is_available: bool = Field(default=None)
    quantity: int= Field(default=None)
    price: float = Field(default=None)
    description: str=Field(default=None)

@app.patch("/update_product/{product_id}")
def update_product(product_id: int, product_update: ProductUpdate):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM products WHERE id = :id")
        result = session.execute(query, {"id": product_id})
        product = result.fetchone()
        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        
        update_data = product_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(
                status_code=400,
                detail="No fields provided for update"
            )

        # update the field provided by the user
        set_clause = ", ".join([f"{field} = :{field}" for field in update_data.keys()])
        update_query = text(f"""
            UPDATE products
            SET {set_clause}
            WHERE id = :id
        """)
        
        session.execute(update_query, {**update_data, "id": product_id})
        session.commit()
        
        return {
            "message": f"Product with ID {product_id} updated successfully",
            "updated_fields": update_data
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()

# delete product based on product id
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM products WHERE id = :id")
        result = session.execute(query, {"id": product_id})
        product = result.fetchone()
        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        
        delete_query = text("DELETE FROM products WHERE id = :id")
        session.execute(delete_query, {"id": product_id})
        session.commit()
        
        return {
            "message": f"Product with ID {product_id} deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()



# orders table
'''
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
  status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled'))
)
'''

# user can place an order for products
class PlaceOrder(BaseModel):
    user_id: int
    product_ids: List[int]
    quantity: int = Field(gt=0, description="Quantity must be greater than 0")
    status: List[str] = Field(default=["pending", "shipped", "delivered", "cancelled"])

@app.post("/place_order")
def place_order(place_order: PlaceOrder):
    session= SessionLocal()
    

# order items table
'''
CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INT REFERENCES orders(id),
  product_id INT REFERENCES products(id),
  quantity INT NOT NULL CHECK (quantity > 0),
  unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
  total_price DECIMAL(10, 2) NOT NULL CHECK (total_price >= 0)
'''


# get all orders from the database
@app.get("/get_all_orders")
def get_all_orders():
    session = SessionLocal()
    try:
        orders_list = []
        query = text("SELECT * FROM orders")
        result = session.execute(query)
        orders = result.fetchall()
        if not orders:
            raise HTTPException(
                status_code=404,
                detail="No orders found"
            )
        for order in orders:
            orders_list.append({
                "order_id": order.id,
                "user_id": order.user_id,
                "order_date": order.order_date,
                "total_amount": float(order.total_amount),
                "status": order.status
            })
        return {
            "message": "Order information",
            "orders": orders_list
        }
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()


# view their orders user_id
@app.get("/user_orders/{user_id}")
def get_user_orders(user_id: int):
    session = SessionLocal()
    try:
        # Check if user exists
        user_query = text("SELECT * FROM users WHERE id = :id")
        user_result = session.execute(user_query, {"id": user_id})
        user = user_result.fetchone()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        
        orders_list = []
        query = text("SELECT * FROM orders WHERE user_id = :user_id")
        result = session.execute(query, {"user_id": user_id})
        orders = result.fetchall()
        if not orders:
            raise HTTPException(
                status_code=404,
                detail="No orders found for this user"
            )
        for order in orders:
            orders_list.append({
                "order_id": order.id,
                "order_date": order.order_date,
                "total_amount": float(order.total_amount),
                "status": order.status
            })
        return {
            "message": f"Orders for user ID {user_id}",
            "orders": orders_list
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()


# update product inventory based on product id
@app.patch("/update_product_inventory/{product_id}")
def update_product_inventory(product_id: int, quantity: int):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM products WHERE id = :id")
        result = session.execute(query, {"id": product_id})
        product = result.fetchone()
        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        
        if quantity < 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity cannot be negative"
            )

        update_query = text("""
            UPDATE products
            SET quantity = :quantity
            WHERE id = :id
        """)
        
        session.execute(update_query, {"quantity": quantity, "id": product_id})
        session.commit()
        
        return {
            "message": f"Product inventory for ID {product_id} updated successfully",
            "new_quantity": quantity
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()


# cancel order based on order id
@app.patch("/cancel_order/{order_id}")
def cancel_order(order_id: int):
    session = SessionLocal()
    try:
        query = text("SELECT * FROM orders WHERE id = :id")
        result = session.execute(query, {"id": order_id})
        order = result.fetchone()
        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )
        
        if order.status == "cancelled":
            raise HTTPException(
                status_code=400,
                detail="Order is already cancelled"
            )

        update_query = text("""
            UPDATE orders
            SET status = 'cancelled'
            WHERE id = :id
        """)
        
        session.execute(update_query, {"id": order_id})
        session.commit()
        
        return {
            "message": f"Order with ID {order_id} has been cancelled successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()


