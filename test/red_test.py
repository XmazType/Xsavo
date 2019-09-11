from selenium import webdriver

def test_mytest():

    browser = webdriver.Chrome('C:\\Users\\Андрей\\PycharmProjects\\sait\\adventure\\test\\chromedriver.exe')
    browser.get('http://127.0.0.1:8000/home/')

    print(browser.title)

    assert browser.title == 'Adventure'