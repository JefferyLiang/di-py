class DIContext:
    @property
    def app(self):
        return self._app

    def __init__(self, app):
        self._app = app
