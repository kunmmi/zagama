#!/usr/bin/env python3
"""
Health check endpoint for Render deployment
"""
from fastapi import FastAPI
import uvicorn
import os
from datetime import datetime

app = FastAPI(title="BearTech Bot Health Check")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "BearTech Token Analysis Bot",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for Render"""
    return {
        "status": "healthy",
        "service": "BearTech Bot",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.getenv("RENDER", "local")
    }

@app.get("/status")
async def status():
    """Detailed status endpoint"""
    return {
        "service": "BearTech Token Analysis Bot",
        "status": "operational",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": {
            "render": bool(os.getenv("RENDER")),
            "python_version": os.getenv("PYTHON_VERSION", "unknown"),
            "telegram_token_set": bool(os.getenv("TELEGRAM_BOT_TOKEN")),
            "goplus_key_set": bool(os.getenv("GOPLUS_API_KEY"))
        }
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
