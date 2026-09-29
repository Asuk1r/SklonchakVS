n = int(input())
n = n % (24 * 60)   # отбрасываем полные сутки
hours = n // 60
minutes = n % 60
print(hours, minutes)