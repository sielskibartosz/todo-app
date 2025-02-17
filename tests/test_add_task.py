import json
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



def test_add_task(driver):
    """2222-Add task to the task list"""
    TASK_TITLE = "test"

    # Check local storage
    local_storage = len(json.loads(driver.execute_script("return window.localStorage.getItem('todoList')") or "[]"))

    # Click Add Task button
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Task')]"))).click()

    # Provide title
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='title']"))).send_keys(f'{TASK_TITLE}')

    # Submit
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Add Task']"))).click()

    # Check updated local storage
    assert local_storage < len(
        json.loads(driver.execute_script(
            "return window.localStorage.getItem('todoList')") or "[]")), f"Local storage not updated"

    # Wait for task to be present
    added_task = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'todoItem_item')])[1]")))

    # Verify task title
    task_title = added_task.find_element(By.XPATH, ".//p[contains(@class, 'todoItem_todoText')]").text
    assert task_title == TASK_TITLE, f"Wrong task title"

    # Verify task date
    task_date = added_task.find_element(By.XPATH, ".//p[contains(@class, 'todoItem_time')]").text
    current_date = datetime.now().strftime("%I:%M %p, %m/%d/%Y").lstrip("0")
    assert task_date == current_date, f'Invalid date'

    # Wait for the popup to appear
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@role='status' and contains(text(), 'Task added successfully')]")))

    # Verify task checkbox is set to Incomplete
    time.sleep(1)
    svg_box = added_task.find_element(By.XPATH, ".//div[contains(@class, 'todoItem_svgBox')]")
    background_color = svg_box.get_attribute('style')
    assert "rgb(222, 223, 225)" in background_color

    # Check if title is not crossed out
    title_element = added_task.find_element(By.XPATH, ".//p[contains(@class, 'todoItem_todoText')]")
    if 'false' in title_element.get_attribute("class"):
        crossed_out = False
    else:
        crossed_out = True
    assert crossed_out == False, f"Title is crossed out"

    # Wait for the popup to disappear
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(
            (By.XPATH, "//div[@role='status' and contains(text(), 'Task added successfully')]")))




