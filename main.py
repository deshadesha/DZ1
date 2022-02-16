myName = "Дарья"
print (myName)
myAge = int(18)
print ("Мне сейчас", myAge, "лет")
myName5 = (myName + " ") * 5
print (myName5)
print ("Как ваше имя?")
while True:
    urName = input()
    if not urName.isalpha():
        print("Пожалуйста введите только ваше имя!")
    else:
        print("Приятно познакомиться,",urName)
        break

print("А лет вам сколько?")
while True:
    urAge = int(input())
    if (urAge > 0) and (urAge < 150):
        break
    else:
        print("Не стесняйтесь, напишите свой настоязий возраст!")

if urAge >= 14 and urAge <= 28 : print(urAge,"лет! Все еще впереди, не выкидывай аттестат.")
if urAge >= 29 and urAge <= 50 : print(urAge, "лет... Выглядите свежо, не унывайте.")
print(urName[2:-1])
print(urName [::-1])
print(urName[-3:])
print(urName[1:6])
length = len(urName)
print(length)
sum = 0
x = 1
while urAge > 0:
    pro = urAge % 10
    sum = sum + pro
    x = x * pro
    urAge = urAge // 10

print("Сумма цифр возраста равна", sum)
print("Произведение равно", x)
print(urName.lower())
print(urName.upper())
print(urName.capitalize())
print(urName.swapcase())

print("Сколько будет 28+28?")
num = int(input())
if (num == 56):
   print("Верно!")
else:
   print("Вы не поступили...")
