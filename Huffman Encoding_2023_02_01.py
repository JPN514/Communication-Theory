#Huffman encoding algorithm
#Used to create an optimal prefix free encoding of a given random source S
#The random source S={s_1,s_2,...,s_m} has probability distribution P=(p_1,p_2,...,p_m) where p_i is the probability of s_i
#We use binary tree to obtain these codewords.


class Node():
    #self.data will contain the s_i
    #prob is the corresponding p_i
    def __init__(self, data,prob):
        self.left = None
        self.right = None
        self.data = data
        self.prob = prob
        return



      
 

class TREE():
    #Class which will contain the methods for the Huffman encoding which generates a binary tree        

    def __init__(self):
        self.L = self.generate_nodes() #list of letters and probabilities
        self.Tree_method_part1()

        return

    def generate_nodes(self):
        #will take the source and create L, the list of nodes although not as node class instance yet
        L = []

        source = get_source()

        for s in source:
            L.append(s)
            print(s)  

        return L

    def Tree_method_part1(self):
        #First part of Huffman algorithm to generate tree
        #gets the list of nodes which is s_i and p_i pairs 
        self.T = []
        
        while len(self.L) >= 2:
            v_i1 , v_i2 = self.lowest_probs()
            self.new_vertex(v_i1,v_i2)

        print(self.L)
        print(self.T)
        


        return    

    def Huffman_concatenation_part2(self):
        #Second part of Huffman algorithm to generate the Huffman codes using tree traversal

        return    


    def lowest_probs(self):
        #method to find the two nodes in L with the lowest probabilities v_i1,v_i2
        v_i1, v_i2 = sorted(self.L, key = lambda x: x[1])[:2]
        print(v_i1,v_i2)


        return v_i1,v_i2

    def new_vertex(self,v_i1,v_i2):
        #this creates a new vertex from the two with lowest probabilities 
        #will also use this to create edges in the tree

        v_i1_i2 = []
        v_i1_i2.append(v_i1[0] + "," + v_i2[0]) #this creates a label to tell us which nodes created the new node
        v_i1_i2.append(v_i1[1]+v_i2[1]) #we add the two lowest probabilites to get the new node's probability 

        #create the nodes and append to the tree T
        new_node = Node(v_i1_i2[0],v_i1_i2[1])
        left = Node(v_i1[0],v_i1[1])
        right = Node(v_i2[0],v_i2[1])
        self.T.append(left)
        self.T.append(right)
        self.T.append(new_node)
        new_node.left = left
        new_node.right = right

        #Alter the list to include new node with probability and remove old nodes
        self.L.append(v_i1_i2)
        self.L.remove(v_i1)
        self.L.remove(v_i2)


        return 
            






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


tree = TREE()
del tree




