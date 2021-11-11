# QuizGame v.1.3 by GrobranGG (https://github.com/GrobranGG/)
import colorama
import os
import sys
from colorama import Fore

def convert():
    colorama.init()
    opersystem = sys.platform

    clean_command = ""
    if sys.platform == "win32":
        clean_command = "cls"
    elif sys.platform == "linux":
        clean_command = "clear"
    os.system(clean_command)

    # Banner

    print(Fore.CYAN)
    print("  ____        _      _____                       ")
    print(" / __ \      (_)    / ____|                      ")
    print("| |  | |_   _ _ ___| |  __  __ _ _ __ ___   ___  ")
    print("| |  | | | | | |_  / | |_ |/ _` | '_ ` _ \ / _ \ ")
    print("| |__| | |_| | |/ /| |__| | (_| | | | | | |  __/ ")
    print(" \___\_\\__,_|_/___| \_____|\__,_|_| |_| |_|\___|")
    print(Fore.BLUE + "                              v.1.3 by GrobranGG")

    print(Fore.WHITE + "Choose a language (number):")
    print("1. English")
    print("2. Russian")

    language = input(Fore.CYAN + "Enter your language: ")

    # Dictionaries
    english = {'youranswer': 'Your answer (number):', 'welcome_message': 'Welcome to QuizGaame! \nNow you have to choose a topic, after which the program will ask you 5 questions on this topic. \nThe more correct answers - the better!',
            'topic': 'Choose a quiz topic:', 'videogame': ' Video games', 'end_1': 'You answered', 'end_2': 'of 5 questions correctly!', 'repeat_question': 'Choose the next action:', 'repeat_variant1': '1. Restart the program',
            'repeat_variant2': '2. Close the program', 'answer_repeat': 'Choose the answer (number): ', 'percent_1': 'This is', 'percent_2': 'of the correct answers!', 'bruh_answer': 'Incorrect answer!'}

    english_quest = {'videogame_1': 'Question 1: The name of the main character literally translates into Russian as "maximum pain", which game is it about?',
                    'videogame_2': 'Question 2: In which game does the main character find himself locked up in his own apartment and travels to other worlds through a hole in the bathroom?',
                    'videogame_3': 'Question 3: What genre of games does not exist?', 
                    'videogame_4': 'Question 4: How many characters are currently in Dota 2? (2021)', 
                    'videogame_5': 'Question 5: In what year was the first Mario game released?'}

    russian = {'youranswer': 'Ваш ответ (число):', 'welcome_message': 'Добро пожаловать в QuizGaame! \nСейчас ты должен выбрать тему, после чего программа задаст тебе 5 вопросов по этой теме. \nЧем больше правильных ответов - тем лучше!',
            'topic': 'Выбери тематику викторины:', 'videogame': ' Видеоигры', 'end_1': 'Ты ответил правильно на', 'end_2': 'из 5 вопросов!', 'repeat_question': 'Выберите следующее действие:', 'repeat_variant1': '1. Переапустить программу',
            'repeat_variant2': '2. Закрыть программу', 'answer_repeat': 'Выбери ответ (число): ', 'percent_1': 'Это', 'percent_2': 'правильных ответов!', 'bruh_answer': 'Некорректный ответ!'}

    russian_quest = {'videogame_1': 'Вопрос 1: Имя главного героя дословно переводится на русский язык как «максимальная боль», о какой игре идёт речь?',
                    'videogame_2': 'Вопрос 2: В какой игре главный герой оказывается взаперти собственной квартиры и путешествует в иные миры через отверстие в ванной комнате?',
                    'videogame_3': 'Вопрос 3: Какого жанра игр не существует?', 
                    'videogame_4': 'Вопрос 4: Сколько персонажей на данный момент в Dota 2? (2021)', 
                    'videogame_5': 'Вопрос 5: В каком году вышла первая игра Mario?'}

    if language == "1":
        lang = english
        quest_lang = english_quest
    elif language == "2":
        lang = russian
        quest_lang = russian_quest
    else:
        print(Fore.RED + "Incorrect language!")
        sys.exit()

    os.system(clean_command)
    print(Fore.RESET + lang['welcome_message'] + "\n")
    print(Fore.CYAN + lang['topic'])

    print(Fore.RESET + "1." + lang['videogame'] + "\n")
    topic = input(lang['youranswer'])

    # QuizGame
    score = 0

    # Topic 1
    if topic == "1":
        os.system(clean_command)

        # Question 1
        print(Fore.CYAN + quest_lang['videogame_1'])

        print(Fore.RESET)
        print("1. Detroit: Become Human")
        print("2. Max Payne")
        print("3. Far Cry 3")
        answer_1 = input(lang['youranswer'])

        if answer_1 == "2":
            score = score + 1
        elif answer_1 == "":
            print(Fore.RED + lang['bruh_answer'])
            input()
            sys.exit()
        else:
            score = score + 0
        
        os.system(clean_command)

        # Question 2
        print(Fore.CYAN + quest_lang['videogame_2'])

        print(Fore.RESET)
        print("1. Silent Hill 4: The Room")
        print("2. Dragon Age: Origins")
        print("3. Tomb Raider")
        answer_1 = input(lang['youranswer'])

        if answer_1 == "1":
            score = score + 1
        elif answer_1 == "":
            print(Fore.RED + lang['bruh_answer'])
            input()
            sys.exit()
        else:
            score = score + 0
        
        os.system(clean_command)

        # Question 3
        print(Fore.CYAN + quest_lang['videogame_3'])

        print(Fore.RESET)
        print("1. Comedy")
        print("2. MMORPG")
        print("3. Shooter")
        answer_1 = input(lang['youranswer'])

        if answer_1 == "1":
            score = score + 1
        elif answer_1 == "":
            print(Fore.RED + lang['bruh_answer'])
            input()
            sys.exit()
        else:
            score = score + 0
        
        os.system(clean_command)

        # Question 4
        print(Fore.CYAN + quest_lang['videogame_4'])

        print(Fore.RESET)
        print("1. 117")
        print("2. 74")
        print("3. 122")
        answer_1 = input(lang['youranswer'])

        if answer_1 == "3":
            score = score + 1
        elif answer_1 == "":
            print(Fore.RED + lang['bruh_answer'])
            input()
            sys.exit()
        else:
            score = score + 0
        
        os.system(clean_command)

        # Question 5
        print(Fore.CYAN + quest_lang['videogame_5'])

        print(Fore.RESET)
        print("1. 1977")
        print("2. 1981")
        print("3. 2003")
        answer_1 = input(lang['youranswer'])

        if answer_1 == "2":
            score = score + 1
        elif answer_1 == "":
            print(Fore.RED + lang['bruh_answer'])
            input()
            sys.exit()
        else:
            score = score + 0
        
        os.system(clean_command)

        print(Fore.CYAN + lang['end_1'], score, lang['end_2'])
        print(Fore.RESET + lang['percent_1'], score * 20, "%", lang['percent_2'])

    else:
        print(Fore.RED + "Incorrect topic!")
        input()
        sys.exit()

    print("\n")
    print(Fore.CYAN + lang['repeat_question'])
    print(Fore.GREEN + lang['repeat_variant1'])
    print(Fore.GREEN + lang['repeat_variant2'])
    repeat = input(Fore.WHITE + lang['answer_repeat'])

    if repeat == "1":
        convert()
    elif repeat == "2":
        sys.exit()
    else:
        sys.exit()

convert()