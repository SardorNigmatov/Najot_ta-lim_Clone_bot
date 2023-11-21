from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler
from inline_handler import registration
from buttons import expert_with_contact
from data import (react_data,
                  vue_data,
                  nodejs_data,
                  python_backend,
                  qa_data,
                  boot_design,
                  odatiy_design,
                  moushn_data,
                  smm_data,
                  bootcamp_data,
                  bootcamp_result_data)

items_per_page = 1
current_page = 1

data_from_db = [
    "1-sahifa",
    "2-sahifa",
    "3-sahifa",
    "4-sahifa",
    "5-sahifa",
    "6-sahifa",
    "7-sahifa",
]




data = [
    """⭐️ <b>Shunchaki kurs emas</b>
Har bir o'quv kursi shunday ishlab chiqilganki, ularni muvaffaqiyatli yakunlab, siz zamonaviy kazb egasiga aylanishingiz va shu sohada o'z ish faoliyatingizni boshlashingiz mumkin. Hammasi o'z qo'lingizda.

👨‍🏫 <b>O'z ishining ustalari</b>
Darslar katta tajribaga ega malakali mutaxassis ustozlar tomonidan o'tiladi. O'z ishining ustalaridan olingan bilim hamisha barakali va manfaatli bo'ladi.

❓ <b>Yordam kerakmi?</b>
Darsdan tashqari vaqtlarda ham sizda savollar tug'ilishi tabiiy. Yordamchi ustozlarga murojaat qilsangiz, ular sizni qiynayotgan masalalar bo'yicha kerakli ko'rsatmalarni berishadi.""",
    """🔄 <b>Doimiy yangilanish</b>
Biz bir joyda to'xtab qolmaganmimz. Markazimizdagi yo'nalishlar yangi va dolzarb kurslar bilan muntazam ravishda boyitib boriladi.

🎯 <b>Nazariyaning o'zi kamlik qiladi</b>
Olgan bilimlaringiz haqiqatda foydali bo'lsihi uchun kurslarimiz amaliy mashg'ulotlar bilan boytilgan.

🔎 <b>Ish topish muammosi</b>
Kursni bitirgandan so'ng «Najot Ta'lim» markazi o'zining hamkor kompaniyalari yordamida sizga sohangiz bo'yicha munosib ish topishda imkon qadar ko'maklashadi. Odatda muvaffaqiyatli o'quvchilarimiz kurs davomidayoq o'z ishini topib ketadi.""",
    """📄 <b>Sertifikat</b>
Kursni muvaffaqiyatli yakunlaganingizdan so'ng sizga maxsus sertifikat taqdim etiladi.

🏢 <b>Jamoamizga taklif qilamiz</b>
Eng salohiyatli va tirishqoq o'quvchilarni biz o'z jamoamizga taklif etamiz. Demak, sizda kuchli jamoada ishlash imkoniyati bor.

🎤 <b>Haftalik master-klasslar</b>
Markazimizning Chilonzor filialida «Najot Ta'lim»ning barcha o'quvchilari uchun har hafta soha bo'yicha professional va muvaffaqiyat qozongan insonlar bilan master-klasslar tashkil qilinadi.""",
    """
    🏆 <b>Sohaga oid tadbirlar</b>
Markazimizda mavjud yo'nalishlar bo'yicha guruhlar o'rtasida har oy 2 marotaba qiziqarli musobaqalar, turli xil tanlovlar tashkil qilinadi va g'olibarga maxsus sovg'alar taqdim etiladi.

🛡 <b>Ta'lim uchun alohida bo'lim</b>
Markazimizda xususiy ta'lim muassasalarida uchramaydigan alohida o'quv bo'limi tashkil qilingan.

O'quv bo'limining vazifasi taklif v shikoyatlar bilash ishlash, o'quvchining o'zlashtirish darajasi va oq'uvchining dars jarayonini nazorat qilish hamda imtihonlarni tashkil etishdan iborat.
    """,
    """🌟 Yana nimalarni qo'lga kiritasiz? 

🕔 <b>24/7 kovorking</b>
Markazimizning barcha filiallarida o'quvchilar erkin dars qilishi uchun kovorking zonalari tashkil qilingan. Chilonzor filialidagi kovorking 24/7 tarzida faoliyat olib boradi. Siz istalgan vaqtda kelib, cheklanmagan muddatgacha dars tayyorlashingiz mumkin.

🔗 <b>Netvorking</b>
Markazimizda turli xil insonlar tahsil olishadi, ularning orassida biznes egalari, har xil soha vakillari, oliy o'quv yurti talabalari ham bor. Siz ushbu insonlar bilan tanishib (netvorking), ulardan ma'lum darajada bilim olish yoki o'z bilimingizni ulashish orqali yanada rivojlanish imkoniyatiga ega bo'lasiz.""",
    """
    💡 <b>Ajoyib atmosfera</b>
Markazimiz zamonaviy dizayn uslubida bezatilgan (Chilonzor filiali). Har bir dars xonasiga jahondagi taniqli kompaniyalar nomlari qo'yilgan va aynan o'sha kompaniyalarning logosiga mos ravishda jihozlangan. Bundan tashqari, xonalar va kovorking  zonalarimizning yozda salqin, qishda issiq bo'lishi ta'minlanadi.

🤝 <b>Tajriba olish yoki ishlash imkoniyati</b>
«Najot Ta'lim» O'zbekistondagi ko'pgina biznes turlari bo'yicha yirik kompaniyalar bilan hamkorlik qiladi. Bizning tavsiyamimz orqali siz shu kompaniyalarda bepul tajriba orttirishingiz yoki to'laqonli ish faoliyatingizni boshlashingiz mumkin.
    """,
    """✅ <b>Ro'yxatdan o'tish</b>
«Najot Ta'lim»dan ro'yxatdan o'tishingiz uchun najottalim.uz sayti,ijtimoiy tarmoq sahifalari, 78 888 9 888 raqamiga qo'ng'iroq qilish yoki o'zingizga yaqin bo'lgan filialga kelish orqali amalga oshirishingiz mumkin.""",
]


def advantages(update, context):
    global matn
    matn = data[0]
    chat_id = update.effective_chat.id
    reply_markup = generate_inline_keyboard()

    context.bot.send_message(chat_id=chat_id, text=f"{matn}",parse_mode='HTML', reply_markup=reply_markup)


def generate_inline_keyboard():
    global matn
    # Calculate start and end indices based on the current page
    start_index = (current_page - 1) * items_per_page
    end_index = start_index + items_per_page

    items = data_from_db[start_index:end_index]

    keyboard_buttons = [
        [InlineKeyboardButton(item, callback_data=item)] for item in items
    ]

    pagination_buttons = []
    if current_page > 1:
        pagination_buttons.append(InlineKeyboardButton("◀️ Orqaga", callback_data="previous"))
    if end_index < len(data_from_db):
        pagination_buttons.append(InlineKeyboardButton(" Davomi ➡️", callback_data="next"))
    if current_page == len(data):
        pagination_buttons.append(InlineKeyboardButton("✅ Ro'yxatdan o'tish",callback_data='advantages_registration'))

    if pagination_buttons:
        keyboard_buttons.append(pagination_buttons)

    reply_markup = InlineKeyboardMarkup(keyboard_buttons)

    return reply_markup

# Function to handle button presses
def button_press(update, context):
    query = update.callback_query
    query.answer()

    button_data = query.data
    chat_id = update.effective_chat.id


    if button_data == "previous":
        previous_page()
        reply_markup = generate_inline_keyboard()
        query.edit_message_text(text=data[current_page - 1], parse_mode='HTML', reply_markup=reply_markup)

    elif button_data == "next":
        next_page()
        reply_markup = generate_inline_keyboard()
        query.edit_message_text(text=data[current_page - 1], parse_mode='HTML', reply_markup=reply_markup)

    elif button_data == 'advantages_registration':
        query.message.reply_text(text="""
        Tizim vaqtinchalik ish faoliyatida emas. 

78 888 9 888 raqami orqali bog'lanishingizni so'raymiz!
        """)
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    elif button_data == "register":
        query.message.reply_text(text="""
                Tizim vaqtinchalik ish faoliyatida emas. 

        78 888 9 888 raqami orqali bog'lanishingizni so'raymiz!
                """)
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    else:
        sp = list(str(query.data).split('_'))
        title = sp[0]
        text =  sp[1]
        if title == 'react':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='react_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='react_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='react_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='react_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='react_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=react_data[text], parse_mode='HTML', reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'vue':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='vue_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='vue_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='vue_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='vue_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='vue_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=vue_data[text], parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'nodejs':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='nodejs_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='nodejs_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='nodejs_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='nodejs_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='nodejs_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=nodejs_data[text], parse_mode='HTML', reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'python':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='python_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='python_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='python_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='python_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='python_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=python_backend[text], parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'qa':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='qa_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='qa_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='qa_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='qa_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='qa_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=qa_data[text], parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'boot':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='boot_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='boot_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='boot_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='boot_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='boot_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=boot_design[text], parse_mode='HTML', reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'oddiy':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='oddiy_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='oddiy_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='oddiy_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='oddiy_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='oddiy_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=odatiy_design[text], parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == 'moushn':
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='moushn_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='moushn_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='moushn_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='moushn_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='moushn_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=moushn_data[text], parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == "smm":
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='smm_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='smm_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='smm_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='smm_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='smm_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=smm_data[text], parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == "bootcamp":
            buttons = [
                [InlineKeyboardButton(text="🎁 Bonus darslar",callback_data='bootcamp_bonus')],
                [InlineKeyboardButton(text='C dasturlash tili asoslari',callback_data='bootcamp_c'),InlineKeyboardButton(text='Python dasturlash tili asoslari',callback_data='bootcamp_python')],
                [InlineKeyboardButton(text="Qo'shimcha bilimlar",callback_data='bootcamp_knowledge'),InlineKeyboardButton(text='Kurs yakunidagi natija',callback_data='bootcamp_result')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=bootcamp_data[text],parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))
        elif title == "result":
            buttons = [
                [InlineKeyboardButton(text='Imkoniyatlar', callback_data='result_chance'),
                 InlineKeyboardButton(text='Ishga joylashish', callback_data='result_work')],
                [InlineKeyboardButton(text='Bilimlar', callback_data='result_knowledge')],
                [InlineKeyboardButton(text='Kurs narxi', callback_data='result_price'), InlineKeyboardButton(
                    text='Kerakli kompyuter', callback_data='result_computer')],
                [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
            ]
            query.edit_message_text(text=bootcamp_result_data[text], parse_mode='HTML', reply_markup=InlineKeyboardMarkup(buttons))


# Function to navigate to the previous page
def previous_page():
    global current_page
    current_page -= 1

# Function to navigate to the next page
def next_page():
    global current_page
    current_page += 1




