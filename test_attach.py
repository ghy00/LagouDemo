# allure实现错误截图功能

import allure


def test_attach_text():
    allure.attach('这是一个纯文本', attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach('<body>这是一段html</body>', "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file('/Users/apple/PycharmProjects/pythonProject/qx_testcase/resource/img.png', name='测试图片',
                       attachment_type=allure.attachment_type.PNG)
