#Huffman encoding algorithm
#Used to create an optimal prefix free encoding of a given random source S
#The random source S={s_1,s_2,...,s_m} has probability distribution P=(p_1,p_2,...,p_m) where p_i is the probability of s_i
#We use binary tree to obtain these codewords.
import operator

class Node():
    #self.data will contain the s_i
    #prob is the corresponding p_i
    def __init__(self, data, prob):
        self.left = None
        self.right = None
        self.data = data
        self.prob = prob
        self.huff = "" #this will be a 0 or 1 depending on its position in the tree
        return

    def __lt__(self, other):
        return self.prob < other.prob
    

    def print_node(self):
        if self.left is not None:
            print("Data = ({}), left = {}, right = {}".format(self.data,self.left.data,self.right.data)) 
        elif self.right is not None:
            print("Data = ({}), left = {}, right = {}".format(self.data,self.left.data,self.right.data))     
        elif self.left == None and self.right == None:
             print("Data = ({}), left = {}, right = {}, LEAF".format(self.data,self.left,self.right))
        return 

    def printNodes(self,node, val=''):
     
        # huffman code for current node
        newVal = val + str(node.huff)
    
        # if node is not an edge node
        # then traverse inside it
        if(node.left):
            self.printNodes(node.left, newVal)
        if(node.right):
            self.printNodes(node.right, newVal)
    
            # if node is edge node then
            # display its huffman code
        if(not node.left and not node.right):
            print(f"{node.data} -> {newVal}")    
 


#Class which will contain the methods for the Huffman encoding which generates a binary tree        

def init():
    L = generate_nodes() #list of letters and probabilities
    L = Tree_method_part1(L)
    Huffman_concatenation_part2(L)

    return

def generate_nodes():
    #will take the source and create L, the list of nodes although not as node class instance yet
    L = []

    source = get_source()
    print(source)
    for s in source:
        L.append(Node(s[0],float(s[1])))
        #print(s)  
    print(L)
    for node in L:
        node.print_node()
        print(node.prob)
    return L

def Tree_method_part1(L):
    #First part of Huffman algorithm to generate tree
    #gets the list of nodes which is s_i and p_i pairs 
    
    
    while len(L) >= 2:
        v_i1 , v_i2, L = lowest_probs(L)
        new_vertex(v_i1,v_i2,L)



    print("L = {}".format(L))
    
    


    return L

def Huffman_concatenation_part2(L):
    #Second part of Huffman algorithm to generate the Huffman codes using tree traversal
    
    root = L[0]

    print("Root is: {}".format(root.data))
    

    root.printNodes(root)

    

    return  

def lowest_probs(L):
    #method to find the two nodes in L with the lowest probabilities v_i1,v_i2
    
    L.sort(key = lambda x: x.prob)
    v_i1, v_i2 = L[:2]
    

    return v_i1,v_i2, L

def new_vertex(v_i1,v_i2,L):
    #this creates a new vertex from the two with lowest probabilities 
    #will also use this to create edges in the tree

    v_i1_i2 = []
    v_i1_i2.append(v_i1.data + "," + v_i2.data) #this creates a label to tell us which nodes created the new node
    v_i1_i2.append(v_i1.prob+v_i2.prob) #we add the two lowest probabilites to get the new node's probability 

    #create the nodes and append to the tree T
    
    new_node = Node(v_i1_i2[0],v_i1_i2[1])
    left = v_i1
    right = v_i2
    left.huff = 0
    right.huff = 1
    new_node.left = left
    new_node.right = right

    

    #Alter the list to include new node with probability and remove old nodes
    
    L.remove(v_i1)
    L.remove(v_i2)
    L.append(new_node)


    return L


def get_source():
    #method to generate S and P
    source = []
    source_size = int(input("How many letters in the source?: "))
    for i in range(0,source_size):
        letter = []
        prob = float(input("What is the probability of s_{}?: ".format(i+1)))
        letter.append(str(i+1)) #to allow for nodes numbered 1,2,...,m
        letter.append(prob)
        source.append(letter)


    return source



init()



