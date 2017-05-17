# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                #converts everything into int and puts into a list
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                traversedSet = []
                while True:
                        if(traversedSet.count(self.parent.index(-1))<=self.parent.count(self.parent.index(-1))):
                                vertex = self.parent.index(-1)
                        else:
                                return maxHeight

                        while((vertex in self.parent) and (traversedSet.count(vertex)<=self.parent.count(vertex))):
                                height += 1
                                traversedSet.append(vertex)
                                vertex = self.parent.index(vertex)
                        traversedSet.append(vertex)
                        maxHeight = max(height, maxHeight)
                        height = 0

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
