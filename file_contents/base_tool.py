content = """
from langchain.agents import tool
from src.knowledge_db.csc_services import csc_services_info


@tool()
def get_base_tool(txt: str) -> str:
    '''Use this tool when you understand the client wants information about the services, this includes: success cases, name, description, implementation time, client company type and if the service is on site or not.
    If the clients asks what kind of services the company provides, answer in a short and brief manner, just include information from the description nothing else.
    '''
    return csc_services_info

"""