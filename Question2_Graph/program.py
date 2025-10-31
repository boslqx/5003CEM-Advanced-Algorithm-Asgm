# a cli program that act like a instagram
from person import Person
from graph import Graph

# insert people (min 5)
def sample_data():
    g = Graph()
    people = {
        "u1": Person("u1", "Alice", "Female", "Just For FUn", "public"),
        "u2": Person("u2", "Bob", "Male", "NERD OUT", "public"),
        "u3": Person("u3", "Charlie", "Male", "MINECRAFTALLSEM", "private"),
        "u4": Person("u4", "Diana", "Female", "blablablabala", "public"),
        "u5": Person("u5", "Eve", "Female", "dont stalk my profile", "private"),
    }

    # Add vertices
    for uid in people:
        g.add_vertex(uid)

    # Add edges (set up following)
    g.add_edge("u1", "u2")  # Eg: Alice follows Bob
    g.add_edge("u1", "u3")
    g.add_edge("u2", "u3")
    g.add_edge("u3", "u1")
    g.add_edge("u4", "u2")
    g.add_edge("u5", "u1")

    return g, people

def menu():
    print("****************************************************")
    print("=== Walmart Instagram ===")
    print("****************************************************")
    print("1. Display all user names")
    print("2. View profile of a user")
    print("3. View followed accounts of a user")
    print("4. View followers of a user")
    print("5. Add a new user profile")
    print("6. Follow a user")
    print("7. Unfollow a user")
    print("8. Exit")
    print("****************************************************")
    print("8. Exit")
    print("****************************************************")

def main():
    g, people = sample_data() # loads graphs and person

    while True:
        menu()
        choice = input("Enter choice: ")

        # display person's info
        if choice == "1":
            print("All users:")
            for uid, person in people.items():
                print(f"- {person.name} ({uid})")

        # shows specific one information
        elif choice == "2":
            uid = input("Enter user ID: ")
            if uid in people:
                print(people[uid])
            else:
                print("User not found.")

        # view specific one followings
        elif choice == "3":
            uid = input("Enter user ID: ")
            if uid in people:
                following = g.list_outgoing_adjacent_vertex(uid)
                if following:
                    print(f"{people[uid].name} follows:")
                    for f in following:
                        print("-", people[f].name)
                else:
                    print("No followed accounts.")
            else:
                print("User not found.")


        # view specific one followers
        elif choice == "4":
            uid = input("Enter user ID: ")
            if uid in people:
                followers = g.list_incoming_adjacent_vertex(uid)
                if followers:
                    print(f"{people[uid].name}'s followers:")
                    for f in followers:
                        print("-", people[f].name)
                else:
                    print("No followers.")
            else:
                print("User not found.")
        
        # add new user profile
        elif choice == "5":  
            uid = input("Enter new user ID: ")
            if uid in people:
                print("User ID already exists.")
            else:
                name = input("Enter name: ")
                gender = input("Enter gender: ")
                bio = input("Enter bio: ")
                privacy = input("Enter privacy (public/private): ").lower()
                if privacy not in ["public", "private"]:
                    privacy = "public"
                people[uid] = Person(uid, name, gender, bio, privacy)
                g.add_vertex(uid)
                print("New user added successfully.")

        # follow user on demand
        elif choice == "6":
            follower = input("Enter follower user ID: ")
            followed = input("Enter followed user ID: ")
            if follower in people and followed in people:
                g.add_edge(follower, followed)
                print(f"{people[follower].name} now follows {people[followed].name}.")
            else:
                print("Invalid user IDs.")

        # unfollow user on demand
        elif choice == "7":
            follower = input("Enter follower user ID: ")
            unfollowed = input("Enter user ID to unfollow: ")
            if follower in people and unfollowed in people:
                if unfollowed in g.adj_list.get(follower, set()):
                    g.adj_list[follower].remove(unfollowed)
                    print(f"{people[follower].name} unfollowed {people[unfollowed].name}.")
                else:
                    print(f"{people[follower].name} is not following {people[unfollowed].name}.")
            else:
                print("Invalid user IDs.")

        # exit
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()