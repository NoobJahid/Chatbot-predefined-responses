import re
import random

responses = {
    "hello": ["Hi there! How can I assist you today?", "Hello! Nice to see you! What can I help with?", "Hey, hi! How's it going?"],
    "hi": ["Hello! How can I help you?", "Hi! What's on your mind?", "Hey there! How can I assist you?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm doing awesome, thanks for asking! How are you?", "I'm here to help, so I'm great! How are you feeling?"],
    "what is your name": ["I'm a chatbot created to assist you. Call me Jahid!", "My name's Jahid, nice to meet you!", "I'm Jahid, your friendly assistant!"],
    "help": ["Sure, I'm here to help. What do you need assistance with?", "I’d love to help! What’s the issue?", "Need assistance? I'm here for you!"],
    "bye": ["Goodbye! Have a great day!", "See you later! Take care!", "Bye bye! Hope to chat again soon!"],
    "thank you": ["You're welcome! I'm happy to help.", "My pleasure! Anything else?", "Glad I could help! You're welcome!"],
    "sad": ["I'm sorry to hear you're feeling sad. Want to talk about it?", "That sounds tough. I'm here for you—what happened?", "I hate hearing you're sad. Can I help in any way?"],
    "happy": ["That's awesome to hear! What’s making you happy?", "Yay, I love that you're happy! What's going on?", "Happy vibes! What’s bringing you joy?"],
    "weather": ["I can’t check the weather right now, but I suggest looking up your local forecast! What's the weather like where you are?", "Weather’s always a fun topic! Is it sunny or rainy where you are?"],
    "joke": ["Why did the computer go to school? It wanted to improve its *byte*!", "What do you call a bear with no socks on? Barefoot!", "Why did the scarecrow become a motivational speaker? He was outstanding in his field!"],
    "food": ["Yum, I love talking about food! What's your favorite dish?", "Food’s the best! Are we talking pizza, sushi, or something else?", "I don’t eat, but I can chat about food! What’s cooking?"],
    "default": ["I'm not sure I understand. Could you please rephrase?", "Hmm, I didn’t catch that. Can you say it another way?", "I’m a bit confused—could you rephrase that for me?"]
}

suggestions = ["Try asking about the weather, a joke, or your favorite food!", 
               "How about we talk about something fun, like your favorite hobby?", 
               "You can ask me how I'm doing, or tell me how you're feeling!"]

def chatbot_response(user_input, last_topic):
    user_input = user_input.lower().strip()

    if not user_input:
        return "Oops, you didn't type anything. Try again!"
    if len(user_input) > 100:
        return "Whoa, that's a long message! Can you keep it shorter, please?"

    for keyword in responses:
        if re.search(r'\b' + keyword + r'\b', user_input):
            response = random.choice(responses[keyword]) if isinstance(responses[keyword], list) else responses[keyword]
            if keyword not in ["hello", "hi", "bye", "thank you", "sad", "happy", "how are you", "what is your name", "help", "default"]:
                last_topic[0] = keyword
            return response

    if last_topic[0]:
        return f"I see we were talking about {last_topic[0]}. Want to continue that topic, or try something else? " + random.choice(suggestions)

    return random.choice(responses["default"]) + " " + random.choice(suggestions)

def chatbot():
    print("Jahid: Hello! I'm Jahid, your friendly assistant. I can talk about the weather, tell a joke, or chat about food! (type 'bye' to exit)")
    last_topic = [None]
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'bye':
            print(f"Jahid: {random.choice(responses['bye'])}")
            break
        response = chatbot_response(user_input, last_topic)
        print(f"Jahid: {response}")

if __name__ == "__main__":
    chatbot()
