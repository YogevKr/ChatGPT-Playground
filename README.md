# ChatGPT-Playground using Streamlit

ChatGPT Playground is a simple Streamlit app that provides a user-friendly interface for interacting with OpenAI's GPT models. Users can have a conversation with the model, similar to the OpenAI Playground.

## Getting Started

These instructions will help you set up and run the ChatGPT Playground on your local machine.

### Prerequisites

To run the ChatGPT Playground, you need Python 3.6 or later. Additionally, you need to install the following packages:

- streamlit
- openai

You can install them using the following command:


```bash
pip install streamlit openai

```

### OpenAI API Key

To use the ChatGPT Playground, you need to have an [OpenAI API key](https://platform.openai.com/account/api-keys). 

### Setting up the project

1. Clone this repository to your local machine:

```bash
git clone https://github.com/YogevKr/ChatGPT-Playground.git
```

2. Navigate to the project directory:

```bash 
cd ChatGPT-Playground
```

3. Open `app.py` in your favorite code editor and replace `your_openai_api_key_here` with your OpenAI API key:

```python
openai.api_key = "your_openai_api_key_here"
```

## Running the ChatGPT Playground

To run the ChatGPT Playground, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start the Streamlit app and open it in your default web browser. If it doesn't open automatically, you can access it at [http://localhost:8501](http://localhost:8501).

## Using the ChatGPT Playground

To use the ChatGPT Playground:

1. Type your message in the "Your Message" input field.
2. Click the "Submit" button to send your message and generate a response from the ChatGPT model.
3. The conversation history will be displayed above the input field, including your messages and the model's responses.
4. To clear the conversation history, click the "Clear History" button.

## License
This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/chat/LICENSE) file for details.

## Acknowledgments

- OpenAI for creating the GPT models and providing the API.
- Streamlit for making it easy to create interactive web apps with Python.




