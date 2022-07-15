time = int(input('Введите время: '))
hour = time // 3600
minute = (time - hour * 3600) // 60
sec = time % 60
print(f'{hour}:{minute}:{sec}')
