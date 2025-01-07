note = {}

note ['username'] = input('Введите имя пользователя: ')
note ['content'] = input('Введите описание заметки: ')
note['status'] = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
note['created_date'] = input('Введите дату создания заметки в формате "день-месяц-год": ')
note['issue_date'] = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год": ')

note['titles'] = []
while True:
    title = input('Введите заголовок (или оставьте пустым для завершения): ').strip()
    if title != '':
        note ['titles'].append(title)
    else:
        break

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
        print('Ошибка: неверный ввод.') # Сообщение об ошибке, если введен неправильный выбор
        continue

note ['status'] = new_status
print(f'Статус заметки успешно обновлён на: {new_status}')

print('\nСобранная информация о заметке:')
for key, value in note.items():
    if key == 'titles':
        print(f'{key.capitalize()}:\n{'\n'.join(value)}')  # Выводим все заголовки с новой строки
    else:
        print(f'{key.capitalize()}: {value}')