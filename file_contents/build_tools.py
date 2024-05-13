content = """
from src.services.llm.tools.create_outfit import tool
from langchain.tools import Tool

from src.services.llm.tools.base_tool import get_base_tool

tools = [get_base_tool]
"""