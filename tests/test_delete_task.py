import json
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_delete_task(driver, add_task):
    """4444-Delete task from tasks list"""

    # Verify there are tasks in local storage
    local_storage = json.loads(driver.execute_script("return window.localStorage.getItem('todoList')") or "[]")
    assert len(local_storage) >= 1, "No elements in local storage"

    # Verify UI task list
    tasks_list = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'todoItem_item')]")))
    assert len(tasks_list) >= 1, "No elements in todo list"

    # Click the first delete icon
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[contains(@class, 'todoItem_icon') and @role='button'])[1]"))).click()

    # Wait for the popup to appear
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@role='status' and contains(text(), 'Todo Deleted Successfully')]")))

    # Verify local storage length
    updated_local_storage = json.loads(driver.execute_script("return window.localStorage.getItem('todoList')") or "[]")
    assert len(local_storage) > len(updated_local_storage), f"Local storage not changed"

    # Verify UI task list
    try:
        updated_tasks_list = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'todoItem_item')]")))
    except TimeoutException:
        updated_tasks_list = []
    assert len(updated_tasks_list) < len(tasks_list), "Task was not removed from UI"

    # Wait for the popup to disappear
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(
            (By.XPATH, "//div[@role='status' and contains(text(), 'Todo Deleted Successfully')]")))
