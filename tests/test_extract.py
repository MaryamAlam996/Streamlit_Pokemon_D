import pandas as pd
import pytest

from app.extract import sum
from app.extract import extract_from_csv


# Test pytest
def test_if_test_folder_works():
    # Arrange
    input = 1
    expected_output = 6
    # Action
    actual_output = sum(input)
    # Assert
    assert expected_output == actual_output


# Write test for a successful extract
def test_extract_function_success():
    # Arrange
    input = 'data/pokemon.csv'
    expected_output = pd.read_csv('data/pokemon.csv')
    # Action
    actual_output = extract_from_csv(input)
    # Assert
    pd.testing.assert_frame_equal(actual_output, expected_output)


# Write a test for an exception
def test_extract_function_fail():
    # Arrange
    input = 'dataa/pokemon.csv'
    expected_error = 'An unexpected error occurred.'
    # Action
    # Assert
    with pytest.raises(Exception) as message:
        extract_from_csv(input)
    assert expected_error in str(message.value)
