from langchain.agents import create_agent
from langchain_core.runnables import RunnablePassthrough

from agent_langc.models import create_model
from agent_langc.prompts import create_prompt_with_context, prompt
from agent_langc.rag.rag import retriever, format_docs
from agent_langc.tools import calculator, get_current_time, get_user, search_documents

tools = [
    calculator,
    get_current_time,
    get_user
]

llm = create_model()

rag_chain = (
    {
        "context":retriever | format_docs,
        "question":RunnablePassthrough()
    }
    | prompt
    | llm
)



agent = create_agent(
    model=rag_chain,
    system_prompt="You are company internal knowledge assistant."
)