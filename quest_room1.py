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
        while life != 0:
            print("В центре комнаты стоит сундук, с кодовым замком.\n"
                  "За сундуком запертая дверь на улицу\n"
                  "Слева от тебя стоит шкаф, с права комод.")
            print("Выбери действие: \n"
                  "-Обыскать: шкаф/комод\n"
                  "-Попробовать открыть: сундук/дверь на улицу")
            answer_room1 = input("Введи ответ: ")
            if answer_room1 == "дверь на улицу":
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
        else:
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
