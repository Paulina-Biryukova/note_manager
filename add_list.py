username = input('Введите имя пользователя: ')
content = input('Введите описание заметки: ')
status = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год":' )

titles = []
for i in range(3):
    title = input(f'Введите заголовок заметки {i + 1}: ')
    titles.append(title)

print('\nВы ввели следующие данные:')
print('Имя пользователя:', username)
print('Описание заметки:', content)
print('Заголовки заметки:', titles)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date)
print('Дата истечения заметки (дедлайн):', issue_date)