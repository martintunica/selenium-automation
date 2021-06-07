from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title# assert: si el titulo existe, sigue corriendo sino, cierra
show_message_button = chrome_browser.find_element_by_class_name('btn-default') #selecciono por el class name
#print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')#selecciono x el id name
chrome_browser.find_element_by_css_selector('#get-input > .btn')#todos con id input y los buttons por css
user_message.clear()
user_message.send_keys('i am cool')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'i am cool' in output_message.text

chrome_browser.close() #si no funciona, QUIT