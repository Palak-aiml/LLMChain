import os

class EnvLoader:
    """Utility to load environment variables from a .env file."""
    def __init__(self, env_path='.env'):
        self.env_path = env_path

    def load(self):
        if not os.path.exists(self.env_path):
            return
        with open(self.env_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, _, value = line.strip().partition('=')
                    os.environ[key] = value
