from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models,schemas
from auth import create_token,verify_token

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Home
@app.get("/")
def home():
    return {"message":"Welcome to my Blog API!"}


#login API
@app.post("/login")
def login():
    return {
        "access_token":create_token({"user":"admin"}),
        "token_type":"bearer"
    }


#Create Blog Protected
@app.post("/blogs",response_model=schemas.BlogResponse)
def create_blog(blog:schemas.BlogCreate, db:Session = Depends(get_db),user = Depends(verify_token)):
    new_blog = models.Blog(
        title = blog.title,
        content = blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

#Read All Blog
@app.get("/blogs",response_model=list[schemas.BlogResponse])
def get_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


#Read Single blog
@app.get("/blogs/{id}",response_model=schemas.BlogResponse)
def get_blog(id: int, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


#Update Blog
@app.put("/blogs/{id}",response_model=schemas.BlogResponse)
def update_blog(id: int, updated_blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog.title = updated_blog.title
    blog.content = updated_blog.content
    db.commit()
    db.refresh(blog)
    
    return blog


#Delete blog
@app.delete("/blogs/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    db.delete(blog)
    db.commit()
    
    return {"message": "Blog deleted successfully"}






