from collections import defaultdict
from AlgoTree.flat_forest_node import FlatForestNode
from AlgoTree.pretty_tree import pretty_tree



'''
Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which:
*form a tree that includes every vertex.
*has the minimum sum of weights among all the trees that can be formed from the graph.


The steps for implementing Kruskal's algorithm are as follows:

1.Sort all the edges from low weight to high.
2.Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
3.Keep adding edges until we reach all vertices.

Kruskal Algorithm Pseudocode
Any minimum spanning tree algorithm revolves around checking if adding an edge creates a loop or not.
The most common way to find this out is an algorithm called Union FInd. The Union-Find algorithm divides the vertices into clusters and allows us to check if two vertices belong to the same cluster or not and hence decide whether adding an edge creates a cycle.

KRUSKAL(G):
A = ∅
For each vertex v ∈ G.V:
    MAKE-SET(v)
For each edge (u, v) ∈ G.E ordered by increasing order by weight(u, v):
    if FIND-SET(u) ≠ FIND-SET(v):       
    A = A ∪ {(u, v)}
    UNION(u, v)
return A
'''
# Kruskal's algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()




'''
Output:
1 - 2: 2
2 - 5: 2
2 - 3: 3
3 - 4: 3
0 - 1: 4

Kruskal's Algorithm Complexity
The time complexity Of Kruskal's Algorithm is: O(E log E).
The space complexity Of Kruskal's Algorithm is: O(|E|+|V|).
'''


#################################################################################

"""

A binary search or half-interval search algorithm finds the position of a target value within a sorted array.
The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and executes in logarithmic time.

Algorithm

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element.
Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

"""


def binary_search(item_list,item):      #function to perform binary search
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):      
		mid = (first + last)//2
		if item_list[mid] == item :     #means Item is present at mid
			found = True
		else:
			if item < item_list[mid]:  #If Item smaller, ignore right half
				last = mid - 1
			else:
				first = mid + 1	    #If Item is greater, ignore left half
	return found                        #It will return If found is true or false

a=[]                                         #initialising the array

#################################################################################

'''
PROBLEM STATEMENT:
Given a binary tree with its root node and two nodes, a and b, present in
the tree. The task is to find the lowest common ancestor of a and b.
The input is in preorder and -1 denotes a null value.
For example:
Input: 3 4 -1 6 -1 -1 5 1 -1 -1 -1
let a = 1, b = 6
The above input will have the following structure:
    3
   / \
  4   5
  \   /
   6  1
Output: 3, as 3 is the lowest common ancestor of 1 and 6
'''


# A class to create a node
class Node:
    # Constructor to initialize node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# A function to builfd the tree in preorder form
def BuildTree():
    d = int(input())
    if d == -1:
        return None
    root = Node(d)
    root.left = BuildTree()
    root.right = BuildTree()
    return root


# A function to find lowest common ancestor of the two entered nodes
def LCA(root, a, b):
    # base case
    if root is None:
        return None
    if root.data == a or root.data == b:
        return root
    # Recursive calls
    leftans = LCA(root.left, a, b)
    rightans = LCA(root.right, a, b)
    if leftans is not None and rightans is not None:
        return root
    elif leftans is not None:
        return leftans
    else:
        return rightans


print("Enter values in a binary tree:")
# A function call to build the tree and return root node
root = BuildTree()
print("Enter a and b:")
# Assuming a and b are present in the tree
a = int(input())
b = int(input())
# CA stores the lowest common ancestor of a and b
CA = LCA(root, a, b)
print("LCA of", a, "and", b, "is", CA.data)


'''
TEST CASES:
1.
Input:
Enter values in a binary tree:
3
4
-1
6
-1
-1
5
1
-1
-1
-1
Enter a and b:
3
6
Output: LCA of 3 and 6 is 3

2.
Input:
Enter values in a binary tree:
2
4
6
-1
7
-1
-1
3
-1
-1
5
-1
-1
Enter a and b:
5
7
Output: LCA of 5 and 7 is 2

TIME COMPLEXITY: O(n), due to a single traversal of the tree
where, 'n' denotes the number of nodes in the tree.
SPACE COMPLEXITY: O(1), no extra space used.
'''