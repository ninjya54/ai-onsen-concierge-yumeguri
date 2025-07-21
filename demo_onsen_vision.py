# demo_onsen_vision.py
import os
import asyncio
import sys
from iointel import Agent, Workflow

async def demonstrate_onsen_concierge_vision():
    """温泉コンシェルジュのビジョン説明"""
    
    print("\n♨️ AI Onsen Concierge Vision Demo...")
    print("=" * 50)
    
    # 将来のコンシェルジュエージェント（コンセプト）
    onsen_guide = Agent(
        name="Onsen Concierge Yusuke",
        instructions="""
        You are a friendly onsen concierge who speaks with warmth.
        Provide personalized recommendations based on health and preferences.
        Explain onsen culture with enthusiasm and care.
        """,
        model="meta-llama/Llama-3.3-70B-Instruct",
        api_key=api_key,
        base_url=base_url
    )
    
    print("♨️ Onsen Concierge created!")
    
    # パーソナライズされた推薦実演
    personal_request = """
    I have shoulder tension from office work and enjoy mild temperatures. 
    I'm also interested in experiencing traditional Japanese hospitality. 
    What onsen experience would you recommend?
    """
    
    print(f"\n👤 Personal Request:\n{personal_request}")
    print("\n🤔 Analyzing preferences and providing recommendations...")
    
    recommendation = await onsen_guide.run(personal_request)
    print(f"♨️ Personalized Onsen Recommendation:\n{recommendation}")
    
    print("\n🌟 This showcases the future of AI-powered cultural experiences!")
    print("🌸 Combining technology with traditional Japanese omotenashi spirit!")
    
    return recommendation