from pychatgptintl.translator import AutoTranslate
from languages import is_supported

import requests
import json


class PyChatGPTIntl:
    def __init__(self, api_key, desired_lang, opts):
        self.endpoint = "https://api.openai.com/v1/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        self.translator = AutoTranslate()
        self.data = {
            "prompt": "",
            "model": opts.model.model | "text-davinci-003",
            "temperature": opts.temperature | 0.5,
            "max_tokens": opts.max_tokens | 100,
            "top_p": opts.top_p | 1,
            "frequency_penalty": opts.frequency_penalty | 0,
            "presence_penalty": opts.presence_penalty | 0
        }
        if is_supported(desired_lang):
            self.lang = desired_lang
        else:
            self.lang = "en"

    def generate_text(self, prompt):
        try:
            translated_text1 = self.translator.translate(prompt, "en")
            self.data.prompt = translated_text1
            response = requests.post(self.endpoint, headers=self.headers, data=json.dumps(self.data))
            if response.status_code == 200:
                translated_text2 = self.translator.translate(response.json()["choices"][0]["text"], self.lang)
                return {"data": translated_text2, "error": ""}
            return {"data": "", "error": response.json()}
        except Exception as er:
            return "Error: Could not generate text using OpenAI's GPT-3." + str(er)
