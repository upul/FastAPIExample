from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from hash import Hash
from auth import oauth2

router = APIRouter(tags=["authentication"])


@router.post("/token")
def get_token(request: OAuth2PasswordRequestForm = Depends()):
    # TODO: Move user and hashed-password into DB
    # or secure key vault if we have only one user
    if request.username != "airudi":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    if not Hash.verify(
        "$2b$12$VfhutA0CvBjJJfE7Wwhvje55o7fgsZZUw0DYPGA4Cf8HQtTA.SB9a", request.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )

    access_token = oauth2.create_access_token(data={"sub": "airudi"})
    return {"access_token": access_token, "token_type": "bearer", "user_id": "airidi"}
