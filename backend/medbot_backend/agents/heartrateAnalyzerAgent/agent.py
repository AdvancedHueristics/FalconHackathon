from langchain.tools import BaseTool
from medbot_backend.agents.heartrateAnalyzerAgent.service.heartRateAnalyzerAgentService import heartRateAnalyzerService as subAgentService

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
        print(run_manager.tags)
        userId = run_manager.tags[0]
        heartRateData = subAgentService.fetch_heart_rate_data(userId=userId)
        return heartRateData