import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
    driver.get('https://duckduckgo.com/')
    content = driver.page_source
    results = []
    soup = BeautifulSoup(content, features="html.parser")
    for element in soup.findAll(attrs={'id':'logo_homepage_link'}):
        name = element.find('span')
        print(name.text)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
