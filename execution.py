# execution.py
class Executor:
    def __init__(self, env):
        self.env = env
    def execute(self, action):
        return self.env.step(action)