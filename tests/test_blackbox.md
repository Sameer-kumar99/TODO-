# Black-box Test Cases for To-Do App

## Test Case TC-01: Create task - valid
- **Precondition**: App running
- **Steps**:
  1. Open "Add task"
  2. Enter title: "Buy milk"
  3. Submit
- **Expected**: Task appears in list with status = pending

## Test Case TC-02: Create task - empty title
- **Precondition**: App running
- **Steps**: 
  1. Open "Add task"
  2. Submit with empty title ""
- **Expected**: Error message "Title is required"; task NOT created

## Test Case TC-03: View tasks
- **Precondition**: App running, at least one task created
- **Steps**: Go to task list
- **Expected**: All previously created tasks are visible

## Test Case TC-04: Mark task complete
- **Precondition**: App running, task "Buy milk" exists
- **Steps**: Click "Complete" on "Buy milk"
- **Expected**: Status changes to "done" / visually struck through

## Test Case TC-05: Edit task
- **Precondition**: App running, task "Buy milk" exists
- **Steps**: Edit title "Buy milk" → "Buy milk and bread"
- **Expected**: Updated title shown in list

## Test Case TC-06: Delete task
- **Precondition**: App running, at least one task exists
- **Steps**: Delete any existing task
- **Expected**: Task removed from list

## Test Case TC-07: Create task - whitespace only title
- **Precondition**: App running
- **Steps**: Submit with title containing only spaces "   "
- **Expected**: Error message "Title is required"; task NOT created

## Test Case TC-08: Update task - empty title
- **Precondition**: App running, at least one task exists
- **Steps**: Try to update task title to empty string ""
- **Expected**: Error message "Title is required"; task NOT updated

## Test Case TC-09: Mark non-existent task as done
- **Precondition**: App running
- **Steps**: Try to mark task with ID 999 as done
- **Expected**: Error message "Not found"; status code 404

## Test Case TC-10: Delete non-existent task
- **Precondition**: App running
- **Steps**: Try to delete task with ID 999
- **Expected**: Error message "Not found"; status code 404

