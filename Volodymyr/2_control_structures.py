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

def number(num):
    if num > 0:
        print(num)
    elif num < 0:
        print(num)
    else:
        print(num)
        

for i in range(1,11):
    print(i)
    
number = range(1,11)
sum_of_numb = sum(number)
print(sum_of_numb)

for i in range (2, 21, 2):
    print(i)
    
    
# a = [i for i in range(1, 11)]
b = [i for i in range(2,21,2)]
print(b)

a = 0
num = 1
while num<=10:
     a += num
     num += 1

print(a)

number = 5
for i in range(1,11):
    result = number * i
    print(result)
    
width = (int(input))
hight = (int(input))
print(width, hight)
for i in range(width):
        for i in range(hight):
print('*')
    


    




    

    

