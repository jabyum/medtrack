from database import get_db
from database.models import Screening
from datetime import datetime
def add_screening_db(test_id, question, answer1, answer2, answer3 = None, answer4 = None):
    db = next(get_db())
    new_question = Screening(test_id=test_id, question=question, answer1=answer1, answer2=answer2,
                             answer3=answer3, answer4=answer4, reg_date=datetime.now())
    db.add(new_question)
    db.commit()
    return new_question.id
def delete_exact_question_db(question_id):
    db = next(get_db())
    exact_question = db.query(Screening).filter_by(question_id=question_id).first()
    if exact_question:
        db.delete(exact_question)
        db.commit()
        return "Успешно удалено"
    return 'Ошибка в данных'
def get_test_db(test_id=0):
    db = next(get_db())
    exact_test = db.query(Screening).filter_by(test_id=test_id).all()
    if exact_test:
        return exact_test
    return 'Ошибка в данных'