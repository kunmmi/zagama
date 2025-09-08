#!/usr/bin/env python3
"""
Test liquidity lock extraction
"""
import asyncio
import sys
sys.path.append('.')

from src.services.goplus import GoPlusService

async def test_liquidity_lock():
    """Test liquidity lock extraction"""
    service = GoPlusService()
    
    # Test with the token that has PinkLock
    result = await service.get_token_security('0x6234641eae20d15f803441f348352794419b44c7', 'base')
    
    print("=== LIQUIDITY LOCK TEST ===")
    print(f"Name: {result.get('name')}")
    print(f"Liquidity lock platform: {result.get('liquidity_lock_platform')}")
    print(f"Liquidity lock unlock time: {result.get('liquidity_lock_unlock_time')}")
    
    # Check if we have any lock-related data
    print("\n=== ALL LOCK-RELATED DATA ===")
    for key, value in result.items():
        if 'lock' in key.lower():
            print(f"{key}: {value}")
    
    # Check if we have lp_holders data
    if 'lp_holders' in result:
        print(f"\nLP Holders data found: {len(result['lp_holders'])}")
    else:
        print("\nNo LP Holders data found")

if __name__ == "__main__":
    asyncio.run(test_liquidity_lock())
