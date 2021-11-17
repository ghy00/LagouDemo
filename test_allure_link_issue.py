# 测试用例链接与测试bug链接方法
import allure


# 测试用例链接方式1
@allure.link("https://www.baidu.com", link_type="url", name="百度")
def test_link():
    print("这是一个链接")
    pass


test_case_link = "https://www.163.com"


# 测试用例链接方式二
@allure.testcase(test_case_link, 'test title')
def test_link1():
    print("这是一条测试用例链接")
    pass


# 测试bug链接方式
# --allure-link-pattern=issue:http://www.mytesttracker.com/issue{}
@allure.issue('140', '这是一个issue')
def test_bug_link():
    print('这是一个测试bug链接的嵌入方式')
    pass
