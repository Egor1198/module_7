
team1_num = 5
team1_name = 'Мастера кода'
team2_num = 6
team2_name = 'Волшебники данных'
score_1 = 40
score_2 = 42
team1_time = 19006.1
team2_time = 18015.2


if (score_1 > score_2) or (score_1 == score_2 and team1_time < team2_time):
    result = f'Победа команды {team1_name}!'
elif score_2 > score_1 or score_2 == score_1 and team2_time < team1_time:
    result = f'Победа команды {team2_name}!'
else:
    result = 'Ничья!'

tasks_total = score_1 + score_2

time_avg = round((team1_time + team2_time) / tasks_total, 1)

print('В команде %s участников: %s' % (team1_name, team1_num))
print('Итого сегодня в командах участиноков: %s и %s' % (team1_num,team2_num))
print('Команда {0} решила задач: {1}'.format(team2_name,score_2))
print('{0} решили задачи за {1}'.format(team2_name, team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')




