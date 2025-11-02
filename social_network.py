class Person:
    '''
    A class representing a person in a social network.
    
    Attributes:
        name (str): The name of the person.
        friends (list): A list of Person objects representing this person's friends.
    
    Methods:
        add_friend(friend): Adds a friend to the person's friends list.
    '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """Adds a friend to the person's friends list if not already present."""
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network using an adjacency list.
    
    Attributes:
        people (dict): A dictionary mapping names (str) to Person objects.
    
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a bidirectional friendship.
        print_network(): Prints the network structure.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """Creates a new Person instance and adds it to the network."""
        if name in self.people:
            print(f"Person '{name}' already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        """Creates a bidirectional friendship between two existing people."""
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. {person1_name if person1_name not in self.people else ''}{' and ' if person1_name not in self.people and person2_name not in self.people else ''}{person2_name if person2_name not in self.people else ''} doesn't exist!")
            return
        
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        """Prints all people and their list of friends."""
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names) if friend_names else 'No friends'}")


# --- TESTING SECTION ---
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Create friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # should trigger an error
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    print("\n--- SOCIAL NETWORK ---")
    network.print_network()



'''
DESIGN MEMO (Approx. 230 words)

A graph is the most effective data structure to represent a social network because relationships between people are inherently non-hierarchical and bidirectional. Each person can have any number of friends, and those friendships can form complex interconnections, cycles, or clusters. A graph naturally models this flexibility through nodes (people) and edges (friendships).

A list would not work well because it represents linear data — it doesn’t allow efficient lookup of who is connected to whom without iterating through the entire structure. A tree is also inappropriate since it enforces a parent–child hierarchy, which doesn’t fit social relationships. In a social network, multiple people can be connected without a single “root,” and friendships are mutual, not one-directional.

By using an adjacency list (implemented as a dictionary of Person objects), the program achieves efficient lookups and updates. Adding a person takes constant time O(1), and adding a friendship is also efficient since it only involves updating two lists. The trade-off is that printing the network requires visiting every person and their connections, which scales linearly with the number of people and friendships.

Overall, the graph structure balances flexibility and performance, accurately representing how social connections operate in real life while remaining efficient and scalable for growing networks.
'''
