---
title: How to play Clash of Tanks
feature_text: If you haven't played before
feature_image: "https://picsum.photos/1300/400?image=989"
---

While the overall objective of the game is relatively simple, our game works a bit differently from the original implementation.

### The Players
We designed our game to be two-player, just like the original. Player One is the tank on the left side and uses the standard **WASD** layout to move up, left, down and right respectively. Player One's tank uses the **E** button to shoot. Player Two is therefore the tank on the right side and uses **IJKL** to move around, with **O** being the button to shoot.

### The Aim
The aim of the game is to destroy the opposing tank by shooting it with a projectile. When a projectile is shot, it will move in that direction for a few seconds before either:
    - Colliding with an obstacle which it will bounce off at a random angle
    - Despawning (after a set time has passed with no collisions)
    - Hitting another tank


When one tank successfully shoots the other, the map will change to a randomly generated one with new obstacles and the starting positions will be reset. The player who destroyed the tank will receive one point.


To win the game, you need to reach 10 points against the other player. There is no time limit!