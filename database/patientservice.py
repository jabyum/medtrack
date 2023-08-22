from database import get_db
from database.models import Patient
from datetime import datetime
def check_patient_db(user_id):
    db = next(get_db())
    checker = db.query(Patient).filter_by(user_id=user_id).first()
    if checker:
        return False
    return True
def add_patient_db(user_id, gender, age, symptoms, other, phone_number, photo, messageid):
    db = next(get_db())
    new_patient = Patient(user_id=user_id, gender=gender, age=age, symptoms=symptoms, other=other,
                          phone_number=phone_number, photo=photo,
                          messageid=messageid, reg_date=datetime.now())
    db.add(new_patient)
    db.commit()
    return new_patient.id
def get_exact_patient_db(user_id):
    db = next(get_db())
    exact_patient = db.query(Patient).filter_by(user_id=user_id).first()
    if exact_patient:
        return exact_patient
    return "Анкета не найдена"
def get_all_patients_db():
    db = next(get_db())
    all_patients = db.query(Patient).all()
    return all_patients
def delete_exact_patient_db(user_id):
    db = next(get_db())
    exact_patient = db.query(Patient).filter_by(user_id=user_id).first()
    if exact_patient:
        db.delete(exact_patient)
        db.commit()
        return "Успешно удалено"
    return 'Ошибка в данных'
