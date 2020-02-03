
# import selenium WebDrivers and additional modules that will be used in the execution
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Assign the location of the Chrome Driver installed on your local machine
driver = webdriver.Chrome(executable_path="/Users/shsrinivasan/Downloads/chromedriver") #-- ChromeDriver
#driver = webdriver.Chrome(executable_path="/Users/shsrinivasan/Downloads/geckodriver") # -- GeckoDriver for Firefox


driver.maximize_window()

# Navigate to www.google.com
driver.get("https://www.google.com")


# Locate the Search Box and enter the "Search String" and start search
searchButton = driver.find_element_by_xpath("//*[@name='q']")
searchButton.clear()
searchButton.send_keys('LexisNexis')
searchButton.send_keys(Keys.RETURN)

# Identify the links displayed in the Search result and click on the third link
# Print the URL of the current page
driver.find_element_by_xpath("(//*[@class='LC20lb'])[3]").click()
print("The name of the  WebPage is " +driver.current_url)

# Close the Browser
driver.quit()