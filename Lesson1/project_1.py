name = input('Введите ваше имя: ')
age = int(input('Введите ваше возраст: '))
gender = input('Укажите ваш пол: ')
email = input('Введите ваш E-Mail: ')
social_status = input("Укажите ваш социальный статус: ")
kids = int(input('Кол-во детей: '))
sidel_or_not_sidel = input("Есть ли судимость? Y or N: ")

# 1) Возрастное ограничение до 16
# 2) Сидел || не сидел
# 3) Женат или разведён
# 4) Кол-во детей > 1 && возраст < 16
# 5) возраст > 18

tax = 0

if name and gender and age > -1 and email and sidel_or_not_sidel and social_status and kids >= 0:

    if 16 <= age <= 135:
        if 16 <= age <= 19 and kids > 0:
            tax += 10000
            print('Do you have kids? Pay taxes!')
        elif age > 18:
            tax = (age -18) * 1000
            print("Why didn't you come earlier?! Pay taxes!")
        elif social_status == "married":
            print('no taxes')
        elif sidel_or_not_sidel == 'Y':
            tax += 10000
            print('Pay taxes thong')
    print('Your taxes are', tax)
