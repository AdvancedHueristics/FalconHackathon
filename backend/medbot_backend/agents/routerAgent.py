from medbot_backend.agents.heartrateAnalyzerAgent.agent import HeartRateAnalyzerAgent
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import GlobalConstants
from medbot_backend.utils import getPromptTemplate

agents = {
    HeartRateAnalyzerAgent : {
        "name": "Heart_Rate_Analyzer",
        "description": "This agent fetches the heart rate data, analyze it and predicts near future."
    }
}



def getMemory(userId):
    message_history = SQLChatMessageHistory(
        connection="mysql+pymysql://root:owaisahmed123@localhost:3306/medbot_db",
        session_id=userId,
        table_name="chat_history",
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        chat_memory=message_history,
        return_messages=True,
        output_key="output",
    )
    return memory


def getLLM():
    llm = ChatOpenAI(
            temperature=0,
            model=GlobalConstants.LLM_MODEL,
            openai_api_key=GlobalConstants.LLM_API_KEY,
            base_url=GlobalConstants.AI71_BASE_URL
        )    

    return llm


def createRouterAgent(userId):
    subAgents = []
    for agent in agents:
        subAgents.append(agent(agentJson=agents[agent], userId=userId))
    print(subAgents)
    memory = getMemory(userId=userId)
    prompt = getPromptTemplate(GlobalConstants.MAIN_AGENT_SYSTEM_MESSAGE)
    llm = getLLM()    
    agent = create_openai_tools_agent(llm=llm, tools=subAgents, prompt=prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=subAgents,
        verbose=GlobalConstants.IS_DEBUG_MODE,
        memory=memory,
        max_iterations=GlobalConstants.MAX_AGENT_ITERATIONS
    )
    return agent_executor    