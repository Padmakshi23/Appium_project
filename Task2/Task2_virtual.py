import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {

    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\Users\146698\Downloads\com.bsl.hyundai_2021-08-09.apk"
}

driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)

driver.implicitly_wait(30)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Don’t allow']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Don’t allow']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='SIGN UP!']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Name*']").send_keys("Padmakshi Jain")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Mobile Number*']").send_keys("1234567891")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Email ID*']").send_keys("pj@gmail.com")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Password*']").send_keys("welcom@123")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Confirm Password*']").send_keys("welcom@123")
driver.find_element(AppiumBy.XPATH,"//android.widget.CheckBox["
                                   "@resource-id='com.bsl.hyundai:id/checkAcceptTermsCondition']").click()
time.sleep(5)
print(driver.page_source)
time.sleep(5)
driver.quit()
