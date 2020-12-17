from lib.di.di_repository import DIRepository
from lib.di.di_scanner import DIScanner
from importlib import import_module
import os


class DIImporter:
    def __init__(self, repository: DIRepository):
        self._repository = repository
        self._base_path = os.path.abspath(".")

    def import_modules(self, scanner: DIScanner, auto_registry_to_repos: bool = True):
        import_dict = {}
        for key, module in scanner.modules.items():
            module_import_path = ".".join(module[len(self._base_path) + 1:-3].split('/'))
            res = import_module(module_import_path)
            registry_cls_name = ''.join([f'{word[:1].upper()}{word[1:]}' for word in key.split('_')])
            cls = getattr(res, registry_cls_name, None)
            if cls is None:
                raise KeyError()
            else:
                if auto_registry_to_repos:
                    self._repository.add_repository(cls)
                else:
                    import_dict[cls.__name__] = cls
        # return import_dict
