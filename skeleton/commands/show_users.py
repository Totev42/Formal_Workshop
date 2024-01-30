from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class ShowUsersCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        if not self._app_data.logged_in_user:
            raise ValueError("You must be logged in to execute this command!")
        if not self._app_data.logged_in_user.is_admin:
            raise ValueError("You are not an admin!")
        output = "--USERS--\n"
        counter = 1
        for user in self._app_data.users:
            output += f"{counter}. {str(user)}\n"
            counter += 1
        return output.removesuffix("\n")

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
