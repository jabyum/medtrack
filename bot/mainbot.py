import telebot
from database import userservice, patientservice, medicservice
import botbuttons
from telebot import types
import time
import requests
bot = telebot.TeleBot("6657750055:AAFY4ZOE2oBQx_AJi4hcl-kUgGYatSiv-MY")
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
bot.polling(none_stop=True)

