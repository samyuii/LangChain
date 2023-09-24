from langchain.llms  import  OpenAI
myllm = OpenAI( 
    model = 'text-davinci-003' , 
    temperature=1,
    openai_api_key=mygptkey )

from langchain.agents import load_tools
# https://serpapi.com/
os.environ['SERPAPI_API_KEY'] = myserpkey
myserptool = load_tools(tool_names=["serpapi"] )


from langchain.agents import AgentType
from langchain.agents import initialize_agent
mygooglechain = initialize_agent(
    llm=myllm, 
    tools=myserptool, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
mygooglechain.run("when chandrayaan 3 launched ?")