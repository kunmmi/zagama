#!/usr/bin/env python3
"""
Test the Clog fix
"""
import sys
sys.path.append('.')
from src.services.goplus import GoPlusService

def test_clog_fix():
    """Test that Clog shows up even when 0%"""
    
    service = GoPlusService()
    
    # Test the calculation method directly
    mock_data = {
        'holders': [],  # No holders data
        'total_supply': '1000000000000000000000000',
        'token_address': '0x6234641eae20d15f803441f348352794419b44c7'
    }
    
    top_ratio, contract_holding = service._calculate_top_holders_ratio(mock_data)
    
    print("=== CLOG CALCULATION TEST ===")
    print(f"Top holders ratio: {top_ratio}")
    print(f"Contract holding percentage: {contract_holding}")
    print(f"Type: {type(contract_holding)}")
    
    # Test the parsing method
    result = service._parse_security_data(mock_data)
    
    print(f"\n=== PARSED RESULT ===")
    print(f"Contract holding percentage: {result.get('contract_holding_percentage')}")
    print(f"Type: {type(result.get('contract_holding_percentage'))}")

if __name__ == "__main__":
    test_clog_fix()
