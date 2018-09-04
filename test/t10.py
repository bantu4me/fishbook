from itsdangerous import JSONWebSignatureSerializer

s = JSONWebSignatureSerializer(
    secret_key='\x13\x7f\x02\xf6\xcb:\x95\xd9\xb8\xdb:\x8ba\xa5\x07\xdd\x8e\xb6\xcb\x8e\xe3I\x97\x1c')

user_info = {'id': 1, 'email': '1024254238@qq.com'}

r = s.dumps(user_info).decode('utf-8')

print(r)

r = s.loads(r)
print(r.get('id'))
print(r.get('email'))
