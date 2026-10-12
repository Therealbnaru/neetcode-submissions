class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:  # if the original list is empty
            return None

        curr = head  # starts at the head of the original list
        listNodes = []  # stores every original node

        while curr is not None:  # go through the original list
            listNodes.append(curr)  # save the current original node
            curr = curr.next  # move to the next node

        nodesRDict = {}  # maps each original node to its copied node

        for x in listNodes:  # create a copy of every original node
            newNode = Node(x.val)  # create a new node with the same value
            nodesRDict[x] = newNode  # original node -> copied node

        for x in listNodes:  # connect all of the copied nodes
            newNode = nodesRDict[x]  # get the copy of the current original node

            if x.next is not None:  # if original node has a next node
                newNode.next = nodesRDict[x.next]  # point to the COPY of its next node

            if x.random is not None:  # if original node has a random node
                newNode.random = nodesRDict[x.random]  # point to the COPY of its random node

        return nodesRDict[head]  # return the copy of the original head