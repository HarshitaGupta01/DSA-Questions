
# from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n=len(rooms)
        visited=[False]*n
        queue=deque([0])
        visited[0]=True
        while queue:
            node = queue.popleft()  # Get the next room to process
            for neighbor in rooms[node]:  # Explore keys in the current room
                if not visited[neighbor]:  # If the room is unvisited
                    visited[neighbor] = True  # Mark it as visited
                    queue.append(neighbor)  # Add it to the queue

        return all(visited)
