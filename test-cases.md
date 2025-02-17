# Test Cases

## 1111. Add task modal
### Description:
Verify that a user can add a new task.

### Preconditions:
- The application is loaded.

### Steps:
1. Click the "Add Task" button.
2. Enter a title in the popup window and submit.

### Expected result:
- The added task appears in the task list with the correct title.
- The task is saved in local storage.
- The task has a default status of "incomplete."
- The task has the correct timestamp.
- Task added popup show up

---

## 2222. Add new task
### Description:
Verify that a user can add a new task.

### Preconditions:
- The application is loaded.

### Steps:
1. Click the "Add Task" button.
2. Enter a title in the popup window and submit.

### Expected result:
- The added task appears in the task list with the correct title.
- The task is saved in local storage.
- The task has a default status of "incomplete."
- The task has the correct timestamp.

---

## 3333. Change status via checkbox
### Description:
Verify that a user can change a task's status from "incomplete" to "complete."

### Preconditions:
- At least one incomplete task is added to the task list.

### Steps:
1. Click on the checkbox associated with the task.

### Expected result:
- The task checkbox icon should change to "complete."
- The task title should be crossed out.
- The task timestamp remains unchanged.

---

## 4444. Delete a task
### Description:
Verify that a user can delete a task.

### Preconditions:
- At least one task is added to the task list.

### Steps:
1. Click on the delete button/icon associated with the task.

### Expected result:
- The task is no longer present in the task list.
- The task is removed from local storage.
- Task deletion pup up show up

---

## 5555. Page refresh
### Description:
Verify that tasks persist after refreshing the page.

### Preconditions:
- At least one task is added to the task list.

### Steps:
1. Refresh the webpage.

### Expected result:
- The number of tasks in the task list remains unchanged after the page reloads.
- The tasks retain their status (complete/incomplete).
- The tasks retain their timestamps.


