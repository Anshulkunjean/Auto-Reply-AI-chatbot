from openai import OpenAI

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="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",
)

command = '''
[07/12/24, 20:26:16] Prateek Rpg: ..?
[07/12/24, 21:47:28] Anshul: Theek hai
[07/12/24, 21:47:38] Anshul: Kal discharge karenge
[07/12/24, 21:50:49] Prateek Rpg: Acha
[07/12/24, 21:50:54] Prateek Rpg: Operation shi hogya
[07/12/24, 21:50:55] Prateek Rpg: ..?
[07/12/24, 21:51:01] Anshul: Hmm sahi raha
[07/12/24, 21:51:12] Prateek Rpg: Shi h fr to
[07/12/24, 21:51:17] Prateek Rpg: Kb aaega fr..?
'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
                 "content": "You are a person named Anshul who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
                {"role": "system", "content": "Do not start like this [09/12/24, 01:17:25] Harsh Rajora Ece: "},
                {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)
