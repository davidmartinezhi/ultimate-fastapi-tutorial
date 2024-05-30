from fastapi import FastAPI, APIRouter

# Instantiate the FastAPI object
app = FastAPI(title="Recipe API", openapi_url="/openapi.json") # this is the main app, the entry we are starting up

# Specify a router for the API
api_router = APIRouter()

# Decorator syntax to specify the api route
@api_router.get("/", status_code=200) # we say the home route "/" will execute the function below
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"} # we return a dictionary which fastAPI converts to json

# Include the router in the app
app.include_router(api_router)

# This is for debugging purposes only
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
