# main.py

from bot import ask_swadsutra

currthread_id = "user1234"
data = {
    "thread_id" : currthread_id,
    "username": "rohit_kumar",
    "email": "rohit.kumar@example.com",
    "password": "SecurePass123",  # In real applications, never store plain text passwords!
    "food_preference": "eggetarian",  # Options: veg, non-veg, vegan, eggetarian
    "taste_preference": ["spicy", "tangy", "savory"],  # Expandable list
    "user_id": "rohit.kumarSecurePass1234",
    "allergic_foods": ["peanuts", "gluten", "shellfish"],
    
}


print(" Welcome to SwadSutra Chatbot!")
print("Type your query below. Enter '-1' to exit.\n")


while True:
    user_input = input("You: ")
        
    user_input= f'''Give an Indian recepie for: {user_input}. Keep in mind the following:
    1. food preference: {data["food_preference"]}
    2. taste preference: {data["taste_preference"]}
    3. allergic foods (never to include in the recepie and if any such ingredient is mentioned, give a warning to the user): {data["allergic_foods"]}'''

    if user_input.strip() == "-1":
        print("🛑 Ending conversation. Goodbye!")
        break

    response = ask_swadsutra(user_input, data)
    print("Bot:", response)
