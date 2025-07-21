import os
import asyncio
from iointel import Agent

async def demonstrate_cultural_agents():
    """日本文化特化エージェントの実演"""
    
    print("🚀 Starting Cultural Agents Demo...")
    print("🌸 Creating Japanese Cultural Agents...")
    print("=" * 50)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    base_url = "https://api.intelligence.io.solutions/api/v1"
    
    try:
        # 茶道師範エージェント作成
        print("🍵 Creating Tea Ceremony Master...")
        tea_master = Agent(
            name="Tea Master Washin", 
            instructions="You are a respectful Japanese tea ceremony master. Explain tea ceremony principles with warmth and wisdom. Keep responses concise but meaningful.",
            model="meta-llama/Llama-3.3-70B-Instruct",
            api_key=api_key,
            base_url=base_url
        )
        
        print("✅ Tea Ceremony Master 'Washin' created!")
        print(f"📝 Agent name: {tea_master.name}")
        
        # 俳句詩人エージェント作成
        print("\n🎋 Creating Haiku Poet...")
        haiku_poet = Agent(
            name="Haiku Poet Kigo",
            instructions="You are a master haiku poet. Create beautiful haiku with 5-7-5 syllable structure. Focus on nature, seasons, and onsen themes.",
            model="meta-llama/Llama-3.3-70B-Instruct", 
            api_key=api_key,
            base_url=base_url
        )
        
        print("✅ Haiku Poet 'Kigo' created!")
        print(f"📝 Agent name: {haiku_poet.name}")
        
        # 茶道師範との対話
        print("\n☕ Asking Tea Master about tea ceremony philosophy...")
        print("🙋 User: Please explain the essence of Japanese tea ceremony in simple terms.")
        
        tea_wisdom = await tea_master.run(
            "Please explain the essence of Japanese tea ceremony in simple terms."
        )
        print(f"🌸 Tea Master's Wisdom:\n{tea_wisdom}")
        
        # 俳句詩人との対話
        print("\n🍃 Requesting haiku from Haiku Poet...")
        print("🙋 User: Create a haiku about cherry blossoms and hot springs.")
        
        spring_haiku = await haiku_poet.run(
            "Create a beautiful haiku about cherry blossoms and hot springs."
        )
        print(f"🎋 Beautiful Haiku:\n{spring_haiku}")
        
        print("\n✨ Cultural agents demonstration completed!")
        print("🎊 Japanese cultural AI agents working perfectly!")
        
        return tea_master, haiku_poet
        
    except Exception as e:
        print(f"❌ Error in cultural agents demo: {e}")
        import traceback
        traceback.print_exc()
        return None, None

if __name__ == "__main__":
    try:
        asyncio.run(demonstrate_cultural_agents())
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        import traceback
        traceback.print_exc()