# Quick Launch Script for QuestBoard

Write-Host "🎮 Launching QuestBoard..." -ForegroundColor Cyan

# Navigate to questboard_app directory
Set-Location -Path "$PSScriptRoot\questboard_app"

# Check if we're in the right place
if (Test-Path "pubspec.yaml") {
    Write-Host "✓ Found pubspec.yaml" -ForegroundColor Green
    Write-Host ""
    Write-Host "Starting Flutter app in Chrome..." -ForegroundColor Yellow
    Write-Host ""
    
    # Run Flutter
    flutter run -d chrome
} else {
    Write-Host "✗ Error: pubspec.yaml not found!" -ForegroundColor Red
    Write-Host "Please run this script from the QuestBoard root directory" -ForegroundColor Yellow
}
