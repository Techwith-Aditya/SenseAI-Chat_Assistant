from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="Your_API_Key"
)

while True:
    user_input = input("Enter your question (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Request completion from LLaMA model
    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
    )

    # Stream and print the response
    print("AI's response:")
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print("\n")
