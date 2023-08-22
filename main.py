from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from database import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/blackhole')
templates = Jinja2Templates(directory="templates")
from api.medic import medic_api
from api.patient import patient_api
from api.screening import screening_api
from api.user import user_api
import bot
