from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext
from main import db, logger
from keyboards import *
from steps import CHOOSING_ACTION, VOTING


def vote_choice(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user = update.message.from_user
    text = update.message.text
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    try:
        user_data['vote_number'] = int(text)
        update.message.reply_text(f'ok', reply_markup=markup_stars)
        return VOTING
    except:
        update.message.reply_text("Error! Enter valid number ", reply_markup=ReplyKeyboardRemove(), )
        return VOTING


def voting(update: Update, context: CallbackContext):
    user_data = context.user_data
    text = update.message.text
    user = update.message.from_user
    logger.info("Location of %s: %s", user.username, update.message.text)
    try:

        user_data['stars'] = int(text)
        if user_data['kind'] == "Games":

            db.connect()
            db.star_game(user_data['vote_number'], user_data['stars'])
            db.conn.close()
            update.message.reply_text(f'Thank You  !', reply_markup=markup_show)
            return CHOOSING_ACTION
        else:
            db.connect()
            db.star(user_data['vote_number'], user_data['stars'])
            db.conn.close()
            update.message.reply_text(f'Thank You  !', reply_markup=markup_show)
            return CHOOSING_ACTION
    except:
        update.message.reply_text("Error! Please try again later", reply_markup=ReplyKeyboardRemove(), )
        return ConversationHandler.END
