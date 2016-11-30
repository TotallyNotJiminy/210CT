class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
    def __init__(self):
      self.head=None
      self.tail=None
      
    def insert(self,n,x):
      #Not actually perfect: how do we prepend to an existing list?
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x              
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x
          
    def display(self):
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
      print("List: ",",".join(values))
      
    #you don't actually delete anything you just ignore it and go around it 
    def delete(self,dele):
        #checks from the head through the lsit
        n=self.head
        while n!=None:
            #checks if its the value you want to delete
            if n.value==dele:
                #if its not the end of the list
                if n.next==None:
                    #if its the end
                    n.prev.next=None
                    self.tail=n.prev
                
                elif n.prev==None:
                    self.head=n.next

                else:
                    n.prev.next=n.next
                    n.next.prev=n.prev
                print("Sucessfully Deleted!")
                break
            n=n.next
        
def main():
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.display()
    dele=int(input("What node do you want to delete: "))
    l.delete(dele)
    l.display()
    
if __name__ == '__main__':
  main()
     
