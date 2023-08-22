from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
def main_menu_kb(check_medic):
    kb = InlineKeyboardMarkup(row_width=1)
    about = InlineKeyboardButton(text="О проекте", callback_data="about")
    vacancy = InlineKeyboardButton(text="Консультация врача", callback_data="vacancy")
    vac_base = InlineKeyboardButton(text="Посмотреть актуальные вакансии", callback_data="vac_base")
    registration = InlineKeyboardButton(text="Хочу быть в базе врачей", callback_data="med_registration")
    delete_registration = InlineKeyboardButton(text="Удалить свою анкету", callback_data="delete_registration")
    question = InlineKeyboardButton(text="Скрининг", callback_data="screening")
    kb.row(vacancy)
    if check_medic == False:
        kb.add(registration)
    elif check_medic == True:
        kb.add(delete_registration)
    kb.row(vac_base)
    kb.row(question)
    kb.row(about)
    return kb
def main_menu_call_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    mm = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    kb.row(mm)
    return kb
def main_menu_reply_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    mm = InlineKeyboardButton(text="Главное меню")
    kb.add(mm)
    return kb
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    male = KeyboardButton("Мужской")
    female = KeyboardButton("Женский")
    mm = InlineKeyboardButton(text="Главное меню")
    kb.add(male, female, mm)
    return kb
def num_button_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    number = KeyboardButton("Поделиться контактом", request_contact=True)
    mm = InlineKeyboardButton(text="Главное меню")
    kb.add(number, mm)
    return kb
def delete_registration_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(text="Да, удалить", callback_data="yes_delete")
    no = InlineKeyboardButton(text="Нет, не удалять", callback_data="no_delete")
    kb.row(yes, no)
    return kb
def delete_vac_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(text="Да, удалить", callback_data="yes_delete_vac")
    no = InlineKeyboardButton(text="Нет, не удалять", callback_data="no_delete_vac")
    kb.row(yes, no)
    return kb
def vac_format_kb(check_vac):
    kb = InlineKeyboardMarkup(row_width=1)
    medic_base = InlineKeyboardButton(text="Посмотреть базу врачей", callback_data="medic_base")
    take_vacancy = InlineKeyboardButton(text="Оставить запрос на консультацию", callback_data="take_vacancy")
    delete_vacancy = InlineKeyboardButton(text="Удалить запрос на консультацию", callback_data="delete_vacancy")
    mm = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    kb.row(medic_base)
    if check_vac == False:
        kb.add(take_vacancy)
    elif check_vac == True:
        kb.add(delete_vacancy)
    kb.row(mm)
    return kb
def withoutphoto_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    wp = KeyboardButton("Без фото")
    mm = InlineKeyboardButton(text="Главное меню")
    kb.add(wp, mm)
    return kb
