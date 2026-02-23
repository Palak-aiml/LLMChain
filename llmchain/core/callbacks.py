class CallbackManager:
    """A simple callback system for events."""
    def __init__(self):
        self._callbacks = {}

    def register(self, event, func):
        self._callbacks.setdefault(event, []).append(func)

    def trigger(self, event, *args, **kwargs):
        for func in self._callbacks.get(event, []):
            func(*args, **kwargs)
