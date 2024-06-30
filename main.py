from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализируем браузер
driver = webdriver.Chrome()

# URL страницы, которую будем парсить
url = 'https://www.divan.ru/category/potolocnye-svetilniki'
# Открываем веб страницу
driver.get(url)
# Даем 5 секунд на прогрузку всей страницы
time.sleep(5)

# Находим товары на странице
products = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

# Список для хранения данных
parsed_data = []

# Парсинг данных с использованием try-except для обработки ошибок
for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = product.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue
    parsed_data.append([name, price, link])

# Закрываем браузер
driver.quit()

# Сохранение данных в CSV файл
with open('new.ceiling_lights.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование светильника', 'Цена Светильника', 'Ссылка на светильник'])
    writer.writerows(parsed_data)

print("Парсинг завершен, данные сохранены в ceiling_lights.csv")
