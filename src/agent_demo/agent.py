import json
from http.client import responses

from openai import OpenAI

from agent_demo.app_config import app_config
from agent_demo.tools import TOOLS, TOOL_FUNCTIONS

client = OpenAI(
    base_url=app_config.llm_base_url,
    api_key=app_config.llm_api_key
)

def run_agent(user_input:str) -> str:
    # Message history
    messages = [
        {
            "role":"user",
            "content":user_input
        }
    ]

    #Start the llm calling loop
    while True:
        # llm call
        response = client.chat.completions.create(
            model=app_config.llm_model,
            messages=messages,
            tools=TOOLS
        )

        assistant_message = response.choices[0].message
        # Add the llm response to our conversation
        messages.append(assistant_message)

        # No tool call -> we are finished
        if not assistant_message.tool_calls:
            return assistant_message.content

        # Else execute every requested tool
        # and each tool call result will be added to conversation
        # once loop finished llm we will be called again with tool results added
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            tool_function = TOOL_FUNCTIONS[tool_name]

            result = tool_function(**args)

            #Now append the tool result in message history for next llm call
            messages.append({
                "role":"tool",
                "tool_call_id":tool_call.id,
                "content":result
            })




