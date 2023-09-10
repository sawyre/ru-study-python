from flask import Flask, json, request, Response


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
        app.add_url_rule("/user", methods=["POST"], view_func=FlaskExercise.create_user)
        app.add_url_rule("/user/<string:name>", methods=["GET"], view_func=FlaskExercise.get_user)
        app.add_url_rule(
            "/user/<string:name>", methods=["PATCH"], view_func=FlaskExercise.update_user
        )
        app.add_url_rule(
            "/user/<string:name>", methods=["DELETE"], view_func=FlaskExercise.delete_user
        )

    @staticmethod
    def create_user() -> Response:
        json_data = request.get_json()
        FlaskExercise.users = {}
        if "name" in json_data and json_data["name"] not in FlaskExercise.users:
            new_user = json_data["name"]
            FlaskExercise.users[new_user] = {}
            return Response(
                response=json.dumps({"data": f"User {new_user} is created!"}),
                status=201,
                content_type="application/json",
            )
        else:
            return Response(
                response=json.dumps({"errors": {"name": "This field is required"}}),
                status=422,
                content_type="application/json",
            )

    @staticmethod
    def get_user(name: str) -> Response:
        if name in FlaskExercise.users:
            return Response(
                response=json.dumps({"data": f"My name is {name}"}),
                status=200,
                content_type="application/json",
            )
        else:
            return Response(
                response=json.dumps({"errors": {"name": f"User {name} not found"}}),
                status=404,
                content_type="application/json",
            )

    @staticmethod
    def update_user(name: str) -> Response:
        json_data = request.get_json()
        if name in FlaskExercise.users:
            FlaskExercise.users[json_data["name"]] = FlaskExercise.users.pop(name)
            return Response(
                response=json.dumps({"data": f"My name is {json_data['name']}"}),
                status=200,
                content_type="application/json",
            )
        else:
            return Response(
                response=json.dumps({"errors": {"name": f"User {name} not found"}}),
                status=404,
                content_type="application/json",
            )

    @staticmethod
    def delete_user(name: str) -> Response:
        if name in FlaskExercise.users:
            FlaskExercise.users.pop(name)
            return Response(status=204)
        else:
            return Response(
                response=json.dumps({"errors": {"name": f"User {name} not found"}}),
                status=404,
                content_type="application/json",
            )
