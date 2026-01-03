from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# IMPORTANT: ensure models are registered before table creation
import models.image

from database import create_tables
from routes.import_routes import router as import_router
from routes.image_routes import router as image_router

app = FastAPI(title="Foto Owl Backend")


@app.on_event("startup")
def startup():
    try:
        create_tables()
        print("✅ Database tables created")
    except Exception as e:
        print("⚠️ Database not available. Skipping table creation.")
        print(e)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(import_router, prefix="/import", tags=["Import"])
app.include_router(image_router, prefix="/images", tags=["Images"])


@app.get("/")
def root():
    return {"message": "Backend is running successfully 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}
