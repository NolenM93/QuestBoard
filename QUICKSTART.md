# ⚡ Quick Start Guide

## 🎯 You're Ready to Go!

Your QuestBoard project is set up! Here's what to do next:

## Step 1: Configure Git (One-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 2: Commit Your Initial Setup

```bash
git commit -m "Initial commit: QuestBoard foundation with all core models"
```

## Step 3: Run the Setup Script

```powershell
.\setup.ps1
```

This will:
- ✅ Check Flutter installation
- ✅ Install dependencies
- ✅ Generate Hive adapters
- ✅ Run Flutter doctor

## Step 4: Launch the App

```bash
cd questboard_app
flutter run -d chrome
```

Or in VS Code: **Press F5**

## 🎮 What You Have

### ✅ Complete Foundation
- 6 core data models (User, Quest, Achievement, Team, Mascot, FeedPost)
- XP calculation system
- Color theme & constants
- Material Design 3 UI
- Cross-platform support

### 📱 Platforms Ready
- 🌐 Web
- 📱 Android
- 🍎 iOS
- 🪟 Windows
- 🍎 macOS
- 🐧 Linux

### 🛠️ Tech Stack
- Flutter 3.9.2+
- Riverpod (state management)
- Hive (local database)
- Material Design 3
- Lottie animations

## 🚀 Next Steps

### Option 1: Build Quest Screen
Create `lib/screens/quest_screen.dart` to display quests

### Option 2: Build User Profile
Create `lib/screens/profile_screen.dart` for user stats

### Option 3: Test the Models
Create sample data and test XP calculations

## 📚 Documentation

- `README.md` - Full project overview
- `docs/getting-started.md` - Detailed setup guide
- `PROJECT_STATUS.md` - What's completed and what's next

## 🆘 Troubleshooting

**Problem**: Git not configured
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

**Problem**: Dependencies missing
```bash
cd questboard_app
flutter pub get
```

**Problem**: Hive adapter errors
```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

**Problem**: Flutter issues
```bash
flutter doctor
```

## 💡 Pro Tips

1. **Hot Reload**: Save files to see changes instantly (press `r` in terminal)
2. **Hot Restart**: Press `R` (capital) for full restart
3. **VS Code**: Install "Flutter" and "Dart" extensions
4. **Theme**: App supports light/dark mode automatically

## 🎉 You're All Set!

Your gamified team tracker is ready to build. Start with a simple screen and iterate from there!

Happy coding! 🚀
