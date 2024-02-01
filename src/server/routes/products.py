from fastapi import APIRouter, Body,Query
from fastapi.encoders import jsonable_encoder
# from fastapi_pagination import LimitOffsetPage, add_pagination, paginate


from server.database import (
    add_product,
    retrieve_products,
)
from server.models.products import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
)

router = APIRouter()


@router.get('/all',response_description="Get All Product List")
async def get_all_products(limit:int,offset:int,min_price:int=Query(0,ge=0),max_price:int=Query(int(1e10))):
    products=await retrieve_products(limit,offset,min_price,max_price)
    if products:
        return ResponseModel(products,"Product data retrieved successfully")
    return ResponseModel(products,"Empty List Return")

@router.post("/", response_description="Product data added into the database")
async def add_product_data(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_product = await add_product(product)
    return ResponseModel(new_product, "Product added successfully.")

