import pandas as pd
import pytest

from app.data_processing import get_image_url

# Set parameters for image url test
@pytest.mark.parametrize("id, expected", [
    (1, "https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/001.png"),
    (10, "https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/010.png"),
    (100, "https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/100.png")
])

# Test image successfull image url creation
def test_get_image_url_success(id, expected):
    # Arrange
    input = id
    expected_output = expected
    # Action
    actual_output = get_image_url(input)
    # Assert
    assert actual_output == expected_output

