# 使用allure设置测试用例级别

import allure


def test_no_severity():
    pass


# TRIVIAL级别，轻微缺陷
@allure.severity(allure.severity_level.TRIVIAL)
def test_severity_trivial():
    pass


# MINOR级别,次要缺陷
@allure.severity(allure.severity_level.MINOR)
def test_severity_minor():
    pass


# NORMAL级别，普通缺陷
@allure.severity(allure.severity_level.NORMAL)
def test_severity_normal():
    pass


# critical级别，临界缺陷
@allure.severity(allure.severity_level.CRITICAL)
def test_severity_critical():
    pass


# blocker级别，中断缺陷
@allure.severity(allure.severity_level.BLOCKER)
def test_severity_blocker():
    pass


# 测试类normal级别
@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_normal(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_critical(self):
        pass