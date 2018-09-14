






def ask_user(dialogs):
    while 1:
        try: 
            users_input = input('Введите свой вопрос: ')
            answer = dialogs.get(users_input)
            print(answer)
        except(KeyboardInterrupt):
            print('Пока!')
            break



dialogs = {
    "Как дела?": "Хорошо",
    "Что делаешь?": "Работаю"
    }


ask_user(dialogs)