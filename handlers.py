from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext

from main import db as db, logger, facts_to_str, bot, ADMIN
from keyboards import *
from steps import CHOOSING_ACTION, CHOOSING_KIND, TYPING_REPLY_FREE_SUGGEST, CHOOSING_GAME_GENRE, CHOOSING_GENRE, \
    CHOOSING_PLATFORM, TYPING_VOTE_CHOICE, ADMIN_ACTION


def user_suggested(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_data = context.user_data
    text = update.message.text
    user_data['Suggested'] = text
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    if user_data['kind'] == "Games":
        db.connect()
        suggested = db.add_game(user_data['Suggested'], user_data['Game_Genre'], user_data['platform'])
        bot.sendMessage(chat_id=ADMIN, text=suggested)
        db.conn.close()
        update.message.reply_text("thanks", reply_markup=markup_genres_games, )
        return CHOOSING_GAME_GENRE

    if user_data['kind'] == "Book":
        db.connect()
        suggested = db.add_item(user_data['Suggested'], user_data['Genre'], user_data['kind'], user_data['action'])
        bot.sendMessage(chat_id=ADMIN, text=suggested)
        db.conn.close()
        update.message.reply_text("thanks", reply_markup=markup_add_book_genres, )
        return CHOOSING_GENRE
    else:
        db.connect()
        suggested = db.add_item(user_data['Suggested'], user_data['Genre'], user_data['kind'], user_data['action'])
        bot.sendMessage(chat_id=ADMIN, text=suggested)
        db.conn.close()
        update.message.reply_text("thanks", reply_markup=markup_genres_add, )
        return CHOOSING_GENRE


def done(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user = update.message.from_user
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    logger.info("Location of %s: %s", user.first_name, facts_to_str(user_data))
    update.message.reply_text(
        "until next time!",
        reply_markup=ReplyKeyboardRemove(),
    )
    user_data.clear()
    return ConversationHandler.END


def choosing_genre(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_data = context.user_data
    text = update.message.text
    user_data['Genre'] = text
    logger.info("Location of %s: %s", user.first_name, update.message.text)

    if user_data['Genre'] == "Return":

        if user_data['kind'] == "Book":
            update.message.reply_text("ok", reply_markup=markup_kind, )

            return CHOOSING_KIND

        update.message.reply_text("ok", reply_markup=markup_kind, )

        return CHOOSING_KIND

    elif user_data['Genre'] == "all":

        db.connect()
        items = db.get_all_items(user_data['kind'])
        db.conn.close()
        counter = 0
        temp = "Type: " + user_data['kind'] + "\n\n\n"
        for x in items:
            temp += " <b>" + str((x[5])) + "</b>" + "  ---  " + x[0] + "       " + "Genre:   " + x[
                1] + "  Votes: " + str(x[4]) + "\n\n"
            counter = counter + 1
            if counter == 25:
                counter = 0
                update.message.reply_text(temp, reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
                temp = ""
        if temp == "\n" or temp == "":
            temp = "Thanks"

        update.message.reply_text(temp, reply_markup=markup_show, parse_mode='HTML')
        return CHOOSING_ACTION
    elif user_data['action'] == "suggest something":
        update.message.reply_text("ok please type", reply_markup=ReplyKeyboardRemove())
        return TYPING_REPLY_FREE_SUGGEST

    elif user_data['action'] == "peoples suggestions":

        db.connect()
        counter = 0
        items = db.get_items(user_data['Genre'], user_data['kind'])
        db.conn.close()
        temp = "Type: " + user_data['kind'] + "         Genre:   " + user_data['Genre'] + "\n\n\n  "
        for x in items:
            temp += " <b>" + str((x[5])) + "</b>" + "  ---  " + x[0] + "       " + "Genre:   " + x[
                1] + "  Votes: " + str(x[4]) + "\n\n"
            counter = counter + 1
            if counter == 25:
                counter = 0
                update.message.reply_text(temp, reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
                temp = ""
        if temp == "\n" or temp == "":
            temp = "Thanks"
        update.message.reply_text(temp, reply_markup=markup_show, parse_mode='HTML')
        return CHOOSING_ACTION


def start(update: Update, _: CallbackContext) -> int:
    if update.message.from_user.username == ADMIN:
        update.message.reply_text(
            "Hi!.Welcome ",
            reply_markup=markup_admin
        )
        return ADMIN_ACTION

    else:
        update.message.reply_text(
            "Hi!. Welcome ",
            reply_markup=markup_kind_action
        )

    print(CHOOSING_ACTION)
    return CHOOSING_ACTION


def regular_choice(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user = update.message.from_user
    text = update.message.text
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    user_data['action'] = text
    if user_data['action'] == "Vote":
        update.message.reply_text(f'ok please type the id  !', reply_markup=ReplyKeyboardRemove())
        return TYPING_VOTE_CHOICE
    elif user_data['action'] == "Return":
        update.message.reply_text(f'ok', reply_markup=markup_kind_action)
        return CHOOSING_ACTION
    elif user_data['action'] == "Games":
        update.message.reply_text(f'ok choose the platform  !', reply_markup=markup_kind)
        return CHOOSING_PLATFORM
    else:
        update.message.reply_text(f'ok choose the kind  !', reply_markup=markup_kind)
        return CHOOSING_KIND


def choosing_kind(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    text = update.message.text
    user_data['kind'] = text
    user = update.message.from_user
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    try:
        if user_data['kind'] == "Return":
            update.message.reply_text("ok", reply_markup=markup_kind_action)
            return CHOOSING_ACTION
        if user_data['kind'] == "Games":
            update.message.reply_text("ok please choose the platform", reply_markup=markup_platform)
            return CHOOSING_PLATFORM
        if user_data['action'] == "suggest something":
            if user_data['kind'] == "Book":

                update.message.reply_text("ok please choose genre", reply_markup=markup_add_book_genres, )
                return CHOOSING_GENRE
            else:
                update.message.reply_text("ok please choose genre", reply_markup=markup_genres_add)
        else:
            if user_data['kind'] == "Book":
                update.message.reply_text("ok please choose genre", reply_markup=markup_book_genres, )
                return CHOOSING_GENRE
            update.message.reply_text("ok please choose genre", reply_markup=markup_genres)
        return CHOOSING_GENRE
    except:
        update.message.reply_text("Error! Please try again later", reply_markup=ReplyKeyboardRemove(), )
        return ConversationHandler.END


def done(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user = update.message.from_user
    logger.info("Location of %s: %s", user.first_name, update.message.text)
    logger.info("Location of %s: %s", user.first_name, facts_to_str(user_data))
    update.message.reply_text(
        "until next time!",
        reply_markup=ReplyKeyboardRemove(),
    )
    user_data.clear()
    return ConversationHandler.END
