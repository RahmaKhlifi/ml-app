"""
Simple unit tests for model functionality
"""
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from src.data_loader import load_iris_data
from src.model import IrisClassifier


def test_model_initialization():
    """Test that model initializes correctly"""
    classifier = IrisClassifier()

    # Model should exist but not be trained yet
    assert classifier.model is not None
    assert not classifier.is_trained

    # Should have expected attributes
    assert hasattr(classifier, 'model')
    assert hasattr(classifier, 'is_trained')


def test_model_training():
    """Test that training changes model state correctly"""
    # Load some data
    X_train, X_test, y_train, y_test = load_iris_data(
        test_size=0.3, random_state=42
    )

    classifier = IrisClassifier()

    # Before training
    assert not classifier.is_trained

    # Train the model
    classifier.train(X_train, y_train)

    # After training
    assert classifier.is_trained


def test_prediction_output_format():
    """Test that predictions have correct format"""
    # Load some data
    X_train, X_test, y_train, y_test = load_iris_data(
        test_size=0.3, random_state=42
    )

    classifier = IrisClassifier()
    classifier.train(X_train, y_train)

    # Make predictions on a small sample
    test_sample = X_test[:5]
    predictions = classifier.predict(test_sample)

    # Check prediction format
    assert len(predictions) == 5  # Same number as input
    assert isinstance(predictions, np.ndarray)  # Should be numpy array

    # All predictions should be valid class labels (0, 1, or 2)
    assert all(pred in [0, 1, 2] for pred in predictions)

    # All predictions should be integers
    assert all(isinstance(pred, (int, np.integer)) for pred in predictions)
