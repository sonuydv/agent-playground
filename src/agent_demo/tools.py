from datetime import datetime




TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate.",
                    }
                },
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_user",
            "description": "Look up a user by their ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "The user's ID.",
                    }
                },
                "required": ["user_id"],
                "additionalProperties": False,
            },
        },
    },
]


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


def get_current_time() -> str:
    """
    Get the current local time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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


TOOL_FUNCTIONS = {
    "calculator": calculator,
    "get_current_time": get_current_time,
    "get_user": get_user,
}