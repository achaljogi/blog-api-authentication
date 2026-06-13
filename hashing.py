from passlib.context import CryptContext

pwd_Context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password:str):
    return pwd_Context.hash(password)

def verify_password(
        plain_password,
        hashed_password):
 
    return pwd_Context.verify(
        plain_password,
        hashed_password   
    )
 