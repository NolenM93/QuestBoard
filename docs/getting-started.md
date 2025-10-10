# 🚀 Getting Started with QuestBoard

Welcome to QuestBoard! This guide will help you set up the project and start your gamified team tracking adventure.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

1. **Flutter SDK** (version 3.9.2 or higher)
   - Download from: https://flutter.dev/docs/get-started/install
   - Verify installation: `flutter --version`

2. **Git**
   - Download from: https://git-scm.com/downloads
   - Verify installation: `git --version`

3. **An IDE** (choose one):
   - VS Code with Flutter extension (recommended)
   - Android Studio with Flutter plugin
   - IntelliJ IDEA with Flutter plugin

## 🔧 Initial Setup

### 1. Configure Git (First Time Only)

If you haven't configured Git yet, run these commands:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Clone or Initialize Repository

If you're starting fresh (already done):
```bash
cd c:\Users\nolen\QuestBoard
git init
```

### 3. Install Flutter Dependencies

Navigate to the Flutter app directory and install dependencies:

```bash
cd questboard_app
flutter pub get
```

This will download all required packages including:
- Riverpod (state management)
- Hive (local database)
- Lottie (animations)
- And more...

### 4. Generate Hive Adapters

Hive needs type adapters for the data models. Generate them with:

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

This creates `.g.dart` files for all your models.

### 5. Verify Flutter Setup

Check that Flutter is properly configured:

```bash
flutter doctor
```

Fix any issues reported (Android/iOS SDK, etc.).

## 🏃‍♂️ Running the App

### Web (Easiest for Development)

```bash
flutter run -d chrome
```

Or in VS Code:
1. Press `F5`
2. Select "Chrome" as the device

### Windows Desktop

```bash
flutter run -d windows
```

### Android

1. Connect an Android device or start an emulator
2. Run: `flutter run`

### iOS (Mac only)

1. Connect an iOS device or start a simulator
2. Run: `flutter run`

## 📁 Project Structure Overview

```
questboard_app/
├── lib/
│   ├── main.dart              # App entry point
│   ├── models/                # Data models
│   │   ├── user.dart         # User model with XP, level, achievements
│   │   ├── quest.dart        # Quest model with types, difficulty, status
│   │   ├── achievement.dart  # Achievement & badge system
│   │   ├── team.dart         # Team & sprint management
│   │   ├── mascot.dart       # Mascot companion system
│   │   └── feed_post.dart    # Social feed posts
│   ├── screens/               # UI screens (to be created)
│   ├── widgets/               # Reusable components (to be created)
│   ├── services/              # Business logic (to be created)
│   ├── providers/             # State management (to be created)
│   └── utils/                 # Utilities
│       ├── constants.dart    # Colors, text styles, spacing
│       └── xp_calculator.dart # XP & level calculations
├── assets/                    # Images, animations, icons
└── pubspec.yaml              # Dependencies
```

## 🎮 Core Concepts

### XP & Leveling System

- **User Levels**: Based on total XP (100 XP per level)
- **Quest XP**: Varies by difficulty
  - Easy: 15 XP
  - Medium: 35 XP
  - Hard: 75 XP
  - Epic: 150 XP
- **Bonuses**: Early completion, streaks, team work

### Quest Types

Each quest type has a unique color and focus:
- 🧠 **Brainstorm** (Orange): Creative thinking, planning
- 🔧 **Build** (Teal): Development, coding
- 📣 **Promote** (Blue): Marketing, communication
- 🔬 **Research** (Green): Analysis, documentation
- 🧪 **Test** (Yellow): QA, testing
- 👀 **Review** (Purple): Code review, feedback
- 📚 **Learn** (Pink): Learning new skills

### Achievement Tiers

- 🥉 **Bronze**: 50 XP
- 🥈 **Silver**: 100 XP
- 🥇 **Gold**: 200 XP
- 💎 **Platinum**: 400 XP
- 💠 **Diamond**: 800 XP

## 🔨 Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Edit files in `lib/`, `assets/`, etc.

### 3. Run the App

```bash
flutter run
```

### 4. Hot Reload

Press `r` in the terminal or save files to see changes instantly!

### 5. Commit Your Changes

```bash
git add .
git commit -m "Description of your changes"
```

## 🐛 Troubleshooting

### "Target of URI doesn't exist" Errors

Run `flutter pub get` to install dependencies.

### Hive Adapter Errors

Run `flutter pub run build_runner build --delete-conflicting-outputs`

### Flutter Doctor Issues

Run `flutter doctor` and follow the suggested fixes.

### Hot Reload Not Working

Try hot restart: press `R` (capital R) in the terminal.

## 📚 Next Steps

1. **Explore the Models**: Check out `lib/models/` to understand the data structure
2. **Review Constants**: See `lib/utils/constants.dart` for colors and styles
3. **Build Your First Screen**: Create a quest creation screen in `lib/screens/`
4. **Add State Management**: Use Riverpod providers in `lib/providers/`
5. **Test the App**: Run on multiple platforms

## 🤝 Getting Help

- **Documentation**: Check `docs/` folder
- **Issues**: Report bugs on GitHub
- **Discussions**: Join the project discussions

## 🎉 Ready to Build!

You're all set! Start by running:

```bash
cd questboard_app
flutter pub get
flutter run -d chrome
```

Happy questing! 🚀
