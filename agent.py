# agent.py
import torch
import torch.nn as nn
import torch.optim as optim

class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )
    def forward(self, x):
        return self.net(x)

class RLAgent:
    def __init__(self, state_dim, action_dim, lr=1e-3):
        self.policy = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
    def select_action(self, state):
        with torch.no_grad():
            probs = self.policy(torch.tensor(state, dtype=torch.float32))
        return torch.multinomial(probs, 1).item()
    def update(self, trajectories):
        # implement PPO or other logic
        pass