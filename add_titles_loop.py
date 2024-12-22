# Реализация цикла для добавления заголовков
note = {}

#note ['username'] = input('Введите имя пользователя: ')
#note ['content'] = input('Введите описание заметки: ')
#note['status'] = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
#note['created_date'] = input('Введите дату создания заметки в формате "день-месяц-год": ')
#note['issue_date'] = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год":' )

note['titles'] = []
title = input('Введите заголовок заметки: ')
note['titles'].append(title)

while True:
    new_title = input('Желаете добавить еще один заголовок? (да/нет)\n').lower()
    if new_title == 'нет':
        continue_input = False
        break
    elif new_title == 'да':
        title = input('Создание нового заголовка: ')
        note['titles'].append(title)
    else:
        print('Выберите да/нет')
        new_title = input('Желаете добавить еще один заголовок? (да/нет)\n').lower()

print('\nСобранная информация о заметке:')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')