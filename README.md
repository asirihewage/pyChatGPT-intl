# pyChatGPT-intl
![Version](https://img.shields.io/github/package-json/v/asirihewage/chatgpt-intl)
![Package Size](https://img.shields.io/github/languages/code-size/asirihewage/chatGPT-intl)
[![Upload Python Package](https://github.com/asirihewage/pyChatGPT-intl/actions/workflows/python-publish.yml/badge.svg)](https://github.com/asirihewage/pyChatGPT-intl/actions/workflows/python-publish.yml)
[![Pylint](https://github.com/asirihewage/pyChatGPT-intl/actions/workflows/pylint.yml/badge.svg)](https://github.com/asirihewage/pyChatGPT-intl/actions/workflows/pylint.yml)

### Enhanced ChatGPT Wrapper for Internationalization - Python3
This NodeJS module acts as a wrapper for ChatGPT API and will help you to use ChatGPT in your own language.
![Logo](res/logo.jpg)

## Installation

Install chatgpt-intl via pip : https://pypi.org/project/pyChatGPT-intl/

```bash
 pip install pyChatGPT-intl
```

## Usage/Examples
First, you have to obtain your API key from OPENAI, then you can use it here.
```python
from pyChatGPT-intl import PyChatGPTIntl

api_key = "sk-Z9bfKN34RT***********RtH4j0FCacAxD"
desired_lang ="si"

pyChatGPTIntl = PyChatGPTIntl(api_key, desired_lang)
print(pyChatGPTIntl.generate_text("ශ්‍රී ලංකාව ගැන මට විස්තරයක් කියන්න"))

```

## API
text - Type: string (The text to be translated)

openAiKey - Type: string (API Key obtained from OpenAI Developer Account)

opts - Type: object (OpenAI Language Model and hyperparameters)

lang - Type: string ( Must be `auto` or one of the codes (not case sensitive) contained in [SUPPORTED_LANGUAGES.md](https://github.com/asirihewage/pyChatGPT-intl/blob/main/SUPPORTED_LANGUAGES.md).)

## Features

- Use ChatGPT API in your own language
- Ability to customize the chatGPT model
- Supports more than 50 languages

## Limitations

- Does not support for syntax and codes
- Does not support larger text inputs

## Language Support
Supported language codes contained in [SUPPORTED_LANGUAGES.md](https://github.com/asirihewage/pyChatGPT-intl/blob/main/SUPPORTED_LANGUAGES.md)

## Demo
```shell
python3 chatGPT-intl.py
```
Sample App I created.
![Demo](res/demo.jpg)

## Authors

- [@asirihewage](https://github.com/asirihewage)

## Contributions

- Issues and feature updates are welcome.


## License

[MIT](https://choosealicense.com/licenses/mit/)
