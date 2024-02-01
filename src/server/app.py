from fastapi import FastAPI

from server.routes.products import router as ProductRouter
from server.routes.new_order import router as OrderRoute
from fastapi_pagination import add_pagination

app = FastAPI()
add_pagination(app)
app.include_router(ProductRouter, tags=["Product"], prefix="/product")
app.include_router(OrderRoute,tags=["Order"],prefix="/order")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Fast Api FrameWork!"}
