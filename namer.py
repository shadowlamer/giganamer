from langchain_community.chat_models import GigaChat
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain


class Namer:
    def __init__(self, gigachat_creds, gigachat_model="GigaChat"):
        self.chat = GigaChat(credentials=gigachat_creds, verify_ssl_certs=False, model=gigachat_model)
        prompt_template = """
        По описанию переменной придумай ей название на английском языке. 
        Обязательно выведи какое-нибудь название переменной.
        Если описание отсутствует или информации из описания недостаточно, придумай произвольное название на английском языке.
        Выведи только название переменной и ничего больше. Не добавляй никаких комментариев от себя.
        Название переменной обязательно отформатируй в стиле {template} 
        Описание: {description}
        """
        prompt = PromptTemplate(
            input_variables=["template", "description"],
            template=prompt_template
        )
        self.chain = LLMChain(llm=self.chat, prompt=prompt)

    def generate(self, description, template):
        return self.chain.invoke({"description": description, "template": template})['text']
