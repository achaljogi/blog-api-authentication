from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from hashing import hash_password
from hashing import verify_password

from database import Base, engine, get_db
import models
import schemas
import hashing

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message" : "Blog API Running"  
    }

@app.post("/register")
def register(user: schemas.UserCreate,
             db : Session = Depends(get_db)):
    
    new_user = models.User(
        username = user.username,
        email = user.email,
        password=hashing.hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message" : "User Registered Successfully"}

@app.post("/login")
def login(user: schemas.UserLogin,
          db: Session = Depends(get_db)):
    
    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    print("Input Email:", user.email)
    print("DB User:", db_user)
    
    if not db_user:
        return {"message" : "Invalid Email or Password"}
    
    print("Input Pasword:", user.password)
    print("DB User:", db_user)
    
    if not hashing.verify_password(
            user.password,
            db_user.password):
        return {"message" : "Invalid Email or Password"}
    
    return {"message" : "Login Successful"}

@app.post("/blogs")
def create_blog(
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db)
):
    new_blog = models.Blog(
        title=blog.title,
        content=blog.content,
        user_id=1
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return {
        "message" : "Blog created successsfully"
    }

@app.get("/blogs")
def get_blogs(
    db: Session = Depends(get_db)
):
    blogs = db.query(models.Blog).all()

    return blogs

@app.get("/blogs/{id}")
def get_blog(
    id: int,
    db: Session = Depends(get_db)
):
    blog = db.query(models.Blog).filter(
        models.Blog.id == id  
    ).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )
    
    return blog 

@app.put("/blogs/{id}")
def update_blog(
    id: int,
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db)
):
    db_blog = db.query(models.Blog).filter(
        models.Blog.id == id
    ).first()

    if not db_blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )
    
    db_blog.title = blog.title
    db_blog.content = blog.content

    db.commit()

    return {
        "Message" : "Blog updated successfully"
    }

@app.delete("/blogs/{id}")
def delete_blog(
    id: int,
    db: Session = Depends(get_db)
):
    blog = db.query(models.Blog).filter(
        models.Blog.id == id
    ).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    db.delete(blog)
    db.commit()

    return {
        "Message" : "Blog deleted successfully"
    }