import requests


class AutoTranslate:
    def __init__(self):
        self.apis = [
            {"name": "Google Translate API",
             "endpoint": "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=%s&dt=t&q=%s"},
            {"name": "Microsoft Translator API",
             "endpoint": "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=auto&to=%s"
                         "&textType=html&text=%s"},
            {"name": "Yandex Translate API",
             "endpoint": "https://translate.yandex.net/api/v1.5/tr.json/translate?key=<API_KEY>&lang=%s&text=%s"}
        ]

    def translate(self, text, target_language):
        for api in self.apis:
            endpoint = api["endpoint"] % (target_language, text)
            response = requests.get(endpoint)
            if response.status_code == 200:
                if api["name"] == "Google Translate API":
                    return response.json()[0][0][0]
                elif api["name"] == "Microsoft Translator API":
                    return response.json()[0]["text"]
                elif api["name"] == "Yandex Translate API":
                    return response.json()["text"][0]
        return "Error: Could not translate text using available APIs."
