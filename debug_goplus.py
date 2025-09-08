#!/usr/bin/env python3
"""
Debug script to check GoPlus API response structure
"""
import asyncio
import aiohttp
import json
import sys
sys.path.append('.')

from src.config import GOPLUS_API_KEY

async def debug_goplus_api():
    """Debug the actual GoPlus API response"""
    
    if not GOPLUS_API_KEY:
        print("❌ GoPlus API key not configured")
        return
    
    url = 'https://api.gopluslabs.io/api/v1/token_security/8453'  # Base chain
    params = {'contract_addresses': '0x6234641eae20d15f803441f348352794419b44c7'}
    headers = {'X-API-KEY': GOPLUS_API_KEY}
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                data = await response.json()
                
                print("=== GOPLUS API RESPONSE ===")
                print(f"Status: {response.status}")
                print(f"Code: {data.get('code')}")
                print(f"Message: {data.get('message')}")
                
                if data.get('result'):
                    result = data['result']
                    print(f"Result keys: {list(result.keys())}")
                    
                    # Check for our token
                    token_address = '0x6234641eae20d15f803441f348352794419b44c7'
                    if token_address.lower() in result:
                        token_data = result[token_address.lower()]
                        print(f"\n=== TOKEN DATA KEYS ===")
                        print(f"Keys: {list(token_data.keys())}")
                        
                        # Check for holders and lp_holders
                        if 'holders' in token_data:
                            print(f"Holders count: {len(token_data['holders'])}")
                            if token_data['holders']:
                                print(f"First holder: {token_data['holders'][0]}")
                        
                        if 'lp_holders' in token_data:
                            print(f"LP Holders count: {len(token_data['lp_holders'])}")
                            if token_data['lp_holders']:
                                print(f"First LP holder: {token_data['lp_holders'][0]}")
                                
                                # Check for lock information
                                for i, lp_holder in enumerate(token_data['lp_holders']):
                                    if lp_holder.get('is_locked') == 1:
                                        print(f"\n=== LOCKED LP HOLDER {i} ===")
                                        print(f"Name: {lp_holder.get('name')}")
                                        print(f"Is locked: {lp_holder.get('is_locked')}")
                                        print(f"Locked detail: {lp_holder.get('locked_detail')}")
                    else:
                        print(f"Token {token_address} not found in result")
                else:
                    print("No result data")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(debug_goplus_api())
