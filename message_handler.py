from buttons import about_center, courses, branches, expert_with_contact, general_data, achievement, programming, design, marketing, programming_education
from pagination import *
from telegram import KeyboardButton, ReplyKeyboardMarkup
from inline_handler import (registration,
                            react,
                            vue,
                            backend_nodejs,
                            backend_python,
                            qa,
                            boot_grafik_dizayn,
                            oddiy_grafik_dizayn,
                            moushn_dizayn,
                            smm_pro,
                            bootcamp_foundation,
                            bootcamp_result,
                            dastur_price,
                            must_computer)


def message_handler(update,context):
    message = update.message.text
    if message == 'Markaz haqida':
        context.user_data['page'] = "Markaz haqida"
        about_center(update,context)
        context.user_data['page'] = 'Markaz haqida'
    elif message == 'Kurslarimiz':
        context.user_data['page'] = "Kurslarimiz"
        courses(update,context)
    elif message == 'Filliallarimiz':
        branches(update, context)
    elif message == "Mutaxassis bilan aloqa":
        expert_with_contact(update, context)
    elif message == "Umumiy ma'lumotlar":
        general_data(update, context)
    elif message == "Afzalliklar":
         advantages(update, context)
    elif message == "Yutuqlar":
        achievement(update, context)
    elif message == '🔙 Orqaga':
        if context.user_data['page'] == 'Markaz haqida' or context.user_data['page'] == 'Kurslarimiz':
            buttons = [
                [KeyboardButton(text='Markaz haqida'), KeyboardButton(text='Kurslarimiz')],
                [KeyboardButton(text='Filliallarimiz'), KeyboardButton(text='Mutaxassis bilan aloqa')],
                [KeyboardButton(text="Imtihonga ro'yxatdan o'tish")]
            ]
            update.message.reply_text(text='Asosiy Menu:',reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        elif context.user_data['page'] in ['Dasturlash','Dizayn','Marketing']:
            courses(update, context)
        elif context.user_data['page'] == 'Dasturlash kasbiy ta\'lim':
            programming(update, context)
    elif message == "Imtihonga ro'yxatdan o'tish":
        registration(update, context)
    elif message == 'Dasturlash':
        context.user_data['page'] = "Dasturlash"
        programming(update, context)
    elif message == 'Dizayn':
        context.user_data['page'] = "Dizayn"
        design(update, context)
    elif message == 'Marketing':
        context.user_data['page'] == "Marketing"
        marketing(update, context)
    elif message == 'Dasturlash kasbiy ta\'lim':
        context.user_data['page'] = 'Dasturlash kasbiy ta\'lim'
        programming_education(update, context)
    elif message == 'Frontend:React':
        react(update, context)
    elif message == 'Frontend:Vue':
        vue(update, context)
    elif message == 'Backend:Nodejs':
        backend_nodejs(update, context)
    elif message == 'Backend:Python':
        backend_python(update, context)
    elif message == 'QA ( quality assurance )':
        qa(update, context)
    elif message == 'Bootcamp Grafik Dizayn':
        boot_grafik_dizayn(update, context)
    elif message == 'Odatiy Grafik Dizayn kursi':
        oddiy_grafik_dizayn(update, context)
    elif message == 'Moushn Grafika':
        moushn_dizayn(update, context)
    elif message == 'SMM Pro':
        smm_pro(update, context)
    elif message == "Bootcamp-foundation":
        bootcamp_foundation(update, context)
    elif message == 'Bootcamp result':
        bootcamp_result(update, context)
    elif message == 'Dastur narxi':
        dastur_price(update, context)
    elif message == 'Kerakli kompyuter':
        must_computer(update, context)




