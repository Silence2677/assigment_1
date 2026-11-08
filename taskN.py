lesson = int(input())
total_minutes = lesson * 45 + (lesson - 1) * 5 + ((lesson - 1) // 2) * 10
hours = 9 + total_minutes // 60
minutes = total_minutes % 60
print(total_minutes)