import json

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_page_refresh(driver, add_task):
    """5555-Test task persisting after refreshing the page."""

    # Verify there are tasks in local storage
    local_storage = json.loads(driver.execute_script("return window.localStorage.getItem('todoList')") or "[]")
    assert len(local_storage) >= 1, "No elements in local storage"

    # Verify UI task list
    tasks_list = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'todoItem_item')]")))
    assert len(tasks_list) >= 1, "No elements in todo list"

    # Refresh the page
    driver.refresh()

    # Verify local storage length
    updated_local_storage = json.loads(driver.execute_script("return window.localStorage.getItem('todoList')") or "[]")
    assert len(local_storage) == len(updated_local_storage), f"Local storage not changed"

    # Verify UI task list
    try:
        updated_tasks_list = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'todoItem_item')]")))
    except TimeoutException:
        updated_tasks_list = []
    assert len(updated_tasks_list) == len(tasks_list), "Task was not removed from UI"
