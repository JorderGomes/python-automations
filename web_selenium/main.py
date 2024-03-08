from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

link = 'https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium'
name = 'Jorder'
email = 'jorderpgomes@gmail.com'
whatsapp = '(85)988934098'

browser.get(link)

browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys(name)
browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys(email)
browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys(whatsapp)

browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/button').click()