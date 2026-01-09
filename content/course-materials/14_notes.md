---
title: 14 - Classical Mechanics Thus Far
weight: 14
date: '2026-01-09'
math: true
---

[![Report Issues](https://img.shields.io/badge/report%20issues-GitHub-blue)](https://github.com/dannycab/phy321msu/issues) 
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Learning Goals

{{< admonition type="admonition" title="After studying Lesson 14, you should be able to:" class="note" >}}
* Synthesize the major conceptual frameworks of classical mechanics, including Newtonian, energy-based, and Lagrangian formulations.
* Identify the appropriate formulation of classical mechanics to apply to different types of physical systems based on their constraints and symmetries.
* Recognize how conservation laws emerge from symmetries and apply them to simplify problem solving.
* Distinguish between linear and nonlinear systems and understand the implications for analytical and numerical solution methods.
* Connect the mathematical formalism of classical mechanics to physical intuition about motion, energy, and stability.
{{< /admonition >}}

## Where We've Been: A Journey Through Classical Mechanics

Over the course of our study, we have developed a deep understanding of classical mechanics - the physics of large, slow, mechanical systems. We started with the fundamental question of what classical mechanics is and where it fits in the broader landscape of physics. We discovered that classical mechanics governs systems that are large enough that quantum effects are negligible and slow enough that relativistic effects don't matter.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Modernphysicsfields.svg/640px-Modernphysicsfields.svg.png" caption="Physics by size and speed showing that slower systems are classical, faster systems typically require relativity, and small systems are often quantized. [SVG File](https://upload.wikimedia.org/wikipedia/commons/5/56/Modernphysicsfields.svg)" >}}

But more importantly, we learned that classical mechanics is not just one thing. It's a rich tapestry of different formulations, each offering unique insights and tools for understanding the motion of physical systems. Let's review the major themes and frameworks we've developed.

### The Three Pillars of Our Classical Mechanics

Throughout our journey, we've encountered three major formulations of classical mechanics. Each has its strengths, and knowing when to use which approach is a key skill we've developed.

#### Newtonian Mechanics: Forces and Accelerations

We began with [Newton's Laws of Motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion), the foundation upon which all of classical mechanics rests. Newton's Second Law provided us with the fundamental relationship:

$$\vec{F}_{net} = m\vec{a}$$

or more generally,

$$\vec{F}_{net} = \frac{d\vec{p}}{dt}$$

This vector formulation allowed us to analyze forces and their effects on motion. We learned to draw free body diagrams, decompose forces into components, and set up the differential equations that govern motion. We applied this framework to problems ranging from blocks on inclined planes to falling objects with air resistance.

{{< admonition type="tip" >}}
**Strengths of the Newtonian approach:**
- Direct physical intuition about forces and motion
- Natural for problems with explicitly known forces
- Vector formulation makes direction of motion clear

**Limitations:**
- Can be cumbersome for systems with constraints
- Requires careful attention to coordinate systems
- Forces of constraint must be explicitly calculated
{{< /admonition >}}

#### Energy Methods: Conservation and Work

We discovered that there's another way to think about mechanics - through the lens of energy. The principle of energy conservation states that for an isolated system:

$$\frac{dE}{dt} = 0$$

or more simply,

$$E_{before} = E_{after}$$

We learned about different forms of energy - kinetic energy $T = \frac{1}{2}mv^2$, potential energy $V$, and internal energy. We discovered the Work-Energy Theorem:

$$\Delta T = W_{net}$$

and learned to identify conservative forces for which we can define potential energy functions through:

$$\vec{F} = -\nabla V$$

The energy formulation gave us powerful tools for analyzing motion without having to track all the details of forces at every instant.

{{< admonition type="tip" >}}
**Strengths of energy methods:**
- Scalar quantities are often easier to work with than vectors
- Conservation laws provide powerful constraints
- Natural for analyzing before/after states
- Works well with conservative forces

**Limitations:**
- Doesn't directly give equations of motion
- Requires identifying all forms of energy
- Can miss directional information
{{< /admonition >}}

#### Lagrangian Mechanics: Symmetries and Generalized Coordinates

Finally, we encountered the most elegant and general formulation: Lagrangian mechanics. We learned to construct the Lagrangian:

$$\mathcal{L} = T - V$$

and apply the Euler-Lagrange equation:

$$\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) - \frac{\partial \mathcal{L}}{\partial q_i} = 0$$

This formulation introduced us to generalized coordinates, which allowed us to choose coordinates that naturally fit the problem's constraints and symmetries. We discovered that cyclic coordinates correspond to conserved quantities through Noether's theorem, and we learned to work with generalized forces and generalized momenta.

{{< admonition type="tip" >}}
**Strengths of Lagrangian mechanics:**
- Freedom to choose any convenient coordinates
- Constraints can be incorporated directly
- Symmetries reveal conserved quantities
- Single systematic procedure for any system
- Extends naturally to more advanced physics

**Limitations:**
- Can seem abstract compared to forces
- Requires identifying appropriate coordinates
- May produce complex equations for simple problems
{{< /admonition >}}

### Conservation Laws: The Deep Structure of Physics

One of the most profound insights we gained is that conservation laws are not just convenient calculation tools - they reflect deep symmetries in nature. We studied three fundamental conservation laws:

#### Conservation of Energy
Energy is conserved when the system has no explicit time dependence. For a closed system:

$$E_{total} = T + V = \text{constant}$$

We learned that while we cannot always say precisely what energy "is," we can always calculate it, and we can trust that it remains constant in isolated systems.

#### Conservation of Linear Momentum

Linear momentum is conserved when there are no external forces. For a system of particles:

$$\vec{p}_{sys} = \sum_{i} m_i\vec{v}_i = \text{constant}$$

We discovered that internal forces always cancel in pairs by Newton's Third Law, so only external forces change the total momentum of a system.

#### Conservation of Angular Momentum

Angular momentum is conserved when there is no net external torque:

$$\vec{L} = \vec{r} \times \vec{p} = \text{constant}$$

This conservation law is particularly powerful for systems with rotational symmetry, where certain coordinates are cyclic.

{{< admonition type="admonition" title="Noether's Theorem and The Symmetries of Reality  (13 minute video)" class="tip" >}}
One of the most beautiful results in physics is [Noether's theorem](https://en.wikipedia.org/wiki/Noether%27s_theorem), which tells us that every continuous symmetry corresponds to a conservation law. Time translation symmetry gives conservation of energy, spatial translation symmetry gives conservation of momentum, and rotational symmetry gives conservation of angular momentum.

This video provides an accessible introduction to this profound connection:

> Some YouTube videos are unable to be embedded in Jupyter Books. Click the image below to watch the video on YouTube.

{{< youtube 04ERSb06dOg >}}

- *Source: <https://www.youtube.com/watch?v=04ERSb06dOg>*
{{< /admonition >}}

### The Oscillator: A Central Character in Our Story

Throughout our journey, one system appeared again and again: the harmonic oscillator. We studied it in many contexts because it represents a universal behavior - whenever a system is displaced slightly from stable equilibrium, it tends to oscillate.

#### The Simple Harmonic Oscillator

We started with the ideal spring-mass system governed by Hooke's Law:

$$F = -kx$$

This led to the differential equation:

$$\ddot{x} + \omega_0^2 x = 0$$

where $\omega_0 = \sqrt{k/m}$ is the natural frequency. The solution is sinusoidal motion:

$$x(t) = A\cos(\omega_0 t + \phi)$$

We learned that the energy sloshes back and forth between kinetic and potential:

$$E = \frac{1}{2}kA^2 = \frac{1}{2}mv^2 + \frac{1}{2}kx^2$$

#### Damped Oscillations

Real systems experience damping. We studied how damping affects oscillations:

$$\ddot{x} + 2\beta\dot{x} + \omega_0^2 x = 0$$

We discovered three regimes:
- **Underdamped** ($\beta < \omega_0$): Oscillations that decay exponentially
- **Critically damped** ($\beta = \omega_0$): Fastest return to equilibrium without oscillating
- **Overdamped** ($\beta > \omega_0$): Slow exponential decay to equilibrium

#### Driven Oscillations and Resonance

When we drive an oscillator with an external periodic force, we found:

$$\ddot{x} + 2\beta\dot{x} + \omega_0^2 x = \frac{F_0}{m}\cos(\omega_D t)$$

The steady-state response exhibits resonance - the amplitude peaks when the driving frequency matches the natural frequency. We learned about the importance of the quality factor $Q$ and how resonance appears everywhere in nature, from musical instruments to bridges to quantum systems.

#### Nonlinear Oscillators

The simple harmonic oscillator is an idealization. Real systems often exhibit nonlinear behavior. We explored how nonlinearities can lead to complex dynamics, including amplitude-dependent frequencies and even chaotic motion in certain regimes. We discussed examples such as the pendulum at large angles and systems with nonlinear restoring forces including familiar systems like the [Duffing oscillator](https://en.wikipedia.org/wiki/Duffing_equation).

{{< admonition type="admonition" title="Resonance in the Real World (8 minute video)" class="tip" >}}
Resonance is not just a mathematical curiosity - it's everywhere in the physical world around us. From the Tacoma Narrows Bridge collapse to how we tune radio stations, resonance plays a crucial role.


> Some YouTube videos are unable to be embedded in Jupyter Books. Click the image below to watch the video on YouTube.

[![Shattering a wine glass](https://i3.ytimg.com/vi/17tqXgvCN0E/hqdefault.jpg)](https://www.youtube.com/watch?v=17tqXgvCN0E)

- *Source: <https://www.youtube.com/watch?v=17tqXgvCN0E>*
{{< /admonition >}}

## The Power of Multiple Perspectives

Perhaps the most important lesson from our study of classical mechanics is that there are multiple valid ways to understand the same physics. Newton's force-based approach, energy methods, and Lagrangian mechanics all describe the same reality - they just offer different perspectives.

### Complementary Views

Each formulation highlights different aspects:
- **Newtonian**: Emphasizes causality and forces
- **Energy**: Emphasizes conservation and transformations
- **Lagrangian**: Emphasizes symmetry and geometry

Being fluent in all three makes you a more capable physicist. You can choose the perspective that makes each problem clearest.

### A Model for Scientific Thinking

This multiplicity of perspectives is characteristic of deep scientific understanding. The same phenomenon can be understood from multiple angles, each valid and each offering unique insights. This is true not just in mechanics but throughout science.

As you continue in physics and science more broadly, remember this lesson: seek multiple perspectives, understand their relationships, and choose the view that serves your purpose best.

## Final Thoughts: The Unity of Classical Mechanics

We began by asking "What is classical mechanics?" We've learned that it's the physics of large, slow, mechanical systems. But more than that, it's a remarkably unified framework for understanding motion, energy, and dynamics.

The journey from Newton's Second Law to the Principle of Least Action represents not just historical development but increasing abstraction and generality. Each new formulation doesn't replace the previous one - it complements and extends it.

### What We Can Now Do

With the tools and insights we've developed, we can:
- Analyze the motion of complex mechanical systems
- Identify and exploit conservation laws
- Understand stability and oscillations
- Recognize and analyze nonlinear and chaotic behavior
- Use computational methods to explore realistic systems
- Connect mathematical formalism to physical intuition
- Choose the right approach for different types of problems

### The Continuing Journey

Classical mechanics is both an endpoint and a beginning. It's a complete and beautiful theory in its own right. But it's also the foundation for everything that follows in physics. The mathematical tools, physical intuition, and problem-solving approaches we've developed will serve us throughout our study of physics.

As we move forward, we carry with us not just equations and methods, but a way of thinking about the physical world - looking for symmetries, seeking conserved quantities, appreciating the interplay of forces and motion, and understanding that beneath the apparent complexity of nature lie elegant and universal principles.

Classical mechanics has been the physics of the cosmos for centuries. While quantum mechanics and relativity extended our reach to the very small and very fast, classical mechanics remains the language we use to describe most of the motion we observe in our everyday world. It is, in the words of Richard Feynman, "the most precise and most tested physical theory we have."

We've come far in our understanding, but the journey continues. The frameworks we've built here will support us as we explore new domains of physics, and the habits of mind we've developed will serve us throughout our scientific careers.


