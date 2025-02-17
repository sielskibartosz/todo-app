import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """Prepare driver and quit it after session"""
    driver = webdriver.Chrome()
    driver.get("https://wc-react-todo-app.netlify.app/")
    yield driver
    driver.quit()


@pytest.fixture
def add_task(driver):
    """Add task to the task list"""
    TASK_TITLE = 'test'
    driver.find_element(By.XPATH, f"//button[normalize-space()='Add Task']").click()
    driver.find_element(By.XPATH, f"//*[@id='title']").send_keys(TASK_TITLE)
    driver.find_element(By.XPATH, "//button[@type='submit' and text()='Add Task']").click()
