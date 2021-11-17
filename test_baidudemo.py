import allure
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度首页"):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')

    with allure.step("输入搜索内容并点击"):
        driver.find_element(By.ID, 'kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element(By.ID, "su").click()
        time.sleep(2)

    with allure.step("保存测试截图并退出"):
        driver.save_screenshot('./resource/b.png')
        allure.attach.file('./resource/b.png', attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head>首页<body></body>', '这是一个html', attachment_type=allure.attachment_type.HTML)
        driver.quit()
