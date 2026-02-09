class node:
    def_init_(self,val):
        self._data=val
        self._left=None
        self._right=None
    def compare(self,val):
        if self._data>val:
            self._left=insert(self._left,val)
        else:
            self._right=insert(self._right,val)

        def inorder(self):
            if self._left:
                self._left.inoreder()
            print(self._data,end=' ')
            if self._right:
                  self._right.inorder()
                def printtree(self):
                    print("Inorder traversal:")
                    self.inorder()
                    print()




        def insert(root,val):
            if root is None:
                root = node(val)
            else:
                root.compare(val)


            return root


        a=[8,4,1,7,3,9,6,2,5]

        root=None
        for i in a:
            root=insert(root,i)
        root.printtree()
                    
            
