from api import app
from fastapi import Request
from database.medicservice import check_medic_db, add_medic_db, get_exact_medic_db, \
    get_all_medics_db, delete_exact_medic_db

@app.get("/api/check_medic")
async def check_medic(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    check = check_medic_db(user_id)
    return {"status": 1, "message": check}
@app.get("/api/check_medic")
async def get_exact_medic(request: Request):
    data = await request.json()
    medic_id = data.get("medic_id")
    exact = get_exact_medic_db(medic_id)
    return {"status": 1, "message": exact}
@app.get("/api/all_medics")
async def get_all_medics(request: Request):
    all_medics = get_all_medics_db()
    return {"status": 1, "message": all_medics}
@app.post("/api/add_medic")
async def add_medic(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    name = data.get("name")
    speciality = data.get("speciality")
    experience = data.get("experience")
    work_place_time = data.get("work_place_time")
    other = data.get("other")
    photo = data.get("photo")
    messageid = data.get("messageid")
    if user_id and name and speciality and experience and work_place_time and other and photo and messageid:
        add_medic_db(user_id, name, speciality, experience, work_place_time, other, photo, messageid)
        return {"status": 1, "message": "Сохранено"}
    return {"status": 0, "message": "ошибка"}
@app.delete("/api/delete_medic")
async def delete_exact_medic(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    if user_id:
        delete = delete_exact_medic_db(user_id)
        return {"status": 1, "message": delete}
    return {"status": 0, "message": "ошибка"}
