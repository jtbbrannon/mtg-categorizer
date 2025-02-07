from pydantic import BaseModel

import yaml

from llm_util import create_gpt4o
from langchain.prompts import PromptTemplate

class CardCategory(BaseModel):
    card_name: str
    card_category: str

class CardCategories(BaseModel):
    cards: list[CardCategory]


def get_card_categories(user_input):
    llm = create_gpt4o()
    # Using a ChatPromt with examples, see info here: https://python.langchain.com/docs/how_to/structured_output/#few-shot-prompting
    prompt = PromptTemplate(
        input_variables=["input"],
        template="""
        You are an expert Magic the Gathering player.

        I want to categorize cards in categories like Ramp, Draw, Board wipe, Land, ect.
            
        I want a category for the following Magic the gathering cards: 
        {input}
        """
    )
    structured_llm = llm.with_structured_output(CardCategories)
    few_shot_structured_llm = prompt | structured_llm
    template = few_shot_structured_llm.invoke({"input":user_input})
    return template


def export_data(cards):
    """
    Used to export seed data
    """
    with open("seed_data.yaml", 'w+') as file:
        yaml.dump([card.model_dump() for card in cards], stream=file, sort_keys=False)