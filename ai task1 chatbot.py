data={
    "hi":"Hi there! I'm a friendly chatbot here to assist you?",
    "hello":"Hello! How can I help you today?",
    "what is your name":"I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    "where are you from":"I'm from the digital world, always ready to chat!",
    "how are you":"I'm just a chatbot, but I'm here to assist you.",
    "do you have any hobbies or interests?":"I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?":"I don't eat, but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?":"I'm a chatbot, so I don't have personal preferences for colors.",
    "do you enjoy listening to music?":"I can't listen to music, but I'm here to chat about it!",
    "bye":"Bye! Take care and have a great day!",
    "how old are you?":"I don't have an age since I'm a chatbot, but I'm always up-to-date with information!",
    "what languages do you speak?":"I can understand and respond in various languages, thanks to my programming!",
    "can you help me with my homework?":"I can certainly try! Please tell me what subject your homework is about.",
    "tell me a joke":"Sure! Why don't scientists trust atoms? Because they make up everything!",
    "what is the weather like today?":"I can check the weather for you if you tell me your location.",
    "what is the meaning of life?":"That's a deep philosophical question! Many people have different perspectives on it.",
}

def get_response(user_input):
    for pattern, response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")
while True:
    user_input = input("Me: ").lower()  # Convert user input to lowercase for case insensitivity
    if user_input == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
