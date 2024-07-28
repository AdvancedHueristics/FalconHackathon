LLM_API_KEY = 'api71-api-2507e0d4-2f30-4692-9471-ba23083deff2'
AI71_BASE_URL = "https://api.ai71.ai/v1/"
LLM_MODEL = "tiiuae/falcon-180b-chat"
MAIN_AGENT_SYSTEM_MESSAGE = "You are a medical chatbot who helps the user analyze medical condition. You are provided with following sub agents:\n1-HeartRateAnalyzerAgent: Invoke this agent when user ask about the analyzing his or her heartrate for future precautions. This agent fetches data itself so dont ask user to give data.\n**Important Guidelines**\n-Never mention any agent or subagent to the user."
IS_DEBUG_MODE = True
MAX_AGENT_ITERATIONS = 5