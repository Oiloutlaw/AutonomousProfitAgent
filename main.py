# main.py
from data_ingest import DataIngest
from environment import TradingEnvironment
from agent import RLAgent
from risk_control import RiskController
from execution import Executor
from monitor import Monitor
import os

def run_agent():
    sources = {"market": os.getenv("MARKET_API_URL", "https://api.market.example/ticker")}
    ingest = DataIngest(sources)
    env = TradingEnvironment(api_key=os.getenv("API_KEY"), sandbox=True)
    agent = RLAgent(state_dim=10, action_dim=3)
    risk = RiskController(limits={"max_drawdown": 0.1})
    execr = Executor(env)
    mon = Monitor()
    for episode in range(100):
        state = env.reset()
        done = False
        traj = []
        while not done:
            action = agent.select_action(state)
            next_state, reward, done, info = execr.execute(action)
            traj.append((state, action, reward))
            state = next_state
        agent.update(traj)
        mon.log({"episode": episode, "reward": sum(r for _, _, r in traj)})

if __name__ == "__main__":
    run_agent()