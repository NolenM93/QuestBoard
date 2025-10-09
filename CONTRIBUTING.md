# Contributing to QuestBoard

Thank you for your interest in contributing to QuestBoard! This document provides guidelines for contributing to the project.

## 🎯 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected behavior vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, etc.)

### Suggesting Features

We welcome feature suggestions! Please create an issue with:
- Clear description of the feature
- Use case and benefits
- Potential implementation approach (if you have ideas)

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Run tests**
   ```bash
   pytest tests/ -v
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe what your changes do
   - Reference any related issues
   - Ensure all tests pass

## 📝 Code Style

- Follow PEP 8 guidelines for Python code
- Use type hints where appropriate
- Write clear, descriptive docstrings
- Keep functions focused and single-purpose
- Add comments for complex logic

## 🧪 Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Use descriptive test names

## 📚 Documentation

- Update README.md if adding features
- Add docstrings to new functions/classes
- Update API reference if needed
- Include examples in documentation

## 🎨 Areas for Contribution

### High Priority
- Web UI interface (React, Vue, or similar)
- Mobile app (React Native or Flutter)
- Database persistence layer
- Real-time collaboration features
- Third-party integrations (Slack, Discord, GitHub)

### Features
- New quest types
- Additional achievement categories
- More mascot types and skins
- Advanced analytics dashboard
- Team calendar and scheduling
- Notification system

### Improvements
- Performance optimizations
- Better AI assistant suggestions
- Enhanced XP calculation algorithms
- More comprehensive testing
- Internationalization support

### Documentation
- Video tutorials
- Interactive demos
- API client examples
- Deployment guides
- Best practices guides

## 💡 Development Setup

1. Clone the repository
   ```bash
   git clone https://github.com/NolenM93/QuestBoard.git
   cd QuestBoard
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests
   ```bash
   pytest tests/ -v
   ```

5. Run the demo
   ```bash
   python -m src.main
   ```

## 🤝 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

## 📄 License

By contributing to QuestBoard, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

Feel free to:
- Open an issue for questions
- Start a discussion on GitHub Discussions
- Reach out to maintainers

Thank you for contributing to QuestBoard! 🎮✨
