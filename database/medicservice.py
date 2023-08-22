from database import get_db
from database.models import Medic
from datetime import datetime
def check_medic_db(user_id):
    db = next(get_db())
    checker = db.query(Medic).filter_by(tg_id=user_id).first()
    if checker:
        return True
    return False
def add_medic_db(user_id, name, speciality, experience, work_place_time, other, phone_number, photo, messageid):
    db = next(get_db())
    new_medic = Medic(user_id=user_id, name=name, speciality=speciality, experience=experience,
                      work_place_time=work_place_time, other=other, phone_number=phone_number, photo=photo,
                      messageid=messageid, reg_date=datetime.now())
    db.add(new_medic)
    db.commit()
    return new_medic.id
def get_exact_medic_db(medic_id):
    db = next(get_db())
    exact_medic = db.query(Medic).filter_by(medic_id=medic_id).first()
    if exact_medic:
        return exact_medic
    return "Анкета не найдена"
def get_all_medics_db():
    db = next(get_db())
    all_medics = db.query(Medic).all()
    return all_medics
def delete_exact_medic_db(user_id):
    db = next(get_db())
    exact_medic = db.query(Medic).filter_by(user_id=user_id).first()
    if exact_medic:
        db.delete(exact_medic)
        db.commit()
        return "Успешно удалено"
    return 'Ошибка в данных'
