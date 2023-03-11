from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Browser Action 1 > Open Web
driver.get("http://google.com")
sleep(2)
# driver.find_element('name', 'q').send_keys("Wikipedia")
# sleep(3)
# driver.quit()


# Browser Action 2 > Print title
# window_title = driver.title
# print(window_title)


# Browser Action 3 > Back & Forward
# driver.get("http://kilid.com")
# sleep(1)
# driver.back()
# sleep(1)
# driver.forward()


# Browser Action 4 > Refresh
# driver.refresh()


# Browser Action 5 > Switch Windows
# driver.switch_to.new_window('tab')
# sleep(3)
# a = driver.title
# print(a)


# Browser Action 6 > Switch Windows 2
# driver.switch_to.new_window('window')
# driver.get('http://kilid.com')
# sleep(3)


# Browser Action 7 > Back to Current Window
# kilid_window = driver.current_window_handle
# print('yahoo handle' + str(kilid_window))


# Browser Action 8 > All Handles
# all_handle = driver.window_handles
# print('all_handles' + str(all_handle))


# Browser Action 9 > Switch
# driver.switch_to.window(all_handle[0])
# sleep(3)


# Browser Action 10 > Close Tab
# driver.close()
# sleep(3)


# Browser Action 11 > Quit session
# driver.quit()


# Browser Action 12 > Window Size
# google_size = driver.get_window_size()
# print(google_size)
# width = google_size['width']
# print(width)
# height = google_size['height']
# print(height)


# Browser Action 13 > Set Window Size
# driver.set_window_size(800, 600)
# sleep(3)
# new_size = driver.get_window_size()
# assert new_size['width'] == 800
# print(new_size)


# Browser Action 14 > Get Window Position
# current_position = driver.get_window_position()
# print(current_position)
# sleep(3)


# Browser Action 15 > Set Window Position
# driver.set_window_position(400, 500)
# sleep(3)
# assert driver.get_window_position()['x'] == 400


# Browser Action 16 > Maximize window
# driver.maximize_window()
# sleep(3)


# Browser Action 17 > Minimize window
# driver.minimize_window()
# sleep(3)


# Browser Action 18 > Full screen window
# driver.fullscreen_window()
# sleep(3)



