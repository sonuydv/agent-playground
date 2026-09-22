import pprint

from langchain_core.callbacks import BaseCallbackHandler, AsyncCallbackHandler
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from agent_demo.app_config import app_config



class Answer(BaseModel):
    answer:str = Field(
        description="The answer to user's question."
    )
    confidence:float = Field(
        description="Confidence between 0 and 1"
    )


class RawResponseLoggerHandler(BaseCallbackHandler):
    def on_llm_end(self, response, **kwargs):
        print("\n=== [RAW LLM API METADATA] ===")
        # response is an LLMResult object
        for generations in response.generations:
            for generation in generations:
                # generation_info contains the raw dictionary from the API
                pprint.pprint(generation)
        print("===============================\n")


def create_model() -> ChatOpenAI:
    return ChatOpenAI(
        base_url=app_config.llm_base_url,
        api_key=app_config.llm_api_key,
        model=app_config.llm_model
        #callbacks=[RawResponseLoggerHandler()]
    )