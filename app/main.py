from fastapi import FastAPI
from app.routes import form_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="KPA Form Data API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI
from app.routes import form_data  

app = FastAPI()

app.include_router(form_data.router)  

@app.get("/")
def root():
    return {"message": "KPA Form API is running"}

app.include_router(form_data.router)
