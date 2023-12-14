from random import randint
num_chamber = 0
player_keys = 0
second_fl_num_cham = 0
while num_chamber == 0:
    print("Вы видите дверь. Выберете, что хотите сделать: ")
    print("Открыть - Осмотреть - Ничего")
    choice_1 = input("Ваше действие - ")
    if choice_1 == "Открыть":
        num_chamber += 1
        print("Скрипя, дверь открывается")
        print("Вам представляется комната")
    elif choice_1 == "Осмотреть":
        print("Дверь скрипит от ветра и выглядит незапертой")
    elif choice_1 == "Ничего":
        print("Вы остались у двери")
while num_chamber == 1:
    print("Вы видите дверь. Выберете, что хотите сделать: ")
    print("Открыть - Осмотреть - Ничего")
    choice_2 = input("Ваше действие - ")
    if choice_2 == "Открыть":
        if player_keys == 0:
            print("На двери висит замок")
            print("На двери висит табличка: ключ в шкафу")
        elif player_keys != 0:
            player_keys -= 1
            print("Замок открылся ключом")
            print("Вы заходите в другую комнату")
            num_chamber += 1
    elif choice_2 == "Осмотреть":
        choice_ch1 = ""
        while choice_ch1 != "Уйти":
            print("Вы видите тумбу, шкаф и стол")
            print("Выберете, что хотите осмотреть: ")
            print("Тумба - Шкаф - Стол")
            choice_ch1 = input("Ваш выбор - ")
            if choice_ch1 == "Тумба":
                print("Вы видите старую тумбу")
                print("Она открывается, но внутри пусто")
                print("Можно вернуться к двери")
                print("но нужно ввести Уйти")
            elif choice_ch1 == "Шкаф":
                print("Вы видите коричневый шкаф")
                print("Открыв шкаф вы находите желтый ключ")
                player_keys += 1
                print("Можно вернуться к двери")
                print("но нужно ввести Уйти")
            elif choice_ch1 == "Стол":
                print("Вы видите старый стол, но на нем лишь тарелки")
                print("Среди тарелок лежит ключ")
                player_keys += 1
                print("Можно вернуться к двери")
                print("но нужно ввести Уйти")
    elif choice_2 == "Ничего":
        print("Вы остались в комнате")
door_ch3_open = False
count_try = 2
while num_chamber == 2 and second_fl_num_cham == 0:
    if player_keys == 0 and count_try == 0:
        print("Попыток и ключей нет или не найдено")
        break
    print("Вы видите лестницу и дверь. Выберете, что хотите сделать: ")
    print("Открыть - Осмотреть - Ничего - Подняться")
    choice_3 = input("Ваше действие - ")
    if choice_3 == "Открыть":
        if count_try > 0:
            if door_ch3_open == False and count_try > 0:
                choice_ch2 = ""
                while count_try > 0:
                    print("Вы видите дверь, На двери табличка")
                    print("Дверь откроется, если правильно ответить")
                    print("Можно ли провести 100% тестирование?")
                    print("Выберете, как ответить: ")
                    choice_ch2 = input()
                    if count_try != 0:
                        if choice_ch2 == "Да" or choice_ch2 == "да":
                            count_try -= 1
                            print(f"Неправильно, осталось {count_try} попыток")
                            if count_try == 0:
                                print(f"Здесь теперь пройти нельзя")
                        elif choice_ch2 == "Нет" or choice_ch2 == "нет":
                            print("Правильно")
                            door_ch3_open = True
                            num_chamber += 1
                            break
                    else:
                        print("Попыток больше нет")
                        choice_ch2 = "Нет"
            elif door_ch3_open == True:
                print("Вы открываете дверь и входите дальше")
                num_chamber += 1
        else:
            print("Попыток открыть дверь больше нет")
    elif choice_3 == "Осмотреть":
        choice_ch2 = ""
        print("Вы видите лестницу и дверь в подвал")
        print("Можно подняться по лестнице")
        print("или войти в дверь")
        print("Можно вернуться к выбору")
        print("но нужно ввести Уйти")
        while choice_ch2 != "Уйти":
            choice_ch2 = input()
    elif choice_3 == "Ничего":
        print("Вы остались в комнате")
    elif choice_3 == "Подняться":
        if player_keys > 0:
            print("Вы поднимаетесь по лестнице")
            second_fl_num_cham += 1
            player_keys -= 1
        else:
            print("На втором этаже дверь на замке")
            print("Без ключа ее не открыть")
if num_chamber == 3:
    print("Добро пожаловать в комнату №1 \n"
          "У тебя 3 жизни что бы выбраться из комнаты")
    print("Продолжим? (да/нет)")
    answer = input("Введи ответ: ")
    life = 3
    key = 0
    a = ""
    b = ""
    answer_room2 = ""
    while True:
        if answer == "нет":
            print("Программа закрыта")
            break
        if answer == "да":
            while life >= 0:
                print("В центре комнаты стоит сундук, с кодовым замком.\n"
                      "За сундуком запертая дверь на улицу\n"
                      "Слева от тебя стоит шкаф, с права комод.")
                print("Выбери действие: \n"
                      "-Обыскать: шкаф/комод\n"
                      "-Попробовать открыть: сундук/дверь")
                answer_room1 = input("Введи ответ: ")
                if answer_room1 == "дверь":
                    if key == 1:
                        print("Ты открыл дверь и вышел на улицу, квест завершен! Ты победил! (:")
                        break
                    else:
                        life -= 1
                        print(f"Дверь заперта! Минус 1 жизнь. Осталось жизней {life}")
                        continue
                if answer_room1 == "сундук":
                    password = int(input("Введи пароль:"))
                    if password == 55:
                        key += 1
                        print("Сундук открыт, в нем лежит ключ от двери на улицу")
                        print("Ты можешь открыть дверь и выйти на улицу")
                        answer_room2 = input("Открыть дверь? (да/нет)")
                        if answer_room2 == "нет":
                            life -= 1
                            print(f"А что еще делать-то?. Минус 1 жизнь. Осталось жизней {life}")
                            continue
                        elif answer_room2 == "да":
                            print("Ты открыл дверь и вышел на улицу, квест завершен! Ты победил! (:")
                            break
                        elif answer_room2 == "да" or answer_room2 == "нет":
                            life -= 1
                            print("Чего? пиши понятней")
                            print(f"Наказание: минус 1 жизнь! Осталось жизней {life}")
                            continue
                    elif password != 55:
                        life -= 1
                        print(f"Пароль не верный, сундук не открыт, минус 1 жизнь. Осталось жизней {life}")
                        continue
                if answer_room1 == "шкаф":
                    if a == "":
                        print("В шкафу ты нашел записку:\n"
                              "Мышь считает дырки в сыре: три плюс две всего ...")  # 5
                        a = input("Ответ: ")
                    else:
                        print("Больше ничего тут нет")
                    continue
                if answer_room1 == "комод":
                    if b == "":
                        print("В комоде ты нашел записку:\n"
                              "230 - 220 * 0.5 = ?")  # 5
                        b = input("Ответ: ")
                    else:
                        print("Больше ничего тут нет")
                    continue
                else:
                    life -= 1
                    print("Чего? пиши понятней")
                    print(f"Наказание: минус 1 жизнь! Осталось жизней {life}")
            if answer_room2 == "":
                print("У тебя закончились жизни, ты проиграл ):")
                break
            elif answer_room2 != "":
                print("Ура!")
                break
        if answer != "да" or answer != "нет":
            life -= 1
            print("Чего? пиши понятней")
            print(f"Наказание: минус 1 жизнь! Осталось жизней {life}")
            answer = input("Введи ответ: ")
        if life == 0:
            print("У тебя закончились жизни, ты проиграл ):")
            break
elif second_fl_num_cham == 1:
    while second_fl_num_cham == 1:
        print(" Угадай чесло ")
        mag_num = randint(1,5)
        count = 0
        user_number = 0
        while user_number != mag_num:
            user_number = int(input())
            count += 1
            if mag_num > user_number:
                print("Загадано число больше")
            elif mag_num < user_number:
                print("Загадано число меньше")
        second_fl_num_cham = 0
        print(f"Угадано {count} раз")
        print("Вы угадали и прошли квест")
