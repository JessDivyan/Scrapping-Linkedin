import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

driver.get(
    "https://www.linkedin.com/jobs/search/?keywords=data%20Analyst&location=United%20Kingdom&geoId=101165590&f_JT=F&f_E=2%2C3&f_TPR=r604800&position=1&pageNum=0"
)

driver.implicitly_wait(1)
n_joblist = driver.find_element(
    By.CLASS_NAME, value="results-context-header__job-count"
).text
n = pd.to_numeric(n_joblist.replace(",", "").replace("+", ""))
print(n)

listing = []


def jobs_list():
    global listing
    job_results = driver.find_element(By.CLASS_NAME, value="jobs-search__results-list")
    listing = job_results.find_elements(By.TAG_NAME, "li")
    return listing


jobs_list()

while len(listing) < 950:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    jobs_list()
    if driver.find_element(
        By.XPATH, "/html/body/div[3]/div/main/section[2]/button"
    ).is_displayed():
        send = driver.find_element(
            By.XPATH, "/html/body/div[3]/div/main/section[2]/button"
        )
        send.click()
        time.sleep(3)

driver.quit()
rolesNlinks = []
for l in listing:
    j = {}
    j["Role"] = l.find_element(By.TAG_NAME, "a").text
    j["Link"] = l.find_element(By.TAG_NAME, "a").get_attribute("href")

    rolesNlinks.append(j)

df_links = pd.DataFrame(rolesNlinks, columns=["Role", "Link"])
df_links.to_csv("analystlinks1.csv", index=False)
