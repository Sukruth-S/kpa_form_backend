from fastapi import FastAPI
from app.routes import form_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="KPA Form Data API")

# Enable CORS for frontend integration (important for Flutter app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI
from app.routes import form_data  # adjust path if needed

app = FastAPI()

app.include_router(form_data.router)  # 👈 make sure this line is there

@app.get("/")
def root():
    return {"message": "KPA Form API is running"}

# Include the form_data router
app.include_router(form_data.router)
