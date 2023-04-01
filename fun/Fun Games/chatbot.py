import random

def chatbot():
   
    greetings = ['hi', 'hello', 'hey']
    farewells = ['goodbye', 'bye', 'see you later']
    thanks = ['thanks', 'thank you']
    
   
    print("Hi, I'm a chatbot! How can I help you today?")
    
  
    while True:
        
        user_input = input().lower()
        
      
        if any(word in user_input for word in greetings):
            print(random.choice(greetings))
        elif any(word in user_input for word in farewells):
            print(random.choice(farewells))
            break
        elif any(word in user_input for word in thanks):
            print("You're welcome!")
        else:
            print("I'm sorry, I didn't understand what you said.")
