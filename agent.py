from memory_vector import retrieve_relevant_memory, store_memory, mark_resolved
from azure_openai_client import chat_completion


def support_agent(customer_id, user_message):
    # Detect resolution keywords
    if any(word in user_message.lower() for word in ["resolved", "thanks", "thank you"]):
        mark_resolved(customer_id)

    # Retrieve unresolved relevant memory
    relevant_memory = retrieve_relevant_memory(customer_id, user_message)

    context = ""
    if relevant_memory:
        context = "Unresolved previous issues:\n" + "\n".join(relevant_memory)

    prompt = f"""
    {context}

    Current customer message:
    {user_message}

    Respond professionally and help resolve the issue.
    """

    response = chat_completion(prompt)

    # Store current message as unresolved issue
    store_memory(customer_id, user_message, status="unresolved")

    return response
