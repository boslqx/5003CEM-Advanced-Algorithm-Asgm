# implement unweighted directed graph
class Graph:
    def __init__(self):
        self.adj_list = {}

    # function to add new vertex
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = set() # usea set ensures each followed use appear once and membership are O(1) avg

    # function to add edge between vertex
    def add_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].add(v2)

    # return set of following of the v
    def list_outgoing_adjacent_vertex(self,v):
        return list(self.adj_list.get(v,[]))
    
    # return v's followers
    def list_incoming_adjacent_vertex(self,v):
        followers = []
        for users, following in self.adj_list.items():
            if v in following:
                followers.append(users)
        return followers
            
    # print every user id         
    def display_graph(self):
        for user, following in self.adj_list.items():
            print(f"{user} follows {', '.join(following) if following else 'None'}")
