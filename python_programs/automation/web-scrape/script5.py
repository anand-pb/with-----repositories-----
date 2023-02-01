from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

response = browser.get('https://www.freecodecamp.org/news/git-cheat-sheet/')

lmnts = browser.find_elements(By.TAG_NAME, 'code')

txtfile = open('C:\\Users\\APB\\Desktop\\git-commands.txt', 'a')

for lmnt in lmnts:
    # print(lmnt.text + "\n")
    txtfile.write(lmnt.text + "\n")

txtfile.close()    