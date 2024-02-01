from pydantic import BaseModel, EmailStr, Field
from typing import List

class OrderItemSchema(BaseModel):
    productId: str
    boughtQuantity: int
class UserAddressSchema(BaseModel):
    city: str
    country: str
    zipCode: str

  

class NewOrderSchema(BaseModel):
    items: List[OrderItemSchema]
    userAddress: UserAddressSchema
    totalAmount: float
    class Config:
        json_schema_extra = {
            "example": {
                "items": [{"productId":"65b771c6a73ec0c1d454e8fa","boughtQuantity":1}],
                "userAddress": {"city":"Ghaziabad","country":"India","zipCode":"201014"},
                "totalAmount":36729
            }
        }
