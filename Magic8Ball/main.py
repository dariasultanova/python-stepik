import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Назови свое имя:\n')
print(f'Приветствую тебя, {name}')

while True:
    question = input('Задай же вопрос и получишь ответ.\n')
    if question != '':
        print(random.choice(answers))
    else:
        continue
    question = input('Остались ли у тебя еще вопросы? (да/нет)\n')
    if question == 'да':
        continue
    else:
        print('До встречи...')
        break
