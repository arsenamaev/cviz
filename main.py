print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы: ")

question = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
            "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
            "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
            "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
            "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
            "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
            "7. Как называется разница между выручкой и затратами компании?"]
answer = ["Стартап",
          "Инвестор",
          "Инвестиция",
          "MVP",
          "Бизнес-план",
          "Конкуренты",
          "Прибыль"]
score = 0
print(question[0])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[0].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

print(question[1])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[1].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

print(question[2])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[2].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

print(question[3])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[3].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

print(question[4])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[4].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

print(question[5])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[5].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

print(question[6])
users_input = input('Вывиди свой ответ: ')
if users_input.lower() == answer[6].lower():
     print('Правильно!')
     score = score + 1
else:
     print('Неправильно.')

# ...

if score > 5:
    print("Это отличный результат! Ты много знаешь о стартапах.")
elif score > 3:
   print("Неплохой результат! Кау здорово, что тебе предстоит узнать так много о стартапах.")
else:
   print("Видимо,ты только наченаеш свой путь к стартапам! Ты ешё много узнаеш о мири, где ты живёш.")

if score == 0:
    print("Ты заработал" ,score, "баллов")

if score == 1:
    print("Ты заработал" ,score, "балл")

if score == 2:
    print("Ты заработал" ,score, "балла")

if score == 3:
    print("Ты заработал" ,score, "балла")

if score == 4:
    print("Ты заработал" ,score, "балла")

if score == 5:
    print("Ты заработал" ,score, "баллов")

if score == 6:
    print("Ты заработал" ,score, "баллов")

if score == 7:
    print("Ты заработал" ,score, "баллов")