#!/usr/bin/env python3
"""
Debug liquidity lock extraction
"""
import sys
sys.path.append('.')

def test_liquidity_extraction():
    """Test the liquidity lock extraction logic"""
    from src.services.goplus import GoPlusService
    
    service = GoPlusService()
    
    # Test with mock data that matches your log
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
    
    print("Testing liquidity lock extraction...")
    result = service._extract_liquidity_lock_info(mock_data)
    
    print(f"Result: {result}")
    
    # Expected results
    expected_platform = "PinkSale"
    expected_unlock = "2025-09-30T11:40:00+00:00"
    
    print(f"\nExpected platform: {expected_platform}")
    print(f"Expected unlock time: {expected_unlock}")
    
    if result['platform'] == expected_platform:
        print("✅ Platform extraction: SUCCESS")
    else:
        print(f"❌ Platform extraction: FAILED (got {result['platform']})")
    
    if result['unlock_time'] == expected_unlock:
        print("✅ Unlock time extraction: SUCCESS")
    else:
        print(f"❌ Unlock time extraction: FAILED (got {result['unlock_time']})")

if __name__ == "__main__":
    test_liquidity_extraction()
