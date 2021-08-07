from telegram import ReplyKeyboardMarkup

reply_keyboard_action = [

    ['suggest something'],
    ['peoples suggestions'],
    ['Done'],

]
reply_platforms = [

    ['PC'],
    ['Consoles'],
    ['Mobile Phones'],
    ['Return'],
    ['Done'],

 ]

reply_show = [

    ['Vote', 'Return'],

]

reply_keyboard_kind = [

    ['movies', 'series'],
    ['mini series', 'anime animation'],
    ['Book', 'Games'],
    ['Return'],
    ['Done'],

]

reply_game_genres = [

    ['Open World', 'Horror'],
    ['Racing', 'FPS'],
    ['Sport', 'Strategy'],
    ['Return'],
    ['Done'],

    ]

Movie_genres = [

    ['all'],
    ['Sci_fiction', 'Biography'],
    ['Comedy', 'Horror'],
    ['Drama', 'Action'],
    ['Thriller_Drama', 'Drama_Mystery'],
    ['Mystery_Crime', 'Drama_Romance'],
    ['Musical', 'Thriller'],
    ['Return'],
    ['Done'],

]
Movie_genres_Add = [

    ['Sci_fiction', 'Biography'],
    ['Comedy', 'Horror'],
    ['Drama', 'Action'],
    ['Thriller_Drama', 'Drama_Mystery'],
    ['Mystery_Crime', 'Drama_Romance'],
    ['Musical', 'Thriller'],
    ['Return'],
    ['Done'],

]
reply_book_genres = [

    ['all'],
    ['Action and Adventure _Fiction', 'History_Fiction', 'Anthology_Fiction'],
    ['Childrens_Fiction', 'Crime_Fiction', 'Drama_Fiction'],
    ['Fantasy_Fiction', 'Horror_Fiction', 'Romance_Fiction'],
    ['Poetry_Fiction', 'Poetry_Fiction', 'Short Story_Fiction'],
    ['Biography_NonFiction', 'Diary_NonFiction', 'History_NonFiction'],
    ['Memoir_NonFiction', 'Philosophy_NonFiction', 'Spirituality_NonFiction'],
    ['True Crime_NonFiction', 'Self Help_NonFiction', 'Other_NonFiction'],
    ['Return'],
    ['Done'],

]

reply_add_book_genres = [

    ['Action and Adventure _Fiction', 'History_Fiction', 'Anthology_Fiction'],
    ['Childrens_Fiction', 'Crime_Fiction', 'Drama_Fiction'],
    ['Fantasy_Fiction', 'Horror_Fiction', 'Romance_Fiction'],
    ['Poetry_Fiction', 'Poetry_Fiction', 'Short Story_Fiction'],
    ['Biography_NonFiction', 'Diary_NonFiction', 'History_NonFiction'],
    ['Memoir_NonFiction', 'Philosophy_NonFiction', 'Spirituality_NonFiction'],
    ['True Crime_NonFiction', 'Self Help_NonFiction', 'Other_NonFiction'],
    ['Return'],
    ['Done'],

]

reply_keyboard_admin_main = [

    ['Delete'],
    ['Edit'],
    ['Confirm'],
    ['Confirm Game'],
    ['Done'],

]
reply_Stars = [

    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['10'],
    ['Return'],
    ['Done'],

]

markup_book_genres = ReplyKeyboardMarkup(reply_book_genres, one_time_keyboard=True)
markup_add_book_genres = ReplyKeyboardMarkup(reply_add_book_genres, one_time_keyboard=True)
markup_stars = ReplyKeyboardMarkup(reply_Stars, one_time_keyboard=True)
markup_genres_add = ReplyKeyboardMarkup(Movie_genres_Add, one_time_keyboard=True)
markup_show = ReplyKeyboardMarkup(reply_show, one_time_keyboard=True)
markup_kind_action = ReplyKeyboardMarkup(reply_keyboard_action, one_time_keyboard=True)
markup_kind = ReplyKeyboardMarkup(reply_keyboard_kind, one_time_keyboard=True)
markup_admin = ReplyKeyboardMarkup(reply_keyboard_admin_main, one_time_keyboard=True, selective=True)
markup_genres = ReplyKeyboardMarkup(Movie_genres, one_time_keyboard=True)
markup_platform = ReplyKeyboardMarkup(reply_platforms, one_time_keyboard=True)
markup_genres_games = ReplyKeyboardMarkup(reply_game_genres, one_time_keyboard=True)
