import os
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import load_tools, create_tool_calling_agent, AgentExecutor

st.set_page_config(page_title="🔎 Web Surfing ChatBot")

def render_ui():
    st.title("🔎 Web Surfing ChatBot 🤖 💬")
    st.caption("🚀 A streamlit chatbot powered by 🦜🔗 LangChain, SerpAPI, and OpenAI LLM")
    link_url = "https://www.linkedin.com/in/rishabhvrm/"
    st.markdown(f'Developed with  ❤️  by <a href="{link_url}" target="_blank">Rishabh Verma</a>', unsafe_allow_html=True)
    st.markdown('---')

    default_text = """
    Sample inputs:
    - How's the weather in NYC right now?
    - Who won the IPL match yesterday?
    - What is LangChain?
    - Where was the last Grand Prix held and who was the winner?
    """
    st.markdown(f"{default_text}")


def set_api_keys():
    '''
    Allows users to input their API keys and sets them as environment variables.
    '''
    with st.sidebar:
        st.header("Do this first!")
        openai_api_key = st.text_input("Enter OpenAI API Key", type="password")
        serpapi_api_key = st.text_input("Enter SerpAPI API Key", type="password")
        
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[Get an SERP API key](https://serpapi.com/)"
        "[View the source code](https://github.com/Rishabhvrm/web-surfing-chatbot)"

        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["SERPAPI_API_KEY"] = serpapi_api_key


def get_user_input():
    return st.chat_input(placeholder="I can search 🔎 the web for you, in REAL TIME! 🕙")


def initialize_agents():
    """
    Initializes OpenAI Chat model, loads necessary tools,
    creates chat prompt template, and creates tool calling agent.
    """

    # Initialize OpenAI Chat model
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # create tool
    tools = load_tools(["serpapi"])

    # create prompt
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            ("human", "{user_input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    # create agent
    agent = create_tool_calling_agent(
            llm,
            tools, 
            prompt=chat_template)
    
    return tools, agent


def execute_input(user_input, agent_executor):
    """
    Processes user input using the provided agent executor
    and displays the output.
    """
    # run agent
    output = agent_executor.invoke({"user_input": user_input})
    st.markdown('---')
    st.write("You:", user_input)
    st.write("Bot:", output["output"])


def main():
    """
    Main function to run the Bot
    """
    render_ui()
    set_api_keys()
    user_input = get_user_input()

    if user_input:
        if not os.environ["OPENAI_API_KEY"]:
            st.info("Please add your OpenAI Api key to continue.")
            st.stop()

        if not os.environ["SERPAPI_API_KEY"]:
            st.info("Please add your SerpApi key to continue.")
            st.stop()

        tools, agent = initialize_agents()
        try:
            # create agent executor
            agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
            execute_input(user_input, agent_executor)

        except Exception as e:
            error_message = str(e)
            if hasattr(e, 'response') and hasattr(e.response, 'json'):
                error_json = e.response.json()
                if 'error' in error_json and 'message' in error_json['error']:
                    error_message = error_json['error']['message']
            st.error(f"Error creating tools or agent: {error_message}")
        
        st.stop()

if __name__ == "__main__":
    main()


