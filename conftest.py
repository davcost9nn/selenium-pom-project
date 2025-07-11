import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language : for example - ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    if browser:
        print("\nSuccess")
    else:
        raise pytest.UsageError("--language should be for example ru or en")
    yield browser
    print("\nquit browser..")
    browser.quit()