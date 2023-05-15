from flask import Flask, make_response, json


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        self.users = {}
        app.add_url_rule("/user", methods=['POST'], view_func=create_user)
        app.add_url_rule("/user/<name>", methods=['GET'], view_func=get_user)
        app.add_url_rule("/user/<name>", methods=['PATCH'], view_func=update_user)
        app.add_url_rule("/user/<name>", methods=['DELETE'], view_func=delete_user)
    
    @staticmethod
    def create_user() -> dict:
        json_data = request.form
        if "name" in json_data and json_data["name"] not in self.users:
            new_user = json_data["name"]
            self.users[new_user] = {}
            response = make_response(
                json.dump(
                    {
                        "data": f"User {name} is created!"
                    },
                    201,
                    {
                        "Content-Type": "application/json"
                    }
                )
            )
        else:
            response = make_response(
                json.dump(
                    {
                        "errors": {"name": "This field is required"}
                    },
                    422,
                    {
                        "Content-Type": "application/json"
                    }
                )
            )
        
        return response

    @staticmethod
    def get_user(name) -> dict:
        if name in self.users:
            response = make_response(
                json.dump(
                    {
                        "data": f"My name is {name}"
                    },
                    201,
                    {
                        "Content-Type": "application/json"
                    }
                )
            )


    @staticmethod
    def update_user(name) -> dict:
        pass

    @staticmethod
    def delete_user(name) -> dict:
        pass
