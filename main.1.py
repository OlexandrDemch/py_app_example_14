firstNumber = int(input("Введіть перше число:"))
secondNumber = int(input("Введіть друге число:"))
action = input("\n1.Сума парних чисел \n2.Сума непарних чисел \n3.Кратних-9 \nВиберіть число від 1 до 3:")

if action == "1":
    for i in range(firstNumber, secondNumber + 1):

        if i % 2 != 0:
            print(i)

elif action == "2":
    for i in range(firstNumber, secondNumber + 1):

        if i % 2 == 0:
            print(i)

elif action == "3":
    for i in range(firstNumber, secondNumber + 1):

        if i % 9 == 0:
            print(i)

