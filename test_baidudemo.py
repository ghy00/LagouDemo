import allure
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    driver.find_element(By.ID, 'kw').send_keys(test_data1)
    time.sleep(2)
    driver.find_element(By.ID, "su").click()
    time.sleep(2)

    driver.save_screenshot('./resource/b.png')
    allure.attach.file('./resource/b.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head>首页<body></body>', '这是一个html', attachment_type=allure.attachment_type.HTML)
    driver.quit()
