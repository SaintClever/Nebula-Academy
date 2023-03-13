from fastapi import FastAPI, Request, Response, status
import bcrypt

app = FastAPI()

fake_user_db = [
    {
        "id": 0,
        "name": "John"
    }, {
        "id": 1,
        "name": "Brandon"
    }, {
        "id": 2,
        "name": "Eric"
    }, {
        "id": 3,
        "name": "Amy"
    }, {
        "id": 4,
        "name": "Abe"
    }, {
        "id": 5,
        "name": "Devin"
    }, {
        "id": 6,
        "name": "Anam"
    }, {
        "id": 7,
        "name": "Laurie"
    },
]

pluck = lambda dict, *args: (dict[arg] for arg in args)


for user in fake_user_db:
    user["salt"] = bcrypt.gensalt()
    password = f'{user["name"]}{user["id"]}'.encode('utf-8')
    user["password"] = bcrypt.hashpw(password, user["salt"])
@app.get("/")
async def root():
    print('hi')
    return {"message": "Hello World"}

@app.get("/users/")
async def get_users(skip: int = 0, limit: int = 5):
    return fake_user_db[skip : skip + limit]

@app.get('/user/{id}')
async def get_user(id: int):
    return fake_user_db[id]

@app.post('/login')
async def login(request: Request, response: Response):
    print('hi')
    data = await request.json()
    user = [x for x in fake_user_db if x["name"] == data["name"]][0]
    response.status_code = status.HTTP_403_FORBIDDEN
    hashed = bcrypt.hashpw(data["password"].encode('utf-8'), user["salt"])
    print(user["password"], hashed)
    if user["password"] == hashed:
        response.status_code = status.HTTP_200_OK
        return user
    return 'Invalid username or password'