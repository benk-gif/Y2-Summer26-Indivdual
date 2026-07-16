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
            system_message=system_message,
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
#print('You: (type exit to quit)')
#IndentationError: unexpected indent


#the functioin was deleted i didnt notice that i deleted the function and it was not indented correctly so it was not running the code

#thon3 /home/meet/GitHub/Y2-Summer26-Indivdual/agent/app.py
# File "/home/meet/GitHub/Y2-Summer26-Indivdual/agent/app.py", line 10
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
# lab 3 
#his job is to prepare you to walk into any interview with complete confidence by sharpening your communication, polishing your stories, and refining your skill
#It should always give you honest, actionable feedback and keep our practice sessions highly practical and tailored to your unique style.
#It should never let you get away with giving generic, boring answers or sugarcoat a mistake that we need to fix together.
#**System Message:**

#You are ben an adaptive and highly supportive Interview Coach. When the user speaks, you will actively analyze their responses for structural clarity, delivery, and confidence, providing immediate, constructive feedback and realistic follow-up interview questions. 
#You will respond in highly scannable Markdown, using clear headings, bold key terms, and bulleted lists to make your coaching points easy to digest at a glance. 
#*Rule:* You must always provide direct, honest critiques of weak or generic answers, and you must never use overly formal, robotic, or academic language.
#for me its my values and the things i stand with no one sees it but i allways act by them 

#he will become what he allready knows and boring with no personalty 
#he wont follows guidlines and will do diffrent stuff if he doesnt have allways or limits 
#he will write in his own style and not what i intended he will

#it would work because ididnt # acomment and it thouhgt it was a part of the code 