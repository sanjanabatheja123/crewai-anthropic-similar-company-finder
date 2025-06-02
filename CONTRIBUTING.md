# Contributing to CrewAI Anthropic Similar Company Finder

Thank you for your interest in contributing to this project! This guide will help you get started.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/crewai-anthropic-similar-company-finder.git
   cd crewai-anthropic-similar-company-finder
   ```

3. **Set up the development environment:**
   ```bash
   # Install uv if you haven't already
   pip install uv
   
   # Install dependencies
   uv sync
   
   # Copy environment template
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run tests to ensure everything works:**
   ```bash
   python test_anthropic.py
   ```

## 🛠️ Development Workflow

### Making Changes

1. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the project structure:
   - Agent configurations: `src/similar_company_finder_template/config/agents.yaml`
   - Task definitions: `src/similar_company_finder_template/config/tasks.yaml`
   - Core logic: `src/similar_company_finder_template/crew.py`
   - Tools: `src/similar_company_finder_template/tools/`

3. **Test your changes:**
   ```bash
   # Run the test suite
   python test_anthropic.py
   
   # Test the full crew execution
   uv run similar_company_finder_template
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

### Commit Message Convention

We follow conventional commits:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### Pull Request Process

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub with:
   - Clear description of changes
   - Reference to any related issues
   - Screenshots/examples if applicable

3. **Ensure CI passes** - GitHub Actions will run tests automatically

## 🧪 Testing

### Running Tests Locally

```bash
# Basic integration test
python test_anthropic.py

# Test Docker build
docker build -t crewai-test .

# Test full deployment
./start_production.sh
```

### Adding New Tests

When adding new features, please include appropriate tests:

1. **Unit tests** for individual components
2. **Integration tests** for crew workflows
3. **Documentation** updates

## 📝 Code Style

### Python Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings for functions and classes
- Keep functions focused and small

### YAML Configuration

- Use consistent indentation (2 spaces)
- Add comments for complex configurations
- Validate YAML syntax

### Documentation

- Update README.md for user-facing changes
- Update DEPLOYMENT.md for deployment-related changes
- Add inline comments for complex logic

## 🔧 Project Structure

```
├── src/similar_company_finder_template/
│   ├── config/           # Agent and task configurations
│   ├── tools/           # Custom tools
│   ├── crew.py          # Main crew logic
│   └── main.py          # Entry point
├── .github/workflows/   # CI/CD configurations
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Multi-container setup
├── DEPLOYMENT.md        # Production deployment guide
└── test_anthropic.py    # Integration tests
```

## 🐛 Reporting Issues

When reporting issues, please include:

1. **Environment details** (Python version, OS, etc.)
2. **Steps to reproduce** the issue
3. **Expected vs actual behavior**
4. **Error messages** or logs
5. **Configuration details** (anonymized)

## 💡 Feature Requests

For new features:

1. **Check existing issues** to avoid duplicates
2. **Describe the use case** and problem it solves
3. **Provide examples** of how it would work
4. **Consider implementation complexity**

## 🔐 Security

- **Never commit API keys** or sensitive data
- Use environment variables for configuration
- Report security issues privately via email

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [Anthropic API Documentation](https://docs.anthropic.com)
- [LangChain Documentation](https://python.langchain.com)

## 🤝 Community

- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and best practices
- Follow the code of conduct

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing! 🎉
