from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dateutil import parser
import time, os, sys, json, webbrowser

# !/usr/bin/env python
# -*- coding: utf-8 -*-

print("Welcome to Dominos Pizza Israel Automated Delivery by Nati Aker!")
print("Version: Beta 0.5")


def selenium_process(city, street, house_number, email, password):

    driver = webdriver.Chrome('chromedriver')

    driver.get("http://www.dominos.co.il")  # Lets start!
    driver.find_element_by_xpath('//*[@id="layer-homepage-video"]/div[2]/a').click()  # Close the popup

    wait = WebDriverWait(driver, 10)  # wait
    element = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#nav > li.order-now-header.des')))
    driver.find_element_by_css_selector('#nav > li.order-now-header.des').click()  # open order

    driver.find_element_by_name('city_text').send_keys(city)  # city

    wait = WebDriverWait(driver, 10)  # wait
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/ul/li')))
    driver.find_element_by_xpath('/html/body/div[4]/ul/li').click()

    wait = WebDriverWait(driver, 10)  # wait
    element = wait.until(EC.element_to_be_clickable(
        (By.NAME, 'street_text')))
    time.sleep(5)
    driver.find_element_by_name('street_text').send_keys(street)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/ul/li[1]'))).click()
    wait = WebDriverWait(driver, 10)  # wait
    element = wait.until(EC.element_to_be_clickable(
        (By.NAME, 'number')))
    driver.find_element_by_name('number').send_keys(house_number)
    time.sleep(5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="btn_delivery"]').click()
    # Second Screen - Choose the Pizza
    driver.find_element_by_xpath('//*[@id="subNav"]/li[5]/a/p').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="itemsList"]/div[1]/ul[4]/li[1]/div/div[2]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="frm-recommended"]/ul[1]/li[1]/div/div[2]/div[2]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="wrapperPastry"]/div/div[1]/div[2]/div/ul/li[1]/a/span').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="builderCategory"]/div[4]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="extra_cheese_popup"]/div[2]/div/span').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="itemsPopupList"]/li[1]/div[2]/div/a/span').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="itemsPopupList"]/li[1]/div[2]/div/a/span').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="goToOrderButton"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="upsales-wrapper-image"]/span[2]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="upsales-wrapper-image"]/span[2]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="upsales-wrapper-image"]/span[3]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="toCart"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="frm_login"]/div[1]/input').send_keys(email)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="frm_login"]/div[2]/input').send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath('// *[ @ id = "btn_login"]').send_keys(password)
    sys.exit()


if os.path.isfile('config.json'):
    with open('config.json') as c:
        obj = c.read()
        config = json.loads(obj)

        valid_answers = ['1', '2', '3', '4', '5']
        print("1. Make a single delivery\n"
              "2. Make a scheduled delivery\n"
              "3. Change the config file\n"
              "4. About\n"
              "5. Exit\n")
        answer = input("Please select an option from the menu: ")

        while answer not in valid_answers:
            answer = input("Please select an option from the menu: ")
        if answer == '1':
            selenium_process(config['City'], config['Street'], config['House_Number'], config['Email'],
                             config['Password'])

        elif answer == '2':  # Option 2 - Make a scheduled delivery
            now = parser.parse(time.strftime("%H:%M:%S"))
            delivery_time = parser.parse(config["Time"])
            delta_time = delivery_time - now
            while str(delta_time) != "0:00:00":
                time.sleep(1)
                now = parser.parse(time.strftime("%H:%M:%S"))
                delivery_time = parser.parse(config["Time"])
                delta_time = delivery_time - now
                print("More " + str(delta_time)[-8:] + " to the delivery.", end='\r')

            print("Time is up. The program will now send a request to Dominos.")
            selenium_process(config['City'], config['Street'], config['House_Number'], config['Email'],
                             config['Password'])

            sys.exit()

        elif answer == '3':  # Option 3 - Change the config file
            with open('config.json', 'w') as config:
                    data = {'Time': input("Time to order (HH:MM): "), 'City': input("City (In Hebrew): "),
                            'Street': input("Street (In Hebrew): "), 'House_Number': input("House Number: "),
                            'Email': input("Email: "), 'Password': input("Password: ")}

                    s = json.dumps(data)
                    config.write(s)
                    sys.exit()

        elif answer == '4':  # Option 4 - About
            print("About me:\n"
                  "My name is Nati Aker,\n"
                  "I'm young and passionate programmer from Ramat-Gan (Israel), a saxophonist and a freelancer.\n"
                  "My favorite language is Python - the possibilities with it are endless!\n"
                  "\n"
                  "About this program:\n"
                  "1. I made it because I started learning Selenium and I wanted to showcase my skills.\n"
                  "2. Also, automated food :D.\n"
                  "3. I'm in now way, shape or form affiliated with Dominos Pizza Israel.\n"
                  "4. I'm also not responsible for any damage done with this program.\n"
                  "5. This program was build for education purposes. It is not an 'hacking' program.\n"
                  "6. The program goes all the way up until the payment part. Going after that part is illegal.\n"
                  "7. This is a 0.5 beta version of this program. It's going to get patched and fixed a lot in the next"
                  " few weeks.\n"
                  "8. The config.json file might be problematic. If so, just delete and remake it.\n"
                  "9. Any comment would be greatly appreciated! You may reach out to me via those platforms (A-D):\n")
            valid_answers = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
            print(
                  "A. Facebook\n"
                  "B. LinkedIn\n"
                  "C. Github (For the source code of this project and more)\n"
                  "D. Exit")
            answer = input()
            while answer not in valid_answers:
                answer = input("A-D\n")
            if answer == 'A' or answer == 'a':
                webbrowser.open("https://www.facebook.com/profile.php?id=100002019295804&ref=bookmarks")
            elif answer == 'B' or answer == 'b':
                webbrowser.open("https://www.linkedin.com/in/nathaniel-aker-172766153/")
            elif answer == 'C' or answer == 'c':
                webbrowser.open("https://github.com/netn10")
            elif answer == 'D' or answer == 'd':
                sys.exit()

        elif answer == '5':  # Option 5 - Exit
            sys.exit()

        else:
            answer = input("Please select an option from the menu: ")

else:  # The config file can't be found
    valid_answers = ['Y', 'y', 'N', 'n']
    answer = input("Config file is not found. Would you like to make one? (Y/N) ")
    while answer not in valid_answers:
        answer = input("Config file is not found. Would you like to make one? (Y/N) ")
    if answer == 'N' or answer == 'n':
        sys.exit()
    elif answer == 'Y' or answer == 'y':
        with open('config.json', 'w') as config:
            data = {'Time': input("Time to order (HH:MM): "), 'City': input("City (In Hebrew): "),
                    'Street': input("Street (In Hebrew): "),
                    'House_Number': input("House Number: "), 'Email': input("Email: "),
                    'Password': input("Password: ")}

            s = json.dumps(data)
            config.write(s)
            sys.exit()
