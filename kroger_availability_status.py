from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def highlight(element):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(4)
    apply_style(original_style)

# below is the mess I copy and pasted to avoid bot detection and it magically worked - sorry for the mess
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Chrome/88.0.4324.192'})
driver.get("https://www.kroger.com/i/coronavirus-update/vaccine")

while True:

    time.sleep(5)

    utah_availability_status = driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div/div[2]/div/ul[32]/li[1]").text
    print(utah_availability_status)
    vaccine_is_available = 'Limited quantities available'
    if utah_availability_status.find(vaccine_is_available) != -1:
        print("we found a vaccine!")
        time.sleep(6)
        print('Signing you up now!')
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Chrome/88.0.4324.192'})
        print(driver.execute_script("return navigator.userAgent;"))
        driver.get("https://www.kroger.com/rx/covid-eligibility")
        time.sleep(5)

        # below are all the actions I take on the elements I locate on the page - there is likely a cleaner way to do this
        driver.find_element_by_xpath("//*[@id='content']/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li/div/div[2]/div[2]/div/div/div/button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[3]/div/div[2]/div[2]/div/div/div/button[2]").click()
        time.sleep(2)
        availability = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[5]/div/div[2]/div[2]/div/div/div/select")
        availability.send_keys("U")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[6]/div/div[2]/div[2]/div/div/div/button[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[8]/div/div[2]/div[2]/div/div/div/button[2]").click()
        time.sleep(2)
              
        # setting up the birthday entry box as an element so I can use "send_keys" on the element to type into it
        birthday_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[10]/div/div[2]/div[2]/div/div/div/div/form/div[1]/input")
        birthday_entry.send_keys("03111945")
        birthday_entry.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[11]/div/div[2]/div[2]/div/div/div/button").click()
        time.sleep(3)
        location_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[1]/div/input")
        location_entry.send_keys("Utah")
        location_entry.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/button[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div[2]/div[4]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div[2]/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div[3]/button").click()
        time.sleep(2)
        
        # where I start filling out the forms
        first_name_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[1]/div[1]/div/input")
        first_name_entry.send_keys("Daniel")
        time.sleep(0.5)
        last_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[1]/div[3]/div/input")
        last_name.send_keys("Wilber")
        time.sleep(0.5)
        address_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[2]/div/div/input")
        address_entry.send_keys("4302 Google Dr.")
        time.sleep(0.5)
        city_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[4]/div[1]/div/input")
        city_entry.send_keys("San Antonio")
        time.sleep(0.5)
        state_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[4]/div[2]/div/div/select")
        state_entry.send_keys("U")
        time.sleep(0.5)
        zip_code_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[5]/div/div/input")
        zip_code_entry.send_keys("78215")
        time.sleep(0.5)
        dob_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[6]/div[1]/div/div/input")
        dob_entry.send_keys("03111945")
        time.sleep(0.5)
        sex_at_birth = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[6]/div[2]/div/select")
        sex_at_birth.send_keys("M")
        time.sleep(0.5)
        weight_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[7]/div/div/input")
        weight_entry.send_keys("200")
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[8]/div[1]/div/div/label[8]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div[8]/div[2]/div/div/label[3]/input").click()
        time.sleep(0.5)
        phone_number_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/input")
        time.sleep(0.5)
        phone_number_entry.send_keys("2107184238")
        time.sleep(0.5)
        email_address_entry=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[2]/div[2]/div/input")
        time.sleep(0.5)
        email_address_entry.send_keys("bigdatadaniel@gmail.com")
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[2]/div/div/form/div/div[5]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[1]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[2]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[3]/div/div/div/label[1]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[4]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[5]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[6]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[7]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[8]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/div[9]/div/div/div/label[2]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[3]/div/div/form/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[4]/div/div/form/div[2]/div/label/input").click()
        time.sleep(0.5)
        full_name_entry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/main/div/section[2]/div/div/div[2]/div/div[4]/div/div/form/div[3]/div[1]/div/input")
        time.sleep(0.5)
        full_name_entry.send_keys("William Walter Waters")
        print("All signed up!")
        time.sleep(5)
        driver.close()

    else:
        print('No vaccines available in your area :(')
        time.sleep(60) # 1 minute wait before next iteration
        driver.refresh()
