from openai import OpenAI
import logging
from config import get_api_key

# Initialize OpenAI client with the API key
client = OpenAI(api_key=get_api_key())


def construct_messages(request_form):
    """Construct the messages for GPT-3.5 API request."""
    system_message = "Provide a max 10 word summary for each of the following inputs in the format 'input[number]: [summary]'."
    messages = [{"role": "system", "content": system_message}]
    for key in sorted(request_form):
        input_text = request_form[key]
        messages.append(
            {"role": "user", "content": f"input{key[-1]}: {input_text}"})
    return messages


def generate_summaries(messages):
    """Generate summaries using OpenAI API."""
    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return [msg.message.content for msg in chat_response.choices if msg.message.role == "assistant"]
    except Exception as e:
        logging.error(f"Error in generating summaries: {e}")
        return None


def parse_summaries(response_text):
    """Parse GPT-3.5 response text into structured data."""
    summary_lines = response_text.split("\n")
    data = {}
    for line in summary_lines:
        parts = line.split(":")
        if len(parts) == 2:
            key = parts[0].replace(" ", "").strip()
            value = parts[1].strip()
            data[key] = value
    return data
