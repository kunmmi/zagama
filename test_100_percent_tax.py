#!/usr/bin/env python3
"""
Test bot response for token with 100% sell tax
"""
import sys
sys.path.append('.')
from src.models.token import *
from src.models.response import ResponseFormatter
from decimal import Decimal

def test_100_percent_sell_tax():
    """Test bot response for token with 100% sell tax"""
    
    # Create a test result with 100% sell tax
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

    # Set the data for a token with 100% sell tax
    result.basic_info.name = 'Suspicious Token'
    result.basic_info.symbol = 'SUS'
    result.basic_info.chain = ChainType.BASE

    # Set high taxes
    result.security_data.buy_tax = Decimal('0.05')  # 5% buy tax
    result.security_data.sell_tax = Decimal('1.0')  # 100% sell tax (1.0 = 100%)
    result.security_data.is_honeypot = False  # Not detected as honeypot by GoPlus
    result.security_data.is_verified = False

    # Set some market data
    result.market_data.liquidity_usd = Decimal('10000')
    result.market_data.price_usd = Decimal('0.001')

    # Set holder data
    result.holder_data.holder_count = 25
    result.holder_data.top_holders_ratio = 95.5

    # Perform risk assessment (this is what the bot does)
    result.risk_assessment.overall_risk = RiskLevel.HIGH
    result.risk_assessment.warnings = [
        "⚠️ High sell tax: 100.0%",
        "⚠️ Very low holder count: 25"
    ]
    result.risk_assessment.recommendations = [
        "AVOID - High sell tax makes it impossible to sell",
        "Consider this a potential scam token"
    ]

    # Format the response
    formatted = ResponseFormatter.format_token_analysis(result)
    
    print("=== BOT RESPONSE FOR 100% SELL TAX TOKEN ===")
    print(formatted)
    
    # Check specific elements
    print("\n=== KEY WARNINGS ===")
    if "High sell tax: 100.0%" in formatted:
        print("✅ High sell tax warning: FOUND")
    else:
        print("❌ High sell tax warning: NOT FOUND")
    
    if "AVOID - High sell tax" in formatted:
        print("✅ Avoid recommendation: FOUND")
    else:
        print("❌ Avoid recommendation: NOT FOUND")

if __name__ == "__main__":
    test_100_percent_sell_tax()
