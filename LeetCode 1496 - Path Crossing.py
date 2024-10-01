"""     https://leetcode.com/problems/path-crossing/solutions/5855661/python-beats-95/     """


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
        'N': [0, 1],    # North increases y
        'S': [0, -1],   # South decreases y
        'E': [1, 0],    # East increases x
        'W': [-1, 0]    # West decreases x 
        }
        count = set()  # Initialize the set to store visited positions
        x, y = 0, 0    # Starting at origin (0, 0)

        for i in path:
            count.add((x, y))  # Add the current position to the set
            temp_x, temp_y = dir[i]  # Get the direction deltas
            x, y = x + temp_x, y + temp_y  # Move to the new position

            if (x, y) in count:  # If the new position is already visited, path crosses
                return True

        return False  # If no crossing, return False
