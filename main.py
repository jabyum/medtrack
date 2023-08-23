from fastapi import FastAPI
from database import Base, engine
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/blackhole')

from api.medic import medic_api
from api.patient import patient_api
from api.screening import screening_api
from api.user import user_api
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_pages)
