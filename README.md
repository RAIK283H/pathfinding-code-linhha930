# Pathfinding Starter Code
Customer Requirements:
- Players begin at the start node
- Players will navigate to the target node through a random path
- Players have to end at the end node
- The path has to be valid such that every two nodes are connected by an edge

My random pathing algorithm only requires the player to begin at start_node. The player will always end at exit_node, but they may visit exit_node before hitting the target. A player can visit all nodes as many times as the path allows, given that they end at the exit_node. The statistic I added was the speed that the player was traveling, which was pulled directly from player_object.py. 
