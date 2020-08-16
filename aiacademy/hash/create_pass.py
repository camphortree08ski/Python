from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

input_pass = input(">>> ")

hash_pass = generate_password_hash(input_pass)
print("hash: ", hash_pass)

##
result = check_password_hash(hash_pass, input_pass)
print(result)
