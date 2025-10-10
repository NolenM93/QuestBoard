# 🎮 QuestBoard - Gamified Team Progress Tracker

![QuestBoard Banner](https://img.shields.io/badge/Flutter-Cross_Platform-02569B?logo=flutter)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In_Development-yellow.svg)

Transform your team's productivity into an epic adventure! QuestBoard is a cross-platform application that gamifies team tasks, goals, and milestones with quests, achievements, and evolving mascot companions.

## 🧩 Core Concept

QuestBoard turns everyday team work into an engaging game-like experience. Perfect for:
- 🎓 **Student Development Teams** managing capstone projects
- 🚀 **Remote Startups** gamifying sprint cycles
- 💻 **Hackathon Squads** tracking progress and celebrating wins
- 👥 **Clubs & Organizations** onboarding new members with interactive quests

## ✨ Key Features

### 📋 Quest System
- **Quest Creation**: Transform tasks into engaging quests with custom titles, difficulty levels, and XP rewards
- **Quest Types**: Color-coded categories (🧠 Brainstorm, 🔧 Build, 📣 Promote, 🔬 Research, 🧪 Test, 👀 Review, 📚 Learn)
- **Difficulty Tiers**: Easy, Medium, Hard, and Epic challenges with scaling XP rewards
- **Quest Steps**: Break down complex quests into manageable sub-tasks
- **Dependencies**: Link quests that depend on each other

### 🏆 Achievement System
- **Tiered Badges**: Bronze → Silver → Gold → Platinum → Diamond
- **Categories**: 
  - 🤝 Contribution (completing quests)
  - 👑 Leadership (leading teams/quests)
  - 💡 Creativity (innovative solutions)
  - 🔥 Consistency (daily/weekly streaks)
  - 🤜🤛 Collaboration (teamwork)
  - 🎯 Milestones (XP/level achievements)
  - ⭐ Special Events (seasonal achievements)

### 🦥 Mascot Companion
- **Customizable Mascots**: Choose from Sloth, Phoenix, Dragon, Unicorn, Robot, Cat, or Owl
- **Evolution System**: Mascots level up and evolve as your team completes quests
- **Moods & Emotions**: Happy, Excited, Focused, Tired, Celebrating, Thinking, Sleeping
- **Unlockable Skins**: Seasonal skins like "Cyber Sloth" and "Pixel Phoenix"
- **Accessories**: Customize with hats, glasses, and other items
- **Interactive Phrases**: Context-aware motivational messages

### 🗺️ Progress Visualization
- **Journey Map**: Visual representation of team progress across sprints/semesters
- **Sprint System**: Organize work into time-boxed sprints with goals
- **XP Tracking**: Real-time experience point calculations with bonuses
- **Level System**: Team and individual progression with level-up celebrations
- **Skill Points**: Track individual strengths (Coding, Leadership, Design, etc.)

### 📱 Team Feed
- **Social Updates**: Share wins, achievements, and milestone completions
- **Loot Drops**: Post helpful resources, tips, and team memes
- **Reactions & Comments**: Engage with team posts
- **Pinned Posts**: Highlight important announcements
- **Activity Types**: Quest completions, level-ups, achievement unlocks, and more

### 🔄 Developer-Friendly Features
- **Git Integration**: Track GitHub branches and repositories
- **Sync & Stash Protocols**: Built-in version control guidance
- **Code Review Quests**: Turn PR reviews into XP-earning activities

### 🤖 AI Assistant Mode
- **Quest Breakdown**: AI suggests how to split large tasks into manageable quests
- **Onboarding Flows**: Automated new member introduction sequences
- **Motivational Nudges**: Behavioral analysis for encouragement
- **Progress Insights**: Team performance analytics and recommendations

## 🏗️ Project Structure

```
QuestBoard/
├── questboard_app/           # Flutter cross-platform app
│   ├── lib/
│   │   ├── models/          # Data models (Quest, User, Team, Achievement, Mascot, etc.)
│   │   ├── screens/         # UI screens
│   │   ├── widgets/         # Reusable UI components
│   │   ├── services/        # Business logic and data services
│   │   ├── providers/       # State management (Riverpod)
│   │   ├── utils/           # Utilities and helpers
│   │   └── main.dart        # App entry point
│   ├── assets/              # Images, animations, mascots
│   └── pubspec.yaml         # Flutter dependencies
├── src/                     # Python backend (optional)
├── config/                  # Configuration files
├── docs/                    # Documentation
└── examples/                # Example team configurations
```

## 🚀 Getting Started

### Prerequisites
- Flutter SDK (>=3.9.2)
- Dart SDK (>=3.9.2)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NolenM93/QuestBoard.git
   cd QuestBoard
   ```

2. **Navigate to Flutter app**
   ```bash
   cd questboard_app
   ```

3. **Install dependencies**
   ```bash
   flutter pub get
   ```

4. **Generate Hive adapters** (for local storage)
   ```bash
   flutter pub run build_runner build --delete-conflicting-outputs
   ```

5. **Run the app**
   ```bash
   # For web
   flutter run -d chrome
   
   # For mobile (with device connected)
   flutter run
   
   # For desktop
   flutter run -d windows  # or macos, linux
   ```

## 📦 Dependencies

### Core
- `flutter_riverpod` - State management
- `hive` & `hive_flutter` - Local database
- `go_router` - Navigation

### UI & Animation
- `animations` - Page transitions
- `lottie` - Animation playback
- `flutter_staggered_animations` - List animations
- `flutter_svg` - SVG support
- `fl_chart` - Charts and graphs
- `percent_indicator` - Progress indicators

### Networking
- `http` - HTTP requests
- `dio` - Advanced networking

### Utilities
- `uuid` - Unique ID generation
- `intl` - Internationalization

## 🎨 Branding & Design

### Color Palette
- **Primary**: Purple (#6C5CE7)
- **Secondary**: Cyan (#00D2D3)
- **Quest Types**: Color-coded for each category
- **Badge Tiers**: Bronze, Silver, Gold, Platinum, Diamond

### Typography
- Font Family: Poppins
- Material Design 3 (Material You)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Documentation

- [Getting Started Guide](./docs/getting-started.md)
- [Quest Guide](./docs/quest-guide.md)
- [API Reference](./docs/api-reference.md)

## 🛣️ Roadmap

- [x] Core data models
- [x] Project structure setup
- [ ] Quest creation UI
- [ ] Achievement system implementation
- [ ] Mascot companion feature
- [ ] Team feed
- [ ] Progress visualization
- [ ] AI assistant integration
- [ ] Real-time collaboration
- [ ] Cloud sync
- [ ] Mobile app release
- [ ] Web app release
- [ ] Desktop app release

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by gamification in education and productivity tools
- Built with Flutter for true cross-platform development
- Community-driven development approach

## 📧 Contact

- **Project Lead**: NolenM93
- **Repository**: [github.com/NolenM93/QuestBoard](https://github.com/NolenM93/QuestBoard)
- **Issues**: [Submit an issue](https://github.com/NolenM93/QuestBoard/issues)

---

**Made with ❤️ for teams that want to level up their productivity!**

🎮 Turn your tasks into quests. 🏆 Celebrate achievements. 🦥 Grow with your mascot.
