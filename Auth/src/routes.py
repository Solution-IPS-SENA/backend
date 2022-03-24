from src.controllers.login_controller import LoginController
from src.controllers.register_controller import RegisterController

version = "/api/v01"

auth: dict = {
    "register":f"{version}/register", "register_controller": RegisterController.as_view("register"),
    "login": f"{version}/login", "login_controller": LoginController.as_view("login"),
}
