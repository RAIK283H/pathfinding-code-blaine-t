# Pathfinding Starter Code

## Customer Requirements

- i. The player should be able to return to the start
- ii. The player should be able to visit the exit before hitting the target
- iii. The player should be ble to wander back and forth between nodes
- iv. Eliminating the ability for the player to do the above things would avoid long loops but theoretically if there is a target and an exit that are both connected to the start there is a solution and thus there isn't an infinite loop. There might be a very large path generated but it will still resolve eventually.

## My algorithm

My algorithm does "true random" it will continue going to nodes, getting the neighbors, and going to a random neighbor until it falls upon the target and then finally the exit.

## Statistic

The statistic I added to the scoreboard was `Nodes Visited`. It lists the amount of nodes the current player has visited. It dynamically updates when the player goes to a new node.
