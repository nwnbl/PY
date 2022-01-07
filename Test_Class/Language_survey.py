from Survey import *

question= "Language?"
survey1=Survey(question)

survey1.show_question()
while True:
    response = input("Language: ")
    if response == 'q':
        break
    survey1.store_response(response)

survey1.show_results()