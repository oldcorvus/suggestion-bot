from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from main import db
from keyboards import *
from steps import ADMIN_CHOICE, ADMIN_ACTION, ADMIN_EDIT


def admin_action(update: Update, context: CallbackContext):
    text = update.message.text
    user_data = context.user_data
    user_data['Admin_Choice'] = text
    update.message.reply_text(f'ok please type the id  !', reply_markup=ReplyKeyboardRemove())
    return ADMIN_CHOICE


def admin_choice(update: Update, context: CallbackContext):
    text = update.message.text
    user_data = context.user_data
    user_data['Item_Id'] = text
    if user_data['Admin_Choice'] == "Delete":
        db.connect()
        db.delete_item(int(user_data['Item_Id']))
        db.conn.close()
        update.message.reply_text(f'Thank You  !', reply_markup=markup_kind_action)
        return ADMIN_ACTION
    elif user_data['Admin_Choice'] == "Confirm":
        db.connect()
        db.confirm(int(user_data['Item_Id']))
        db.conn.close()
        update.message.reply_text("thanks", reply_markup=markup_admin, )
        return ADMIN_ACTION
    elif user_data['Admin_Choice'] == "Confirm Game":
        db.connect()
        db.confirm_game(int(user_data['Item_Id']))
        db.conn.close()
        update.message.reply_text("thanks", reply_markup=markup_admin, )
        return ADMIN_ACTION
    elif user_data['Admin_Choice'] == "Edit":
        update.message.reply_text(f'ok name:', reply_markup=ReplyKeyboardRemove(), )
        return ADMIN_EDIT


def admin_edit(update: Update, context: CallbackContext):
    text = update.message.text
    user_data = context.user_data
    user_data['Edited'] = text
    db.connect()
    db.edit(user_data['Item_Id'], user_data['Edited'])
    db.conn.close()
    update.message.reply_text("thanks", reply_markup=markup_admin, )
    return ADMIN_ACTION
