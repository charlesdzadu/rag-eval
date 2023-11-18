from langchain.chains import LLMChain
from langchain.chains.base import Chain
from langchain.llms import BaseLLM
from langchain.prompts import PromptTemplate

from .prompts import QuestionGeneratorPromptTemplate


class QuestionGenerator(LLMChain):
    """Chain to generate questions based on the products available"""

    @classmethod
    def from_llm(cls, llm: BaseLLM, prompt_key: str, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        if prompt_key == "prompt_key_csv" or prompt_key == "stateful_qa_prompt_key_csv":
            prompt = PromptTemplate(
                template=QuestionGeneratorPromptTemplate.get(prompt_key),
                input_variables=["products", "number_of_questions", "schema"],
            )
        else:
            prompt = PromptTemplate(
                template=QuestionGeneratorPromptTemplate.get(prompt_key),
                input_variables=["products", "number_of_questions"],
            )
        return cls(prompt=prompt, llm=llm, verbose=verbose)


class NERGenerator(LLMChain):
    """Chain to generate questions based on the products available"""

    @classmethod
    def from_llm(cls, llm: BaseLLM, prompt_key: str, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        prompt = PromptTemplate(
            template=QuestionGeneratorPromptTemplate.get(prompt_key),
            input_variables=["sample_size", "entity_name"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
