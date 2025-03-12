# from collections import defaultdict, deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        dict=defaultdict(list)
        n=len(edges)
        for i in range(0,n):
            u=edges[i][0]
            v=edges[i][1]
            dict[u].append(v)
            dict[v].append(u)
        queue=deque([(source)])
        visit={source}
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for ngh in dict[node]:
                if ngh not in visit:
                    visit.add(ngh)
                    queue.append(ngh)
        return False
        