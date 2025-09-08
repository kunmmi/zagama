#!/usr/bin/env python3
"""
Test bot response formatting with new fields
"""
import sys
sys.path.append('.')
from src.models.token import *
from src.models.response import ResponseFormatter
from decimal import Decimal

def test_bot_response():
    """Test that the bot will display the new fields"""
    
    # Create a test result with the new fields populated
    result = TokenAnalysisResult(
        basic_info=TokenBasicInfo(),
        market_data=TokenMarketData(),
        security_data=TokenSecurityData(),
        liquidity_data=TokenLiquidityData(),
        holder_data=TokenHolderData(),
        deployer_data=TokenDeployerData(),
        contract_data=TokenContractData(),
        risk_assessment=TokenRiskAssessment(),
        analysis_timestamp='2025-01-08T10:00:00Z'
    )

    # Set the data
    result.basic_info.name = 'Test Token'
    result.basic_info.symbol = 'TEST'

    # Add holder data with contract holdings (Clog)
    result.holder_data.holder_count = 557
    result.holder_data.top_holders_ratio = 77.78
    result.holder_data.contract_holding_percentage = 8.4  # Clog field

    # Add liquidity data with lock info
    result.liquidity_data.liquidity_usd = Decimal('50000')
    result.liquidity_data.liquidity_locked = True
    result.liquidity_data.liquidity_lock_platform = 'PinkSale'
    result.liquidity_data.liquidity_lock_unlock_time = '2025-09-30T11:40:00+00:00'

    # Format the response
    formatted = ResponseFormatter.format_token_analysis(result)
    
    print("=== BOT RESPONSE FORMAT ===")
    print(formatted)
    
    # Check if our new fields are in the response
    if "Clog (Contract Holdings): 8.4%" in formatted:
        print("\n✅ Clog field: FOUND in response")
    else:
        print("\n❌ Clog field: NOT FOUND in response")
    
    if "Platform: PinkSale" in formatted:
        print("✅ Liquidity lock platform: FOUND in response")
    else:
        print("❌ Liquidity lock platform: NOT FOUND in response")
    
    if "Unlocks: 2025-09-30T11:40:00+00:00" in formatted:
        print("✅ Liquidity unlock time: FOUND in response")
    else:
        print("❌ Liquidity unlock time: NOT FOUND in response")

if __name__ == "__main__":
    test_bot_response()
