import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Web sahifani yuklash
url = "https://uz.yellowpages.uz/rubrika/xususiy-bolalar-bogchasi/toshkent"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Ma'lumotlarni yig'ish
data = []
cards = soup.find_all('div', class_='yp-card')  # Ma'lumot saqlangan asosiy bo'lim

for card in cards:
    # Bog'cha nomi
    name = card.find('h5', class_='yp-card__title')
    name = name.text.strip() if name else 'Noma’lum'

    # Manzil
    address = card.find('div', class_='yp-card__address')
    address = address.text.strip() if address else 'Manzil keltirilmagan'

    # Yuridik nomi
    legal_name = card.find('div', class_='yp-card__legal-name')
    legal_name = legal_name.text.strip() if legal_name else 'Yuridik nom keltirilmagan'

    # Telefon raqami
    phone = card.find('a', class_='yp-card__phone-number')
    phone = phone.text.strip() if phone else 'Telefon keltirilmagan'

    # Yig'ilgan ma'lumotni ro'yxatga qo'shish
    data.append([name, address, legal_name, phone])

# Excel faylga yozish
wb = Workbook()
ws = wb.active
ws.append(['Bog\'cha nomi', 'Manzili', 'Yuridik nomi', 'Telefon'])  # Ustunlar nomlari

for row in data:
    ws.append(row)

wb.save('bolalar_bogchasi.xlsx')
print("Ma'lumotlar Excel faylga saqlandi!")
