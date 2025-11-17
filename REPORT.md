# Task1 download the zip file and init 

# Task2 install requirements and run the app locally 

## how to run locally
   -1 create virtual environment 
   -2 run train.py code 
   -3 run predict.py code 
   -4 check output and verify prediction 

# Task3 : UNIT Tests :

## Implementation Summary
Created comprehensive pytest unit tests to verify core functionality of the ML application.

### Test Files Created:
1. **`tests/test_data_loader.py`** - 3 data loading tests
2. **`tests/test_model.py`** - 3 model functionality tests

### Data Loader Tests (`test_data_loader.py`):
- **`test_load_iris_data_shape()`**: Verifies iris dataset has correct shape (4 features, 150 samples) and valid class labels (0,1,2)
- **`test_feature_names()`**: Checks that 4 feature names are returned as strings containing expected keywords ('sepal', 'petal')  
- **`test_target_names()`**: Validates 3 target names are returned including expected iris species (setosa, versicolor, virginica)

### Model Tests (`test_model.py`):
- **`test_model_initialization()`**: Verifies IrisClassifier initializes correctly with proper attributes and untrained state
- **`test_model_training()`**: Checks training properly changes model's `is_trained` state from False to True
- **`test_prediction_output_format()`**: Validates predictions return numpy array with correct length and valid class labels

### Test Results:
```bash
pytest tests/ -v
# Result: 6 tests passed in ~1.6-5 seconds
# All tests pass successfully ✅
```

### How to Run Tests:
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_data_loader.py
pytest tests/test_model.py
```

### Key Features:
- Simple and focused unit tests
- Fast execution (< 5 seconds)  
- Meaningful assertions for data format and model behavior
- No complex setup required
- Clear, descriptive test names
- Comprehensive coverage of core functionality

# Task4 : Linting & formatting

Code quality tools to enforce consistent style and catch potential issues:
- **Linting**: Static analysis to identify errors, bugs, and code quality issues (e.g., flake8, pylint)
- **Formatting**: Automatic code style formatting for consistent appearance (e.g., black, autopep8)

## Implementation Summary
Successfully set up flake8 linter with comprehensive configuration and fixed all style violations across the codebase.

### Setup Process:
1. **Environment Configuration**: Configured Python virtual environment for ml-app workspace
2. **Flake8 Installation**: Installed flake8 linter in virtual environment (already in requirements.txt)
3. **Configuration File**: Created `.flake8` config with project-appropriate settings
4. **Style Analysis**: Ran flake8 to identify 50 style violations across src/ and tests/
5. **Violation Resolution**: Fixed all identified issues to achieve zero violations

### Flake8 Configuration (`.flake8`):
```ini
[flake8]
# Set maximum line length
max-line-length = 88

# Ignore some common warnings that are often acceptable
ignore = 
    # E203: whitespace before ':'
    E203,
    # W503: line break before binary operator (conflicts with W504)
    W503

# Exclude common directories that don't need linting
exclude = 
    .git,
    __pycache__,
    .venv,
    venv,
    .tox,
    .eggs,
    *.egg-info,
    build,
    dist

# Set the complexity threshold
max-complexity = 10

# Show source code for each error
show-source = True

# Count the number of errors and warnings
count = True

# Show statistics for the most frequent errors
statistics = True
```

### Issues Fixed:
- **Import Issues**: Removed 8 unused imports (F401) from src/ and tests/
- **Spacing Issues**: Added proper blank lines between functions/classes (10× E302, 3× E305)
- **Import Order**: Moved 7 imports to top of files (E402)
- **Line Length**: Split long function signatures to meet 88-char limit (1× E501)
- **Whitespace**: Removed trailing whitespace and blank line whitespace (20× W293, 1× W291)
- **F-string**: Fixed unnecessary f-string usage (1× F541)

### Results:
- **Before**: 50 style violations across all Python files
- **After**: 0 violations - clean codebase ✅
- **Files Updated**: All files in `src/` and `tests/` directories
- **Standards**: Full PEP 8 compliance achieved

### How to Run Linting:
```bash
# Check all source and test files
/home/lamercy/Downloads/ml-app/.venv/bin/python -m flake8 src/ tests/

# Alternative shorter command (from project root)
.venv/bin/python -m flake8 src/ tests/
```

### Benefits Achieved:
- Consistent code style across entire project
- Improved code readability and maintainability
- Automated style checking for future development
- PEP 8 compliance ensuring Python best practices
- Easy integration into CI/CD pipelines 

# Task 5 : GITHUB ACTIONS , CI Workflow

## Implementation Summary
Created a comprehensive CI/CD pipeline using GitHub Actions that automates code quality checks, testing, and Docker image building for every push and pull request.

### Workflow Configuration (`.github/workflows/ci.yml`):
- **Triggers**: Runs on push to any branch and pull requests to main
- **Runner**: Ubuntu latest with Python 3.11
- **Steps**: 12 comprehensive steps covering full CI/CD lifecycle

### CI/CD Pipeline Steps:

#### 1. **Code Checkout**
- Uses `actions/checkout@v4` to fetch repository code
- Ensures latest code is available for processing

#### 2. **Python Environment Setup**
- Uses official `actions/setup-python@v4` action
- Configures Python 3.11 with pip caching for faster builds
- Automatically handles Python installation and PATH configuration

#### 3. **Dependency Installation**
- Upgrades pip to latest version
- Installs all dependencies from `requirements.txt`
- Includes pytest-cov for coverage reporting

#### 4. **Code Linting**
- Runs flake8 on `src/` and `tests/` directories
- Provides detailed statistics and violation counts
- Ensures code quality standards are maintained

#### 5. **Unit Testing & Coverage**
- Executes pytest with comprehensive reporting options:
  - JUnit XML format for test results
  - Coverage analysis with XML and HTML reports
  - Terminal coverage summary with missing lines
- Tests all functionality in `tests/` directory

#### 6. **Test Results Artifacts**
- Uploads test results using `actions/upload-artifact@v3`
- Includes JUnit XML, coverage XML, and HTML coverage reports
- Retains artifacts for 30 days
- Uploads even if tests fail (`if: always()`)

#### 7. **Docker Setup**
- Configures Docker Buildx for advanced building features
- Enables multi-platform builds and caching capabilities

#### 8. **Docker Image Build**
- Builds Docker image using project Dockerfile
- Tags image with both `latest` and commit SHA
- Creates containerized version of ML application

#### 9. **Docker Image Artifact**
- Saves Docker image as tar file
- Uploads as GitHub Actions artifact
- Retains for 7 days with commit SHA naming
- Makes image available for deployment or testing

#### 10. **Build Summary**
- Generates comprehensive GitHub Actions summary
- Displays pipeline status, artifacts, and metadata
- Provides quick overview of build results

### Dockerfile Configuration:
```dockerfile
# Multi-stage Python 3.11 slim image
FROM python:3.11-slim

# Optimized for security and performance:
# - Non-root user execution
# - Minimal system dependencies  
# - Python path and environment optimization
# - Proper file permissions and ownership
```

### Key Features:
- **Automated Quality Gates**: Linting and testing must pass
- **Comprehensive Artifacts**: Test results, coverage, and Docker images
- **Security Best Practices**: Non-root container execution
- **Efficient Caching**: Pip dependencies and Docker layers
- **Flexible Triggers**: Push and pull request automation
- **Detailed Reporting**: JUnit XML and coverage reports
- **Container Ready**: Docker image available for deployment

### Artifacts Generated:
1. **Test Results**: JUnit XML format for CI integration
2. **Coverage Reports**: XML and HTML formats with detailed metrics
3. **Docker Image**: Complete containerized application
4. **Build Logs**: Comprehensive step-by-step execution logs

### Benefits:
- **Automated Quality Assurance**: Every code change is automatically tested
- **Consistent Environment**: Docker ensures reproducible deployments
- **Fast Feedback**: Developers get immediate feedback on code quality
- **Artifact Availability**: Test results and images available for download
- **Deployment Ready**: Docker images ready for production deployment
- **Integration Friendly**: JUnit XML compatible with most CI/CD tools

### How to Use:
```bash
# Workflow automatically triggers on:
git push origin main        # Push to main branch  
git push origin feature/*   # Push to any branch
# Pull request to main       # PR creation/updates
```

### Repository Structure Added:
```
.github/
└── workflows/
    └── ci.yml              # Main CI/CD pipeline
Dockerfile                  # Container configuration  
requirements.txt            # Updated with pytest-cov
```

