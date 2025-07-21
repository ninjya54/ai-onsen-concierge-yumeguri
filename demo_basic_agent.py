import os
import asyncio
import sys
from iointel import Agent, Workflow

async def demonstrate_basic_framework():
    """io.net Framework基本機能の実演"""
    
    print("🌸 Welcome to io.net Agent Framework Demo!")
    print("=" * 50)
    
    # APIキー設定確認
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found")
        print("Please run: export OPENAI_API_KEY='your-api-key'")
        return
    
    base_url = "https://api.intelligence.io.solutions/api/v1"
    
    # 基本エージェント作成
    print("🤖 Creating basic AI agent...")
    
    try:
        basic_agent = Agent(
            name="Hello Agent",
            instructions="You are a friendly AI assistant. Respond warmly and briefly.",
            model="meta-llama/Llama-3.3-70B-Instruct",
            api_key=api_key,
            base_url=base_url
        )
        
        print("✅ Agent created successfully!")
        print(f"📝 Agent name: {basic_agent.name}")
        
        # 基本対話テスト
        print("\n💬 Testing basic conversation...")
        print("🙋 User: Hello! Please introduce yourself briefly.")
        
        response = await basic_agent.run("Hello! Please introduce yourself briefly.")
        
        print(f"🤖 Agent Response: {response}")
        
        print("\n✨ Basic framework demonstration completed!")
        return basic_agent
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("💡 Tip: Check your API key and internet connection")
        return None

async def main():
    """メイン関数"""
    print("🚀 Starting Basic Agent Demo...")
    agent = await demonstrate_basic_framework()
    
    if agent:
        print("\n🎊 Demo completed successfully!")
        print("🌸 io.net Agent Framework is working perfectly!")
    else:
        print("\n😞 Demo failed. Please check the error messages above.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")