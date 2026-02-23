import time

class RateLimiter:
    """A simple rate limiter utility."""
    def __init__(self, calls_per_second):
        self.calls_per_second = calls_per_second
        self.last_call = 0

    def wait(self):
        now = time.time()
        elapsed = now - self.last_call
        wait_time = max(0, 1.0 / self.calls_per_second - elapsed)
        if wait_time > 0:
            time.sleep(wait_time)
        self.last_call = time.time()
