from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
router = APIRouter(
    prefix="",
    tags=["Pages"]
)
templates = Jinja2Templates(directory="templates")
@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
@router.get("/imt")
def get_search_page(request: Request):
    return templates.TemplateResponse("imt.html", {"request": request})
