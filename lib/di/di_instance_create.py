import re


class DIInstanceCreate:
    def __init__(self, cls, inject_kwargs, cache: bool = False):
        self._cls = cls
        self._inject_kwargs = inject_kwargs
        self._cache = cache
        self.__name__ = cls.__name__

    def __call__(self, *args, **kwargs):
        inject_dict = {}
        if 'di_context' in kwargs:
            di_context = kwargs['di_context']
            for key in self._inject_kwargs:
                regex = re.compile('[A-Z][a-z]*')
                inject_name = str.lower('_'.join([match.group() for match in regex.finditer(key)]))
                svc = di_context.get_instance(key)
                if svc is None:
                    svc = getattr(di_context.app, key, None)
                    if svc is None:
                        raise KeyError()
                inject_dict.update({inject_name: svc})
            del kwargs['di_context']
        return self._cls(**inject_dict, **kwargs)
