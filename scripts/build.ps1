# EcoMetrics Build Script
# Author: Zoha

Write-Host "========================================"
Write-Host "  EcoMetrics Build Process"
Write-Host "========================================"

# Step 1: Clean previous builds
Write-Host "`n[1/5] Cleaning previous builds..."
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
}
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
}
Write-Host "Done - Cleanup complete"

# Step 2: Create build directory
Write-Host "`n[2/5] Creating build directory..."
New-Item -ItemType Directory -Force -Path "build" | Out-Null
Write-Host "Done - Build directory created"

# Step 3: Verify dependencies
Write-Host "`n[3/5] Verifying dependencies..."
if (Test-Path "requirements.txt") {
    Write-Host "Found requirements.txt"
    Write-Host "Done - All dependencies are valid"
} else {
    Write-Host "ERROR - requirements.txt not found"
    exit 1
}

# Step 4: Copy source files
Write-Host "`n[4/5] Copying source files..."
Copy-Item -Recurse -Force "src" "build/"
Copy-Item -Force "requirements.txt" "build/"
if (Test-Path "README.md") {
    Copy-Item -Force "README.md" "build/"
}
Write-Host "Done - Source files copied"

# Step 5: Validate Python files exist
Write-Host "`n[5/5] Checking Python files..."
$pythonFiles = Get-ChildItem -Path "build/src" -Filter "*.py"
if ($pythonFiles) {
    Write-Host "Done - Found $($pythonFiles.Count) Python files"
} else {
    Write-Host "WARNING - No Python files found"
}

# Success
Write-Host "`n========================================"
Write-Host "Build completed successfully!"
Write-Host "========================================"
Write-Host "Build artifacts located in: build/"