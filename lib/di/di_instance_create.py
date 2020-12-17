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
                svc = getattr(di_context, key, None)
                if svc is None:
                    svc = getattr(di_context.app, key, None)
                inject_dict[key] = svc
        del kwargs['di_context']
        return self._cls(**inject_dict, **kwargs)
