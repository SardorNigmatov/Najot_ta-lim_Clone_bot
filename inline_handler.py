from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from data import react_data

def registration(update,context):
    text = "<b>Dasturlash intensiv</b> kursiga ro'yxatdan o'tishdan oldin ushbu havola orqali kurs haqida tanishib chiqishingizni so'raymiz.\n\n 👉 https://telegra.ph/Dasturlash-kasbiy-talim-11-26"
    button = [
         [InlineKeyboardButton(text='✅ Kurs bilan tanishib chiqdim!',callback_data='register')]
    ]
    update.message.reply_text(text=f"{text}",parse_mode='HTML',reply_markup=InlineKeyboardMarkup(button))

def react(update,context):
    buttons = [
        [InlineKeyboardButton(text='Imkoniyatlar',callback_data='react_chance'),InlineKeyboardButton(text='Ishga joylashish',callback_data='react_work')],
        [InlineKeyboardButton(text='Kurs narxi',callback_data='react_price'),InlineKeyboardButton(text='Kerakli kompyuter',callback_data='react_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish",callback_data='advantages_registration')]
    ]
    update.message.reply_text(
        text="""
        <b>React kursi 8 oy bo’lib, haftada 3 kun 1 soat-u 50 daqiqadan bo’lib o’tadi. Kurs davomida siz:</b>

- Dasturchiga oid ma’lum bir ko’nikmalar, Algoritmlar, dasturlash va uning mashhur yo’nalishlari bo'yicha tushuncha
- HTML, CSS 
- SASS, BOOTSTRAP
- JAVASRCIPT Core
- JAVASCRIPT DOM, Native
- REACT, REDUX, TYPESCRIPT kabi bilimlar va ko’nikmalarga ega bo’lasiz.""",
    parse_mode='HTML',
    reply_markup=InlineKeyboardMarkup(buttons)
    )

def vue(update,context):
    buttons = [
        [InlineKeyboardButton(text='Imkoniyatlar', callback_data='vue_chance'),
         InlineKeyboardButton(text='Ishga joylashish', callback_data='vue_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='vue_price'),
         InlineKeyboardButton(text='Kerakli kompyuter', callback_data='vue_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]
    update.message.reply_text(
        text="""
            <b>Kurs 8 oy bo’lib, haftada 3 kun 1 soat-u 50 daqiqadan bo’lib o’tadi. Kurs davomida siz:</b>

    - kompyuter savodxonligi darsi, Algoritmlar, barcha yo'nalishlar bo'yicha tushuncha
- HTML, CSS
- SASS, Tailwind CSS
- JAVASRCIPT Core
- JAVASCRIPT DOM, Native
- Vue JS, VueX , Pinia kabi bilimlarga ega bo’lasiz.""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def backend_nodejs(update,context):
    buttons = [
        [InlineKeyboardButton(text='Imkoniyatlar', callback_data='nodejs_chance'),
         InlineKeyboardButton(text='Ishga joylashish', callback_data='nodejs_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='nodejs_price'),
         InlineKeyboardButton(text='Kerakli kompyuter', callback_data='nodejs_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]
    update.message.reply_text(
        text="""
                <b>Kurs 8 oy bo’lib, haftada 3 kun 1 soat-u 50 daqiqadan bo’lib o’tadi. Kurs davomida siz:</b>

- Kompyuter savodxonligi darsi, Algoritmlar, barcha yo'nalishlar bo'yicha tushuncha
- JAVASCRIPT boshlang'ich tushunchalari
- JAVASRCIPT DOM
- DATABASE (PostgrSQL va MongoDB)
- NodeJS
- ORM, ODM, REDIS, TypeScript kabi bilimlar va ko’nikmalarga ega bo’lasiz.""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def backend_python(update,context):
    buttons = [
        [InlineKeyboardButton(text='Imkoniyatlar', callback_data='python_chance'),
         InlineKeyboardButton(text='Ishga joylashish', callback_data='python_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='python_price'),
         InlineKeyboardButton(text='Kerakli kompyuter', callback_data='python_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]
    update.message.reply_text(
        text="""
                    <b>Kursi 8 oy bo’lib, haftada 3 kun 1 soat-u 50 daqiqadan bo’lib o’tadi. Kurs davomida siz:</b>

- Kompyuter savodxonligi darsi, Algoritmlar, barcha yo'nalishlar bo'yicha tushuncha
- Python dasturlash tilining boshlang'ich tushunchalari
- Pythonda OOP va Ma'lumotlar bazasi bilan ishlash
- Django framework
- Web application in Django va Telegram bot""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def qa(update,context):
    buttons = [
        [InlineKeyboardButton(text='Imkoniyatlar', callback_data='qa_chance'),
         InlineKeyboardButton(text='Ishga joylashish', callback_data='qa_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='qa_price'),
         InlineKeyboardButton(text='Kerakli kompyuter', callback_data='qa_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]
    update.message.reply_text(
        text="""
                        <b>QA kursi 4 oy bo'lib (oxirgi oy amaliyot), haftada 3 kun 2 soatdan davom etadi.</b>

Kurs davomida siz:

Bo’lajak dasturiy ta’minot testlovchisi (QA engineer) bo’lib yetishishingiz davomida quyidagi bilimlarni chuqur egallaysiz:

• Dasturiy ta’minotlarni testlashda xatoliklarni aniqlash va ularni sifatli tarzda dasturchilarga taqdim etish usullarini;
• Sifatli test case, check-list, test report (tekshiruv hujjatlari) yozishni;
• Dasturiy ta’minotning boshlang’ich holatidan yakuniy holatigacha bo’lgan sifat nazoratini to’g’ri boshqara olishni;
• Dasturiy ta’minotlarni dinamik va statik tarzda tekshirish;
• Kompaniya ichki sifat nazorati standartlarini amalda tatbiq qilishni;
• Dasturiy ta’minotlarning UX jarayonini sifatli nazorat qila olishni;
• Mutaxassis sifatida muhim hisoblangan tekshiruv texnikalarini, amaliy ko’nikma o’rganasiz va loyiq maosh asosida ish o’rniga ega bo’lasiz.""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def boot_grafik_dizayn(update,context):
    buttons = [
        [InlineKeyboardButton(text='Bilimlar',callback_data='boot_knowledge'),InlineKeyboardButton(text='Imkoniyatlar', callback_data='boot_chance')],
        [InlineKeyboardButton(text='Ishga joylashish', callback_data='boot_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='boot_grafik_price'),InlineKeyboardButton(text='Kerakli kompyuter', callback_data='boot_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]

    update.message.reply_text(
        text="""
                            <b>Bootcamp Grafik Dizayn kursimiz 8 oydan iborat bo'lib, haftada 5 kun 3-4 soatdan bo’ladi</b>

Kurs davomida o'rgatiladigan bilimlar haqida ma'lumot olish uchun quyidagi tugmani bosing:""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def oddiy_grafik_dizayn(update,context):
    buttons = [
        [InlineKeyboardButton(text='Bilimlar',callback_data='oddiy_knowledge'),InlineKeyboardButton(text='Imkoniyatlar', callback_data='oddiy_chance')],
        [InlineKeyboardButton(text='Ishga joylashish', callback_data='oddiy_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='oddiy_grafik_price'),InlineKeyboardButton(text='Kerakli kompyuter', callback_data='oddiy_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]

    update.message.reply_text(
        text="""
                            <b>Odatiy tarzda o’tiladigan grafik dizayn kursimiz 7 oydan iborat bo'lib, oxirgi oy amaliyotdan iborat. Haftada 3 kun 1 soat 50 daqiqadan davom etadi.</b>

Kurs davomida o'rgatiladigan bilimlar haqida ma'lumot olish uchun quyidagi tugmani bosing:""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def moushn_dizayn(update,context):
    buttons = [
        [InlineKeyboardButton(text='Bilimlar',callback_data='moushn_knowledge'),InlineKeyboardButton(text='Imkoniyatlar', callback_data='moushn_chance')],
        [InlineKeyboardButton(text='Ishga joylashish', callback_data='moushn_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='moushn_price'),InlineKeyboardButton(text='Kerakli kompyuter', callback_data='moushn_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]

    update.message.reply_text(
        text="""
                            <b>Moushn grafika</b>

Moushn grafika kursimiz 8 oydan iborat bo'lib (oxirgi oy amaliyot), haftada 3 kun 3 soat  davom etadi.

Kurs davomida o'rgatiladigan bilimlar haqida ma'lumot olish uchun quyidagi tugmani bosing:""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def smm_pro(update,context):
    buttons = [
        [InlineKeyboardButton(text='Bilimlar',callback_data='smm_knowledge'),InlineKeyboardButton(text='Imkoniyatlar', callback_data='smm_chance')],
        [InlineKeyboardButton(text='Ishga joylashish', callback_data='smm_work')],
        [InlineKeyboardButton(text='Kurs narxi', callback_data='smm_price'),InlineKeyboardButton(text='Kerakli kompyuter', callback_data='smm_computer')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data='advantages_registration')]
    ]

    update.message.reply_text(
        text="""
                           SMM Pro kursi  4 oydan iborat bo'lib, haftada 3 kun 1  soat 50 daqiqa davom etadi.

Kurs davomida o'rgatiladigan bilimlar haqida ma'lumot olish uchun quyidagi tugmani bosing:""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def bootcamp_foundation(update,context):
    buttons = [
        [InlineKeyboardButton(text='🎁 Bonus darslar',callback_data='bootcamp_bonus')],
        [InlineKeyboardButton(text='C dasturlash tili asoslari',callback_data='bootcamp_c'),InlineKeyboardButton(text='Python dasturlash tili asoslari',callback_data='bootcamp_python')],
        [InlineKeyboardButton(text="Qo'shimcha bilimlar",callback_data='bootcamp_knowledge'),InlineKeyboardButton(text='Kurs yakunidagi natija',callback_data='bootcamp_result')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish",callback_data='advantages_registration')]
    ]

    update.message.reply_text(
        text="""
       <b>Bootcamp foundation bosqichi</b>

Ushbu bosqich dasturlashga ilk qadam qo’yayotganlar uchun hisoblanadi. Bu bosqichda <b>C va Python dasturlash tillarining asoslari</b> o’rgatiladi va <b>bonus tarzida</b> kompyuter savodxonligi darslari taqdim etiladi.

Bootcamp foundation bosqichida dasturlash <b>strukturasi, dasturlash mantig'i, uning algoritmi,</b> dastur yaratilgandan keyin uning orqa fonida qanday prosseslar bo'layotganini to'laqonli tarzda <b>anglab yetasiz.</b>

Bootcamp foundation bosqichi sizga dasturlashning ma’lum bir <b>yo’nalishini tanlashingizda</b> yordam bo’ladi. Masalan, siz uchun frontend qulaymi yoki backend bilib olasiz. Buni bilish bilan birgalikda, mutaxassislik kursimizda mavzularni <b>qiynalmasdan o'zlashtirasiz</b  >, sababi siz, dasturlash mantig’ini bilasiz va bu bosqichdan so’ng boshqa dasturlash tillarini oson o’zlashtirishingiz mumkin.

Bootcamp foundation bosqichi — <b>5 oydan</b> iborat bo'lib, haftada <b>5 kun 2-3 soatdan</b> davom etadi. Quyidagi tugmalar orqali beriladigan bilimlar bilan tanishishingiz mumkin;
        """,
    parse_mode='HTML',
    reply_markup=InlineKeyboardMarkup(buttons)
    )

def bootcamp_result(update,context):
    buttons = [
        [InlineKeyboardButton(text='Bilimlar',callback_data='result_knowledge'),InlineKeyboardButton(text='Ishga joylashish',callback_data='result_work')],
        [InlineKeyboardButton(text='Imkoniyatlar',callback_data='result_chance')],
        [InlineKeyboardButton(text="✅ Ro'yxatdan o'tish",callback_data='advantages_registration')],
    ]
    update.message.reply_text(
        text="""<b>Bootcamp result bosqichi</b>

Bootcamp foundation bosqichi yakunlangandan so’ng o’quvchilardan Bootcamp result bosqichiga o’tish uchun yakuniy imtihon olinadi va bu vaqt mobaynida qisqa ta’til beriladi.

<b>Bootcamp result bosqichi 6 oydan iborat bo'lib, haftada 5 kun 3-4 soatdan davom etadi.</b>

Bu bosqichimizda 6 ta yo’nalish mavjud bo’lib, o’quvchi o’zining qiziqishlari va ustozlarning tavsiyasiga ko’ra yo’nalishlardan birini tanlab o’qishni davom ettiradi.

1. Fullstack (NodeJS + Vuejs)
2. Frontend
3. Flutter Mobile
4. Go (Golang) backend
5. C# .NET (dotnet) backend""",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def dastur_price(update,context):
    update.message.reply_text(
        text="""
        Farg'ona filiali uchun kurs narxi:

🔰 Kurs narxi oyiga: 1 mln 850 ming so'm.
🔰 Ikkiga bo’lib to’lash: 8 mln 500 ming so’m (Jami: 17 mln so'm) (3 mln 350 ming so’m tejab qolasiz)
🔰 Bittada umumiy toʻlov qilinsa: 16 mln 150 ming so'm (4 mln 200 ming so’m tejab qolasiz) 

Kurs narxi: (Toshkent filiali uchun)

🔰Odindan oyma-oy: 2 mln 300 ming so’m  
🔰Oldindan 2 marta to'lov: 10 mln 580 ming so’m 
🔰Oldindan bittada: 20 mln 100 ming so’m
        """
    )

def must_computer(update,context):
    update.message.reply_text(
        text="""🔰 <b>Dasturlash uchun talab qilinadigan minimum noutbuk, agar yangi olmoqchi bo’lsangiz:</b>

- Kami bilan Core i5 (10-avlod) yoki AMD Ryzen 5 (Core i7 bo’lsa yaxshi)
- Tezkor xotira RAM kami bilan 8GB (16 bo'lsa yaxshi)\- Asosiy Xotira SSD kami bilan 256 GB

🔰 <b>Agar Apple MacBook olmoqchi bo’lsangiz va pulingiz yetarli bo’lsa:</b>

- Kami bilan M1 Protsessor
- Kami bilan 8GB RAM xotira
- Kami bilan 256GB doimiy SSD xotira

🔰 <b>Agar oldingi kompyuteringiz bo’lsa uning texnik holatini quyidagilarga keltirib olishingiz maqsadga muvofiq:</b>

- RAM xotira 8GB kamida;
- Agar HDD xotira bo’lsa, uni kamida 256GB SSDga almashtirish yoki HDD yoniga o’rnatish""",
        parse_mode='HTML'
    )

