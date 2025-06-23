import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

st.title("LA Court Tentative Ruling Checker")

case_number = st.text_input("Enter Case Number", value="254stcv24605")

if st.button("Check Ruling"):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    try:
        driver.get("https://www.lacourt.org/tentativeRulingNet/ui/main.aspx?casetype=civil")
        time.sleep(3)

        input_box = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtCaseNumber")
        input_box.send_keys(case_number)

        button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
        button.click()
        time.sleep(5)

        try:
            message = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblMessage").text
            st.info(message)
        except:
            ruling = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblRuling").text
            st.success("Tentative Ruling:")
            st.write(ruling)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
    finally:
        driver.quit()
