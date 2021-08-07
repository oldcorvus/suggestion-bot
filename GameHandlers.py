from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext
from main import db, logger
from keyboards import *
from steps import CHOOSING_ACTION, CHOOSING_KIND, TYPING_REPLY_FREE_SUGGEST, CHOOSING_GAME_GENRE, \
    CHOOSING_ACTION_GAME, CHOOSING_PLATFORM, TYPING_VOTE_CHOICE


def game_action(update: Update, context: CallbackContext):
    user_data = context.user_data
    user = update.message.from_user
    text = update.message.text
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    if text == "Vote":
        user_data['vote'] = "true"
        update.message.reply_text(f'ok please type the id  !', reply_markup=ReplyKeyboardRemove())
        return TYPING_VOTE_CHOICE
    elif text == "Return":
        update.message.reply_text(f'ok', reply_markup=markup_kind_action)
        return CHOOSING_ACTION


def game_genres(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    text = update.message.text
    user_data['Game_Genre'] = text
    user = update.message.from_user
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    try:
        if user_data['Game_Genre'] == "Return":
            update.message.reply_text("ok", reply_markup=markup_platform)
            return CHOOSING_PLATFORM
        if user_data['action'] == "suggest something":
            update.message.reply_text("ok please type", reply_markup=ReplyKeyboardRemove())
            return TYPING_REPLY_FREE_SUGGEST
        else:
            db.connect()
            items = db.get_games(user_data['Game_Genre'], user_data['platform'])
            db.conn.close()
            temp = "Platform: " + user_data['platform'] + "         Genre:   " + user_data['Game_Genre'] + "\n\n\n  "
            for x in items:
                temp += str(x[4]) + "  ---  " + x[0] + "   Votes: " + str(x[3]) + "\n\n"
            if temp == "":
                temp = "Thanks"
            update.message.reply_text(temp, reply_markup=markup_show)
            return CHOOSING_ACTION_GAME
    except:
        update.message.reply_text("Error! Please try again later", reply_markup=ReplyKeyboardRemove(), )
        return ConversationHandler.END


def choosing_platform(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    platform = 'platform'
    text = update.message.text
    user_data[platform] = text
    user = update.message.from_user
    logger.info("Location of %s: %s", user.first_name, update.message.text)

    if user_data['platform'] == "Return":
        update.message.reply_text("ok", reply_markup=markup_kind)
        return CHOOSING_KIND
    update.message.reply_text("ok please choose genre", reply_markup=markup_genres_games)
    return CHOOSING_GAME_GENRE
