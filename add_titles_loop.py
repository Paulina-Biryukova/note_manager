# Реализация цикла для добавления заголовков
note = {}

note ['username'] = input('Введите имя пользователя: ')
note ['content'] = input('Введите описание заметки: ')
note['status'] = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
note['created_date'] = input('Введите дату создания заметки в формате "день-месяц-год": ')
note['issue_date'] = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год":' )

note['titles'] = []

while True:
    title = input('Введите заголовок (или оставьте пустым для завершения): ').strip()
    if title != '':
        note ['titles'].append(title)
    else:
        break

print('\nСобранная информация о заметке:')
for key, value in note.items():
    if key == 'titles':
        print(f'{key.capitalize()}:\n{'\n'.join(value)}')  # Выводим все заголовки с новой строки
    else:
        print(f'{key.capitalize()}: {value}')