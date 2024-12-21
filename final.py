information_about_note = []

username = input('Введите имя пользователя: ')
content = input('Введите описание заметки: ')
title_1 = input('Введите первый заголовок заметки: ')
title_2 = input('Введите второй заголовок заметки: ')
title_3 = input('Введите третий заголовок заметки: ')
titles = [title_1, title_2, title_3]
status = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год":' )

print('Имя пользователя:', username)
print('Описание заметки:', content)
print('Заголовки заметки:', titles)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date)
print('Дата истечения заметки (дедлайн):', issue_date)

information_about_note = [username,
        content,
        titles,
        status,
        created_date,
        issue_date]