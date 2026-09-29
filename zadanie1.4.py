"""
Задача 4. Переменная seconds хранит количество секунд.
Перевести это число в дни:часы:минуты:секунды.
"""

seconds = 200000

days = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 3600 // 60
secs = seconds % 60

print(f"{days}:{hours}:{minutes}:{secs}")