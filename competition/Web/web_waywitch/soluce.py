import jwt

def sign_token(p,secret="halloween-secret",algo='HS256'):
    try:
        return jwt.encode(p, secret, algorithm=algo)
    except:
        print("invalide key", secret)
        return ""

Headers = {"alg":"HS256","typ":"JWT"}
Payload = {"username":"guest_8266","iat":1729826584}
Payload2 = {"username":"admin","iat":1729917458}

jwt_token_init_sign = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imd1ZXN0XzgyNjYiLCJpYXQiOjE3Mjk4MjY1ODR9.wyaiazkzoF-Amm8GVS-WU1VaRvmf817hOjbWTqAFWTk"

mtysign = sign_token(Payload)
print("verification pass 1er jwt:",mtysign,"\n", mtysign == jwt_token_init_sign)

print("jwt admin",sign_token(Payload2))