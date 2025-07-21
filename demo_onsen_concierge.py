import os
import asyncio
from iointel import Agent

async def onsen_concierge_demo():
    print("🚀 AI Onsen Concierge Vision Demo")
    print("♨️ Future of Cultural AI Experiences")
    print("=" * 40)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    base_url = "https://api.intelligence.io.solutions/api/v1"
    
    try:
        onsen_guide = Agent(
            name="Onsen Concierge Yusuke",
            instructions="You are a friendly onsen concierge. Provide personalized recommendations with warmth and cultural insight.",
            model="meta-llama/Llama-3.3-70B-Instruct",
            api_key=api_key,
            base_url=base_url
        )
        
        print("♨️ Onsen Concierge 'Yusuke' created!")
        
        request = "I have shoulder tension and enjoy mild temperatures. I want to experience traditional Japanese hospitality."
        
        print(f"\n👤 Personal Request:")
        print(f"'{request}'")
        
        print("\n🤔 Analyzing preferences...")
        recommendation = await onsen_guide.run(request)
        
        print(f"♨️ Personalized Recommendation:")
        print(f"{recommendation}")
        
        print("\n🌟 This showcases the future of AI-powered cultural experiences!")
        print("🌸 Technology meets traditional Japanese omotenashi spirit!")
        print("✅ Onsen Concierge demo completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(onsen_concierge_demo())