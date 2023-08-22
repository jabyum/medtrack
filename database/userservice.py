from database import get_db
from database.models import User
from datetime import datetime
def register_user_db(user_id, phone_number):
    db = next(get_db())
    new_user = User(tg_id=user_id, phone_number=phone_number, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return new_user.id
def check_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(tg_id=user_id).first()
    if checker:
        return False
    return True
def show_all_user_db():
    db = next(get_db())
    users = db.query(User).all()
    return {"status": 1, "message": users}
def get_phone_number_db(user_id):
    db = next(get_db())
    filter_id = db.query(User).filter_by(tg_id=user_id).first()
    phone_number = filter_id.phone_number
    return {"status": 1, "message": phone_number}