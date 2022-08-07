from models.user import UserModel

"""
users = [
    User(1, "User1", "Password1")
]

username_mapping = {
    u.username : u for u in users
}


userid_mapping = {
    u.id : u for u in users
}
"""


def authenticate(username, password):
    user = UserModel.find_by_username(username)  #This was "username_mapping.get(user, None)"
    if user and user.password == password:  #Note: "if user" here is originally "if user is not None"
        return user  #Quest: what if the password is wrong, he didn't mention the procesure?

def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)  #This was "userid_mapping.get(user_id, None)"