def success_response(language, result):

    return {
        "status": "success",
        "language": language,
        "classification": result["classification"],
        "confidenceScore": result["confidenceScore"],
        "explanation": result["explanation"]
    }


def error_response(message):

    return {
        "status": "error",
        "message": message
    }
