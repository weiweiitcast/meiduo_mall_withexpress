


import json
import base64
import hmac,hashlib



# header
header = {
  'typ': 'JWT',
  'alg': 'HS256'
}

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 --> 根据base64编码得到的

# 1、将字典数据转化成json字符串
header = json.dumps(header) # --> 字符串
# 2、再将json字符串编码成base64 --> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
header = base64.b64encode(header.encode())
print("header: ", header)



# payload
# 记录用户数据，不可记录敏感信息
payload = {
  "sub": "1234567890",
  "name": "John Doe",
  "admin": True,
  "iss": "weiwei",
  "age": 18,
}
# eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9

# 1、json
payload = json.dumps(payload) # --> "{..}"
# 2、base64
payload = base64.b64encode(payload.encode())
print("payload: ", payload)


# signature
# 根据header和payload进行加密处理

# 1、获得拼接的加密数
msg = header + b'.' + payload
print("msg: ", msg)
# 2、加密得到signature
# 获得加密对象
SECRET_KEY = b'j*h(69kj^)ofyw+re!3!fpsh28a^wnm9iv1xv@9mi%^$)(dgm='
hobj = hmac.new(SECRET_KEY, msg, digestmod=hashlib.sha256)
# 获得签名字符串
signature = hobj.hexdigest()
print("signature: ", signature)


# jwt_token = header + payload + signature
JWT_TOKEN = header.decode() + '.' + payload.decode() + '.' + signature
print("JWT_TOKEN: ", JWT_TOKEN)





# 模拟校验流程
# 浏览器传来的JWT_TOKEN
JWT_TOKEN_FROM_BROWSER =  JWT_TOKEN

# 1、解析出header、payload和signature
header_from_browser = JWT_TOKEN_FROM_BROWSER.split(".")[0]
payload_from_browser = JWT_TOKEN_FROM_BROWSER.split(".")[1]
signature_from_browser = JWT_TOKEN_FROM_BROWSER.split(".")[2]

# 2、将header和payload再一次加密，得到一个新的new_signature
new_msg = header_from_browser + '.' + payload_from_browser
new_signature = hmac.new(SECRET_KEY, new_msg.encode(), digestmod=hashlib.sha256).hexdigest()

# 3、判断signature和new_signature是否一致
if new_signature == signature:
    # 3.1、一致，说明：数据是完整的（没有被篡改)
    print("校验成功")
else:
    # 3.2、如果不一致，说明：header和payload数据被篡改了
    print("数据不完整（可能被篡改了）")















