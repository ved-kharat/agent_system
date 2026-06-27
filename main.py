import json
import time

# --- STEP 2: THE MAIN BRAIN ---
def orchestrator_brain(user_request):
    print(f"🤖 [Main Brain] Received task: '{user_request}'")
    print("🧠 [Main Brain] Decomposing task into small pieces...\n")
    
    todo_list = [
        {"step": 1, "agent": "Retriever", "task": f"Gather raw facts about: {user_request}"},
        {"step": 2, "agent": "Analyzer", "task": "Filter the raw facts and organize them into an outline"},
        {"step": 3, "agent": "Writer", "task": "Write a beautiful, simple summary from the outline"}
    ]
    return todo_list


# --- STEP 3: THE EXPERT WORKER ROBOTS ---

def retriever_agent(task_description):
    print(f"🔍 [Retriever Agent] Starting work on: '{task_description}'")
    time.sleep(1) # Pretend the robot is searching hard!
    
    # The retriever outputs raw data
    raw_facts = "Fact A: Plants need sunlight for photosynthesis. Fact B: In space, artificial LED lights are used. Fact C: Zero gravity affects how roots grow."
    print("🔍 [Retriever Agent] Finished gathering raw facts!\n")
    return raw_facts

def analyzer_agent(raw_data):
    print(f"📊 [Analyzer Agent] Structuring and filtering data...")
    time.sleep(1) # Pretend the robot is thinking!
    
    # The analyzer takes raw facts and organizes them neatly
    structured_outline = f"Outline based on data: 1. Core Process (Photosynthesis) -> 2. Space Solution (LED Lights) -> 3. Space Obstacle (Zero Gravity impact on roots)."
    print("📊 [Analyzer Agent] Finished analyzing and created outline!\n")
    return structured_outline

def writer_agent(outline):
    print(f"✍️ [Writer Agent] Crafting the final response from outline...")
    time.sleep(1) # Pretend the robot is writing beautifully!
    
    # The writer makes it look pretty for the user
    final_story = f"🚀 PLANTS IN SPACE SUMMARY 🚀\nGrowing plants in space is highly heavily dependent on technology. Since there is no natural sunlight, scientists use specialized artificial LED lights. The biggest challenge is weightlessness (zero gravity), which changes how plant roots navigate down into the soil."
    print("✍️ [Writer Agent] Finished writing!\n")
    return final_story


# --- RUNNING THE SYSTEM PIPELINE ---
if __name__ == "__main__":
    # 1. The user gives a big task
    user_job = "Create a report on how plants grow in space"
    
    # 2. Main Brain chops it up
    checklist = orchestrator_brain(user_job)
    
    # We will hold data moving from one agent to the next in this variable
    current_data = ""
    
    # 3. Handing chores to specific robots manually (No black-box frameworks!)
    for step_info in checklist:
        agent_name = step_info["agent"]
        specific_task = step_info["task"]
        
        if agent_name == "Retriever":
            # Retriever takes the task instruction and gives us raw data
            current_data = retriever_agent(specific_task)
            
        elif agent_name == "Analyzer":
            # Analyzer takes the raw data and gives us a clean outline
            current_data = analyzer_agent(current_data)
            
        elif agent_name == "Writer":
            # Writer takes the clean outline and creates the final beautiful output
            current_data = writer_agent(current_data)

    print("==================================================")
    print("🎉 ALL STEPS COMPLETE! FINAL USER OUTPUT:")
    print("==================================================")
    print(current_data)