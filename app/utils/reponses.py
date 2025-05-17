from fastapi.responses import JSONResponse

def custom_response(data, message="Success"):
    return JSONResponse(content={"message": message, "data": data})