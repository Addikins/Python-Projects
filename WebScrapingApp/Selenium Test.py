from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path=r'geckodriver.exe')


def login():
    loginPage = "https://account.cengage.com/login?SAMLRequest=fZJdS8MwFIb%2FSsl92%2FTLdmGdDIcw0CF%2BId6F9KwG25Oak27u3xs7J3qhkKtwzvO%2BPMn8%2FL3vgh1Y0gZrlkScBYDKNBrbmj3cX4YVO1%2FMSfZdOojl6F7wFt5GIBcsicA6v3ZhkMYe7B3YnVbwcHtVsxfnBhJxLP1GpABb2UKkTB8TmXiixdzI9Kyoki3S5qnYtMusKFmw8miN0k11vilKmRHdL1BnWo0suDRWwdSrZlvZEbBgvaqZbtIkr5IsL8sqTytezvKkyGY5z6oy8yNEI6yRnERXs5SnPORFyKt7zkWa%2BxPxbPbMgseTmPRTjFeFJI4uajZaFEaSJoGyBxJOibvl9ZXwo2KwxhllOvalTkyB9ifhf4A8yWWLk4T9fh%2BZVyePGieFdDQe%2BridbsDGNOyw6QHlwQy2fZPNoXHz%2BGeF77fc%2BMz16sZ0Wh0%2BLfbS%2FV0piZLpRjfhdhoVI9IASm81NCxefGX8%2FiGLDw%3D%3D&RelayState=%252Foauth2%252Fv1%252Fauthorize%252Fredirect%253Fokta_key%253DmUZ5SaWzHrF6kZvOBzTDWEaWyyUqhGIoQwCeZnc6SY8&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=SR1vbgj1rRGB0UzqFsizypFVawWZqZ1gWZTEEl7F7B0lI9bsfLgjbsXjqNblfLhbTcY02nN%2F%2BuSD2jAJFCDJUobr0plfSMzuqCXZ%2FRXb8rXN5FYo5ApTMlDJELQ56C5bu2HoZJRk5BFgch7HCF5pSSGgFBmTNpFiWO3CKIneL7qhSTiYfeB3loTe295TKxBTJydUffGaOexJvbUmJ97pynjialRrJAxe5FSQ0%2FiyM%2Bi8vwywcDXS37iYX2ql7%2BWrig34n9fEyFNMFOP5Dv2iSGCsHnjjg1OLyzSQAf1nc7%2FdcPdgp8SZlkm7u6OKibvm%2B0CwiZTScUUDSIcZYHvdYA%3D%3D"
    browser.get(loginPage)

    #Enter this:
    email = "addyahs14@gmail.com"
    #Into this:
    emailField = browser.find_element_by_css_selector("#idp-discovery-username")
    emailField.send_keys(email)

    #Click this
    emailField.submit()
    # nextButton = browser.find_element_by_css_selector("#idp-discovery-submit")
    # nextButton.click()

    #Enter this:
    password = ""
    #Into this:
    while True:
        time.sleep(1)
        try:
            passwordField = browser.find_element_by_css_selector("#okta-signin-password")
            passwordField.send_keys(password)
            time.sleep(1)
            passwordField.submit()
            break
        except ValueError:
            print("Can't find password field!")
    time.sleep(1)
    returnButton = browser.find_element_by_css_selector(".button")
    returnButton.click()

    time.sleep(1)
    signinButton = browser.find_element_by_css_selector(".js-signin")
    signinButton.click()
    time.sleep(1)

    browser.get("https://www.cengage.com/dashboard/#/my-dashboard/authenticated?page=")

    time.sleep(2)
    classQuickLink = browser.find_element_by_css_selector("#tile1 > a > div")
    classQuickLink.click()


login()
startAttempt = "#mtAttempt"
# Module 8: "#activity-heading-686357593"
# Module 9: "#activity-heading-686357609"
