#!/usr/bin/env python3
"""
Docker training script for ML application
Runs training inside Docker container with proper setup
"""

import os
import sys

# Add current directory to Python path
sys.path.insert(0, '/app')

from src.train import main as train_main


def docker_train():
    """
    Train the model inside Docker container
    """
    print("🐳 Starting Docker-based ML training...")
    print(f"Working directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")

    # Ensure models directory exists
    os.makedirs('/app/models', exist_ok=True)

    try:
        # Run the training
        train_main()

        # Verify model was created
        model_path = '/app/models/iris_classifier.pkl'
        if os.path.exists(model_path):
            print(f"✅ Model successfully trained and saved to {model_path}")
            print(f"📊 Model file size: {os.path.getsize(model_path)} bytes")
        else:
            print("❌ Model training completed but file not found")
            return 1

    except Exception as e:
        print(f"❌ Training failed with error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit_code = docker_train()
    sys.exit(exit_code)
