from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

# input_pass = input(">>> ")
input_pass = "abc" # 正しいパス
# input_pass = "aaa" # 正しくないパス

# hash_pass = generate_password_hash(input_pass) # DBにインサート

# hash_passは各ユーザーの入力したパスワードをハッシュ化している。(abcをハッシュ化させたものが下記)
hash_pass = "pbkdf2:sha256:50000$eU0B5xZb$77902a948c4f1c2dfaeb9dbb094b376d11e1745bf6e4d1156ab0f73837cc62ff"
print("hash: ", hash_pass)
result = check_password_hash(hash_pass, input_pass)
print(result)
