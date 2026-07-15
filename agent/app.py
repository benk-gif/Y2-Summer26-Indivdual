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
            max_tokens=300,
            #how creative the model should be in its responses higher values is more creative
            system=system_message,
            messages=history
        )

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
 #  print('You: (type exit to quit)')
#IndentationError: unexpected indent


#the functioin was deleted i didnt notice that i deleted the function and it was not indented correctly so it was not running the code
