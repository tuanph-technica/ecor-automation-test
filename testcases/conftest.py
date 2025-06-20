import pytest
from selenium import webdriver
import seleniumwire
from selenium.webdriver.support.wait import WebDriverWait
from utilities.ExcelUtil import readData
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())



class EdgeCromiumDriverManager:
    pass

@pytest.fixture(scope="class")
def setup(request):
    # for debuging
    ENVIRONMENT_CONFIG_FILE = '..//testdata/car_infomation_testing_jpn.xlsx'

    #ENVIRONMENT_CONFIG_FILE = './/testdata/car_infomation_testing_jpn.xlsx'
    browser = readData(ENVIRONMENT_CONFIG_FILE,'Sheet2',2,2)
    url = readData(ENVIRONMENT_CONFIG_FILE,'Sheet2',2,3)
    role = readData(ENVIRONMENT_CONFIG_FILE,'Sheet2',2,1)
    if browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Ie()
    driver.get(url=url)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.role = role
    yield
    driver.close()


"""
@pytest.fixture(scope="class")
def setup(request):
    ENVIRONMENT_CONFIG_FILE = './/testdata/car_infomation_testing_jpn.xlsx'
    browser = readData(ENVIRONMENT_CONFIG_FILE,'Sheet2',2,2)
    url = readData(ENVIRONMENT_CONFIG_FILE,'Sheet2',2,3)
    role = readData(ENVIRONMENT_CONFIG_FILE,'Sheet2',2,1)
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeCromiumDriverManager().install())
    else:
        driver = webdriver.Ie()
    driver.get(url=url)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.role = role
    yield
    driver.close()
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
    parser.addoption("--role")
@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return  request.config.getoption("--browser")
@pytest.fixture(scope="class",autouse=True)
def url(request):
    return  request.config.getoption("--url")
@pytest.fixture(scope="class",autouse=True)
def role(request):
    return  request.config.getoption("--role")
"""





