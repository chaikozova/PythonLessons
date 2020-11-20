from bs4 import BeautifulSoup
import requests

url = 'https://cars.kg/offers'
page = requests.get(url)
cars = []
list_of_cars = []
description = []

print(page.status_code)
soap = BeautifulSoup(page.text, 'html.parser')
cars = soap.find_all('span', class_='catalog-item-params')
descriptions = soap.find_all('span', class_='catalog-item-descr')

for i in range(len(cars)):
    if cars[i].find('span', class_='catalog-item-caption') is not None:
        list_of_cars.append(cars[i].text.replace('  ', '').replace('\n', ''))

for i in range(len(descriptions)):
    description.append(descriptions[i].text.replace('  ', '').replace('\n', ''))


with open('cars_kg.txt', 'w') as file:
    for car in list_of_cars:
        file.writelines(car+' ')
        for descr in description:
            file.writelines(descr+'\n')

