#!/usr/bin/env python3
"""
Test the new improvements: Not Honeypot indicator and 0% Clog display
"""
import sys
sys.path.append('.')
from src.models.token import *
from src.models.response import ResponseFormatter
from decimal import Decimal

def test_safe_token():
    """Test bot response for a safe token (not honeypot, 0% contract holdings)"""
    
    # Create a test result for a safe token
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

    # Set the data for a safe token
    result.basic_info.name = 'Safe Token'
    result.basic_info.symbol = 'SAFE'
    result.basic_info.chain = ChainType.BASE

    # Set security data - NOT a honeypot
    result.security_data.buy_tax = Decimal('0.02')  # 2% buy tax
    result.security_data.sell_tax = Decimal('0.02')  # 2% sell tax
    result.security_data.is_honeypot = False  # NOT a honeypot
    result.security_data.is_verified = True

    # Set market data
    result.market_data.liquidity_usd = Decimal('100000')
    result.market_data.price_usd = Decimal('0.01')

    # Set holder data - 0% contract holdings
    result.holder_data.holder_count = 1000
    result.holder_data.top_holders_ratio = 45.2
    result.holder_data.contract_holding_percentage = 0.0  # 0% contract holdings

    # Set risk assessment for safe token
    result.risk_assessment.overall_risk = RiskLevel.LOW
    result.risk_assessment.warnings = []
    result.risk_assessment.recommendations = ["Token appears safe to trade"]

    # Format the response
    formatted = ResponseFormatter.format_token_analysis(result)
    
    print("=== BOT RESPONSE FOR SAFE TOKEN ===")
    print(formatted)
    
    # Check specific improvements
    print("\n=== CHECKING IMPROVEMENTS ===")
    
    if "• Honeypot: ✅ Not Honeypot" in formatted:
        print("✅ Not Honeypot indicator: FOUND")
    else:
        print("❌ Not Honeypot indicator: NOT FOUND")
    
    if "• Clog (Contract Holdings): 0.0%" in formatted:
        print("✅ 0% Clog display: FOUND")
    else:
        print("❌ 0% Clog display: NOT FOUND")

def test_honeypot_token():
    """Test bot response for a honeypot token"""
    
    # Create a test result for a honeypot token
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

    # Set the data for a honeypot token
    result.basic_info.name = 'Scam Token'
    result.basic_info.symbol = 'SCAM'
    result.basic_info.chain = ChainType.BASE

    # Set security data - IS a honeypot
    result.security_data.buy_tax = Decimal('0.05')  # 5% buy tax
    result.security_data.sell_tax = Decimal('1.0')  # 100% sell tax
    result.security_data.is_honeypot = True  # IS a honeypot
    result.security_data.is_verified = False

    # Set holder data
    result.holder_data.holder_count = 10
    result.holder_data.top_holders_ratio = 95.0
    result.holder_data.contract_holding_percentage = 15.5  # 15.5% contract holdings

    # Set risk assessment for honeypot
    result.risk_assessment.overall_risk = RiskLevel.HONEYPOT
    result.risk_assessment.warnings = ["🚨 HONEYPOT DETECTED - DO NOT BUY!"]
    result.risk_assessment.recommendations = ["DO NOT BUY THIS TOKEN"]

    # Format the response
    formatted = ResponseFormatter.format_token_analysis(result)
    
    print("\n=== BOT RESPONSE FOR HONEYPOT TOKEN ===")
    print(formatted)
    
    # Check honeypot detection
    print("\n=== CHECKING HONEYPOT DETECTION ===")
    
    if "• Honeypot: 🚨 HONEYPOT DETECTED" in formatted:
        print("✅ Honeypot detection: FOUND")
    else:
        print("❌ Honeypot detection: NOT FOUND")

if __name__ == "__main__":
    test_safe_token()
    test_honeypot_token()
