import logging
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)
from DbHandler import DBHelper

db = DBHelper()

import telegram


# Add your token here
TOKEN = "REPLACETOKEN"
# Add Admin's id here
ADMIN = "ADMINID"
bot = telegram.Bot(TOKEN)



def facts_to_str(user_data):
    """Helper function for formatting the gathered user info."""
    facts = [f'{key} - {value}' for key, value in user_data.items()]
    return "\n".join(facts).join(['\n', '\n'])


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
from GameHandlers import *
from handlers import *
from VoteHandlers import *
from AdminHandlers import *
from steps import *

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    db.setup()
    db.conn.close()

    # Add conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING_ACTION: [
                MessageHandler(
                    Filters.regex(
                        '^(|Vote|Return|suggest something|peoples suggestions)$'),
                    regular_choice
                ),
            ],
            CHOOSING_KIND: [
                MessageHandler(
                    Filters.regex('^(Return|movies|series|mini series|anime animation|Book|Games)$'), choosing_kind
                ),

            ],
            ADMIN_ACTION: [

                MessageHandler(
                    Filters.regex(
                        '^(Delete|Edit|Confirm|Confirm Game|Done)$'),
                    admin_action
                ),

            ],
            ADMIN_CHOICE: [

                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    admin_choice
                )
            ],
            ADMIN_EDIT: [

                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    admin_edit
                )
            ],
            CHOOSING_ACTION_GAME: [

                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    game_action
                )
            ],

            CHOOSING_GENRE: [
                MessageHandler(
                    Filters.regex(
                        '^(Return|Sci_fiction|Comedy|Horror|Drama|Musical|Thriller_Drama|Drama_Mystery|Mystery_Crime'
                        '|Drama_Romance|Biography|Action|all|Thriller|Action and Adventure '
                        '_Fiction|History_Fiction|anthology_Fiction|Childrens_Fiction|Crime_Fiction|Drama_Fiction'
                        '|Fantasy_Fiction|Horror_Fiction|Romance_Fiction|Poetry_Fiction|Poetry_Fiction|Short '
                        'Story_Fiction|Biography_NonFiction|Diary_NonFiction|History_NonFiction|Memoir_NonFiction'
                        '|Philosphy_NonFiction|Sprituality_NonFiction|True Crime_NonFiction|Self '
                        'Help_NonFiction|Other_NonFiction)$'),
                    choosing_genre
                ),

            ],
            VOTING: [
                MessageHandler(
                    Filters.regex('^(1|2|3|4|5|6|7|8|9|10|Return)$'), voting
                ),

            ],
            CHOOSING_PLATFORM: [
                MessageHandler(
                    Filters.regex('^(Return|PC|Consoles|Mobile Phones)$'), choosing_platform
                ),

            ],

            CHOOSING_GAME_GENRE: [
                MessageHandler(
                    Filters.regex('^(Open World|Horror|Racing|FPS|Sport|Strategy|Return)$'), game_genres
                ),

            ],

            TYPING_VOTE_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    vote_choice
                )
            ],
            TYPING_REPLY_FREE_SUGGEST: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    user_suggested
                )
            ],

        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot

    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
