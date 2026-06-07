import flask

home_app = flask.Blueprint(
    name= "home_app",
    import_name= "home_app",
    template_folder= "templates",
    static_folder= "static",
    static_url_path="/home_app/static"
)

online_users = {}


"""
1. Регістрація
2. Создать группу
3. Создать связи юзера и группы
4. Создать online_users

5. Отображение данных группы
6. Отображение пользователей



{
    1: {
        "123123",
        "123123",
        "123123"
    },
    2: {}
}

"""

