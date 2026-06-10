from pydantic import BaseModel

#InputSchema
class BlogCreate(BaseModel):
    title:str
    content:str
    
#OutputSchema
class BlogResponse(BaseModel):
    id:int
    title:str
    content:str
    
    class Config:
        from_attributes = True