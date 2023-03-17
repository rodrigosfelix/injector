from injector import Module, provider, Injector


class UserRepository:
    def get_user(self, user_id):
        return {'id': user_id, 'name': 'Alice'}


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)


class MyModule(Module):
    @provider
    def provide_user_repository(self) -> UserRepository:
        return UserRepository()

    @provider
    def provide_user_service(self, user_repository: UserRepository) -> UserService:
        return UserService(user_repository)


if __name__ == "__main__":
    injector = Injector(MyModule())
    user_service = injector.get(UserService)

    user = user_service.get_user(1)
    print(user)
