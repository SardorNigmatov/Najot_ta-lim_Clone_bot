from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import BotCommand, KeyboardButton, ReplyKeyboardMarkup
from message_handler import message_handler
from pagination import  button_press
from config import TOKEN

def start_command(update,context):

    commands = [
        BotCommand(command='start',description='start'),
        BotCommand(command='help',description='help'),
    ]

    buttons = [
        [KeyboardButton(text='Markaz haqida'),KeyboardButton(text='Kurslarimiz')],
        [KeyboardButton(text='Filliallarimiz'),KeyboardButton(text='Mutaxassis bilan aloqa')],
        [KeyboardButton(text="Imtihonga ro'yxatdan o'tish")]
    ]
    context.bot.set_my_commands(commands=commands) # botga kommandalarni o'rnatish
    update.message.reply_text(text='Asosiy Menu:',reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True))




def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start',start_command)) # start komandasi ishga tushadigan fuunksiya
    dispatcher.add_handler(MessageHandler(Filters.text,message_handler)) # message kelganda ishga tushadigan funksiya
    dispatcher.add_handler(CallbackQueryHandler(button_press)) # inline buttonlar uchun ishlaydigan funksiya

    updater.start_polling() # botni serverga ulaydi yangilanishlarni olub kelib turadi
    updater.idle() # sever bilan aloqani uzadi va kelgan yangilanishlatni kutib turishini taminlydi

if __name__ == '__main__':
    main() # aynan shu faylni run qilish uchun ishlatilinadi


