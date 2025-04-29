# Function to open the image from a URL
def fetch_image():
    url = "https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/001.png"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        return Image.open(response.raw)
    else:
        raise Exception(f"Failed to retrieve image. Status code: {response.status_code}")

# Test Case 1: Test successful image fetch and open
def test_fetch_image_success():
    with patch('requests.get') as mock_get:
        # Mock the response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raw = b"fake image content"
        
        # Return the mocked response when requests.get is called
        mock_get.return_value = mock_response
        
        # Call the function and assert that an image object is returned
        im = fetch_image()
        
        # Assert that the result is an instance of PIL.Image
        assert isinstance(im, Image.Image)

# Test Case 2: Test image fetch failure (status code 404)
def test_fetch_image_failure():
    with patch('requests.get') as mock_get:
        # Mock the response object
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # Check that an exception is raised
        with pytest.raises(Exception, match="Failed to retrieve image. Status code: 404"):
            fetch_image()