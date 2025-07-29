# risk_control.py
class RiskController:
    def __init__(self, limits):
        self.limits = limits  # e.g., max drawdown
    def check(self, portfolio):
        # enforce risk limits
        return True