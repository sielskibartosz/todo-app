import json
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_add_task_modal(driver):
    """1111- Verify all elements in the Add Task Modal"""

    # Click the "Add Task" button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Task')]"))).click()

    # Wait for modal to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'modal_container')]")))

    # Verify modal has input field
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input")))

    # Verify modal has a select dropdown with the correct options
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "type"))
    )
    options = select_element.find_elements(By.TAG_NAME, "option")
    status_values = [option.text for option in options]

    assert "Incomplete" in status_values, "'Incomplete' option is missing."
    assert "Completed" in status_values, "'Completed' option is missing."

    # Verify modal has a submit button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Add Task')]")))

    # Verify modal has a cancel button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(text(), 'Cancel')]")))
