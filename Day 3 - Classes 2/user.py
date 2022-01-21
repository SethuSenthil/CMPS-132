class User:
    def __init__(self, __first_name, __last_name, __username, __isVerified):
        self.first_name = __first_name
        self.last_name = __last_name
        self.username = __username,
        self.isVerified = __isVerified
    def describeUser(self):
        print(f'About @{self.username}')
        print(f'Name: {self.first_name} {self.first_name}')
        if self.isVerified:
         print("User is verified")
        else:
         print("User is not verified")
    def greetUser(self):
        print(f"Hello @{self.username}!")