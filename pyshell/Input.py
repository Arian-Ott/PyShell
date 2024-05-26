class Input:
    def __init__(self, name: str, dtype, abort_on_err: bool):
        self._name = name
        self._dtype = dtype
        self._abort = abort_on_err


class TextField(Input):
    def __init__(self, name, hashed: bool, abort_on_err: bool):
        super().__init__(name, str, abort_on_err)
        self._hashed = hashed
        
    def __call__(self, *args, **kwargs):
        pass