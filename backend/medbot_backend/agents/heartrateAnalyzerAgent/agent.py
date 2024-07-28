from langchain.tools import BaseTool
import medbot_backend.agents.heartrateAnalyzerAgent.service.heartRateAnalyzerAgentService as subAgentservice

class HeartRateAnalyzerAgent(BaseTool):
    name = ""
    description = ""
    userId = ""
    
    def __init__(self, agentJson, userId):
        super().__init__()
        self.name = agentJson["name"]
        self.description = agentJson["description"]
        self.userId = userId
        self.return_direct = False    
    
    def _run(self, input, run_manager) -> str:
        return "Your heart rate seems to be fine."