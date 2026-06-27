import json

# This is our Main Brain function
def orchestrator_brain(user_request):
    print(f"🤖 Main Brain received giant task: '{user_request}'")
    print("🧠 Decomposing task into small pieces...\n")
    
    # In a real app, we send this to an LLM API (like OpenAI/Gemini) 
    # and tell it to return a clean list. Here is what the list looks like:
    todo_list = [
        {
            "step": 1, 
            "agent": "Retriever", 
            "task": f"Search and gather raw data about: {user_request}"
        },
        {
            "step": 2, 
            "agent": "Analyzer", 
            "task": "Clean up the data, find patterns, and make an outline."
        },
        {
            "step": 3, 
            "agent": "Writer", 
            "task": "Take the outline and write a beautiful summary for the user."
        }
    ]
    
    return todo_list

# Let's test our Main Brain!
if __name__ == "__main__":
    test_job = "Create a report on how plants grow in space"
    checklist = orchestrator_brain(test_job)
    
    # Print the checklist nicely so we can see it
    print("📋 Here is the generated checklist:")
    print(json.dumps(checklist, indent=4))