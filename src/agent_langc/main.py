import langchain
from langchain_core.messages import SystemMessage, HumanMessage

from agent_langc.agents import agent, rag_chain
from agent_langc.models import create_model
from agent_langc.tools import calculator, get_current_time, get_user

langchain.debug = True


def main():
    llm = create_model()

    # Adding structure to output
    #struct_llm = llm.with_structured_output(Answer)

    llm_with_tools = llm.bind_tools([calculator,get_current_time,get_user])

    # messages = [
    #     SystemMessage(content="You are a helpful assistant."),
    #     HumanMessage(content="what is 25 * 4 ?")
    # ]
    # print(response.content)


    # prompt = create_prompt()

    # messages = prompt.invoke({
    #     "question":"what is 30 * 4?"
    # })

    # response = llm.invoke(messages)

    # chain = prompt | llm

    response = rag_chain.invoke("what is the company name?")
    print(response.content)
    return

    result = agent.invoke({
        "messages":[
            HumanMessage("what is the company name and get me user 1 ?")
        ]
    })


    for i, message in enumerate(result["messages"]):
        print(f"\n--- MESSAGE {i} ---")
        print("TYPE:", type(message).__name__)
        print("CONTENT:", message.content)

        if hasattr(message, "tool_calls"):
            print("TOOL CALLS:", message.tool_calls)



if __name__ == "__main__":
    main()
