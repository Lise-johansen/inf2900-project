import jwt


def test_id():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6M30.6_grpok6fEk5SfuV53nekD6KciJYXE-m1h5ChM1xAI4"
    secret_key = 'St3rkP@ssord'
    payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    print(payload)

    user = payload.get('token')
    print(user)

    


test_id()