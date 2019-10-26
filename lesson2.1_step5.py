from selenium import webdriver
import time
import math

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	
	# нашли значение
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	
	#answer
	element = browser.find_element_by_css_selector("#answer")
	element.send_keys(y)
	
	#checkbox
	ch_rule = browser.find_element_by_css_selector("label[for='robotCheckbox']")
	ch_rule.click()
	
	#radiobutton
	radio_rule = browser.find_element_by_css_selector("label[for='robotsRule']")
	radio_rule.click()
	
	time.sleep(2)
    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector(".btn")
	button.click()

finally:
	time.sleep(5)
	browser.quit()

#C:\Users\DronGo\enviroments\selenium_course\