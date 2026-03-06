"""
fonction utilitaire pour formater les réponses
"""

from fastapi.responses import JSONResponse

def formatResponse(data, status_code, message):
    """
    fonction utilitaire pour formater les réponses
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "status": message,
            "data": data
        }
    )