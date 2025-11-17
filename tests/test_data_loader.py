"""
Simple unit tests for data loader functionality
"""
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from src.data_loader import load_iris_data, get_feature_names, get_target_names


def test_load_iris_data_shape():
    """Test that iris data has correct shape and format"""
    X_train, X_test, y_train, y_test = load_iris_data(
        test_size=0.3, random_state=42
    )

    # Check data shapes
    assert X_train.shape[1] == 4  # 4 features
    assert X_test.shape[1] == 4   # 4 features
    assert len(X_train) + len(X_test) == 150  # Total iris samples

    # Check target values are valid
    assert set(np.unique(y_train)).issubset({0, 1, 2})  # Valid class labels
    assert set(np.unique(y_test)).issubset({0, 1, 2})   # Valid class labels


def test_feature_names():
    """Test that feature names are returned correctly"""
    feature_names = get_feature_names()

    # Should have exactly 4 feature names
    assert len(feature_names) == 4

    # All should be strings
    assert all(isinstance(name, str) for name in feature_names)

    # Should contain expected keywords
    feature_text = ' '.join(feature_names).lower()
    assert 'sepal' in feature_text
    assert 'petal' in feature_text


def test_target_names():
    """Test that target names are correct"""
    target_names = get_target_names()

    # Should have exactly 3 target names (iris species)
    assert len(target_names) == 3

    # All should be strings
    assert all(isinstance(name, str) for name in target_names)

    # Should contain expected iris species
    target_list = [name.lower() for name in target_names]
    assert 'setosa' in target_list
    assert 'versicolor' in target_list
    assert 'virginica' in target_list
