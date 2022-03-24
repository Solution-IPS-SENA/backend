from src.controllers.login_controller import LoginController

version = "/api/v01"

auth: dict = {
    "login": f"{version}/login", "login_controller": LoginController.as_view("login"),
}
