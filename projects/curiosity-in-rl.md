---
layout: page
title: "Curious Agents"
---
Deep reinforcement learning has proven to be a power general purpose framework that can be used to train agents to solve complicated tasks. However defining rewards for some tasks might not always be feasible, especially in large open-ended environment. Imagine if we could somehow allow our agents to first explore environments without external rewards. Then it could become more easy to fine-tune them to solve any downstream task we care about. In this series I investigate methods that can allow our agents to do just that! Enjoy!

### Curious Agents: An Introduction
In <a href="https://medium.com/@dries.epos/curious-agents-ebfee02ef024"  target="_blank">the</a> first blogpost I provide some background motivation for why this might be an interesting research direction to take one. This includes remarks from prominient researchers in the field.

### Curious Agents II: Solving MountainCar without Rewards
In <a href="https://medium.com/@dries.epos/curious-agents-ii-solving-mountaincar-without-rewards-c49ae2177819"  target="_blank">this</a> blogpost I train an agent to solve MountainCar. But it is done with a twist. I never provide the actual external rewards to the agent. It learns on its own by just taking in observation sequences. All code used in this series is also open source. So feel free to try it out yourself.
<div class="d-flex justify-content-center">
  <div class="col-md-6 d-flex justify-content-center align-items-center">
      <img src="{{ site.github.url }}/assets/img/mountain_car.gif" alt="Home" width="100%">
  </div>
</div>

### Curious Agents III: BYOL-Explore
<a href="https://medium.com/@dries.epos/curious-agents-iii-byol-explore-93f34fa6146a"  target="_blank">Next</a> we take a look at some more recent developments in the field. Specifically I implement a version BYOL-Explore, a recent development by DeepMind. I train it on a JAX based Maze environment and show that it can learn to solve randomly generated Mazes without ever being instructed to do so.

<div class="d-flex justify-content-center">
  <div class="col-md-6 d-flex justify-content-center align-items-center">
      <img src="{{ site.github.url }}/assets/img/maze.gif" alt="Home" width="100%">
  </div>
</div>

### Curious Agents IV: BYOL-Hindsight
The lastest blogpost can be found <a href="https://medium.com/@dries.epos/curious-agents-iv-byol-hindsight-318c559175f0"  target="_blank">here</a>. In this post I discuss an followup to BYOL-Explore called BYOL-Hindsight. BYOL-Hindsight addressed many of the shortcommings faced by previous curiosity-based algorithms. To test the algorithm I built a new JAX based 2D Minecraft environment. I then showed that the agent could sucessfully learn to perform multiple actions to build a diamond pickaxe purly out of curiosity. Enjoy the series!
<div class="d-flex justify-content-center">
  <div class="col-md-6 d-flex justify-content-center align-items-center">
      <img src="{{ site.github.url }}/assets/img/minecraft.gif" alt="Home" width="100%">
  </div>
</div>