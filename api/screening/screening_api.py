from api import app
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from database.screeningservice import add_screening_db, get_test_db
from pages.router import templates
@app.post("/api/add_screening")
async def add_screening(request: Request):
    data = await request.json()
    test_id = data.get("test_id")
    question = data.get("question")
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = data.get("answer4")
    if test_id and question and answer1 and answer2:
        add_screening_db(test_id, question, answer1, answer2, answer3, answer4)
        return {"status": 1, "message": "Сохранено"}
    return {"status": 0, "message": "ошибка"}
# @app.post("/api/add_screening")
# async def add_screening(test_id: int, question: str, answer1: str, answer2: str, answer3: str, answer4: str):
#     if test_id and question and answer1 and answer2:
#         add_screening_db(test_id, question, answer1, answer2, answer3, answer4)
#         return {"status": 1, "message": "Сохранено"}
#     return {"status": 0, "message": "ошибка"}
@app.get("/api/test")
async def get_test(request: Request):
    data = await request.json()
    test_id = data.get("test_id")
    if test_id:
        tests = get_test_db(test_id)
        return ("test.html", {"request": request})
    return {"status": 0, "message": "ошибка"}
@app.get("/test")
async def get_test(request: Request):
    return ("imt.html", {"request": request})
@app.post("/imt")
async def imt(weight: int = Form(), height: int = Form()):
    imt_calc = weight / (height/100) ** 2
    imt_round = round(imt_calc)
    imt_message = f"Ваш ИМТ: {imt_round}"
    if imt_calc <= 16:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас выраженный дефицит веса</h2></body>'
        return HTMLResponse(message)
    elif imt_calc > 16 and imt_calc < 18:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас недостаток массы</h2></body>'
        return HTMLResponse(message)
    elif imt_calc > 18 and imt_calc < 25:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас нормальный вес</h2></body>'
        return HTMLResponse(message)
    elif imt_calc > 25 and imt_calc < 30:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас предожирение</h2></body>'
        return HTMLResponse(message)
    elif imt_calc > 30 and imt_calc < 35:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас ожирение I степени</h2></body>'
        return HTMLResponse(message)
    elif imt_calc > 35 and imt_calc < 40:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас ожирение II степени</h2></body>'
        return HTMLResponse(message)
    elif imt_calc > 40:
        message = f'<body bgcolor="e1f4f5"> {imt_message}<br>' \
                  f'<h2>У вас ожирение III степени</h2></body>'
        return HTMLResponse(message)
