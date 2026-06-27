import asyncio
import sys

# --- STEP 2: THE MAIN BRAIN (ASYNC) ---
async def orchestrator_brain(user_request):
    print(f"🤖 [Main Brain] Received task: '{user_request}'")
    print("🧠 [Main Brain] Decomposing task into small pieces...\n")
    await asyncio.sleep(1) # Simulated network pause
    
    todo_list = [
        {"step": 1, "agent": "Retriever", "task": f"Gather space plant facts for: {user_request}"},
        {"step": 2, "agent": "Analyzer", "task": "Filter facts and organize them into an outline"},
        {"step": 3, "agent": "Writer", "task": "Write a beautiful summary"}
    ]
    return todo_list


# --- STEP 3 & 4: EXPERT ROBOTS WITH STREAMING PIPELINES ---

async def retriever_agent(task_description):
    print(f"🔍 [Retriever Agent] Searching data servers...")
    await asyncio.sleep(1.5) # Simulated async fetch
    raw_facts = "Fact A: Artificial LED lights replace sunlight. Fact B: Zero gravity messes with root growth."
    print("🔍 [Retriever Agent] Raw facts retrieved successfully!\n")
    return raw_facts

async def analyzer_agent(raw_data):
    print(f"📊 [Analyzer Agent] Structuring data into an outline...")
    await asyncio.sleep(1) # Simulated analysis time
    structured_outline = "Outline: 1. Lighting Solution (LEDs) -> 2. Gravity Problem (Roots)"
    print("📊 [Analyzer Agent] Outline finalized!\n")
    return structured_outline

# This agent STREAMS its output piece by piece!
async def writer_agent(outline):
    print(f"✍️ [Writer Agent] Initiating live story generation streaming...")
    await asyncio.sleep(0.5)
    
    story_chunks = [
        "\n🚀 ", "PLANTS ", "IN ", "SPACE", " 🚀\n",
        "Growing ", "crops ", "in ", "orbit ", "is ", "tough. ",
        "Without ", "natural ", "sunlight, ", "scientists ", "rely ", "on ", "LEDs. ",
        "Furthermore, ", "zero ", "gravity ", "confuses ", "how ", "roots ", "grow!"
    ]
    
    # yield lets us stream words out one-by-one
    for chunk in story_chunks:
        yield chunk
        await asyncio.sleep(0.2) # This delay simulates the AI typing live!


# --- STEP 4: THE ASYNC RUNTIME ENGINE ---
async def main():
    user_job = "Report on Space Farming"
    
    # 1. Ask the Brain for a plan
    checklist = await orchestrator_brain(user_job)
    
    current_data = ""
    
    # 2. Run through the pipeline steps
    for step_info in checklist:
        agent_name = step_info["agent"]
        specific_task = step_info["task"]
        
        if agent_name == "Retriever":
            current_data = await retriever_agent(specific_task)
            
        elif agent_name == "Analyzer":
            current_data = await analyzer_agent(current_data)
            
        elif agent_name == "Writer":
            print("==================================================")
            print("🎉 PIPELINE COMPLETE! LIVE STREAMING FINAL OUTPUT:")
            print("==================================================")
            
            # Since the writer streams, we use an async for loop to catch pieces
            async for word_piece in writer_agent(current_data):
                # Print each chunk instantly without jumping to a new line
                sys.stdout.write(word_piece)
                sys.stdout.flush()
            print("\n")

if __name__ == "__main__":
    # Start our async pipeline engine
    asyncio.run(main())