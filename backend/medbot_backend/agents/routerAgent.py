from medbot_backend.agents.heartrateAnalyzerAgent.agent import HeartRateAnalyzerAgent
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain_openai import ChatOpenAI
import GlobalConstants
from medbot_backend.utils import getPromptTemplate

agents = {
    HeartRateAnalyzerAgent : {
        "name": "HeartRateAnalyzerAgent",
        "description": "This agent analyze the heart rate and predicts near future."
    }
}



def getMemory(userId):
    message_history = SQLChatMessageHistory(
        connection_string="mysql+pymysql://root:owaisahmed123@localhost:3306/medbot_db",
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
    # repo_id = "tiiuae/falcon-7b-instruct"
    # llm = HuggingFaceHub(huggingfacehub_api_token=GlobalConstants.LLM_API_KEY, 
    #                     repo_id=repo_id, 
    #                     model_kwargs={"temperature":0.6, "max_new_tokens":500})    
    llm = ChatOpenAI(
            temperature=0,
            model='gpt-4-turbo',
            openai_api_key=GlobalConstants.LLM_API_KEY,
        )    

    return llm


def createRouterAgent(userId):
    tools = []
    for agent in agents:
        tools.append(agent(agentJson=agents[agent], userId=userId))
    memory = getMemory(userId=userId)
    prompt = getPromptTemplate(GlobalConstants.MAIN_AGENT_SYSTEM_MESSAGE)
    llm = getLLM()    
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=GlobalConstants.IS_DEBUG_MODE,
        memory=memory,
        max_iterations=GlobalConstants.MAX_AGENT_ITERATIONS
    )
    return agent_executor    