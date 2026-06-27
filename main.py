import asyncio
import sys

# --- STEP 2: THE MAIN BRAIN ---
async def orchestrator_brain(user_request):
    print(f"🤖 [Main Brain] Received task: '{user_request}'")
    print("🧠 [Main Brain] Decomposing task into small pieces...\n")
    await asyncio.sleep(0.5)
    
    todo_list = [
        {"step": 1, "agent": "Retriever", "task": f"Gather facts for: {user_request}"},
        {"step": 2, "agent": "Analyzer", "task": "Filter facts and organize into outline"},
        {"step": 3, "agent": "Writer", "task": "Write the final summary"}
    ]
    return todo_list


# --- STEP 3 & 5: EXPERT ROBOTS WITH RETRY LOGIC (SAFETY NETS) ---

# We add a special switch called 'simulated_fail' so you can show a failure in your video!
async def retriever_agent(task_description, simulated_fail=False):
    print(f"🔍 [Retriever Agent] Attempting to search data servers...")
    
    # This is our safety net loop. It gives the robot 3 chances!
    for attempt in range(1, 4):
        try:
            await asyncio.sleep(1)
            
            # If the switch is turned on, we FORCE an error to show off our safety net
            if simulated_fail:
                raise ConnectionError("Server connection timed out!")
            
            # If no error, everything goes perfectly
            raw_facts = "Fact A: Artificial LED lights replace sunlight. Fact B: Zero gravity messes with roots."
            print("🔍 [Retriever Agent] Raw facts retrieved successfully!\n")
            return raw_facts
            
        except ConnectionError as e:
            print(f"⚠️ [Retriever Agent] Attempt {attempt} failed: {e}")
            if attempt < 3:
                print("⏳ Waiting 2 seconds before trying again...")
                await asyncio.sleep(2)
            else:
                # If it fails all 3 times, this is our backup plan (Fallback logic)
                print("🚨 [Retriever Agent] All retry attempts failed! Activating backup logic...")
                return "Fallback Data: Essential plant survival data loaded from local offline memory database."

async def analyzer_agent(raw_data):
    print(f"📊 [Analyzer Agent] Structuring data into an outline...")
    await asyncio.sleep(1)
    structured_outline = "Outline: 1. Lighting Solution (LEDs) -> 2. Gravity Problem (Roots)"
    print("📊 [Analyzer Agent] Outline finalized!\n")
    return structured_outline

async def writer_agent(outline):
    print(f"✍️ [Writer Agent] Initiating live story generation streaming...")
    await asyncio.sleep(0.5)
    story_chunks = [
        "\n🚀 ", "PLANTS ", "IN ", "SPACE", " 🚀\n",
        "Growing ", "crops ", "in ", "orbit ", "is ", "tough. ",
        "Without ", "natural ", "sunlight, ", "scientists ", "rely ", "on ", "LEDs. ",
        "Furthermore, ", "zero ", "gravity ", "confuses ", "how ", "roots ", "grow!"
    ]
    for chunk in story_chunks:
        yield chunk
        await asyncio.sleep(0.1)


# --- STEP 4: THE ASYNC RUNTIME ENGINE ---
async def run_pipeline(user_job, trigger_error=False):
    checklist = await orchestrator_brain(user_job)
    current_data = ""
    
    for step_info in checklist:
        agent_name = step_info["agent"]
        specific_task = step_info["task"]
        
        if agent_name == "Retriever":
            # We pass the error trigger here to test our safety net
            current_data = await retriever_agent(specific_task, simulated_fail=trigger_error)
            
        elif agent_name == "Analyzer":
            current_data = await analyzer_agent(current_data)
            
        elif agent_name == "Writer":
            print("==================================================")
            print("🎉 LIVE STREAMING FINAL OUTPUT:")
            print("==================================================")
            async for word_piece in writer_agent(current_data):
                sys.stdout.write(word_piece)
                sys.stdout.flush()
            print("\n")

# Main execution controller
async def main():
    print("--- 🟢 RUN 1: SUCCESS CASE (Everything runs smooth) ---")
    await run_pipeline("Report on Space Farming", trigger_error=False)
    
    print("\n" + "="*50 + "\n")
    
    print("--- 🔴 RUN 2: FAILURE CASE (Testing your Safety Net for your video!) ---")
    await run_pipeline("Report on Space Farming", trigger_error=True)

if __name__ == "__main__":
    asyncio.run(main())