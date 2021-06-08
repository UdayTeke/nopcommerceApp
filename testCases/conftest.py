from selenium import  webdriver
import pytest
import pytest_metadata
from pytest_metadata import hooks

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
    else:
        driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
    return driver




def pytest_addoption(parser):                                               #this will get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):                                               #this will return the Browser value to setup method
    return request.config.getoption("--browser")



################ PyTest HTML Report #################
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module name'] = 'Customer'
    config._metadata['Tester'] = 'Uday'

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)