from agent import support_agent

print("Agentic Customer Support Bot (Vector Memory + Status Tracking)\n")

customer_id = input("Customer ID: ").strip()

while True:
    user_input = input("Customer: ").strip()

    # Ignore empty inputs
    if not user_input:
        continue

    # Exit condition
    if user_input.lower() == "exit":
        print("Exiting support session. Goodbye!")
        break

    reply = support_agent(customer_id, user_input)
    print("Bot:", reply)
