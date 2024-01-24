from fastapi import FastAPI
from routes.api import api

app = FastAPI()

app.include_router(api, prefix="/api", tags=["api"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
