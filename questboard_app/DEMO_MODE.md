# 🎮 Demo Mode - Quick Start Guide

## What's the Demo Button?

A **"Try Demo Mode"** button has been added to the login screen that lets you instantly explore the QuestBoard app without creating an account!

---

## 🚀 How to Use Demo Mode

### Step 1: Run the App
```powershell
cd questboard_app
flutter run -d chrome
```
(Or use Windows with `-d windows`)

### Step 2: Click "Try Demo Mode"
On the login screen, you'll see a **white outlined button** that says:

```
▶ Try Demo Mode
```

Click it! That's it! 🎉

---

## 🎭 What Happens

When you click the demo button:

1. **Auto-Creates Demo User** (if it doesn't exist)
   - Username: `DemoHero`
   - Email: `demo@questboard.com`
   - Password: `demo123`
   - Level: 1
   - XP: 0

2. **Logs You In Automatically** - No forms to fill!

3. **Takes You to Dashboard** - You'll see:
   - Your XP progress bar (Level 1, 0 XP)
   - Quick stats cards
   - Navigation tabs at the bottom
   - Empty quest/achievement sections (ready for content!)

4. **Shows Success Message** - Green snackbar: "🎮 Logged in as Demo User!"

---

## 🔄 Persistent Demo User

The demo user is saved to your local Hive database, so:

- ✅ **Stays logged in** across app restarts (until you logout)
- ✅ **Remembers progress** - Any XP/quests you add will persist
- ✅ **Can be used multiple times** - Just click the button again!

---

## 🎯 Perfect For

- **Quick Testing** - Check out features without signup
- **Development** - Fast way to test new features
- **Demonstrations** - Show the app to others instantly
- **Debugging** - Consistent test user for bug fixing

---

## 📱 What You Can Do in Demo Mode

Currently you can:

✅ **Navigate** - Switch between Home, Quests, Achievements, Team, Profile tabs  
✅ **View Dashboard** - See XP progress, stats cards, empty states  
✅ **Explore UI** - Check out the beautiful Material Design 3 interface  

Coming soon (when features are built):
⏳ Create quests  
⏳ Earn achievements  
⏳ Gain XP and level up  
⏳ Customize mascot  
⏳ Join teams  

---

## 🔐 Want a Real Account?

You can always:

1. **Sign Up** - Click "Join the Quest" → Create your own hero
2. **Regular Login** - Use the email/password form above the demo button

Demo mode doesn't prevent you from creating a real account!

---

## 🛠 Developer Notes

### How It Works

The demo button calls `_handleDemoLogin()` which:

```dart
1. Tries to login as demo@questboard.com
2. If user doesn't exist, creates it via signup
3. Auto-logs in and navigates to dashboard
```

### Code Location
- **File:** `lib/screens/login_screen.dart`
- **Method:** `_handleDemoLogin()`
- **Button:** `_buildDemoButton()`

### Customization

Want to change the demo user? Edit the credentials in `_handleDemoLogin()`:

```dart
await ref.read(currentUserProvider.notifier).signup(
  'YourHeroName',      // Username
  'your@email.com',    // Email
  'yourpassword',      // Password
);
```

---

## 🎨 Visual Location

```
┌─────────────────────────────────────┐
│         🏆 QuestBoard               │
│   Gamify Your Team Progress!        │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  Email Field                │   │
│  │  Password Field             │   │
│  │  [Start Your Quest]         │   │  ← Login Button
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ ▶ Try Demo Mode             │   │  ← NEW DEMO BUTTON!
│  └─────────────────────────────┘   │
│                                     │
│         ── OR ──                    │
│                                     │
│   [G]  [🍎]  [</>]                 │  ← Social Login
│                                     │
│  Don't have an account?             │
│  [Join the Quest]                   │
└─────────────────────────────────────┘
```

---

## ✨ Benefits

- 🚀 **Instant Access** - No registration needed
- 🎯 **Test Features** - Try everything immediately
- 👥 **Demo to Others** - Quick way to show the app
- 🔧 **Development Speed** - Skip login during testing
- 💾 **Persistent** - Demo user persists across sessions

---

**That's it! Just click "Try Demo Mode" and start exploring QuestBoard!** 🎮✨

---

*Note: This is a local demo. In production, you'd want to add rate limiting and possibly use a more sophisticated demo system.*
