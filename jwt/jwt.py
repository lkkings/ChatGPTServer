from typing import Any, Union, Optional
from datetime import datetime, timedelta
from fastapi import Header
from jose import jwt
from utils import AccessTokenFail

async def check_jwt_token(token: Optional[str] = Header(...)) -> Union[str, Any]:
    """ 解密token """
    try:
        payload = jwt.decode(token=token, key="2893891716", algorithms=["HS256" ])
        return payload
    except Exception as e:  # jwt.JWTError, jwt.ExpiredSignatureError, AttributeError
        raise AccessTokenFail(f'token已过期! -- {e}')


if __name__ == '__main__':
    p = check_jwt_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDAwMDAxIiwic2NvcGVzIjpbInVzZXIiXSwiZXhwIjoxNjc1ODM2OTY3fQ.i7Io79Y1lLncS-ETlyfK_kFXOBteolXzRbqSH29LhWg")
