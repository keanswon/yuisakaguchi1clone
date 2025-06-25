# file to upload videos

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time, os

import dotenv

dotenv.load_dotenv()

# ─── CONFIG ────────────────────────────────────────────────────────────────
USERNAME   = os.getenv("USERNAME")
PASSWORD   = os.getenv("PASSWORD")
VIDEO_PATH = os.path.join(os.getcwd(), "OUTPUT", "final.mp4")
CAPTION    =    """follow for more relatable content...

                
                
                inspired by @yuisakaguchi1 and automated using python

                #fyp #shorts
                """
# ───────────────────────────────────────────────────────────────────────────

def upload_reel_firefox(username, password, video_path, caption):
    # 1) Build a Firefox profile that pretends to be an iPhone
    profile = FirefoxProfile()

    # 2) Launch Firefox with that profile & a mobile-sized window
    options = FFOptions()
    # optionally run headless: options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 20)

    try:
        # 3) Go to Instagram login
        driver.get("https://www.instagram.com/accounts/login/")
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

        # 4) Fill creds & submit
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("login info submitted!")

        # 5) Dismiss “Save Login Info?” and “Turn on Notifications”
        # not_now = WebDriverWait(driver, 10).until(
        # EC.element_to_be_clickable((By.XPATH,
        #     # look for any div with role=button, any whitespace normalized, exact text "Not now"
        #     "//div[@role='button' and normalize-space(.)='Not now']"
        # ))
        # )
        # not_now.click()
        # print("not now clicked!")
        time.sleep(5)

        print("making a new post!")
        # 6) Tap the “+” (new post) button
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="New post"]'))
        )
        element.click()

        # 8) Upload video via the file-input
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"][class="_ac69"]'))
        )
        file_input.send_keys(os.path.abspath(video_path))
        print("files sent!")

        # unsure if this is a one time thing, may have to remove
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
        )
        ok_button.click()
        
        print("ready to select video size!")

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Select crop"]'))
        )
        button.click()

        original_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Original']"))
        )
        original_button.click()

        print("video resized!")

        # 9) “Next” till the description screen
        for _ in range(2):
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Next']"))
            )
            next_button.click()
            time.sleep(1)

        # 10) Enter caption - wait for the final page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Write a caption..."]'))
        )

        caption_box = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Write a caption..."]')
        caption_box.click()
        time.sleep(0.5)
        print("caption: " + caption)
        print("caption printed!")
        [caption_box.send_keys(c) for c in caption] 
        time.sleep(5)

        # 11) Share
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Share']"))
        ).click()

        # 12) Wait a few seconds for the upload to finish
        time.sleep(20)
        print("✅ Uploaded reel successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    upload_reel_firefox(USERNAME, PASSWORD, VIDEO_PATH, CAPTION)
