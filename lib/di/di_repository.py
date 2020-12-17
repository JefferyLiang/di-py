from lib.di.di import DIContext
from lib.di.di_injector import DIInjector


class DIRepository:

    @property
    def app(self):
        return self._context.app

    def __init__(self, context: DIContext):
        self._context = context
        self._repos_dict = {}
        self._instance_dict = {}
        self._injector = DIInjector()
        self._injector.set_repository(self)

    def add_repository(self, cls):
        self._repos_dict[cls.__name__] = cls

    def get_repository(self, name):
        repository = self._repos_dict.get(name, None)
        if repository is None:
            raise KeyError()
        return repository

    def get_instance(self, name, cache: bool = False):
        instance = self._instance_dict.get(name, None)
        if instance is None:
            cls = self._repos_dict.get(name, None)
            if cls is None:
                raise KeyError()
            instance = self._injector.get_inject_instance(cls)
            if cache:
                self._instance_dict[name] = instance
        return instance
