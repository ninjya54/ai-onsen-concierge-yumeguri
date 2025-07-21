import os
import asyncio
from iointel import Agent, Workflow

async def demonstrate_workflow_integration():
    print("🚀 Starting Workflow Integration Demo...")
    print("🔄 Demonstrating Multi-Agent Collaboration...")
    print("=" * 50)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    base_url = "https://api.intelligence.io.solutions/api/v1"
    
    try:
        print("🌸 Creating Cultural Collaboration Team...")
        
        tea_master = Agent(
            name="Tea Master Washin",
            instructions="You are a tea ceremony master. Provide cultural wisdom about Japanese hospitality.",
            model="meta-llama/Llama-3.3-70B-Instruct",
            api_key=api_key,
            base_url=base_url
        )
        
        haiku_poet = Agent(
            name="Haiku Poet Kigo", 
            instructions="You are a haiku poet. Create beautiful haiku about cultural experiences.",
            model="meta-llama/Llama-3.3-70B-Instruct",
            api_key=api_key,
            base_url=base_url
        )
        
        print("✅ Cultural team assembled!")
        print("🍵 Tea Master ready")
        print("🎋 Haiku Poet ready")
        
        cultural_request = "I want to experience authentic Japanese onsen culture. Please guide me on cultural significance and etiquette."
        
        print(f"\n👤 Tourist Request:")
        print(f"'{cultural_request}'")
        
        print("\n🔄 Processing with Workflow integration...")
        
        workflow = Workflow(objective=cultural_request, client_mode=False)
        
        print("⚙️ Executing integrated cultural guidance...")
        integrated_response = await workflow.summarize_text(
            max_words=100,
            agents=[tea_master, haiku_poet]
        ).run_tasks()
        
        print(f"\n✨ Integrated Cultural Guide:")
        print(f"{integrated_response}")
        
        print("\n🎊 Workflow integration completed!")
        return integrated_response
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    try:
        asyncio.run(demonstrate_workflow_integration())
    except Exception as e:
        print(f"💥 Error: {e}")