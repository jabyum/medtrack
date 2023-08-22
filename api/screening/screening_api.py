from api import app, templates
from fastapi import Request, Response
from database.screeningservice import add_screening_db, get_test_db
# @app.post("/api/add_screening")
# async def add_screening(request: Request):
#     test_id = data.get("test_id")
#     question = data.get("question")
#     answer1 = data.get("answer1")
#     answer2 = data.get("answer2")
#     answer3 = data.get("answer3")
#     answer4 = data.get("answer4")
#     if test_id and question and answer1 and answer2:
#         add_screening_db(test_id, question, answer1, answer2, answer3, answer4)
#         return {"status": 1, "message": "Сохранено"}
#     return {"status": 0, "message": "ошибка"}
@app.post("/api/add_screening")
async def add_screening(test_id: int, question: str, answer1: str, answer2: str, answer3: str, answer4: str):
    if test_id and question and answer1 and answer2:
        add_screening_db(test_id, question, answer1, answer2, answer3, answer4)
        return {"status": 1, "message": "Сохранено"}
    return {"status": 0, "message": "ошибка"}
@app.get("/api/test")
async def get_test(request: Request):
    data = await request.json()
    test_id = data.get("test_id")
    if test_id:
        tests = get_test_db(test_id)
        return templates.TemplateResponse("test.html", context=tests)
    return {"status": 0, "message": "ошибка"}