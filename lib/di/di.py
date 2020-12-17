from lib.di.di_context import DIContext
from lib.di.di_repository import DIRepository
from lib.di.di_scanner import DIScanner
from lib.di.di_importer import DIImporter
import os


class DI:

    @property
    def context(self):
        return self._context

    @property
    def repository(self):
        return self._repos

    def __init__(self, app, scan_base_path: os.path):
        self._context = DIContext(app)
        self._repos = DIRepository(self._context)
        self._scanner = DIScanner(scan_base_path)
        self._importer = DIImporter(self._repos)

    def scan_modules(self, paths: [str]):
        for path in paths:
            self._scanner.scan_modules(path)

    def import_modules(self):
        self._importer.import_modules(self._scanner)

    def get_instance(self, name):
        return self._repos.get_instance(name)
