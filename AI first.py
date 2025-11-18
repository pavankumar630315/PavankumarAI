from selenium import webdriver
from selenium.webdriver.common.by import By
from difflib import SequenceMatcher
import time

# Function to compare expected text with actual text using AI similarity
def ai_text_match(expected, actual):
    similarity = SequenceMatcher(None, expected, actual).ratio()
    return similarity

# Open browser
driver = webdriver.Chrome()

# Go to webpage
driver.get("https://example.com")
time.sleep(2)

# Expected text
expected_heading = "Example Domain"

# Locate heading
element = driver.find_element(By.TAG_NAME, "h1")
actual_heading = element.text

# AI similarity validation
score = ai_text_match(expected_heading, actual_heading)

print("Expected Text:", expected_heading)
print("Actual Text:", actual_heading)
print("Similarity Score:", score)

# Pass/Fail based on similarity threshold
if score > 0.8:
    print("TEST RESULT: PASS (Text matches closely)")
else:
    print("TEST RESULT: FAIL (Text mismatch)")

driver.quit()

























