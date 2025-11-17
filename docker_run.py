#!/usr/bin/env python3
"""
Docker run script for ML application
Handles both training and prediction in containerized environment
"""

import os
import sys
import argparse

# Add current directory to Python path
sys.path.insert(0, '/app')

from src.train import main as train_main
from src.predict import main as predict_main


def check_model_exists():
    """Check if trained model exists"""
    model_path = '/app/models/iris_classifier.pkl'
    return os.path.exists(model_path)


def run_training():
    """Run model training"""
    print("🏋️ Starting model training...")
    try:
        train_main()
        if check_model_exists():
            print("✅ Training completed successfully")
            return True
        else:
            print("❌ Training failed - model not created")
            return False
    except Exception as e:
        print(f"❌ Training error: {str(e)}")
        return False


def run_prediction():
    """Run model prediction"""
    print("🔮 Starting model prediction...")
    try:
        predict_main()
        print("✅ Prediction completed successfully")
        return True
    except Exception as e:
        print(f"❌ Prediction error: {str(e)}")
        return False


def main():
    """Main entry point for Docker container"""
    parser = argparse.ArgumentParser(description='ML App Docker Runner')
    parser.add_argument('--mode', choices=['train', 'predict', 'auto'],
                        default='auto', help='Operation mode')

    args = parser.parse_args()

    print("🐳 ML App Docker Container Started")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🐍 Python version: {sys.version}")
    print(f"⚙️ Mode: {args.mode}")

    # Ensure models directory exists
    os.makedirs('/app/models', exist_ok=True)

    success = True

    if args.mode == 'train':
        success = run_training()
    elif args.mode == 'predict':
        if check_model_exists():
            success = run_prediction()
        else:
            print("❌ No trained model found. Please run training first.")
            success = False
    else:  # auto mode
        if not check_model_exists():
            print("🤖 No model found, running training first...")
            success = run_training()

        if success:
            print("🤖 Running prediction...")
            success = run_prediction()

    if success:
        print("🎉 Docker container execution completed successfully!")
        return 0
    else:
        print("💥 Docker container execution failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
