import requests
from requests.exceptions import HTTPError, Timeout, RequestException

class GenericHttpClient:
    def __init__(self, base_url=None, timeout=10):
        """
        Initializes the HttpClient instance with optional base_url and timeout.

        :param base_url: Base URL for all requests (optional).
        :param timeout: Default timeout for all requests (in seconds).
        """
        self.base_url = base_url
        self.timeout = timeout

    def _get_full_url(self, endpoint):
        """
        Combines the base URL with the endpoint if a base_url is provided.

        :param endpoint: The API endpoint to call.
        :return: Full URL string.
        """
        if self.base_url:
            return f"{self.base_url}/{endpoint}"
        return endpoint

    def _handle_response(self, response):
        """
        Handles the response, raising exceptions for error status codes.

        :param response: The response object to check.
        :return: Parsed JSON content if the response was successful.
        :raises HTTPError: If the response contains an error status code.
        """
        try:
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
            return response.json() if response.content else {}
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"Other error occurred: {err}")
            raise

    def get(self, endpoint, params=None):
        """
        Performs a GET request.

        :param endpoint: API endpoint.
        :param params: URL parameters (optional).
        :return: JSON response.
        """
        url = self._get_full_url(endpoint)
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except (Timeout, RequestException) as e:
            print(f"Request failed: {e}")
            raise

    def post(self, endpoint, data=None, json=None):
        """
        Performs a POST request.

        :param endpoint: API endpoint.
        :param data: Form data (optional).
        :param json: JSON body (optional).
        :return: JSON response.
        """
        url = self._get_full_url(endpoint)
        try:
            response = requests.post(url, data=data, json=json, timeout=self.timeout)
            return self._handle_response(response)
        except (Timeout, RequestException) as e:
            print(f"Request failed: {e}")
            raise

    def put(self, endpoint, data=None, json=None):
        """
        Performs a PUT request.

        :param endpoint: API endpoint.
        :param data: Form data (optional).
        :param json: JSON body (optional).
        :return: JSON response.
        """
        url = self._get_full_url(endpoint)
        try:
            response = requests.put(url, data=data, json=json, timeout=self.timeout)
            return self._handle_response(response)
        except (Timeout, RequestException) as e:
            print(f"Request failed: {e}")
            raise

    def delete(self, endpoint, params=None):
        """
        Performs a DELETE request.

        :param endpoint: API endpoint.
        :param params: URL parameters (optional).
        :return: JSON response.
        """
        url = self._get_full_url(endpoint)
        try:
            response = requests.delete(url, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except (Timeout, RequestException) as e:
            print(f"Request failed: {e}")
            raise

    def patch(self, endpoint, data=None, json=None):
        """
        Performs a PATCH request.

        :param endpoint: API endpoint.
        :param data: Form data (optional).
        :param json: JSON body (optional).
        :return: JSON response.
        """
        url = self._get_full_url(endpoint)
        try:
            response = requests.patch(url, data=data, json=json, timeout=self.timeout)
            return self._handle_response(response)
        except (Timeout, RequestException) as e:
            print(f"Request failed: {e}")
            raise
