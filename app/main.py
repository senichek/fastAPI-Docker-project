from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
import os

stage_name = os.environ.get("STAGE", None)

print(f"Stage is: {stage_name}")

app = FastAPI()

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=f"/{stage_name}/openapi.json",
        title="Your API Swagger UI"
    )

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Yo API",
        version="1.0.0",
        description='''Test API setup' ''',
        routes=app.routes,
    )

@app.get("/health")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)