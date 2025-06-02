#!/usr/bin/env python
"""
Quick test script to verify Anthropic integration is working.
Run this before deploying to production.
"""

import os
import sys
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

def test_anthropic_connection():
    """Test basic Anthropic API connection"""
    load_dotenv()
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found in environment variables")
        return False
    
    if api_key == 'your_anthropic_api_key_here':
        print("❌ Please replace the placeholder ANTHROPIC_API_KEY with your actual API key")
        return False
    
    try:
        print("🔄 Testing Anthropic API connection...")
        llm = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=api_key,
            temperature=0.1,
            max_tokens=100,
        )
        
        response = llm.invoke("Hello! Please respond with 'Connection successful' if you can read this.")
        print(f"✅ Anthropic API connection successful!")
        print(f"📝 Response: {response.content}")
        return True
        
    except Exception as e:
        print(f"❌ Anthropic API connection failed: {e}")
        return False

def test_crew_import():
    """Test that the crew can be imported successfully"""
    try:
        print("🔄 Testing crew import...")
        from similar_company_finder_template.crew import SimilarCompanyFinderTemplateCrew
        crew_instance = SimilarCompanyFinderTemplateCrew()
        print("✅ Crew import successful!")
        return True
    except Exception as e:
        print(f"❌ Crew import failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Running production readiness tests...\n")
    
    tests = [
        ("Anthropic API Connection", test_anthropic_connection),
        ("Crew Import", test_crew_import),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        result = test_func()
        results.append(result)
    
    print("\n" + "="*50)
    print("📊 TEST RESULTS:")
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    if all(results):
        print("\n🎉 All tests passed! Your crew is ready for production.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
