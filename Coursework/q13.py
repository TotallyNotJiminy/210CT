class Node():
    
    def __init__(self, value):
        self.value=value
        self.connected=[]

    def Connect(self, connected):
        self.connected.append(connected)
        
    def __str__(self):
        return "Name: {0} {1}".format(self.value,self.connected)
    
def addedge(graph,a,b):
    for each in graph:
        if each.value==a:
            each.connected.append(b)
            for each2 in graph:
                if each2.value==b:
                    each2.connected.append(a)
    return graph

def delnode():
    print("not don")


def deledge():
    print("not don")

def gengraph():
    graph=[Node("a"),Node("b"),Node("c"),Node("d"),Node("e")]
    addedge(graph,"a","c")
    addedge(graph,"c","d")
    return graph

def display(graph):
    for each in graph:
        print(each)

def addnode(graph):
    while 1:
        node=input("Enter the node name: ")
        Pass=True
        for each in graph:
            if each.value==node:
                Pass=False
        if not Pass:
            print("That's already a node")
        else:
            graph.append(Node(node))
            print("Node Added")
            break
                
    return graph
def main():
    graph=[]
    while 1:
        print("Graph Stuff")
        print()
        print("1. Add Edge")
        print("2. Delete Edge")
        print("3. Add Node")
        print("4. Delete Node")
        print("5. Display Nodes")
        print("6. Generate Test Graph")
        print("9. Quit")
        print()
        while 1:
            try:
                choice=int(input("Enter Choice: "))
                if choice in [1,2,3,4,5,6,7,9]:
                    break
                else:
                    print("That's not a valid input")
            except:
                print("That's not a number!")
        if choice==9:
            break
    
        if choice==1:
            addedge(a,b)

        elif choice==2:
            deledge()
            
        elif choice==3:
            addnode(graph)

        elif choice==4:
            delnode()
            
        elif choice==5:
            display(graph)
            
        elif choice==6:
            graph=gengraph()            
        print()
       
            
    
    
if __name__=="__main__":
    main()
