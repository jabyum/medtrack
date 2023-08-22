from api import app
from fastapi import Request, Response, Body
from database.userservice import register_user_db, show_all_user_db, check_user_db
@app.post("/api/add_user")
async def add_user(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    phone_number = data.get("phone_number")
    if user_id and phone_number:
        register_user_db(user_id, phone_number)
        return {"status": 1, "message": "Сохранено"}
    return {"status": 0, "message": "ошибка"}
@app.get("/api/check_user")
async def check_user(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    checker = check_user_db(user_id)
    return {"status": 1, "message": checker}
@app.get("/api/all_users")
async def all_users():
    return show_all_user_db()