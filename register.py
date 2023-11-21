# elif button_data == 'register':
# buttons = [
#     [InlineKeyboardButton(text="Toshkent", callback_data='toshkent'),
#      InlineKeyboardButton(text="Farg'ona", callback_data='fargana')],
# ]
# query.message.reply_text(text=f"""
#         ✅ Judayam yaxshi, {first_name}.
#
#     📍 Siz qaysi filialimizda ta'lim olmoqchisiz?
#         """,
#                          reply_markup=InlineKeyboardMarkup(buttons))
# context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
# elif str(button_data) == "toshkent" or str(button_data) == "fargana":
# button = [
#     InlineKeyboardButton(text='4-iyun', callback_data='date')
# ]
# context.bot.send_message(chat_id=chat_id, text="""
#         📍 Siz, Toshkent filialini tanladingiz.
#
#     📅 Qaysi sanadagi imtihonga tashrif buyurmoqchisiz?
#         """,
#                          reply_markup=InlineKeyboardMarkup(button))
# context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
# elif button_data == "date":
# buttons = [
#     [InlineKeyboardButton(text="10:00", callback_data='ten'),
#      InlineKeyboardButton(text="14:00", callback_data="fourteen")]
# ]
# query.message.reply_text(
#     text="""📅 Siz, 4-iyun sanasida bo'ladigan imtihonni tanladingiz.
#
#     🕰 Qaysi vaqtdagi imtihonga tashrif buyurmoqchisiz?""",
#     reply_markup=InlineKeyboardMarkup(buttons)
# )
# context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
# elif button_data == "ten" or button_data == "fourteen":
# query.message.reply_text(
#     text="""🎉 Tabriklaymiz! Intensiv dasturlash kursi imtihoni uchun muvaffaqiyatli ro'yxatdan o'tdingiz.
#
#     Filial: Toshkent
#     Sana: 4-iyun
#     Soat: 10:00
#     Manzil:
#      📍 <a href="https://maps.google.com/maps?q=41.285547,69.203981&ll=41.285547,69.203981&z=16">«Najot Ta'lim» Chilonzor filiali</a>:Toshkent shahar, Chilonzor tumani, Qatortol ko'chasi
#     Mo'ljal: Rayhon milliy taomlar qarshisida
#
#     Imtihon manziliga kamida yarim soat oldin, shaxsingizni tasdiqlovchi hujjat va 30 ming so'm imtihon to'lovi bilan borishingizni so'raymiz.
#
#     Passport yoki ID kartangiz bo'lmasa, tug'ilganlik haqidagi guvohnoma va bir dona 3:4 hajmdagi rasm bilan kelishingiz so'raladi"""
# )
# context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)