
# TODO : writing code to use the target needed model type 

# TODO : use prompt template to easy access the model
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

class translator():
    # initing with the google api key
    def __init__(self):
        load_dotenv()   # load the .env file in the project 
        self.api_key=os.getenv("GOOGLE_API_KEY")
        self.llm=None


    def init_llm(self):
        llm=init_chat_model(model="gemini-2.5-flash",model_provider="google_genai")
        self.llm=llm

    def run(self,source_lang, target_lang, source_sentence):
        self.init_llm()
        system_prompt="You are a helpful translator that translates from {lang1} to {lang2}"
        user_prompt="translate this :{sentence}"

        final_prompt_template=ChatPromptTemplate.from_messages([("system",system_prompt),("user",user_prompt)])

        final_prompt=final_prompt_template.invoke({"lang1":f"{source_lang}","lang2":f"{target_lang}","sentence":f"{source_sentence}"})
        print(final_prompt)
        response=self.llm.invoke(final_prompt)
        return response.content

        

        



