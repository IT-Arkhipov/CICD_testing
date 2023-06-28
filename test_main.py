import requests

class TestMath:

    @staticmethod
    def test_check_number():
        a = 5
        assert a == 5

    @staticmethod
    def test_get_response_code():
        url = "https://jsonplaceholder.typicode.com/posts"

        response = requests.get(url)

        assert response.status_code == 200