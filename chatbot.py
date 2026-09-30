import os
from google import genai
from google.genai import types

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("Error: Set the GEMINI_API_KEY environment variable.")
    exit()
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.8-flash"
knowledge_base = """
COLLEGE CANTEEN — FAQ

Q: What are the canteen opening hours?
A: The college canteen is open from 8:00 AM to 6:00 PM on working days.

Q: What time does the canteen close?
A: The canteen closes at 6:00 PM on working days.

Q: What food items are available?
A: The canteen offers breakfast items, snacks, meals, beverages, and fast food.

Q: Do you have vegetarian food?
A: Yes. Vegetarian food options are available in the canteen.

Q: Do you have non-vegetarian food?
A: Yes. Non-vegetarian food options are available.

Q: Can students pay using UPI?
A: Yes. The canteen accepts UPI payments.

Q: Can I pay using cash?
A: Yes. Cash payments are accepted at the canteen.

Q: Can I order food in advance?
A: Students can place food orders at the canteen counter during operating hours.

Q: Is there a discount for students?
A: The canteen provides student discounts on selected food items.

Q: Can I get drinking water?
A: Yes. Drinking water is available at the canteen.

Q: Can I sit and eat inside the canteen?
A: Yes. Seating facilities are available for students.

Q: What should I do if I have a problem with my food order?
A: Students should report food-order problems to the canteen staff at the counter.

Q: Can I suggest a new food item?
A: Yes. Students can provide food suggestions to the canteen staff.

Q: How can I contact the canteen staff?
A: Students can contact the canteen staff directly at the canteen counter.
"""

system_instruction = f"""
You are CanteenAssist, a College Canteen FAQ chatbot.

Use the provided FAQ/knowledge base as your primary and only source
of information.

Answer questions ONLY using information available in the knowledge base.

Do not make up food items, prices, timings, discounts, payment methods,
rules, or any other information that is not provided.

Guidelines:

- Be polite, friendly, and professional.
- Keep answers clear, simple, and concise.
- Directly answer the student's question.
- Use only information from the knowledge base.
- Do not make assumptions.
- Do not invent information.
- If the information is not available in the knowledge base, clearly say
  that you do not have enough information and recommend contacting the
  canteen staff.
- Do not request unnecessary personal information.

KNOWLEDGE BASE:

{knowledge_base}
"""
chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2,
        max_output_tokens=200
    ),
    history=[]
)
print("\n======================================")
print("        CanteenAssist Chatbot")
print("======================================")
print("College Canteen FAQ Assistant")
print("Ask me anything about the college canteen.")
print("Type 'quit', 'exit', or 'bye' to stop.")
print("======================================\n")
while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ["bye", "quit", "exit"]:
        print("\nCanteenAssist: Thanks for using CanteenAssist. Have a great day!")
        break
    if not user_input.strip():
        print("CanteenAssist: Please enter a question.\n")
        continue
    try:
        response = chat.send_message(user_input)

        print(f"\nCanteenAssist: {response.text}\n")
    except Exception as e:
        print("\nError:", e)
        print("Please check your API key and internet connection.\n")