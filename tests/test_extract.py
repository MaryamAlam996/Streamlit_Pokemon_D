from app.extract import sum


def test_if_tes_folder_works():
    # Arrange
    input = 1
    expected_output = 6
    # Action
    actual_output = sum(input)
    # Assert
    assert expected_output == actual_output
    
# Write test for a successful extract