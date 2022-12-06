from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt

from auth import oauth2
from auth.oauth2 import oauth2_schema
from schemas import SentimentDisplay, SentimentInput

router = APIRouter(prefix="/predictions", tags=["Predictions"])


@router.post("/sentiment", response_model=SentimentDisplay)
def sentiment(request: SentimentInput, token: str = Depends(oauth2_schema)):

    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authentication": "Bearer"},
    )

    try:
        payload = jwt.decode(token, oauth2.SECRET_KEY, algorithms=[oauth2.ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise credential_exception

    except JWTError:
        raise credential_exception

    if username != "airudi":  # TODO: Read user from the DB
        raise credential_exception

    # All Good!
    return SentimentDisplay(
        input_text=request.input_text,
        prediction="NEGATIVE",
        confidence_probability=0.98,
    )
