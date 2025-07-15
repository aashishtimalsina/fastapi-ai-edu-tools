"""
Test script for Google AI integration
Run this to test if your Google AI Studio API key is working
"""

import os
import sys
from dotenv import load_dotenv

# Add the app directory to the Python path
sys.path.append('app')

# Load environment variables
load_dotenv()

def test_google_ai():
    try:
        from google_ai_integration import ask_gpt
        
        print("Testing Google AI Studio integration...")
        print("=" * 50)
        
        # Test prompt
        test_prompt = "Explain what photosynthesis is in simple terms."
        
        print(f"Test prompt: {test_prompt}")
        print("\nGenerating response...")
        
        response = ask_gpt(test_prompt)
        
        print("\nResponse:")
        print("-" * 30)
        print(response)
        print("-" * 30)
        
        print("\n✅ Google AI Studio integration test successful!")
        
    except Exception as e:
        print(f"\n❌ Error testing Google AI integration: {str(e)}")
        print("\nPossible solutions:")
        print("1. Make sure your .env file exists and contains GOOGLE_API_KEY")
        print("2. Verify your Google AI Studio API key is correct")
        print("3. Check if google-generativeai package is installed: pip install google-generativeai")
        
if __name__ == "__main__":
    # Check if API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY not found in environment variables")
        print("Please create a .env file and add your Google AI Studio API key:")
        print("GOOGLE_API_KEY=your_api_key_here")
        sys.exit(1)
    
    test_google_ai()
