from src.client.base_api import BaseApi
from src.utils.conftest import Configuration
from src.utils.data_generator import UserData


class UsersApi(BaseApi):
    def get_users(self):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get(f'users', headers=headers)

    def get_user_by_id(self, user_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get(f'users/{user_id}',headers=headers)

    def update_user(self, user_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        data=UserData.update_user()
        return self.put(f'users/{user_id}', body=data, headers=headers)

    def delete_user(self, user_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.delete(f'users/{user_id}', headers=headers)
