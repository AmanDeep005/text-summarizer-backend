from fastapi import FastAPI
from .api.routes import app_router  # Correct import for app_router
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI(title="Chat App API")

# Include the router from api.routes
app.include_router(app_router)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You might want to restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint to test if the API is working
@app.get("/")
async def root():
    return {"message": "Hello World"}
