import motor.motor_asyncio
from bson.objectid import ObjectId
from fastapi_pagination import LimitOffsetPage, add_pagination
from fastapi_pagination.ext.motor import paginate
MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client["productsDatabase"]

products_collection = database.get_collection("products_collection")

order_collection=database.get_collection("order_collection")
# This is a helper function that convert results from a database query into a Python dict.
def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "product_name": product["product_name"],
        "product_price": product["product_price"],
        "quantity": product["quantity"],
    }

def order_helper(order)->dict:
    return {
        "order_id":str(order["_id"])
    }

# Retrieve all products present in the database
async def retrieve_products(limit:int,offset:int,min_price:float,max_price:float):
    filter_query={"product_price":{"$gte":min_price,"$lte":max_price}}
    total_count = await products_collection.count_documents(filter_query)
    products = []
    async for product in products_collection.find(filter_query).skip(offset).limit(limit):
        products.append(product_helper(product))
    next_offset = offset + limit if offset + limit < total_count else None
    prev_offset = offset - limit if offset - limit >= 0 else None

    return {
        "data": products,
        "page": {
            "limit": limit,
            "nextOffset": next_offset,
            "prevOffset": prev_offset,
            "total": total_count,
        },
    }


# Add a new product into to the database
async def add_product(product_data: dict) -> dict:
    product = await products_collection.insert_one(product_data)
    new_product = await products_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_product)


async def create_new(order_details:dict)->dict:
    res=await order_collection.insert_one(order_details)
    order=await order_collection.find_one({"_id":res.inserted_id})
    return order_helper(order)


    