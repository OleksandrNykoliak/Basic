# Напишіть програму, яка перевіряє, чи є число позитивним чи негативним.
# Розширте попередню програму, додавши перевірку, чи є число нулем, позитивним чи негативним.
# Напишіть цикл for для друку чисел від 1 до 10.


# Реалізуйте цикл while для знаходження суми чисел від 1 до 10.
# Використовуйте цикл for для створення рядка, що складається з парних чисел від 2 до 20.
# Напишіть програму з використанням циклу while, яка буде запитувати у користувача числа до тих пір, поки не буде введено 0.
# Реалізуйте цикл for для друку таблиці множення для числа 5.
# Напишіть програму, яка використовує вкладені цикли для друку прямокутника з зірочок заданого розміру.
# Створіть програму, яка використовує if-else для визначення, чи є рік високосним.
# Використовуйте цикл для обчислення факторіалу числа.




def positiv_negativ(num):
    if num > 0:
        print("Число позитивне ")
    elif num < 0:
            print("Число негативне")
    else:
        print("Число дорівнює нулю ")  

positiv_negativ(7)


for i in range(1, 11):
     print(i)


a = 0
num = 1
while num<=10:
     a += num
     num += 1

print(a)



for i in range(2, 20):
    if i %2 == 0:
         print(i,end="")



nums = []

while True:
    num = int(input("Введіть число"))
    if num == 0:
        break
    nums.append(num)

print("Введіть число: ", nums )





    