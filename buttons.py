from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Asosiy menu ni  buttonlari

def about_center(update,context):
    context.user_data['page'] = "Markaz haqida"
    buttons = [
        [KeyboardButton(text='Umumiy ma\'lumotlar'),KeyboardButton(text='Afzalliklar')],
        [KeyboardButton(text='Yutuqlar'),KeyboardButton(text='🔙 Orqaga')],
    ]
    update.message.reply_text(
        text="Markaz haqida ko'proq bilish uchun quyidagi bo'limlardan birini tanlang:",
        reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True)

    )

def courses(update,context):
    context.user_data['page'] = "Kurslarimiz"
    buttons = [
        [KeyboardButton(text='Dasturlash'),KeyboardButton(text='Dizayn')],
        [KeyboardButton(text='Marketing'),KeyboardButton(text='🔙 Orqaga')]
    ]
    update.message.reply_text(
        text="""
        🎯 «Najot Ta'lim»da umumiy 3 ta zamonaviy kasb yo'nalishi bor:

<b>1. Dasturlash</b>
<b>2. Dizayn</b>
<b>3. Marketing</b>

Yo'nalishlarda mavjud kurslarni ko'rish uchun quyidagi
bo'limlardan birini tanlang.
        
        """,
        reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True),
        parse_mode='HTML',
    )


def branches(update,context):
    update.message.reply_text(
        text="""
    <b>Toshkent va Farg'ona shahrida filiallarimiz mavjud:</b>

 📍 <a href="https://maps.google.com/maps?q=41.325080,69.245168&ll=41.325080,69.245168&z=16">Chorsu</a>
 📍 <a href="https://maps.google.com/maps?q=41.285547,69.203981&ll=41.285547,69.203981&z=16">Chilonzor</a>
 📍 <a href="https://maps.google.com/maps?q=41.346844,69.215791&ll=41.346844,69.215791&z=16">Chimboy bekati</a>

<b>Najot Ta'lim Farg’ona filiali manzili:</b>

 📍 <a href="https://maps.google.com/maps?q=40.388038,71.788190&ll=40.388038,71.788190&z=16">Farg’ona shahar Terakmozorni orqasida Marg’ilon soy bo’yida Bolajaon parki ichida</a>

Telefon raqam: 78 888 9 888""",
        parse_mode='HTML'
    )

def expert_with_contact(update,context):
    update.message.reply_text(
        text="""
        Tizim vaqtinchalik ish faoliyatida emas. 

78 888 9 888 raqami orqali bog'lanishingizni so'raymiz!
        """
    )

# Markaz haqida bo'limi buttonlari

def general_data(update,context):
    update.message.reply_text(
        text="""
        ❓ <b>Nima uchun «Najot Ta'lim»?</b>

Buyuk olim va muhaddis Imom Buxoriyning <b>"Ilmdan o'zga najot yo'q va bo'lmagay!"</b> degan jumlalari markaz nomi uchun asos qilib olingan, ya'ni markaz xalq va jamiyat uchun najot kemasi vazifasini bajarsin, degan maqsadda <b>"Najot Ta'lim"</b> nomi tanlangan.

ℹ️ <b>Hozirda "Najot Ta'lim" markazining umumiy hisobda 4 ta filiali mavjud</b>

<b>• «Najot Ta'lim»</b> markazi 2018-yilning oktyabr oyida <b>120 kv. metr</b> maydonga ega 4 xonali joyda ish boshlagan.

<b>•</b> 2019-yilda <b>450 kv. metr</b> maydonga ega <b>«Najot Ta'lim»</b> <b>Chimboy filiali</b> o'z ish faoliyatini boshladi.

<b>•</b> 2020-yilda <b>1000 kv. metr</b> maydonga ega <b>«Najot Ta'lim»</b> <b>Xadra filiali</b> o'z ish faoliyatini boshladi.

<b>•</b> 2021-yilda <b>3000 kv. metr</b> maydonga ega <b>«Najot Ta'lim»</b> <b>Chilonzor filiali</b> o'z ish faoliyatini boshladi.

<b>•</b> 2022-yilda <b>1500 kv. metr</b> maydonga ega <b>«Najot Ta'lim»</b> markazining <b>Farg'ona filiali</b> o'z ish faoliyatini boshladi. Bu <b>«Najot Ta'lim»</b>ning viloyatlardagi ilk filiali hisoblanadi.
        """,
    parse_mode="HTML",
    )

def achievement(update,context):
    update.message.reply_text(
        text="""
        📊 Shu kungacha kurslarni muvaffaqiyatli bitirganlar soni: <b>3000+</b>

🔥 Shu kungacha bitirgan o'quvchilarning ishga joylashishi: <b>70-80%</b>

🏆 2020-yilda <b>«Yil brendi»</b> nominatsiyasi g'olibi.

🏆 2021-yilda <b>«Eng yaxshi IT maktab»</b> nominatsiyasi g'olibi.

🎯 <b>"Osmondagi bolalar"</b> loyihasi muallifi.

🏅 <b>"Osmondagi bolalar"</b> loyihasi «Tahsin» mukofoti sovrindori.

🥈 YouTube kumush tugmasi.

🏅 2021-yilda <b>"Osmondagi bolalar"</b> loyihasi «Yil kanali» deb e'tirof etildi.

🎙 <b>"Alohida mavzu"</b> loyihasi muallifi.""",
    parse_mode='HTML',
    )

def programming(update,context):
    context.user_data['page'] = "Dasturlash"
    buttons = [
        [KeyboardButton(text='Dasturlash kasbiy ta\'lim'),KeyboardButton(text='Frontend:React')],
        [KeyboardButton(text='Frontend:Vue'),KeyboardButton(text='Backend:Nodejs')],
        [KeyboardButton(text='Backend:Python'),KeyboardButton(text='QA ( quality assurance )')],
        [KeyboardButton(text='🔙 Orqaga')]
    ]


    update.message.reply_text(
        text="""
        🖥 Dasturlash yo'nalishida mavjud kurslarimiz:

<b>Chuqulashtirilgan, intensiv:</b>
1. Dasturlash kasbiy ta'lim

<b>Odatiy kurslar:</b>
1. Frontend: React
2. Frontend: Vue
3. Backend: NodeJs
4. Backend: Java
5. Backend: Python
6. QA ( quality assurance )

Kurslar haqida batafsil ma'lumot olish uchun quyidagi bo'limlardan birini tanlang.
        """,
        parse_mode='HTML',
        reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
    )

def design(update,context):
    buttons = [
        [KeyboardButton(text='Bootcamp Grafik Dizayn'),KeyboardButton(text='Odatiy Grafik Dizayn kursi')],
        [KeyboardButton(text='Moushn Grafika'),KeyboardButton(text='🔙 Orqaga')]
    ]

    update.message.reply_text(
        text="""📏 <b>Dizayn yo'nalishida mavjud kurslarimiz:</b>

<b>1. Bootcamp Grafik Dizayn</b>
<b>2. Odatiy Grafik Dizayn kursi</b>
<b>3. Moushn Grafika</b>
<b>4. Bootcamp: Web Design UX/UI</b>

Kurslar haqida batafsil ma'lumot olish uchun quyidagi bo'limlardan birini tanlang.""",
    parse_mode='HTML',
    reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
    )

def marketing(update,context):
    context.user_data['page'] = "Marketing"
    buttons = [
        [KeyboardButton(text='SMM Pro'),KeyboardButton(text='🔙 Orqaga')]
    ]
    update.message.reply_text(
        text="""📊<b>Marketing yo'nalishida mavjud kurslarimiz:</b>

<b>1. SMM Pro</b>

Kurslar haqida batafsil ma'lumot olish uchun quyidagi bo'limlardan birini tanlang.""",
    parse_mode='HTML',
    reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
    )

def programming_education(update,context):
    context.user_data['page'] = 'Dasturlash kasbiy ta\'lim'
    buttons = [
        [KeyboardButton(text='Bootcamp-foundation'),KeyboardButton(text='Bootcamp result')],
        [KeyboardButton(text='Dastur narxi'),KeyboardButton(text='Kerakli kompyuter')],
        [KeyboardButton(text='🔙 Orqaga')]
    ]
    update.message.reply_text(
        text="""1 yillik kasbiy ta’lim dasturi 2 bosqichdan iborat bo’lib, bular: <b>Bootcamp foundation</b> va <b>Bootcamp result’dan</b> iborat. Darslar Chilonzor filialida bo’lib o'tadi.""",
        parse_mode='HTML',
        reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
    )


