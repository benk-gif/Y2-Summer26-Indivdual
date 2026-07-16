# Set up everything the program needs before it can begin
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
# a function to run a chat with the user
def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Alex. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity."
    # a list to keep track of the conversation history
    history = []
    #a loop so the user can chat with out stoping 
    while True:
        user_input = input('>> ')
        # if the user types exit the prograline m will stop
        if user_input.lower() == 'exit':
            break
        # add the user's input to the conversation history
        history.append({'role': 'user', 'content': user_input})
        
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,  # limit the response length
            #how creative the model should be in its responses higher values is more creative
            temperature=0.7,
            system=system_message,
            messages=history
        )
        print('History:', history)
        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
# its like how every start of the year the school do a refresh on the subjects to start working on them again 
#i think it will run but it wil not remember 
#
#ase_client.py, #line 1195, in request
    #raise self._make_status_error_from_response(response) from None
#anthropic.BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'messages: at least one message is required'}}


#i think it will ask for the input but then crash because we ruiend the set up and we cant useload_dotenv()
# api key


#i think nothing will change just he will have no creativity
# nothing changed just he was not creative 



#thon3 /home/meet/GitHub/Y2-Summer26-Indivdual/agent/app.py
# File "/home/meet/GitHub/Y2-Summer26-Indivdual/agent/app.py", line 10
 # print('You: (type exit to quit)')
#IndentationError: unexpected indent


#the functioin was deleted i didnt notice that i deleted the function and it was not indented correctly so it was not running the code

#thon3 /home/meet/GitHub/Y2-Summer26-Indivdual/agent/app.py
# File "/home/meet/GitHub/Y2-Summer26-Indivdual/agent/app.py", line 10
 # print('You: (type exit to quit)')
#IndentationError: unexpected indent


#the functioin was deleted i didnt notice that i deleted the function and it was not indented correctly so it was not running the code


#2 lab- 1. Input tokens count the data your code sends to the AI ​​API, while output tokens count the response data the AI ​​generates back.
#2. (nada told me i could move on it (it didnt change the temperature)) 
#lab2  Reflection
# its like when you sunfalwer seeds and you wight it and the more it wights the more you have to pay
#part2
#The AI will not receive the user's new message. input tokens decrease
#The AI forgets its own previous answers.
#only removes the display for the programmer and does not change the AI’s behavior, memory, or token count.
# the api didnt work i thought i didnt set it up correctly but it was set up correctly i just didnt have connection to the internet so it was not working and i thought it was my code but it was not my code it was the internet connection
