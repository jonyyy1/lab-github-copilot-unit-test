import pytest
from unittest.mock import patch, Mock
import requests

from weather_service import get_weather


def test_get_weather_calls_requests_get_with_correct_url():
    location = "NewYork"
    expected_url = f"https://api.weather.com/v3/weather/{location}"

    mock_response = Mock()
    mock_response.json.return_value = {"temp": 20, "condition": "Sunny"}

    with patch("weather_service.requests.get", return_value=mock_response) as mock_get:
        result = get_weather(location)

        mock_get.assert_called_once_with(expected_url)
        assert result == {"temp": 20, "condition": "Sunny"}


def test_get_weather_propagates_requests_exception():
    location = "Paris"
    expected_url = f"https://api.weather.com/v3/weather/{location}"

    with patch("weather_service.requests.get", side_effect=requests.exceptions.RequestException("fail")) as mock_get:
        with pytest.raises(requests.exceptions.RequestException):
            get_weather(location)

        mock_get.assert_called_once_with(expected_url)
