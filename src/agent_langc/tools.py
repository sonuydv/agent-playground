from datetime import datetime
from langchain_core.tools import tool

from agent_langc.rag.rag import retriever


@tool
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    """
    try:
        # Learning implementation only.
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"


@tool
def get_current_time() -> str:
    """
    Get the current local time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def get_user(user_id: int) -> str:
    """
    Simulate looking up a user in a database.
    """

    users = {
        1: {"name": "Alice", "role": "admin"},
        2: {"name": "Bob", "role": "developer"},
        3: {"name": "Charlie", "role": "designer"},
    }

    user = users.get(user_id)

    if not user:
        return f"User {user_id} not found."

    return str(user)


# RAQ retriever tool
@tool
def search_documents(query: str) -> str:
    """
    Search tool for company related information.
    """
    results = retriever.invoke(query)

    return "\n\n".join(
        result.page_content
        for result in results
    )
