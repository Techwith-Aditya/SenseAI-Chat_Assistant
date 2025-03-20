# This one is for one-to-one single response from model:
# from openai import OpenAI

# client = OpenAI(
#     base_url="https://integrate.api.nvidia.com/v1",
#     api_key="Your_API_Key"
# )

# while True:
#     user_input = input("Enter your question (or type 'exit' to quit): ")

#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break

#     # Request completion from LLaMA model
#     completion = client.chat.completions.create(
#         model="meta/llama-3.1-8b-instruct",
#         messages=[{"role": "user", "content": user_input}],
#         temperature=0.2,
#         top_p=0.7,
#         max_tokens=1024,
#         stream=True
#     )

#     # Stream and print the response
#     print("AI's response:")
#     for chunk in completion:
#         if chunk.choices[0].delta.content is not None:
#             print(chunk.choices[0].delta.content, end="")
#     print("\n")


# For responses in batch:
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="Your_API_Key"
)

def get_batch_responses(questions):
    """ Sends multiple questions in a batch request to the API """
    try:
        completion = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=questions,
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024
        )
        return completion.choices  # Returns a list of responses

    except Exception as e:
        print(f"❌ Error while fetching response: {e}")
        return None

def main():
    """ Main function to take batch inputs and get AI responses """
    print("🤖 Enter your questions one by one. Type 'done' when finished:")

    user_inputs = []
    while True:
        question = input("> ")
        if question.lower() == "done":
            break
        user_inputs.append({"role": "user", "content": question})

    if not user_inputs:
        print("⚠️ No questions entered. Exiting...")
        return

    print("\n⏳ Fetching AI responses...")
    
    # Call API to get responses in batch
    responses = get_batch_responses(user_inputs)

    if responses:
        print("\n✅ AI's Responses:")
        for i, response in enumerate(responses):
            print(f"\n🔹 Question {i+1}: {user_inputs[i]['content']}")
            print(f"🔹 Answer: {response.message.content}")

if __name__ == "__main__":
    main()
