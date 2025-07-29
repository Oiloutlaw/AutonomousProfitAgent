# environment.py
class TradingEnvironment:
    def __init__(self, api_key, sandbox=True):
        self.api_key = api_key
        self.sandbox = sandbox
    def step(self, action):
        # integrate with trading API (sandbox or live)
        return {}, 0.0, False, {}
    def reset(self):
        return {}