import bcrypt

def hash_password(password:str)->str:

    # ["GodKnows811"]-->[72,78,90,63]-->Math operations-->[466877654,65544576778]-->"#gihjhgfhvhbjbk"
    pwd_bytes=password.encode('utf-8')  
    salt= bcrypt.gensalt() #-->random characters[788765]
    hash_pwd_bytes=bcrypt.hashpw(pwd_bytes, salt)
    hash_pwd= hash_pwd_bytes.decode('utf-8')
    return hash_pwd
