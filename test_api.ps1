# PowerShell script to test the To-Do API
# Make sure the Flask server is running first!

Write-Host "Testing To-Do API..." -ForegroundColor Green

# Create a task
Write-Host "`n1. Creating a task..." -ForegroundColor Yellow
$body = @{title = "Buy milk"} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://localhost:5000/tasks" -Method POST -Body $body -ContentType "application/json"
Write-Host "Response:" $response.Content
$task = $response.Content | ConvertFrom-Json
$taskId = $task.id
Write-Host "Created task with ID: $taskId" -ForegroundColor Green

# Get all tasks
Write-Host "`n2. Getting all tasks..." -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:5000/tasks" -Method GET
Write-Host "All tasks:" $response.Content

# Mark task as done
Write-Host "`n3. Marking task $taskId as done..." -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:5000/tasks/$taskId/done" -Method POST
Write-Host "Response:" $response.Content

# Update task
Write-Host "`n4. Updating task $taskId..." -ForegroundColor Yellow
$body = @{title = "Buy milk and bread"} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://localhost:5000/tasks/$taskId" -Method PUT -Body $body -ContentType "application/json"
Write-Host "Response:" $response.Content

# Get all tasks again
Write-Host "`n5. Getting all tasks again..." -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:5000/tasks" -Method GET
Write-Host "All tasks:" $response.Content

# Delete task
Write-Host "`n6. Deleting task $taskId..." -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:5000/tasks/$taskId" -Method DELETE
Write-Host "Task deleted (Status: $($response.StatusCode))" -ForegroundColor Green

Write-Host "`nTesting complete!" -ForegroundColor Green

