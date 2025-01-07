note = {}

note ['username'] = input('Введите имя пользователя: ')
note ['content'] = input('Введите описание заметки: ')
note['status'] = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
note['created_date'] = input('Введите дату создания заметки в формате "день-месяц-год": ')
note['issue_date'] = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год": ')

note['titles'] = []
for i in range(3):
    title = input(f'Введите заголовок заметки {i + 1}: ')
    note['titles'].append(title)

print('\nСобранная информация о заметке:')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')