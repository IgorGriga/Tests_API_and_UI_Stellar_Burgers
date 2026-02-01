import allure


class Assertions:

    def __init__(self):
        self.response = None
        self.response_json = None

    @allure.step('Проверка успешной отработки запроса')
    def check_success(self, err_msg=None):
        if not self.response_json['success']:
            err_msg = self.response_json['message'] if err_msg is None else (err_msg)
        assert self.response_json['success'], err_msg
