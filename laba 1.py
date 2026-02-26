import re

class File:
    def __init__(self, name, date, size):
        self.name = name
        self.date = date
        self.size = size


creat_file = input("Введите через пробел название файла (строка), дата создания, размер (целое число байт)")

data = re.findall(r'\s*"([^"]+)"\s+(\S+)\s+(\S+)\s*$', creat_file)[0]


name = data[0]

date = data[1]

size = int(data[2])

file = File(name, date, size)

print(file.name)
print(file.date)
print(file.size)
