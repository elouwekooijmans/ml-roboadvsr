import math
import selenium.webdriver.support.wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from random import random, randint
import re
import keyboard

# Initialize dictionary containing news articles
newslist = {}

chromedriver_path = "C:/Users/zacha/Projects/fall_2023/capstone/final_project/chromedriver.exe"

# site url
url = "https://www.proquest.com/wallstreetjournal/advanced?accountid=10003&language=En&parentSessionId=Wtqf8zFd4nz6CRabQsonSR9hFH0o570bd477rRDgFps%3D"


def traverse_wsj(start_date, end_date, sector_name, ucf_user, ucf_pw, pro_user, pro_pw):
    # establishes the path to chrome driver
    service = Service(chromedriver_path)
    options = Options()
    # open in incognito to avoid cookies
    options.add_argument("--incognito")
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=options)
    sleep(random()*10)
    # open wsj page with a timeout to force proceed
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")

    # Maximize window
    driver.maximize_window()
    # add pause to circumvent bot detection
    sleep(random()*10 + 2)

    try:
        # get current url to check for ucf log in
        test_url = driver.current_url
        if test_url != url:
            element = driver.find_element(By.XPATH, """//*[@id="userNameInput"]""")
            element.send_keys(ucf_user)
            sleep(random() + randint(3, 8))

            element = driver.find_element(By.XPATH, """//*[@id="passwordInput"]""")
            element.send_keys(ucf_pw)
            sleep(random() + randint(3, 8))

            element = driver.find_element(By.XPATH, """//*[@id="submitButton"]""")
            element.click()
            sleep(random()*10+2)
        else:
            pass

        # close out first pop-up
        element = driver.find_element(By.XPATH, """//*[@id="onetrust-close-btn-container"]/button""")
        element.click()
        sleep(random()*10 +2)

        # close out second pop-up
        element = driver.find_element(By.XPATH, """//*[@id="pendo-close-guide-87416894"]""")
        element.click()
        sleep(random()*10)

        # click profile in proquest
        element = driver.find_element(By.XPATH, """//*[@id="mrDropdown"]/span[2]""")
        element.click()
        sleep(random() + randint(3, 8))

        # click sign in
        element = driver.find_element(By.XPATH, """//*[@id="mrMenu"]/li[1]/a""")
        element.click()
        sleep(randint(5, 10) + 2)

        # enter proquest username
        element = driver.find_element(By.XPATH, """//*[@id="1-email"]""")
        element.send_keys(pro_user)
        sleep(random() + randint(3, 8))

        # enter proquest password
        element = driver.find_element(By.XPATH, """//*[@id="hiw-login-container"]/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input""")
        element.send_keys(pro_pw)
        sleep(random() + randint(3, 8))

        # sign in to proquest
        element = driver.find_element(By.XPATH, """//*[@id="hiw-login-container"]/div/div/form/div/div/div/button""")
        element.click()
        sleep(randint(8, 12) + 2)

        # open side menu
        element = driver.find_element(By.XPATH, """//*[@id="DREproductBanner"]/div/div[1]/button""")
        element.click()
        sleep(random() + randint(3, 8))

        # click advanced search
        element = driver.find_element(By.XPATH, """//*[@id="navmenu1"]/li[2]/a""")
        element.click()
        sleep(random() + randint(5, 8))

        # click search bar
        element = driver.find_element(By.XPATH, """//*[@id="queryTermField"]""")
        element.send_keys(sector_name)
        sleep(random() + randint(3, 8))

        # click date range
        element = driver.find_element(By.XPATH, """//*[@id="select_multiDateRange"]/option[10]""")
        element.click()
#        sleep(random() + randint(3, 8))

        # input start month
        element = driver.find_element(By.XPATH, f"""//*[@id="month2"]/option[{str(int(start_date[5:7])+1)}]""")
        element.click()
#        sleep(random() + randint(3, 8))

        # input start day
        element = driver.find_element(By.XPATH, f"""//*[@id="day2"]/option[{str(int(start_date[8:10])+1)}]""")
        element.click()
#        sleep(random() + randint(3, 8))

        # input start year
        element = driver.find_element(By.XPATH, """//*[@id="year2"]""")
        element.send_keys(start_date[0:4])
#        sleep(random() + randint(3, 8))

        # input end month
        element = driver.find_element(By.XPATH, f"""//*[@id="month2_0"]/option[{str(int(end_date[5:7])+1)}]""")
        element.click()
#        sleep(random() + randint(3, 8))

        # input end day
        element = driver.find_element(By.XPATH, f"""//*[@id="day2_0"]/option[{str(int(end_date[8:10])+1)}]""")
        element.click()
#        sleep(random() + randint(3, 8))

        # input end year
        element = driver.find_element(By.XPATH, """//*[@id="year2_0"]""")
        element.send_keys(end_date[0:4])
        sleep(random() + randint(3, 8))

        # click search bar
        element = driver.find_element(By.XPATH, """//*[@id="searchToResultPage"]""")
        element.click()
        sleep(random() + 8)

        # click full text
        element = driver.find_element(By.XPATH, """//*[@id="filterCheckbox_fulltext"]""")
        element.click()
        sleep(random() + randint(7, 7))

        # click document type
        element = driver.find_element(By.XPATH, """//*[@id="objectype-header"]""")
        element.click()
        sleep(random() + randint(7, 11))
        print("test1")
        # click news
        element = driver.find_element(By.XPATH, """//*[@id="objectype-zone"]/ul/li[1]/a/span""")
        element.click()
        sleep(random() + randint(7, 11))

        if NoSuchElementException:
           driver.refresh()
           sleep(random() + randint(4, 8))
        else:
           pass
        print("test2")
        # click location
        element = driver.find_element(By.XPATH, """//*[@id="locationAll-hzone"]/h3/a""")
        element.click()
        sleep(random() + randint(4, 8))
        print("test3")
        # filter by United States
        element = driver.find_element(By.XPATH, """//*[@id="locationAll-zone"]/ul/li[1]/a/span""")
        element.click()
        sleep(random() + randint(7, 11))

        if NoSuchElementException:
            driver.refresh()
            sleep(random() + randint(7, 11))
        else:
           pass
        print("test4")
        # click 100
        element = driver.find_element(By.XPATH, """//*[@id="itemsPerPage"]/option[4]""")
        element.click()
        sleep(random() + randint(7, 11))

        if NoSuchElementException:
            driver.refresh()
            sleep(random() + randint(4, 8))
        else:
            pass
        print("test5")

        # sort by most recent first
        element = driver.find_element(By.XPATH, """//*[@id="sortType"]/option[3]""")
        element.click()
        sleep(random() + randint(7, 11))

        if NoSuchElementException:
            driver.refresh()
            sleep(random() + randint(7, 11))
        else:
            pass
        print("test6")
        sleep(5)
        # collect number of search results
        num_results = driver.find_element(By.XPATH, """//*[@id="pqResultsCount"]""").text
        sleep(random() + randint(7, 11))
        print("here7")
        num_results = int("".join(re.findall(r'\d+', num_results)))

        # number of times to click to the next page
        num_results = math.floor(num_results/100)
        print("test8")
        # select articles

        for page in range(1, num_results+1):
            # click all articles
            element = driver.find_element(By.XPATH, """//*[@id="mlcbAll"]""")
            element.click()
            sleep(random() + randint(7, 11))
            print("test9")
            driver.refresh()
            sleep(random() + randint(7, 11))
            # go to next page
            # trouble accessing the arrow to go to the next page when their of various lengths of results
            # might be able to solve with a nested for loop to check the length of the list
            element = driver.find_element(By.XPATH, """//*[@id="updateForm"]/nav/ul/li[-2]/a""")
            element.click()
            sleep(random() + randint(7, 11))
            print("test10")

        element = driver.find_element(By.XPATH, """//*[@id="mlcbAll"]""")
        element.click()
        sleep(random() + randint(7, 11))

        # click all save and export options
        element = driver.find_element(By.XPATH, """//*[@id="allSaveOptionsLink"]/span[1]/span""")
        element.click()
        sleep(random() + randint(7, 11))

        # download text only
        element = driver.find_element(By.XPATH, """//*[@id="allSaveOptionsOverlay"]/div[2]/div/div[2]/div[3]/div[5]/a/span[1]/span""")
        element.click()
        sleep(random() + randint(7, 11))

        # click continue
        element = driver.find_element(By.LINK_TEXT, "Continue")
        element.click()
        sleep(240)

        # create file name
        file_name = sector_name + "_" + start_date + "_to_" + end_date
        file_name = file_name.replace("/", "_")
        print(file_name)

        # input file name
        for character in file_name:
            keyboard.press_and_release(character)

        # navigate documents window
        for i in range(1, 4):
            keyboard.press_and_release("Tab")

        keyboard.press_and_release("Enter")

        sleep(120)
        driver.quit()

    except NoSuchElementException:
        driver.quit()
        traverse_wsj(start_date, end_date, sector_name, ucf_user, ucf_pw, pro_user, pro_pw)





dates_list = [["2006/01/03", "2006/12/31"], ["2007/01/01", "2007/12/31"], ["2008/01/01", "2008/12/31"],
              ["2009/01/01", "2009/12/31"], ["2010/01/01", "2010/12/31"], ["2011/01/01", "2011/12/31"],
              ["2012/01/01", "2012/12/31"], ["2013/01/01", "2013/12/31"], ["2014/01/01", "2014/12/31"],
              ["2015/01/01", "2015/12/31"], ["2016/01/01", "2016/12/31"], ["2017/01/01", "2017/12/31"],
              ["2018/01/01", "2018/12/31"], ["2019/01/01", "2019/12/31"], ["2020/01/01", "2020/12/31"],
              ["2021/01/01", "2021/12/31"], ["2022/01/01", "2022/12/31"], ["2023/01/01", "2023/10/31"]]


# collecting data from 2017/01/02 to 2023/10/31
# sectors complete: semiconductors through 1599


# changed to consumer goods to get more results
# financial has over 10k
# not many in semiconductors, consider using electronics in addition
# not many in utilities

sectors = ["Energy", "Materials", "Consumer Goods", "Healthcare", "Financial", "Semiconductors",
           "Utilities", "Real Estate", "Telecommunications", "Industrial", "Consumer Discretionary"]

# need to create a ProQuest account first and verify email so that you don't have to keep clicking the bot verification
# loop through sectors
for sector in sectors:
    # call function for each date range
    #Currently only downloads to default downloads folder
    for dates in dates_list:
        traverse_wsj(dates[0], dates[1], sector, "your_ucf_id", "your_ucf_password", "your_proquest_user", "your_proquest_password")

