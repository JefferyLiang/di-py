import os


class DIScanner:

    @property
    def modules(self):
        return self._modules

    def __init__(self, base_path: os.path):
        self._modules = {}
        self._base_scan_path = base_path

    def scan_modules(self, path: [str]):
        scan_path = f'{self._base_scan_path}/{path}'
        print(f'[ SCANNER ] scanning {scan_path} now ...')
        file_list = list(
            filter(lambda name: name != '__init__.py' and name != '__pycache__', os.listdir(scan_path)))
        for item in file_list:
            if os.path.isdir(item):
                scanner = DIScanner(scan_path)
                scanner.scan_modules(item)
                self._modules[item] = scanner
            else:
                self._modules[item[:-3]] = f'{scan_path}/{item}'
