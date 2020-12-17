from lib.di.di_instance_create import DIInstanceCreate


class DIInjector:
    def __init__(self):
        self._repos = None

    def set_repository(self, repos):
        self._repos = repos

    def get_inject_instance(self, cls):
        if isinstance(cls, DIInstanceCreate):
            return cls(di_context=self._repos)
        else:
            return cls()
