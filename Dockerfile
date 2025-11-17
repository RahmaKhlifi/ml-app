# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code and configuration
COPY src/ src/
COPY tests/ tests/
COPY .flake8 .
COPY pytest.ini .
COPY docker_run.py .
COPY docker_train.py .

# Create models directory and handle optional models
RUN mkdir -p models

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app && \
    chmod +w models
USER app

# Expose port (optional, for future web interface)  
EXPOSE 8000

# Health check to verify container is working
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import src.data_loader; print('OK')" || exit 1

# Default command - run the Docker application script
CMD ["python", "docker_run.py", "--mode", "auto"]