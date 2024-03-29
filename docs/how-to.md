---
title: How to play Clash of Tanks
feature_image: "https://spectrum.ieee.org/media-library/atari-console.jpg?id=28145520&width=1200&height=900"
---

While the overall objective of the game is relatively simple, our game works a bit differently from the original implementation.

<style>
img, video {
  border: 1px solid black;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
![](https://pbs.twimg.com/media/C5MakjBWAAI0bgJ.jpg:large)

### The Players
We designed our game to be two-player, just like the original. Player One is the tank on the left side and uses the standard **WASD** layout to move up, left, down and right respectively. Player One's tank uses the **E** button to shoot. Player Two is therefore the tank on the right side and uses **IJKL** to move around, with **O** being the button to shoot.

### The Goal
The goal of this game is to destroy the opposing tank by shooting it with a projectile. When a projectile is shot, it will move in that direction for a few seconds before either:
  * Colliding with an obstacle which it will bounce off at a random angle
  * Despawning (after a set time has passed with no collisions)
  * Hitting another tank


When one tank successfully shoots the other, the map will change to a randomly generated one with new obstacles and the starting positions will be reset. The player who destroyed the tank will receive one point.


To win the game, you need to reach 10 points against the other player. There is no time limit!

![](assets/kills.gif)