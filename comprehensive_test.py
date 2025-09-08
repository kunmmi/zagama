#!/usr/bin/env python3
"""
Comprehensive test for all new features
"""
import asyncio
import sys
sys.path.append('.')

from src.services.goplus import GoPlusService

def test_liquidity_lock_extraction():
    """Test liquidity lock extraction with mock data"""
    print("=== TESTING LIQUIDITY LOCK EXTRACTION ===")
    
    service = GoPlusService()
    
    # Mock data based on your log details
    mock_data = {
        'lp_holders': [
            {
                'is_locked': 1,
                'locked_detail': [
                    {
                        'amount': '20000000.000000000000000000',
                        'end_time': '2025-09-30T11:40:00+00:00',
                        'opt_time': '2025-09-02T11:42:59+00:00',
                        'tag': 'PinkLock02'
                    }
                ]
            }
        ]
    }
    
    result = service._extract_liquidity_lock_info(mock_data)
    print(f"Platform: {result['platform']}")
    print(f"Unlock time: {result['unlock_time']}")
    
    # Verify expected results
    expected_platform = "PinkSale"
    expected_unlock = "2025-09-30T11:40:00+00:00"
    
    if result['platform'] == expected_platform:
        print("✅ Platform extraction: PASSED")
    else:
        print(f"❌ Platform extraction: FAILED (got {result['platform']}, expected {expected_platform})")
    
    if result['unlock_time'] == expected_unlock:
        print("✅ Unlock time extraction: PASSED")
    else:
        print(f"❌ Unlock time extraction: FAILED (got {result['unlock_time']}, expected {expected_unlock})")

async def test_full_goplus_integration():
    """Test the full GoPlus integration"""
    print("\n=== TESTING FULL GOPLUS INTEGRATION ===")
    
    service = GoPlusService()
    result = await service.get_token_security('0x6234641eae20d15f803441f348352794419b44c7', 'base')
    
    print(f"Name: {result.get('name')}")
    print(f"Top holders ratio: {result.get('top_holders_ratio')}")
    print(f"Contract holding percentage: {result.get('contract_holding_percentage')}")
    print(f"Liquidity lock platform: {result.get('liquidity_lock_platform')}")
    print(f"Liquidity lock unlock time: {result.get('liquidity_lock_unlock_time')}")
    
    # Check if we have the expected data
    if result.get('liquidity_lock_platform'):
        print("✅ Liquidity lock platform: FOUND")
    else:
        print("❌ Liquidity lock platform: NOT FOUND")
    
    if result.get('liquidity_lock_unlock_time'):
        print("✅ Liquidity lock unlock time: FOUND")
    else:
        print("❌ Liquidity lock unlock time: NOT FOUND")

def main():
    """Run all tests"""
    print("🧪 COMPREHENSIVE TESTING")
    print("=" * 50)
    
    # Test 1: Liquidity lock extraction
    test_liquidity_lock_extraction()
    
    # Test 2: Full integration
    asyncio.run(test_full_goplus_integration())
    
    print("\n" + "=" * 50)
    print("🏁 TESTING COMPLETE")

if __name__ == "__main__":
    main()
