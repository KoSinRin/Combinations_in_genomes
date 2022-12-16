# Открыть файл с геномной цепочкой и прочитать его содержимое в строку
with open("genome.txt", "r") as f:
  genome = f.read()

# Создать пустой словарь, который будет хранить частоту вхождения каждого символа
frequencies = {}

# Перебрать каждый символ в строке и увеличить счетчик символа в словаре на 1
for char in genome:
  if char in frequencies:
    frequencies[char] += 1
  else:
    frequencies[char] = 1

# Перебрать каждый элемент в словаре и вывести те, у которых частота вхождения больше 1
for char, frequency in frequencies.items():
  if frequency > 1:
    print(f"{char}: {frequency}")