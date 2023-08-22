from api import app
from fastapi import Request
from database.patientservice import check_patient_db, add_patient_db, get_exact_patient_db, \
    get_all_patients_db, delete_exact_patient_db

@app.get("/api/check_patient")
async def check_patient(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    check = check_patient_db(user_id)
    return {"status": 1, "message": check}
@app.get("/api/check_patient")
async def get_exact_patient(request: Request):
    data = await request.json()
    patient_id = data.get("patient_id")
    exact = get_exact_patient_db(patient_id)
    return {"status": 1, "message": exact}
@app.get("/api/all_patients")
async def get_all_patient(request: Request):
    all_patients = get_all_patients_db()
    return {"status": 1, "message": all_patients}
@app.post("/api/add_patient")
async def add_patient(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    gender = data.get("gender")
    age = data.get("age")
    symptoms = data.get("symptoms")
    other = data.get("other")
    phone_number = data.get("phone_number")
    photo = data.get("photo")
    messageid = data.get("messageid")
    if user_id and gender and age and symptoms and other and phone_number and messageid:
        add_patient_db(user_id, gender, age, symptoms, other, phone_number, photo, messageid)
        return {"status": 1, "message": "Сохранено"}
    return {"status": 0, "message": "ошибка"}
@app.delete("/api/delete_patient")
async def delete_exact_patien(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    if user_id:
        delete_exact_patient_db(user_id)
        return {"status": 1, "message": "успешно удалено"}
    return {"status": 0, "message": "ошибка"}
