import subprocess
import time

def pause_for_filming(message="Press Enter to continue to next demo..."):
    print(f"\n⏸️ {message}")
    input()

def run_demo(demo_name, demo_file):
    print(f"\n{'='*60}")
    print(f"🎬 {demo_name}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(['python3', demo_file], 
                              capture_output=False, 
                              text=True)
        
        if result.returncode == 0:
            print(f"✅ {demo_name} completed successfully!")
        else:
            print(f"❌ {demo_name} encountered issues")
            
    except Exception as e:
        print(f"💥 Error running {demo_name}: {e}")

def main():
    print("🌸" + "="*60 + "🌸")
    print("       AI温泉コンシェルジュ「湯めぐり」")
    print("    World's First AI Onsen Concierge System")
    print("     io.net Launch IO Hackathon 2025")
    print("         Beginner Track Demonstration")
    print("🌸" + "="*60 + "🌸")
    
    demos = [
        ("🤖 Demo 1: Basic Agent Framework", "demo_basic_agent.py"),
        ("🌸 Demo 2: Japanese Cultural Agents", "demo_cultural_agents.py"),
        ("🔄 Demo 3: Workflow Integration", "demo_workflow_integration.py"), 
        ("♨️ Demo 4: Onsen Concierge Vision", "demo_onsen_concierge.py")
    ]
    
    print("\n🎯 Ready to demonstrate the complete AI Onsen Concierge system!")
    pause_for_filming("Start Demo 1? (Basic Framework)")
    
    for i, (demo_name, demo_file) in enumerate(demos, 1):
        run_demo(demo_name, demo_file)
        
        if i < len(demos):
            pause_for_filming(f"Continue to Demo {i+1}?")
    
    print("\n" + "🎊"*20)
    print("🏆 COMPLETE DEMONSTRATION FINISHED! 🏆")
    print("🌸 AI Onsen Concierge 'Yumeguri' Successfully Demonstrated!")
    print("🙏 Thank you for watching this cultural AI innovation!")
    print("💫 Created with passion for io.net Launch IO Hackathon 2025")
    print("🎊"*20)

if __name__ == "__main__":
    main()