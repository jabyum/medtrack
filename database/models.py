from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    tg_id = Column(BigInteger, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    reg_date = Column(DateTime)
class Medic(Base):
    __tablename__ = "medics"
    medic_id = Column(BigInteger, autoincrement=True, primary_key=True)
    tg_id = Column(BigInteger, ForeignKey("users.tg_id"), nullable=False)
    name = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    work_place_time = Column(String, nullable=False)
    other = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    messageid = Column(String, nullable=False)
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")
class Patient(Base):
    __tablename__ = "patients"
    patient_id = Column(BigInteger, autoincrement=True, primary_key=True)
    tg_id = Column(BigInteger, ForeignKey("users.tg_id"), nullable=False)
    gender = Column(String, nullable=False)
    age = Column(String, nullable=False)
    symptoms = Column(String, nullable=False)
    other = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    messageid = Column(String, nullable=False)
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")
class Screening(Base):
    __tablename__ = "screening"
    test_id = Column(BigInteger)
    question_id = Column(BigInteger, autoincrement=True, primary_key=True)
    question = Column(String, nullable=True)
    answer1 = Column(String, nullable=False)
    answer2 = Column(String, nullable=False)
    answer3 = Column(String, nullable=True)
    answer4 = Column(String, nullable=True)
    reg_date = Column(DateTime)
class Tg_admin(Base):
    __tablename__ = "admins"
    admin_id = Column(BigInteger, autoincrement=True, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    rank = Column(Integer, nullable=False)
    reg_date = Column(DateTime)



