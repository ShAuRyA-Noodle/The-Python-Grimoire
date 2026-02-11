from openai import OpenAI

# The API key is automatically read from the OPENAI_API_KEY
# environment variable (secure practice)
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named Jarvis skilled in general tasks."
        },
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print(response.choices[0].message.content)
