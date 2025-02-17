import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_task_status(driver, add_task):
    """3333-Change task status"""
    TASK_TITLE = 'test'

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

    # Click check box
    added_task.find_element(By.XPATH, ".//div[contains(@class, 'todoItem_svgBox')]").click()

    # Verify task checkbox is set to Complete
    time.sleep(1)
    svg_box = added_task.find_element(By.XPATH, ".//div[contains(@class, 'todoItem_svgBox')]")
    background_color = svg_box.get_attribute('style')
    assert "rgb(100, 111, 240)" in background_color

    # Check if title is crossed out
    title_element = added_task.find_element(By.XPATH, ".//p[contains(@class, 'todoItem_todoText')]")
    if 'false' in title_element.get_attribute("class"):
        crossed_out = False
    else:
        crossed_out = True
    assert crossed_out == True, f"Title not crossed out"

    # Verify task date
    task_date = added_task.find_element(By.XPATH, ".//p[contains(@class, 'todoItem_time')]").text
    assert task_date == current_date, f'Invalid date'





