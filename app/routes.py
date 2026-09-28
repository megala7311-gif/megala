from fastapi import APIrouter

router =APIrouter()

@router.get("/")
def home():
    return {"message": "fitbuddy AI"}