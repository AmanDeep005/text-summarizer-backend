from fastapi import APIRouter
from .endpoints import amit_function, duhan

app_router = APIRouter()

# Correct way to add routes
app_router.add_api_route("/amit", amit_function, methods=["GET"])
app_router.add_api_route("/textsummarizer", duhan, methods=["POST"])
