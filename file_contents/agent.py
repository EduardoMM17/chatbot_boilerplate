content = """
import os
import traceback

from langchain_community.callbacks import get_openai_callback
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory

from src.services.llm.prompt import prompt_raw
from src.services.llm.tools.build_tools import tools


async def ask_assistant(input: str) -> str | tuple:
    prompt = PromptTemplate.from_template(prompt_raw)

    prompt = prompt.partial(
        language="Spanish",
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    )

    def create_agent_executor(model_name: str, max_execution_time: float):
        llm = ChatOpenAI(
            temperature=0,
            model_name=model_name,
            openai_api_key=os.environ["OPENAI_API_KEY"],
        )

        llm_with_stop = llm.bind(stop=["\nObservation"])

        agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_log_to_str(
                    x["intermediate_steps"]
                ),
                "chat_history": lambda x: x["chat_history"],
            }
            | prompt
            | llm_with_stop
            | ReActSingleInputOutputParser()
        )

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        return AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            memory=memory,
            max_execution_time=max_execution_time,
            handle_parsing_errors=True,
        )

    attempts = [
        ("gpt-4-turbo", 60),
        ("gpt-4-turbo", 40),
        ("gpt-3.5-turbo", 50),
    ]

    for model, time in attempts:
        try:
            with get_openai_callback() as cb:
                print(f"Calling model: {model} for {time} seconds")
                agent_executor = create_agent_executor(model, time)
                clara_ai_resp = await agent_executor.ainvoke({"input": input})
                clara_ai_output = clara_ai_resp["output"]

                return clara_ai_output, input, cb
        except Exception as e:
            print(f"Exception using {model}: {e}")
            error_traceback = traceback.format_exc()
            print(error_traceback)
    return "Estamos experimentando una alta demanda en nuestro servicio, por favor contáctanos en 2 minutos"
"""