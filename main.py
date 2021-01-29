import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests import RequestException


def check_availability(soup):
    is_unavailable = True if soup.body(text='Indisponível') else False
    if is_unavailable:
        print("Product is unavailable at the moment, try again later :(\n")
    else:
        print("The product is now available!\n")


'''Check additional upgrade values, type is the keyword of the section title'''
def check_additional_upgrade_values(soup, type):
    additional_options = []
    additional_prices = []
    for element in soup.findAll('div', class_='product-config'):
        if element.find(text=type):  # Additional RAM
            option_ram = element.findAll('p', class_='product-config__item-text')
            for option in option_ram:
                additional_options.append(option.string)
            option_prices = element.findAll('li', class_='product-config__item')
            for option in option_prices:
                additional_prices.append(option.find('span').string)
    return additional_options, additional_prices


if __name__ == '__main__':
    try:
        page = requests.get('https://www.navegamer.com.br/gamer-note/notebook--gamer--nave--polaris--gk5np50--2--144hz')
        soup = BeautifulSoup(page.content, features="html.parser")
        check_availability(soup)
        # Price of the laptop without upgrades
        productBasePrice = soup.find('p', id="product-total__price").string
        print(productBasePrice.string)
        additionalRamPrices = []
        additionalRamOptions = []
        additionalSSDPrices = []
        additionalSSDOptions = []

        additionalRamOptions, additionalRamPrices = check_additional_upgrade_values(soup, 'Memória Ram')
        additionalSSDOptions, additionalSSDPrices = check_additional_upgrade_values(soup, 'SSD')

    except RequestException:
        print("Something happened, try again!")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
