import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
	browser.get(link)
	time.sleep(30)
	# определяем кнопку
	button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
	# проверяем видимость кнопки
	assert button.is_displayed()
