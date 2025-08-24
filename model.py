
# TODO : writing code to use the target needed model type 

# TODO : use prompt template to easy access the model
from dotenv import load_dotenv
import os

class translator():
    # initing with the google api key
    def __init__(self):
        load_dotenv()
        self.api_key=os.getenv("GOOGLE_API_KEY")
        print(self.api_key)



def run(source_lang, target_lang, source_sentence):

    return "hello world"



x=translator()