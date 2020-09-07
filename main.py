import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

dir_path = os.path.dirname(os.path.realpath(__file__))


def getBlockText(driver, blockRequested):
    current_day = driver.find_element_by_class_name('current-day')
    blocks = current_day.find_elements_by_class_name('block')
    if(blockRequested == 1):
        blockElement = blocks[0]
    else:
        blockElement = blocks[1]

    blockWanted = blockElement.find_element_by_class_name('selected-activity')
    return blockWanted


def ifCustomGetName(driver, customID):
    driver.get('https://ion.tjhsst.edu/eighth/?activity=' + customID)
    className = driver.find_element_by_class_name('activity-detail-link')
    return className.text


def join_class(link):
    driver = webdriver.Chrome(dir_path + r'\chromedriver.exe', options  =chrome_options)
    driver.get(link)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "confirm"))
        )
    except:
        pass

    audio = driver.find_element_by_class_name('confirm')
    audio.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "confirm"))
        )
    except:
        pass

    video = driver.find_element_by_class_name('confirm')
    video.click()

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.close')))
    button.click()

    while True:
        x = 1

    # id_box = driver.find_element_by_name('username')
    # id_box.send_keys(username)
    # pass_box = driver.find_element_by_name('password')
    # pass_box.send_keys(password)
    # login = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/input[4]")
    # login.click()
    #
    # if 'Upcoming' not in driver.page_source:
    #     status_label.configure(text='Incorrect Login')
    #     return 'Terminated'
    #
    # eighth = driver.find_element_by_xpath('/html/body/div[3]/ul/li[2]/a')
    # eighth.click()
    #
    # current_day = driver.find_element_by_class_name('current-day')
    # blocks = current_day.find_elements_by_class_name('block')
    #
    #
    # blockParent = blockElement.find_element_by_xpath('..')
    # blockParent.click()
    #
    # if customID:
    #     activitySliver = ifCustomGetName(driver, customID).strip()
    #     activity = customID
    # else:
    #     activitySliver = IDtonames.get(activity)
    #
    # blockWanted = getBlockText(driver, blockRequested)
    # timesTried = 0
    # while(activitySliver not in blockWanted.text):
    #     driver.get(driver.current_url + '?activity=' + activity)
    #     try:
    #         signup_button = driver.find_element_by_id('signup-button')
    #         signup_button.click()
    #     except Exception:
    #         timesTried += 1
    #         status_label.configure(text='Times tried:' + str(timesTried))
    #         root.update_idletasks()
    #         print('bing bang boom here is your times tried:' + str(timesTried))
    #
    #     blockWanted = getBlockText(driver, blockRequested)
    #     time.sleep(6)

    # driver.close()



join_class('https://us.bbcollab.com/invite/11e7abad5c0649b2a0b170d61237b567')
