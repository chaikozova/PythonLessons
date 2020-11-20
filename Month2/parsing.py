import requests

response = requests.get('https://cars.kg/offers')
text = response.text
accum = 0
result_text = []
for item in range(20):
    a = text.find('<span class="catalog-item-caption">', accum) + 35
    b = text. find(',', a)
    final_text = text[a:b-1].replace('  ', '').replace('\n', '')
    q = text.find('<span class="catalog-item-price"', b)
    e = text.find('>', q)+1
    w = text.find('</span>', q)
    result_text.append(f'{final_text}. Цена - {text[e:w]}')
    accum = b

with open ('cars.txt', 'w') as file:
    for sale in result_text:
        file.writelines(sale+'\n')