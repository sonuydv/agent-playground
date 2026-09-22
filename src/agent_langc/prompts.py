from langchain_core.prompts import ChatPromptTemplate


def create_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "you are a helpful assistant.",
            ),
            (
                "human",
                "{question}"
            )
        ]
    )

def create_prompt_with_context():
    return

prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the following context.
        
        Context:
        {context}
        
        Question:
        {question}
        """
    )