from src.controllers.login_controller import LoginController
from src.controllers.register_controller import RegisterController

auth: dict = {
    "register":"/api/v01/register", "register_controller": RegisterController.as_view("register"),
    "login": "/api/v01/login", "login_controller": LoginController.as_view("login"),
}
