# To-Do List Testing Project

A comprehensive To-Do List application with full test coverage, demonstrating black-box and white-box testing methodologies. This project serves as a portfolio piece showcasing testing skills including unit testing, integration testing, and test design.

## Project Overview

This project implements a simple To-Do List application using Flask (Python) with a focus on testing. It demonstrates:

- **Black-box testing**: Test cases designed from requirements without knowledge of internal implementation
- **White-box testing**: Unit tests that test internal logic and code paths
- **Integration testing**: API-level tests that verify end-to-end functionality
- **Test automation**: Automated test suites using pytest

## Requirements

### Functional Requirements

1. User can create a task (title required)
2. User can view all tasks
3. User can mark a task as complete
4. User can edit a task title
5. User can delete a task
6. Title must not be empty
7. Tasks are stored in memory (for this version)

## Project Structure

```
todo-testing-project/
├── app/
│   ├── __init__.py
│   ├── app.py          # Flask application with REST API
│   └── services.py     # Business logic (TodoService)
├── tests/
│   ├── test_blackbox.md  # Manual black-box test cases
│   ├── test_services.py  # Unit tests (white-box)
│   └── test_app.py       # API integration tests
├── requirements.txt
└── README.md
```

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd "TO-DO APP"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Start the Flask Server

You can run the Flask app in one of these ways:

**Option 1: Run as a module (recommended)**
```bash
python -m app
```

**Option 2: Run the app file directly**
```bash
python app/app.py
```

The server will start on `http://localhost:5000` (default Flask port).

### API Endpoints

- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task (requires JSON: `{"title": "Task title"}`)
- `PUT /tasks/<task_id>` - Update a task (requires JSON: `{"title": "New title"}`)
- `POST /tasks/<task_id>/done` - Mark a task as complete
- `DELETE /tasks/<task_id>` - Delete a task

### Example API Usage

**Using PowerShell (Windows):**

```powershell
# Create a task
$body = @{title = "Buy milk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://localhost:5000/tasks" -Method POST -Body $body -ContentType "application/json"

# Get all tasks
Invoke-WebRequest -Uri "http://localhost:5000/tasks" -Method GET

# Mark task as done (replace 1 with actual task ID)
Invoke-WebRequest -Uri "http://localhost:5000/tasks/1/done" -Method POST

# Update a task
$body = @{title = "Buy milk and bread"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://localhost:5000/tasks/1" -Method PUT -Body $body -ContentType "application/json"

# Delete a task
Invoke-WebRequest -Uri "http://localhost:5000/tasks/1" -Method DELETE
```

**Or use the test script:**
```powershell
.\test_api.ps1
```

**Using curl.exe in PowerShell (Windows):**

```powershell
# Create a task (use single quotes and escape inner quotes)
curl.exe -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{\"title\": \"Buy milk\"}'

# Get all tasks
curl.exe http://localhost:5000/tasks

# Mark task as done
curl.exe -X POST http://localhost:5000/tasks/1/done

# Update a task
curl.exe -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{\"title\": \"Buy milk and bread\"}'

# Delete a task
curl.exe -X DELETE http://localhost:5000/tasks/1
```

**Using curl (Linux/Mac/Git Bash):**

```bash
# Create a task
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Buy milk"}'

# Get all tasks
curl http://localhost:5000/tasks

# Mark task as done
curl -X POST http://localhost:5000/tasks/1/done

# Update a task
curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "Buy milk and bread"}'

# Delete a task
curl -X DELETE http://localhost:5000/tasks/1
```

## Running Tests

### Run All Tests

```bash
python -m pytest
```

Or with verbose output:
```bash
python -m pytest -v
```

### Run Specific Test File

```bash
# Run unit tests only
python -m pytest tests/test_services.py

# Run API tests only
python -m pytest tests/test_app.py
```

### Run Tests with Coverage (optional)

First install coverage:
```bash
pip install pytest-cov
```

Then run:
```bash
python -m pytest --cov=app --cov-report=html
```

**Note:** On Windows, use `python -m pytest` instead of just `pytest` to avoid PATH issues.

## Test Plan

### Scope

- **In Scope**: CRUD operations for tasks (Create, Read, Update, Delete, Mark as Done)
- **Out of Scope**: 
  - Authentication and authorization
  - Multi-user support
  - Persistent storage (database)
  - User interface (HTML/JavaScript)
  - Task priorities, due dates, categories

### Test Types

1. **Black-box Tests** (`tests/test_blackbox.md`)
   - Manual test cases based on requirements
   - Test cases cover valid and invalid inputs
   - Boundary value testing (empty titles, whitespace)

2. **White-box Tests** (`tests/test_services.py`)
   - Unit tests for `TodoService` class
   - Tests internal logic and code paths
   - Tests error handling (ValueError, KeyError)
   - Tests edge cases and boundary conditions

3. **Integration Tests** (`tests/test_app.py`)
   - API endpoint tests
   - End-to-end workflow tests
   - HTTP status code verification
   - JSON response validation

### Test Coverage

- ✅ Create task (valid and invalid inputs)
- ✅ List tasks
- ✅ Mark task as complete
- ✅ Update task (valid and invalid inputs)
- ✅ Delete task
- ✅ Error handling (non-existent tasks, empty titles)
- ✅ Task ID incrementing
- ✅ Multiple operations workflow

## Test Cases

Detailed black-box test cases are documented in `tests/test_blackbox.md`. These test cases include:

- TC-01: Create task - valid
- TC-02: Create task - empty title
- TC-03: View tasks
- TC-04: Mark task complete
- TC-05: Edit task
- TC-06: Delete task
- TC-07: Create task - whitespace only title
- TC-08: Update task - empty title
- TC-09: Mark non-existent task as done
- TC-10: Delete non-existent task

## Testing Concepts Demonstrated

### Black-box Testing
- Testing from the user's perspective
- Test cases based on requirements
- No knowledge of internal implementation
- Focus on inputs and expected outputs

### White-box Testing
- Testing internal code structure
- Code path coverage
- Testing error handling
- Testing edge cases and boundary conditions

### Test Automation
- Automated test execution with pytest
- Repeatable test runs
- Fast feedback on code changes
- CI/CD integration ready

### Test Design Techniques
- Equivalence partitioning
- Boundary value analysis
- Positive and negative test cases
- Error condition testing

## Defect Log

While testing, any bugs found should be logged with:
- **ID**: Unique defect identifier
- **Steps**: Steps to reproduce
- **Expected**: Expected behavior
- **Actual**: Actual behavior
- **Status**: Open/Fixed/Closed

*(No defects logged yet - all tests passing)*

## Future Enhancements

Potential improvements for this project:

1. **Database Integration**: Replace in-memory storage with SQLite or PostgreSQL
2. **User Interface**: Add HTML/JavaScript frontend
3. **Selenium Tests**: Add end-to-end UI tests
4. **Authentication**: Add user authentication and authorization
5. **Task Features**: Add priorities, due dates, categories
6. **API Documentation**: Add Swagger/OpenAPI documentation
7. **Docker**: Containerize the application
8. **CI/CD**: Add GitHub Actions or similar for automated testing

## Technologies Used

- **Python 3.7+**: Programming language
- **Flask**: Web framework for REST API
- **pytest**: Testing framework
- **JSON**: Data format for API communication

## Learning Outcomes

This project demonstrates:

1. Understanding of black-box vs white-box testing
2. Test case design and documentation
3. Test automation with pytest
4. API testing
5. Test-driven development concepts
6. Software testing best practices

## Author

This project was created as a portfolio piece to demonstrate testing skills and methodologies.

## License

This project is open source and available for educational purposes.

