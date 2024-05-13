#!/usr/bin/env python3
import os
import subprocess

from file_contents.agent import content as agent_content
from file_contents.assistant import content as assistant_content
from file_contents.base_tool import content as base_tool_content
from file_contents.build_tools import content as build_tool_content
from file_contents.gitignore import content as gitignore_content
from file_contents.main import content as main_content
from file_contents.prompt import content as prompt_content
from file_contents.twilio.client import content as twilio_client_content
from file_contents.twilio.twilio import content as twilio_methods_content
from file_contents.twilio.utils import content as twilio_utils_content
from file_contents.catalog import content as catalog_content

def create_project_structure(base_path):
    directories = [
        f"{base_path}/src",
        f"{base_path}/src/api",
        f"{base_path}/src/knowledge_db",
        f"{base_path}/src/services",
        f"{base_path}/src/services/llm",
        f"{base_path}/src/services/llm/tools",
        f"{base_path}/src/services/twilio"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        open(os.path.join(directory, '__init__.py'), 'a').close()


    files_with_content = {
        f"{base_path}/src/api/assistant.py": assistant_content,
        f"{base_path}/main.py": main_content,
        f"{base_path}/src/services/llm/agent.py": agent_content,
        f"{base_path}/src/knowledge_db/catalog.py": catalog_content,
        f"{base_path}/src/services/llm/prompt.py": prompt_content,
        f"{base_path}/.gitignore": gitignore_content,
        f"{base_path}/src/services/llm/tools/build_tools.py": build_tool_content,
        f"{base_path}/src/services/llm/tools/base_tool.py": base_tool_content,
        f"{base_path}/src/services/twilio/client.py": twilio_client_content,
        f"{base_path}/src/services/twilio/utils.py": twilio_utils_content,
        f"{base_path}/src/services/twilio/twilio.py": twilio_methods_content,
    }

    for file_path, content in files_with_content.items():
        with open(file_path, 'w') as f:
            f.write(content.strip())

def setup_python_environment(base_path):
    # Set the Python version using pyenv
    subprocess.run(["pyenv", "local", "3.12.1"], cwd=base_path)


def main():
    project_name = input("Enter new project name: ")
    base_path = os.path.join(os.getcwd(), project_name)
    create_project_structure(base_path)
    setup_python_environment(base_path)
    print(f"Boilerplate for {project_name} created at {base_path}!")


if __name__ == "__main__":
    main()
