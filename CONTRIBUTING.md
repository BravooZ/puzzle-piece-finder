# Contributing to Puzzle Piece Finder

Thank you for your interest in contributing to the project! This guide will help you get started.

## 🚀 How to Contribute

### Report Bugs

1. **Check** if the bug has already been reported in [Issues](https://github.com/BravooZ/puzzle-piece-finder/issues)
2. **Create a new issue** with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Screenshots (if applicable)
   - Python version and operating system

### Suggest Improvements

1. **Open an issue** with `enhancement` tag
2. **Describe** the proposed functionality
3. **Explain** why it would be useful
4. **Consider** alternative implementations

### Contribute Code

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/my-new-feature
   ```
4. **Make your changes** following project standards
5. **Test** your changes
6. **Commit** with descriptive messages:
   ```bash
   git commit -m "feat: add automatic edge detection"
   ```
7. **Push** to your branch:
   ```bash
   git push origin feature/my-new-feature
   ```
8. **Open a Pull Request**

## 📝 Code Standards

### Style Guide
- **PEP 8** for Python style
- **Type hints** for public functions
- **Docstrings** for modules, classes, and functions
- **Comments** in English

### Function Example
```python
def calculate_similarity(image1: Image.Image, image2: Image.Image) -> float:
    """Calculate similarity between two images.
    
    Args:
        image1: First image for comparison
        image2: Second image for comparison
        
    Returns:
        float: Similarity value between 0.0 and 1.0
        
    Raises:
        ValueError: If images have incompatible sizes
    """
    # Implementation here
    pass
```

### Commit Structure
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation changes
- `style:` formatting, no code changes
- `refactor:` refactoring without changing functionality
- `test:` add or change tests
- `perf:` performance improvement

## 🧪 Testing

### Run Tests Locally
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# With coverage
python -m pytest --cov=src tests/
```

### Testing the GUI
- Test all main functionalities
- Check behavior with different image sizes
- Confirm cancellation works correctly
- Test with and without GPU enabled

## 📚 Areas That Need Help

### High Priority
- [ ] **Unit tests** for matching modules
- [ ] **Documentation** for internal APIs
- [ ] **Optimization** of template matching algorithms
- [ ] **More robust error handling**

### Desired Features
- [ ] **Automatic segmentation** of pieces
- [ ] **Machine learning** for classification
- [ ] **REST API** for integration
- [ ] **Geometric shape analysis**

### UX Improvements
- [ ] **Drag & drop** images in GUI
- [ ] **Real-time preview** of results
- [ ] **Persistent settings**
- [ ] **Internationalization** (i18n)

## 💡 Tips for Contributors

### Environment Setup
```bash
# Clone repository
git clone https://github.com/BravooZ/puzzle-piece-finder.git
cd puzzle-piece-finder

# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt
```

### Debug and Performance
- Use **cProfile** to identify bottlenecks
- **Detailed logging** for debugging
- **GPU profiling** with nvidia-smi
- **Memory profiling** with memory_profiler

### Documentation
- Keep README updated
- **Detailed docstrings**
- **Practical usage examples**
- **Diagrams** for complex algorithms

## 🤝 Code of Conduct

- **Be respectful** and inclusive
- **Collaborate** constructively
- **Keep** discussions focused on the project
- **Help** other contributors

## 🆘 Need Help?

- **Issues**: For bugs and suggestions
- **Discussions**: For general questions
- **Email**: [keep private for now]
- **Discord/Slack**: [links when available]

## 🎯 Contribution Roadmap

### Q1 2025
- [ ] Robust testing system
- [ ] Complete API documentation
- [ ] Performance optimizations

### Q2 2025
- [ ] Basic machine learning
- [ ] REST API
- [ ] Docker deployment

### Q3+ 2025
- [ ] Mobile app
- [ ] Web interface
- [ ] Cloud processing

Thank you for helping to make this project even better! 🧩✨
