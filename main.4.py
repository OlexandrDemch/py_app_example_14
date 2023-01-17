min_value = None
max_value = None

sum_value = 0

while True:
    value = int(input("Введіть число:"))

    if value == 7:
        break

    sum_value += value

    if min_value is None or value < min_value:
        min_value = value
    if max_value is None or value > max_value:
        max_value = value

print("Good bye!")
print("Suma:", sum_value)
print("Min znachennya:", min_value)
print("Max znachennya:", max_value)