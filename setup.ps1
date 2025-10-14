# QuestBoard Setup Script for Windows PowerShell
# Updated and cleaned

Write-Host "🎮 QuestBoard Setup Script" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Flutter is installed
Write-Host "Checking Flutter installation..." -ForegroundColor Yellow
try {
    flutter --version 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Flutter is installed" -ForegroundColor Green
    }
} catch {
    Write-Host "✗ Flutter is not installed" -ForegroundColor Red
    Write-Host "Please install Flutter from: https://flutter.dev/docs/get-started/install" -ForegroundColor Yellow
    exit 1
}

# Check if Git is configured
Write-Host ""
Write-Host "Checking Git configuration..." -ForegroundColor Yellow
$gitUser = git config --global user.name 2>$null
$gitEmail = git config --global user.email 2>$null

if ([string]::IsNullOrEmpty($gitUser) -or [string]::IsNullOrEmpty($gitEmail)) {
    Write-Host "✗ Git is not configured" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please configure Git with your information:" -ForegroundColor Yellow
    Write-Host "  git config --global user.name `"Your Name`"" -ForegroundColor Cyan
    Write-Host "  git config --global user.email `"your.email@example.com`"" -ForegroundColor Cyan
    Write-Host ""
    
    $configure = Read-Host "Would you like to configure Git now? (y/n)"
    if ($configure -eq "y") {
        $name = Read-Host "Enter your name"
        $email = Read-Host "Enter your email"
        git config --global user.name "$name"
        git config --global user.email "$email"
        Write-Host "✓ Git configured successfully" -ForegroundColor Green
    } else {
        Write-Host "Skipping Git configuration. You can do it later." -ForegroundColor Yellow
    }
} else {
    Write-Host "✓ Git is configured as: $gitUser <$gitEmail>" -ForegroundColor Green
}

# Navigate to Flutter app directory
Write-Host ""
Write-Host "Setting up Flutter project..." -ForegroundColor Yellow
Set-Location -Path "questboard_app"

# Install Flutter dependencies
Write-Host ""
Write-Host "Installing Flutter dependencies..." -ForegroundColor Yellow
flutter pub get

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Run Flutter doctor
Write-Host ""
Write-Host "Running Flutter doctor..." -ForegroundColor Yellow
flutter doctor

# Generate Hive adapters
Write-Host ""
Write-Host "Generating Hive adapters..." -ForegroundColor Yellow
Write-Host "(This may take a few moments...)" -ForegroundColor Gray
flutter pub run build_runner build --delete-conflicting-outputs

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Hive adapters generated successfully" -ForegroundColor Green
} else {
    Write-Host "⚠ Hive adapter generation had issues (this is OK for now)" -ForegroundColor Yellow
}

# Go back to root directory
Set-Location -Path ".."

# Summary
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "🎉 Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. cd questboard_app" -ForegroundColor Cyan
Write-Host "2. flutter run -d chrome" -ForegroundColor Cyan
Write-Host ""
Write-Host "Or press F5 in VS Code to run the app!" -ForegroundColor Yellow
Write-Host ""
Write-Host "📚 Check docs/getting-started.md for more information" -ForegroundColor Gray
Write-Host ""
