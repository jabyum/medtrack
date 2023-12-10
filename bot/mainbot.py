import telebot
import botbuttons
from telebot import types
import time
import requests
bot = telebot.TeleBot("")
url = "http://127.0.0.1:8000/"
@bot.message_handler(commands=["start"])
def start_message(message):
    user_id = message.from_user.id
    mm = bot.send_message(user_id, "Главное меню", reply_markup=types.ReplyKeyboardRemove())
    bot.delete_message(user_id, mm.message_id)
    user_checker_url = url + "api/check_user"
    response = requests.get(user_checker_url, json={"user_id": user_id})
    data = response.json()
    if data.get("message") == True:
        bot.send_message(user_id, "Для регистрации отправьте свой номер", reply_markup=botbuttons.num_button_kb())
        bot.register_next_step_handler(message, end_register)
    if data.get("message") == False:
        medic_checker_url = url + "api/check_medic"
        response = requests.get(medic_checker_url, json={"user_id": user_id})
        medicdata = response.json()
        check_medic = medicdata.get("message")
        bot.send_message(user_id, "Выберите пункт меню", reply_markup=botbuttons.main_menu_kb(check_medic))
def end_register(message):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        register_url = url + "api/add_user"
        response = requests.post(register_url, json={"user_id": user_id, "phone_number": phone_number})
        data = response.json()
        if data.get("status") == 1:
            bot.send_message(user_id, "Вы успешно зарегистрированы", reply_markup=types.ReplyKeyboardRemove())
            start_message(message)
        else:
            bot.send_message(user_id, "Ошибка регистрации, попробуйте позже", reply_markup=types.ReplyKeyboardRemove())
            start_message(message)
    else:
        bot.send_message(user_id, "Отправьте свой номер через кнопку в меню")
        bot.register_next_step_handler(message, end_register)
@bot.callback_query_handler(lambda call: call.data in ["about", "main_menu", "med_registration",
                                                       "delete_registration", "yes_delete", "no_delete",
                                                       "vac_base", "vacancy", "medic_base", "take_vacancy",
                                                       "delete_vacancy", "no_delete_vac", "yes_delete_vac"])
def calling(call):
    user_id = call.message.chat.id
    if call.data == "about":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Проект Medtrack направлен на облегчение "
                                  "получения медицинской консультации и отслеживание своего состояния здоровья",
                         reply_markup=botbuttons.main_menu_call_kb())
    elif call.data == "main_menu":
        bot.delete_message(user_id, call.message.message_id)
        return start_message(call)
    elif call.data == "med_registration":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Для того, чтобы оставить свою анкету в базе врачей, пожалуйста ответьте"
                                  " на следующие вопросы.\n\n"
                                  "Напишите своё имя и фамилию.\n\n"
                                  "Если вы нажмете на кнопку 'Главное меню' в процессе заполнения, "
                                  "анкету придется заполнять заново",
                         reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(call.message, get_med_name)
    elif call.data == "delete_registration":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Вы уверены, что хотите удалить свою анкету?",
                         reply_markup=botbuttons.delete_registration_kb())
    elif call.data == "no_delete":
        bot.delete_message(user_id, call.message.message_id)
        return start_message(call)
    elif call.data == "yes_delete":
        try:
            bot.delete_message(user_id, call.message.message_id)
            delete_medic_url = url + "api/delete_medic"
            delete_medic_response = requests.delete(delete_medic_url, json={"user_id": user_id})
            medic_message = delete_medic_response.json().get("message")
            medic_message_id = int(medic_message)
            bot.send_message(user_id, "Ваша анкета удалена")
            start_message(call)
            try:
                bot.delete_message(-1001804040786, medic_message_id)
            except:
                pass
        except:
            bot.delete_message(user_id, call.message.message_id)
            bot.send_message(user_id, "Произошла ошибка. Обратиться в службу поддержки")
            return start_message(call)
    elif call.data == "vac_base":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Канал с актуальными вакансиями\n"
                                  "https://t.me/+_iYh4_uI7YhiNjJi",
                         reply_markup=botbuttons.main_menu_call_kb())
    elif call.data == "vacancy":
        bot.delete_message(user_id, call.message.message_id)
        patient_checker_url = url + "api/check_patient"
        response = requests.get(patient_checker_url, json={"user_id": user_id})
        patientdata = response.json()
        check_vac = patientdata.get("message")
        bot.send_message(user_id, "Вы можете выбрать услугу "
                                  "или ознакомиться с базой врачей",
                         reply_markup=botbuttons.vac_format_kb(check_vac))
    elif call.data == "medic_base":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Канал с анкетами медиков\n"
                                  "https://t.me/+z7J6v_DBzxc5YzVi",
                         reply_markup=botbuttons.main_menu_call_kb())
    elif call.data == "take_vacancy":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Для того, чтобы оставить свой запрос на консультацию, пожалуйста ответьте"
                                  " на следующие вопросы.\n\n"
                                  "Выберите пол пациента.\n\n"
                                  "Если вы нажмете на кнопку 'Главное меню' в процессе заполнения, "
                                  "запрос придется заполнять заново",
                         reply_markup=botbuttons.gender_kb())
        bot.register_next_step_handler(call.message, get_patient_gender)
    elif call.data == "delete_vacancy":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Вы уверены, что хотите удалить свой запрос на консультацию?",
                         reply_markup=botbuttons.delete_vac_kb())
    elif call.data == "no_delete_vac":
        bot.delete_message(user_id, call.message.message_id)
        return start_message(call)
    elif call.data == "yes_delete_vac":
        try:
            bot.delete_message(user_id, call.message.message_id)
            delete_patient_url = url + "api/delete_patient"
            delete_patient_response = requests.delete(delete_patient_url, json={"user_id": user_id})
            patient_message = delete_patient_response.json().get("message")
            patient_message_id = int(patient_message)
            bot.send_message(user_id, "Ваша анкета удалена")
            start_message(call)
            try:
                bot.delete_message(-1001929729129, patient_message_id)
            except:
                pass
        except:
            bot.delete_message(user_id, call.message.message_id)
            bot.send_message(user_id, "Произошла ошибка. Обратиться в службу поддержки")
            return start_message(call)


def get_patient_gender(message):
    user_id = message.from_user.id
    gender = message.text
    if gender == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Напишите возраст пациента", reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_patient_age, gender)
def get_patient_age(message, gender):
    user_id = message.from_user.id
    age = message.text
    if age == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Коротко опишите основные жалобы и симптомы",
                         reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_patient_symptoms, gender, age)
def get_patient_symptoms(message, gender, age):
    user_id = message.from_user.id
    symptoms = message.text
    if symptoms == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Оставьте какие-нибудь примечания к заявке",
                         reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_patient_other, gender, age, symptoms)
def get_patient_other(message, gender, age, symptoms):
    user_id = message.from_user.id
    other = message.text
    if other == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Вы можете прикрепить одну фотографию к заявке. Если фото не требуется,"
                                  " нажмите на кнопку 'Без фото'",
                         reply_markup=botbuttons.withoutphoto_kb())
        bot.register_next_step_handler(message, get_patient_photo, gender, age, symptoms, other)
def get_patient_photo(message, gender, age, symptoms, other):
    user_id = message.from_user.id
    if message.photo:
        photo = message.photo[-1].file_id
        user_phone_url = url + "api/user_phone_number"
        phone_response = requests.get(user_phone_url, json={"user_id": user_id})
        phone_data = phone_response.json()
        number = phone_data.get("message")
        phone_number = number.get("message")
        bot.send_message(user_id, "Ваша запрос готов",
                         reply_markup=types.ReplyKeyboardRemove())
        posting = bot.send_photo(-1001929729129, photo=photo, caption=f"<b>Пол</b>: {gender}\n"
                                                                      f"<b>Возраст</b>: {age}\n"
                                                                      f"<b>Жалобы и симптомы</b>: {symptoms}\n"
                                                                      f"<b>Примечания</b>: {other}\n"
                                                                      f"<b>Номер телефона</b>: {phone_number}",
                                 parse_mode="html")
        messageid = posting.message_id
        add_patient_url = url + "api/add_patient"
        patient_response = requests.post(add_patient_url, json={"user_id": user_id, "gender": gender, "age": age,
                                                                "symptoms": symptoms, "other": other,"photo": photo,
                                                                "messageid": messageid})
        add_med_data = patient_response.json()
        start_message(message)
    elif message.text == "Главное меню":
        start_message(message)
    elif message.text == "Без фото":
        photo = None
        user_phone_url = url + "api/user_phone_number"
        phone_response = requests.get(user_phone_url, json={"user_id": user_id})
        phone_data = phone_response.json()
        number = phone_data.get("message")
        phone_number = number.get("message")
        bot.send_message(user_id, "Ваша запрос готов",
                         reply_markup=types.ReplyKeyboardRemove())
        posting = bot.send_message(-1001929729129, f"<b>Пол</b>: {gender}\n"
                                                   f"<b>Возраст</b>: {age}\n"
                                                   f"<b>Жалобы и симптомы</b>: {symptoms}\n"
                                                   f"<b>Примечания</b>: {other}\n"
                                                   f"<b>Номер телефона</b>: {phone_number}",
                                   parse_mode="html")
        messageid = posting.message_id
        add_patient_url = url + "api/add_patient"
        patient_response = requests.post(add_patient_url, json={"user_id": user_id, "gender": gender, "age": age,
                                                                "symptoms": symptoms, "other": other, "photo": photo,
                                                                "messageid": messageid})
        add_med_data = patient_response.json()
        start_message(message)
    else:
        bot.send_message(user_id, "Отправьте фотографию или нажмите на кнопку 'Без фото'")
        bot.register_next_step_handler(message, get_patient_photo, gender, age, symptoms, other)

def get_med_name(message):
    user_id = message.from_user.id
    name = message.text
    if name == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Укажите свою специальность", reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_med_speciality, name)
def get_med_speciality(message, name):
    user_id = message.from_user.id
    speciality = message.text
    if speciality == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Коротко напишите о своем опыте работы и кратко опишите навыки", reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_med_experience, name, speciality)
def get_med_experience(message, name, speciality):
    user_id = message.from_user.id
    experience = message.text
    if experience == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Коротко напишите о месте и графике вашей работы",
                         reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_med_work_time, name, speciality, experience)
def get_med_work_time(message, name, speciality, experience):
    user_id = message.from_user.id
    work_place_time = message.text
    if work_place_time == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Напишите дополнительную информацию", reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_med_other, name, speciality, experience, work_place_time)
def get_med_other(message, name, speciality, experience, work_place_time):
    user_id = message.from_user.id
    other = message.text
    if work_place_time == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Отправьте свою фотографию", reply_markup=botbuttons.main_menu_reply_kb())
        bot.register_next_step_handler(message, get_med_photo, name, speciality, experience, work_place_time, other)
def get_med_photo(message, name, speciality, experience, work_place_time, other):
    user_id = message.from_user.id
    if message.photo:
        photo = message.photo[-1].file_id
        user_phone_url = url + "api/user_phone_number"
        phone_response = requests.get(user_phone_url, json={"user_id": user_id})
        phone_data = phone_response.json()
        number = phone_data.get("message")
        phone_number = number.get("message")
        bot.send_message(user_id, "Ваша анкета готова",
                         reply_markup=types.ReplyKeyboardRemove())
        posting = bot.send_photo(-1001804040786, photo=photo, caption=f"{name}\n"
                                                                      f"<b>Специальность</b>: {speciality}\n"
                                                                      f"<b>Опыт и навыки</b>: {experience}\n"
                                                                      f"<b>Место и график работы</b>: {work_place_time}\n"
                                                                      f"<b>Дополнительная информация</b>: {other}\n"
                                                                      f"<b>Номер телефона</b>: {phone_number}",
                                 parse_mode="html")
        messageid = posting.message_id
        add_med_url = url + "api/add_medic"
        medic_response = requests.post(add_med_url, json={"user_id": user_id, "name": name, "speciality": speciality,
                                                          "experience": experience, "work_place_time": work_place_time,
                                                          "other": other, "photo": photo, "messageid": messageid})
        add_med_data = medic_response.json()
        start_message(message)
    elif message.text == "Главное меню":
        start_message(message)
    else:
        bot.send_message(user_id, "Отправьте фотографию")
        bot.register_next_step_handler(message, get_med_photo, name, speciality, experience, work_place_time, other)
# def mailing(message):
#     user_id = message.from_user.id
#     text = message.text
#     if text == "Отмена❌":
#          bot.send_message(user_id, "Рассылка отменена", reply_markup=types.ReplyKeyboardRemove())
#     else:
#         for i in targets_id:
#             try:
#                 time.sleep(1)
#                 bot.send_message(i, text)
#             except:
#                 continue
#     bot.send_message(user_id, "Рассылка завершена", reply_markup=types.ReplyKeyboardRemove())
#     admin_panel(message)
bot.polling(none_stop=True)

