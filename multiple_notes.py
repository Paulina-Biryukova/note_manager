from datetime import datetime, date

all_notes = []
note_counter = 1  # Счетчик заметок

while True:

    note = {}
    note['number'] = note_counter  # Добавление номера заметки

    note ['username'] = input('Введите имя пользователя: ')

    # Ввод заголовков
    note['titles'] = []
    while True:
        title = input('Введите заголовок (или оставьте пустым для завершения): ').strip()
        if title != '':
            note['titles'].append(title)
        else:
            break

    note ['content'] = []
    while True:
        content_user = input('Введите описание заметки: ').strip()
        if content_user != '':
            note['content'].append(content_user)
            break
        else:
            print('Описание заметки отсутствует, просьба добавить описание или поставить любой знак.')
            continue

    note['status'] = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
    note['created_date']  = now = datetime.now().strftime('%d-%m-%Y')
    print('Дата создания заметки: ',now)

# Ввод и проверка дедлайна
    while True:
        try:
            issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год": ')
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате 'день-месяц-год'")

    note['issue_date'] = issue_date

# Обработка дедлайнов
    first_date = issue_date
    second_date = datetime.strptime(now,'%d-%m-%Y').date()
    difference_date = first_date - second_date

    if difference_date.days == 0:
        print(f'Дедлайн сегодня!')
    elif difference_date.days > 0:
        print(f'До дедлайна осталось {difference_date.days} дней')
    else:
        print(f'Внимание! Дедлайн истёк {-difference_date.days} дней назад')

    note['difference_date'] = difference_date.days

# Проверка и обновление статуса заметки
    current_status = note['status']

    while True:
        print(f'Текущий статус заметки: {current_status}')
        print('Выберите новый статус заметки: ', '\n1. выполнено', '\n2. в процессе', '\n3. отложено', '\n4. ввести иной статус')
        selected_new_status = input('Ваш выбор: ')

        if selected_new_status == '1':
            new_status = 'выполнено'
            break
        elif selected_new_status == '2':
            new_status = 'в процессе'
            break
        elif selected_new_status == '3':
            new_status = 'отложено'
            break
        elif selected_new_status == '4':
            new_status = input('Введите новый статус заметки: ')
            break
        else:
            print('Ошибка: неверный ввод. Попробуйте снова.') # Сообщение об ошибке, если введен неправильный выбор
            continue

    note ['status'] = new_status
    print(f'Статус заметки успешно обновлён на: {new_status}')

    #print('\nСобранная информация о заметке:')
    #for key, value in note.items():
        #if key == 'titles':
            #print(f'{key.capitalize()}:\n{'\n'.join(value)}')  # Выводим все заголовки с новой строки
        #else:
            #print(f'{key.capitalize()}: {value}')

    all_notes.append(note)

    note_counter += 1  # Увеличиваем счётчик заметок

    s = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
    if s == 'да':
        continue
    else:
        break

# Вывод всех заметок
print('\nИнформация о собранных заметках:')
for note in all_notes:
    print('-' * 50)  # Разделительная линия между заметками
    for key, value in note.items():
        if key == 'titles':
            print(f'{key.capitalize()}:\n{"\n".join(value)}')
        else:
            print(f'{key.capitalize()}: {value}')
    print('-' * 50)  # Разделительная линия после заметки