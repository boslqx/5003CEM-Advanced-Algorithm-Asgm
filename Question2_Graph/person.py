# implement class Person
class Person:
    def __init__(self, userID, name, gender, bio, privacy="public"):
        self.userID = userID
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy


    # print user information
    def __str__(self):
        if self.privacy == "private":
            return f"User: {self.name} (Private Profile)"
        else:
            return (f"User ID: {self.userID}\n"
                f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Bio: {self.bio}\n"
                f"Privacy: {self.privacy}")
        