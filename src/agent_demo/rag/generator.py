from openai import OpenAI

from agent_demo.app_config import app_config

client = OpenAI(base_url=app_config.llm_base_url,api_key=app_config.llm_api_key)



def generate_answer(
    question: str,
    retrieved_documents: list[str],
) -> str:

    context = "\n\n".join(retrieved_documents)

    prompt = f"""
Answer the user's question using the provided context.

If the answer cannot be found in the context,
say that you don't have enough information.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=app_config.llm_model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You answer questions using only the provided context."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content