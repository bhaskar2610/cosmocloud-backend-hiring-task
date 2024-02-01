from pydantic import BaseModel, EmailStr, Field


class ProductSchema(BaseModel):
    product_name:str= Field(...)
    product_price:int= Field(...)
    quantity:int= Field(...)
    class Config:
        json_schema_extra = {
            "example": {
                "product_name": "Laptop",
                "product_price": 320000,
                "quantity": 10,
            }
        }
def ResponseModel(data, message):
    return {
        "res": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel( code, message):
    return { "code": code, "message": message}


