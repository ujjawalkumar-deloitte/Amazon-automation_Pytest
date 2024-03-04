import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from pytest_metadata.plugin import metadata_key

@pytest.fixture(scope="class")
def setup(request, browser):

    if browser == "edge":
        edge_service = EdgeService()
        edge_options = EdgeOptions()
        edge_options.binary_location = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        driver = webdriver.Chrome(service=edge_service, options=edge_options)
        driver.maximize_window()
        print("Launching Edge Browser..................")

    elif browser == "chrome":
        chrome_service = ChromeService()
        chrome_options = ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.maximize_window()
        print("Launching Chrome Browser..................")
    else:
        chrome_service = ChromeService()
        chrome_options = ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.maximize_window()
        print("Launching Chrome Browser..................")

    yield driver  # The test will run here

    # Teardown code to close the browser after the entire class
    print("Closing the browser..................")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser (chrome/edge)")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

######################## HTML Reports ##########################

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Amazon"
    config.stash[metadata_key]["Tester Name"] = "Ujjawal Kumar"

# Command to delete extra items from report
# def pytest_unconfigure(config):
#     if metadata_key in config.stash:
#         config.stash[metadata_key].pop("Plugins", None)  # Delete extra item 1
#         config.stash[metadata_key].pop("Packages", None)  # Delete extra item 2
