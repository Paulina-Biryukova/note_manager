information_about_note = []

username = input('Введите имя пользователя: ')
information_about_note.append(username)

content = input('Введите описание заметки: ')
information_about_note.append (content)

title_1 = input('Введите первый заголовок заметки: ')
title_2 = input('Введите второй заголовок заметки: ')
title_3 = input('Введите третий заголовок заметки: ')
titles = [title_1, title_2, title_3]
information_about_note.append(titles)

status = input('Введите статус по работе с заметкой (например: в работе, в архиве, закрыта и проч.): ')
information_about_note.append(status)

created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
information_about_note.append(created_date)

issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год":' )
information_about_note.append(issue_date)

print(*information_about_note, sep='\n')