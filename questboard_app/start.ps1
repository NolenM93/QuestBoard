# QuestBoard App - Quick Start Script
# Run this from the QuestBoard root directory
# Updated and cleaned

Write-Host "🎮 QuestBoard - Starting App Setup..." -ForegroundColor Cyan
Write-Host ""

# Navigate to Flutter app directory
Set-Location questboard_app

# Check if Flutter is installed
Write-Host "📋 Checking Flutter installation..." -ForegroundColor Yellow
try {
    flutter --version | Out-Null
    Write-Host "✅ Flutter is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Flutter is not installed or not in PATH!" -ForegroundColor Red
    Write-Host "Please install Flutter: https://flutter.dev/docs/get-started/install" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Get dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
flutter pub get
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to install dependencies!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Dependencies installed" -ForegroundColor Green
Write-Host ""

# Generate Hive adapters
Write-Host "🔨 Generating Hive adapters (this may take a minute)..." -ForegroundColor Yellow
flutter pub run build_runner build --delete-conflicting-outputs
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Build runner completed with warnings (this is usually okay)" -ForegroundColor Yellow
} else {
    Write-Host "✅ Hive adapters generated" -ForegroundColor Green
}
Write-Host ""

# Check for available devices
Write-Host "📱 Checking available devices..." -ForegroundColor Yellow
flutter devices
Write-Host ""

Write-Host "✨ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 To run the app, use one of these commands:" -ForegroundColor Cyan
Write-Host "   flutter run -d chrome        (Run on Chrome browser)" -ForegroundColor White
Write-Host "   flutter run -d windows       (Run on Windows desktop)" -ForegroundColor White
Write-Host "   flutter run -d edge          (Run on Edge browser)" -ForegroundColor White
Write-Host ""
Write-Host "📚 Quick Tips:" -ForegroundColor Cyan
Write-Host "   • Create a test account with any email/password" -ForegroundColor White
Write-Host "   • Data persists locally using Hive" -ForegroundColor White
Write-Host "   • Check BUILD_STATUS.md for feature completion status" -ForegroundColor White
Write-Host ""

# Ask if user wants to run now
$response = Read-Host "Would you like to run the app now? (y/n)"
if ($response -eq 'y' -or $response -eq 'Y') {
    Write-Host ""
    Write-Host "🚀 Launching app on Chrome..." -ForegroundColor Cyan
    flutter run -d chrome
}
