import requests
import allure


class TestMath:
    @staticmethod
    def test_check_number():
        with allure.step('assert a == 5'):
            a = 5
            assert a == 5

    @staticmethod
    @allure.step('Test response code')
    def test_get_response_code():
        url = "https://jsonplaceholder.typicode.com/posts"

        response = requests.get(url)

        assert response.status_code == 200
