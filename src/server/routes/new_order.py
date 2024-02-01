from fastapi import APIRouter, Body,Query
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from server.database import (
    add_product,
    retrieve_products,
    create_new
)
from server.models.new_order import (
    OrderItemSchema,
    UserAddressSchema,
    NewOrderSchema,
)

from server.models.products import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
)

router = APIRouter()

@router.post('/create',response_description="Order Created Successfully")
async def create_new_order(order_data: NewOrderSchema = Body(...)):
    order_data_json = jsonable_encoder(order_data)
    order_data_json["createdOn"] = datetime.now()
    response=await create_new(order_data_json)
    # return response
    if response:
        return ResponseModel(response,"Ordered Successfully")
    return ErrorResponseModel(400,"Your order was Unsuccessful")



