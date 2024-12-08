import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="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",
)


def is_last_message_from_sender(chat_log, sender_name="Hindustan Bhai Rpg +1"):
    """
    Checks if the last message in the chat log is from the specified sender.

    Args:
        chat_log (str): The entire chat log as a string.
        sender_name (str): The name of the sender to check. Default is "Bharat Saini Bhai Rpg".

    Returns:
        bool: True if the last message is from the specified sender, False otherwise.
    """
    # Split the chat log into individual messages
    messages = chat_log.strip().split("\n")  # Assuming each message is on a new line

    # Check if there are any messages in the log
    if not messages:
        return False

    # Get the last message
    last_message = messages[-1]

    # Check if the sender's name is in the last message
    return sender_name in last_message

    # Step 1: Click on the chrome icon at coordinates (850,855)



pyautogui.click(850, 855)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (903, 163) to (1363, 747) to select the text
    pyautogui.moveTo(903, 163)
    pyautogui.dragTo(1363, 747, duration=1.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('command', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(889 , 617)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a person named Anshul who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
                {"role": "system", "content": "Do not start like this [09/12/24, 00:53:04] Hindustan Bhai Rpg +1:" },
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (950, 790)
        pyautogui.click(950, 790)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('command', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')