#Huffman encoding algorithm
#Used to create an optimal prefix free encoding of a given random source S
#The random source S={s_1,s_2,...,s_m} has probability distribution P=(p_1,p_2,...,p_m) where p_i is the probability of s_i
#We use a binary tree to obtain these codewords.
import operator
import math

class Node():
    #self.data will contain the s_i
    #prob is the corresponding p_i
    def __init__(self, data, prob):
        self.left = None #left child
        self.right = None #right child
        self.data = data #this is the letter from the source
        self.prob = prob #probability associated with the letter from the source
        self.huff = "" #this will be a 0 or 1 depending on its position in the tree
        self.encoding = "" #binary string obtained from the Huffman encoding
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
        
        # if node is not an leaf node
        # then traverse inside it
        if(node.left):
            self.printNodes(node.left, newVal)
        if(node.right):
            self.printNodes(node.right, newVal)
        
            # if node is leaf node then
            # display its huffman code
        if(not node.left and not node.right):
            print(f"{node.data} -> {newVal}") 
            node.encoding = newVal #this is the binary representation of the source letter

        return 

    def inorderTraversal(self, root):
        #in-order traversal used to accumulate data and corresponding probabilites from nodes 
        #for calculations in expected length
       ret = []
       if root:
           ret = self.inorderTraversal(root.left)
           ret.append(root)
           ret = ret + self.inorderTraversal(root.right)
       return ret    


#Functions which will contain the methods for the Huffman encoding which generates a binary tree        

def init():
    #runs the algorithm from start to finish
    L, S = generate_nodes() #list of letters and probabilities
    print("The entropy of the source S. H(S) = {}".format(entropy(S)))
    node_list = L #this creates a copy of the nodes for later.
    L = Tree_method_part1(L)
    node_list = Huffman_concatenation_part2(L)
    expected_length(node_list)
    

    return

def generate_nodes():
    #will take the source and create L, the list of nodes although not as node class instance yet
    L = []

    source = get_source() #obtains letters and probabilities
    print(source)
    for s in source:
        L.append(Node(s[0],float(s[1])))
        #print(s)  
    print(L)
    for node in L:
        node.print_node()
        print(node.prob)
    return L, source

def Tree_method_part1(L):
    #First part of Huffman algorithm to generate the rooted binary tree from leaves back up to the root
    #gets the list of nodes which is s_i and p_i pairs 
    
    while len(L) >= 2:
        v_i1, v_i2, L = lowest_probs(L)
        new_vertex(v_i1,v_i2,L)

    print("L = {}".format(L))
    
    return L

def Huffman_concatenation_part2(L):
    #Second part of Huffman algorithm to generate the Huffman codes using tree traversal
    #also calls the traversal to obtain the list of nodes with their associated encoding 
    
    root = L[0] #from part1, we are left with a single node in the node list and this is the root.

    print("Root is: {}".format(root.data))
    
    root.printNodes(root)

    encoded_nodes = root.inorderTraversal(root)

    return encoded_nodes

def lowest_probs(L):
    #method to find the two nodes in L with the lowest probabilities v_i1,v_i2
    #sort the nodes by probability, from lowest to highest 
    
    L.sort(key = lambda x: x.prob)
    v_i1, v_i2 = L[:2]
    
    return v_i1,v_i2, L

def new_vertex(v_i1,v_i2,L):
    #this creates a new vertex from the two with lowest probabilities 
    #will also use this to create edges in the tree/children for each node

    v_i1_i2 = []
    v_i1_i2.append(v_i1.data + "," + v_i2.data) #this creates a label to tell us which nodes created the new node
    v_i1_i2.append(v_i1.prob+v_i2.prob)         #we add the two lowest probabilites to get the new node's probability 

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

def entropy(S):
        #We will use a summation of the logarithms of the probability distribution associated to S in order to obtain the entropy of S.
    H = 0 #H is the entropy of the source S, essesntially measuring the randomness of S.
          #Low entropy means the source is more predictable (0 entropy would mean the source is deterministic).
          #High entropy implies the source is unpredictable.  

    #Note that the source S contains the letter and its probability in a list/pair format, where s[1] is the prob.

    for s in S:
        H += s[1]*math.log(s[1],2)

    H = -H    

    return H    

def expected_length(node_list):
    #this will use the probability of each letter in the source and the length letter's corresponding Huffman encoding.
    #We use a summation to gain the expected length of the encoding, denoted E_f.
    #This can be thought of as the efficiency of the encoding of S.

    E_f = 0 #expected length
    for node in node_list:
        E_f += node.prob*int(len(node.encoding))

    print("Expected length of the Huffman encoding of S, E(l(f)) = {}".format(E_f))
    return    



init() #to run the algorithm 





