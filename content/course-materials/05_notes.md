---
title: 05 - Conservation Laws Govern and Constrain our Physics
weight: 5
date: '2026-01-08'
math: true
---

[![Report Issues](https://img.shields.io/badge/report%20issues-GitHub-blue)](https://github.com/dannycab/phy321msu/issues) 
[![GitHub Issues](https://img.shields.io/github/issues/dannycab/phy321msu)](https://github.com/dannycab/phy321msu/issues)

## Learning Goals

{{< admonition type="admonition" title="After studying Lesson 05, you should be able to:" class="note" >}}
* Predict the conditions under which the total energy of a system remains constant using the principle of energy conservation.
* Differentiate between various forms of energy (e.g., kinetic, potential, internal) and describe their transformations within a system.
* Analyze the role of energy conservation in systems with external forces and quantify energy changes throughout a process.
* Apply the concept of a point particle to simplify energy calculations and understand its limitations in modeling real-world systems.
* Predict the conditions under which the total linear and angular momentum of a system remain constant using conservation laws.
* Derive and apply the discrete update equations for linear and angular momentum in systems with external forces.
{{< /admonition >}}

We started with Newton's Laws of Motion because they provide a framework for us to develop the equations of motion. However, there is a broader framework that can help us understand and organize our knowledge of physics. These are [conservation laws](https://en.wikipedia.org/wiki/Conservation_law).

Conservation laws are principles that state that certain properties of a system remain constant over time. These properties are called conserved quantities. In classical mechanics, there are three main conservation laws:

1. **Conservation of Energy**: The total energy of an isolated system remains constant over time.
2. **Conservation of Momentum**: The total momentum of an isolated system remains constant over time.
3. **Conservation of Angular Momentum**: The total angular momentum of an isolated system remains constant over time.

We will discuss them briefly below, before we dive into the details of conservation of energy. The concept of energy is so important and complimentary to our understanding of motion that we will focus on it before returning to momentum and angular momentum.

## What is Energy?

[Energy](https://en.wikipedia.org/wiki/Energy) is a central concept of science. It is also a very challenging conceptual idea. Physicists are known to say things like, 

> *"I can't tell you what energy is, but I can tell you how to calculate it."*

Richard Feynman is known to have had a disdain for the wildly different units of energy that we use in physics.

### Feynman on the units of energy (2 minute video)

{{< youtube roX2NXDUTsM >}}

Feynman is quoted as saying: 
> *"It is important to realize that in physics today, we have no knowledge of what energy is."*

Energy is a number, a quantity, that when we compute it, we find it stays the same before and after a process - so long as we account for all the interactions and uses in that case. 

Conservation of energy states that there is not temporal change in the total energy of a system. This is a very powerful idea, but it is not always easy to apply.

$$\dfrac{dE}{dt} = 0$$

If this equation holds between any two states of a system, we say that energy is conserved. A simpler statement is thus,

$$E_{before} = E_{after}$$

## Energy is a challenging concept

To frame how interesting and complex energy can be, consider this video from Veritasium:

### How do we get light from a circuit when we close a switch? (14 minute video)

{{< youtube bHIhgxav9LY >}}

There a many potential forms of energy and lots of processes that convert energy from one form to another. Below is a table of some common forms in physics. In addition, we have listed subsets of these forms that are often useful to distinguish. We will do analyses that include most of these forms.

| **Main Form of Energy** | **Narrower Distinction** | **Description**                                     |
|---------------------|----------------------|-------------------------------------------------|
|   Kinetic Energy    |                      | Energy of macroscopic motion                    |
|                     | Translational        | Energy due to point particle translation        |
|                     | Rotational           | Energy due to rotation                          |
|                     | Vibrational          | Energy due to vibration                         |
|   Potential Energy  |                      | Energy due to position                          |
|                     | Gravitational        | Energy due to position in a gravitational field |
|                     | Elastic              | Energy due to deformation of an elastic object  |
|                     | Electric             | Energy due to position in an electric field     |
|   Internal Energy   |                      | Energy due to microscopic motion                |


## The Point Particle

Critical to the understanding of energy is that it is a property of a system. A system can consist of a single object or be made of many different objects. In the case of modeling the motion of a single object, we often introduce the concept of a [point mass](https://en.wikipedia.org/wiki/Point_mass) or [point particle](https://en.wikipedia.org/wiki/Point_particle). A point mass is an idealized object that has mass but no size or shape. It has no internal structure and thus no internal energy. It is a useful abstraction for modeling the motion of objects in classical mechanics.

### Point Particle and Real Models (6 minute video)

The video below is from an introductory physics course at Georgia Tech. It covers the important aspects of a point particle and how we miss some of the details when we focus exclusively on the point particle model.

{{< youtube fbiNKrqVajM >}}

*Click the image above to watch the video on YouTube (6 minutes)* <https://www.youtube.com/watch?v=fbiNKrqVajM>

### Kinetic Energy of a Point Mass

In that case of a point particle, we often focus on the kinetic energy of the object. The classical kinetic energy of a point mass is given by the equation:

$$K = \frac{1}{2}mv^2$$

where $m$ is the mass of the object and $v$ is its velocity. The kinetic energy of a point mass is a scalar quantity, which as we will learn is much easier to work with than a vector quantity. 

However, we can loose some information by moving to an energy-only framework; we typically focus on the behavior before and after a process and not the details of the process itself when using energy conservation. 

### Work 

Work is a concept closely related to energy, it describes the transfer of energy from one system to another. Our definition of work is macroscopic and thus will not related to temperature. Increases in temperature are related to internal energy, and thus the micrscopic motion of the particles in a system. As we consider a point particle moving from one location to another under a given force, we can define the work done by that force as:

$$W = \int_{x_i}^{x_f} F(x) dx$$

where $F(x)$ is the one-dimensional force acting on the particle between locations $x_i$ and $x_f$. More generally, if there is a position dependent force, we can write the work done by that force as:

$$W = \int_{C} \vec{F} \cdot d\vec{l}$$

where $C$ is the path taken by the particle and $d\vec{l}$ is a differential displacement vector along that path. 

### Work-Energy Theorem

The work-energy theorem show the relationship between work and the change in kinetic energy of a point mass. The work done on a point mass is equal to the change in its kinetic energy:

$$W = \Delta K = K_f - K_i$$

## Conservation of Momentum and Angular Momentum

[Linear Momentum](https://en.wikipedia.org/wiki/Momentum) is a vector quantity that describes the motion of an object. It is defined as the product of an object's mass and its velocity:

$$\vec{p} = m\vec{v}$$

[Angular Momentum](https://en.wikipedia.org/wiki/Angular_momentum) is a vector quantity that describes the rotational motion of an object. It is defined as the cross product of the position vector and the momentum vector:

$$\vec{L} = \vec{r} \times \vec{p}$$

These two other conservation laws are vector conservation laws. That is, they hold in each direction. Much like the definition of conservation of energy, we can start with the time derivatives of both momentum and angular momentum.

$$\dfrac{d\vec{p}}{dt} = 0$$

$$\dfrac{d\vec{L}}{dt} = 0$$

As before, we can take small steps in time and write the change in momentum and angular momentum as:

$$\Delta \vec{p} = 0 $$

$$\Delta \vec{L} = 0$$

And thus, we see that each component is conserved. For momentum,

$$\langle \Delta p_x, \Delta p_y, \Delta p_z \rangle = 0$$

$$\Delta p_x = 0 \qquad \Delta p_y = 0 \qquad \Delta p_z = 0$$

$$p_{x,i} = p_{x,f} \qquad p_{y,i} = p_{y,f} \qquad p_{z,i} = p_{z,f}$$

If the linear momentum is conserved in each direction, then the total linear momentum is conserved. The linear momentum will be the same before and after a process. For angular momentum, we find,

$$\langle \Delta L_x, \Delta L_y, \Delta L_z \rangle = 0$$

$$\Delta L_x = 0 \qquad \Delta L_y = 0 \qquad \Delta L_z = 0$$

$$L_{x,i} = L_{x,f} \qquad L_{y,i} = L_{y,f} \qquad L_{z,i} = L_{z,f}$$

If the angular momentum is conserved in each direction, then the total angular momentum is conserved. The angular momentum will be the same before and after a process.

After we get a handle on energy, we will return to momentum and angular momentum.

## Conservation of Energy

One expression of a conservation law is the [conservation of energy](https://en.wikipedia.org/wiki/Conservation_of_energy). For an isolated and closed system, the total energy is conserved. That is, before and after any process, we can account for all the energy in the system and it is the same. More generally, conservation of energy accounts for the energy "lost" to the surroundings. All of the changes to the system must be accounted for in changes the surroundings. 

For a given choice of system that interacts with its surroundings, the change in energy of the system is equal to the work done on the system and any heat exchanged with the surroundings. This is a statement of the [first law of thermodynamics](https://en.wikipedia.org/wiki/First_law_of_thermodynamics). We can write that statement mathematically as:

$$\Delta E_{\text{system}} = W + Q$$


where $\Delta E_{\text{system}}$ is the change in energy of the system, $W$ is the work done on the system, and $Q$ is the heat exchanged with the surroundings.

{{< admonition type="admonition" title="Sign conventions" class="warning" >}}
Note that the signs of the work done and heat exchanged are important. But we can remember them by asking if the system is going to increase its energy. 

If we add energy into the system by heating it, then $Q$ is positive because $\Delta E_{\text{system}}$ is positive. If the remove energy from the system through an exchange of heat, then $Q$ is negative.

If the system does work on the surroundings, for example, by exerting a force on an external object over some displacement, then $W$ is negative because $\Delta E_{\text{system}}$ is negative. If instead the surroundings do work on the system, then $W$ is positive.
{{< /admonition >}}

We can rewrite this energy equation as an update equation for the energy of the system:

$$E_{\text{system,f}} = E_{\text{system,i}} + W + Q$$

From this equation, we can see that the final state of the system's energy is determined by the sum of its initial energy, the work done on the system, and the heat exchanged with the surroundings.

### The Work-Energy Theorem

We often model a system as a single object that interacts with its surroundings. In this case, it's often beneficial to select the object alone to be the system of interest. Then all of our work is to explain and predict the dynamics of the object.

This simplification allows us to employ a more specialized case of the general energy equation. We can write the work-energy theorem as:

$$\Delta E_{\text{object}} = W_{\text{net}}$$
where $\Delta E_{\text{object}}$ is the change in energy of the object and $W_{\text{net}}$ is the net work done on the object.

More specifically, we often focus only on the changes to the object's motion. This is because we use often use the model of a [point particle](https://en.wikipedia.org/wiki/Point_particle) to describe the object. In this case, the object has no internal structure and thus no internal energy. The only energy we need to consider is the object's kinetic energy, $K$. 

{{< admonition type="admonition" title="Limitation of this model" >}}
The point particle model where we focus on the kinetic energy of an object is an obvious simplification. But it might not be so obvious how quickly it is to break down.

Consider pushing a block across the floor. The block is a point particle and we model it as such. It comes to a stop and we argue the block's kinetic energy was converted to heat in the floor. 

But what about the block itself? Would it's surface temperature increase? It does, but we don't account for it.

A great account of these kinds of situations is from my colleague [Bruce Sherwood](https:/brucesherwood.net/).  Bruce's paper, [*Pseudowork and real work*, American Journal of Physics (1982)](https://pubs.aip.org/aapt/ajp/article-abstract/51/7/597/1052185/Pseudowork-and-real-work?redirectedFrom=fulltext), is an important read about the limitation of the point particle model. You can find a PDF copy [here](https://brucesherwood.net/wp-content/uploads/2017/06/Pseudowork1983.pdf).
{{< /admonition >}}

#### Kinetic Energy

Our model of [kinetic energy](https://en.wikipedia.org/wiki/Kinetic_energy) stems from a [series of experiments dropping stones into clay](https://en.wikipedia.org/wiki/Willem_%27s_Gravesande). The depth of the hole made was proportional to the square of the impact speed.

Through many additional experiments we have quantified the kinetic energy of a point particle as:

$$K = \frac{1}{2}m\vec{v}\cdot\vec{v}.$$

We also use $T$ to represent kinetic energy, so you might see it written as:

$$T = \frac{1}{2}mv^2.$$

Note that this description of the kinetic energy is fully classical. It is the energy of motion in the limit that object moves much slower than the speed of light. We learned from [Einstein's special theory of relativity](https://en.wikipedia.org/wiki/Special_theory_of_relativity) that the total energy of an point particle is:

$$E_{tot} = \gamma mc^2,$$

where $\gamma$ is the [Lorentz factor](https://en.wikipedia.org/wiki/Lorentz_factor) and $c$ is the speed of light. The Lorentz factor is defined as:

$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}.$$

Notice that if $v/c =0$ then,

$$\gamma = 1 \longrightarrow E_{tot} = mc^2.$$

We call this the "rest energy" of the object. It is the energy of the object when it is not moving, and it demonstrates the [mass-energy equivalence](https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence).

$$E_{rest} = mc^2.$$

The remaining energy of the object is the kinetic energy, $T$. We can write that as:

$$T = E_{tot} - E_{rest} = (\gamma - 1)mc^2.$$

We can take the limit that $v/c \ll 1$ and expand the Lorentz factor in a Taylor series to find that:

$$\gamma = 1 + \frac{1}{2}\frac{v^2}{c^2} + \ldots.$$

Then we find that the kinetic energy is:

$$T = \left(1 + \frac{1}{2}\frac{v^2}{c^2} + \ldots - 1\right)mc^2 = \frac{1}{2}mv^2 + \ldots.$$

We have recovered the classical expression for kinetic energy. The higher order terms in the expansion are negligible when $v/c \ll 1$.

### Developing the Work-Energy Theorem

Let's start with our definition of the classical kinetic energy of a point particle:

$$T = \frac{1}{2}m\vec{v}\cdot\vec{v}.$$

We ask how does $T$ change with time? We take the time derivative of $T$:

$$\dfrac{dT}{dt} = \frac{1}{2}m\frac{d}{dt}\left(\vec{v}\cdot\vec{v}\right) = \frac{1}{2}m\left(\frac{d\vec{v}}{dt}\cdot\vec{v} + \vec{v}\cdot\frac{d\vec{v}}{dt}\right).$$

The last term can be combined because the dot product is commutative. We can factor out the $m/2$ and write:

$$\dfrac{dT}{dt} = \dfrac{m}{2}\left(2 \dfrac{d\vec{v}}{dt}\cdot\vec{v}\right) = m\left(\dfrac{d\vec{v}}{dt}\cdot\vec{v}\right).$$

Ok, in that expression is the net force on the object,

$$\vec{F}_{net} = m\dfrac{d\vec{v}}{dt}.$$

So that,

$$\dfrac{dT}{dt} = \vec{F}_{net}\cdot\vec{v}.$$

Now let's discretize the time derivative to make sense of this.

$$\dfrac{\Delta T}{\Delta t} = \vec{F}_{net}\cdot\vec{v}.$$

$$\Delta T = \vec{F}_{net}\cdot\vec{v}\Delta t.$$

That last term is the displacement of the object, $\Delta \vec{x} = \vec{v}\Delta t$. So we can write:

$$\Delta T = \vec{F}_{net}\cdot\Delta \vec{x}.$$

This is the work done on the object by the net force. We can write that as:

$$\Delta T = W_{\text{net}}.$$

#### Overall Effect of the Forces

Consider that we are looking at the changes in the object's motion over a longer period of space and time. This discrete model above helps us understand the relationship between the work done on the object and the change in its kinetic energy in a small interval, but what about the overall effect of the forces on the object?

Consider a discrete set of $n$ spatial intervals, $\Delta x_i$, where $i$ is the index of the interval. 

$$x = {x_0, x_1, x_2, \ldots, x_n}$$

At each of these spatial intervals, we experience a different net force, like in the figure below.

![Work done by a net force](/images/notes/week5/discrete-force-intervals.png)

$$F_{net} = {F_{net,0}, F_{net,1}, F_{net,2}, \ldots, F_{net,n}}$$

The work done by this force is the change in kinetic energy of the object:

$$W_{\text{net}} = \sum_{i=0}^{n} F_{net,i}\Delta x_i = \Delta T.$$

$$W_{\text{net}} = K_f - K_i.$$

$$W_{\text{net}} = \dfrac{1}{2}m\vec{v}_f\cdot\vec{v}_f - \dfrac{1}{2}m\vec{v}_i\cdot\vec{v}_i.$$

Notice that in the limit that $n \rightarrow \infty$ and $\Delta x_i \rightarrow 0$, we have a continuous function of the net force. We can write that as:

$$\lim_{n \rightarrow \infty} \sum_{i=0}^{n} F_{net,i}\Delta x_i = \int_{x_i}^{x_f} F_{net}(x)dx.$$

Thus, in our continuous limit, we can write the work done by the net force as:

$$\Delta T = W_{\text{net}} = \int_{x_i}^{x_f} F_{net}(x)dx.$$

What about in more than one dimension?

#### Work done in more than one dimension

Consider a path $C$ that we have discretized into $n$ intervals. The object starts at $\vec{r}_0$ and ends at $\vec{r}_n$. Each interval is $\Delta \vec{r}_i$ and the net force is $\vec{F}_{net,i}$. The figure below shows the work done by the net force in each interval.

![Work done by a net force](/images/notes/week5/path-integral-work.png)


The work done by the net force is:

$$W_{\text{net}} = \sum_{i=0}^{n} \vec{F}_{net,i}\cdot\Delta \vec{r}_i.$$

as $\Delta \vec{r}_i \rightarrow 0$ and $n \rightarrow \infty$, we have a continuous function of the net force. We can write that as:

$$W_{\text{net}} = \int_{C} \vec{F}_{net}\cdot d\vec{r}.$$

The work can be positive, if the force and displacement are in the same direction, or negative, if they are in opposite directions. It can also be zero, if the force is perpendicular to the displacement.

If the force is **always** perpendicular to the displacement, then the work done by the force is zero. This is because the dot product of two perpendicular vectors is zero. But what kind of motion is possible?

### Example: The Simple Harmonic Oscillator

Consider, again, the humble [SHO](https://en.wikipedia.org/wiki/Harmonic_oscillator). If we have a horizontal spring mass system, we know we can write the force on the mass as:

$$F_s = -kx.$$

Let's allow the spring to move from $x_i$ to $x_f$, while the speed changes from $v_i$ to $v_f$. 

The change in kinetic energy is:

$$\Delta T = \dfrac{1}{2}mv_f^2 - \dfrac{1}{2}mv_i^2.$$

The work done by the spring is:

$$W_s = \int_{x_i}^{x_f} F_s dx = -\int_{x_i}^{x_f} kx dx = -\left[\dfrac{1}{2}kx^2\right]_{x_i}^{x_f} = -\left(\dfrac{1}{2}kx_f^2 - \dfrac{1}{2}kx_i^2\right).$$

Or more simply,

$$W_s = \dfrac{1}{2}k(x_i^2 - x_f^2).$$

The Work-Energy Theorem tells us that:

$$\Delta T = W_s.$$

$$\dfrac{1}{2}mv_f^2 - \dfrac{1}{2}mv_i^2 = \dfrac{1}{2}k(x_i^2 - x_f^2).$$

We can rearrange this to find the relationship between the states before and after the motion:

$$\dfrac{1}{2}mv_f^2 + \dfrac{1}{2}k x_f^2 = \dfrac{1}{2}mv_i^2 + \dfrac{1}{2}k x_i^2.$$

The first term on the left and right side are the energy due to motion. The second terms are some other energy, but taken together before and after the motion, they are the same. They are a constant. **This is a [conserved quantity](https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence#Conservation_of_mass_and_energy).** 

We call the second quantity the **potential energy** of the spring-mass system. It is the energy of the system due to its position, or it's "configuration". We define the potential energy of the spring as:

$$U_s = \dfrac{1}{2}kx^2.$$

We often use $V$ to represent potential energy, so you might see it written as:

$$V_s = \dfrac{1}{2}kx^2.$$

What we have discovered is that the total energy of the spring-mass system is:

$$E_{tot} = T + U_s = \dfrac{1}{2}mv^2 + \dfrac{1}{2}kx^2 = \text{constant}.$$

You have likely seen this previously in your study of the SHO. It is a very important result. But it is also the case that we don't always have a potential energy function.

We need to have a [conservative force](https://en.wikipedia.org/wiki/Conservative_force) to have a potential energy function. A conservative force is one where the work done by the force is independent of the path taken. Above, we assumed that in our calculations because the force was only dependent on the position of the object. That is a key feature of a conservative force.



### Example: A Lattice Chain

A less obivous example that produces a potential energy function is a [lattice chain](https://en.wikipedia.org/wiki/Lattice_chain). Here we model an electron moving in 1D near but not too near a long chain of atoms. The picture below shows the model.

![Lattice chain model](/images/notes/week5/lattice-chain.png)

Here the location of the particle and it's initial velocty are zero. The force model for a chain of atoms in this arrangement is:

$$F(x) = -F_0 \sin \left(\dfrac{2\pi x}{b}\right)$$

where $b$ is the spacing between the atoms and $F_0$ is a constant.

We can again find the kinetic energy change and work done by the force:

$$\Delta T = \dfrac{1}{2}mv_f^2 - \dfrac{1}{2}mv_i^2 = \dfrac{1}{2}mv_f^2.$$

$$W = \int_{0}^{x_f} F(x) dx = -F_0 \int_{0}^{x_f} \sin \left(\dfrac{2\pi x}{b}\right) dx = -\left[-\dfrac{b}{2\pi}F_0 \cos \left(\dfrac{2\pi x}{b}\right)\right]_{0}^{x_f}$$

$$ = \dfrac{b}{2\pi}F_0 \left(\cos \left(\dfrac{2\pi x_f}{b}\right) - \cos \left(0\right)\right).$$

Using the Work-Energy Theorem, we can write:

$$\dfrac{1}{2}mv_f^2 = \dfrac{b}{2\pi}F_0 \left(\cos \left(\dfrac{2\pi x_f}{b}\right) - 1\right).$$

Thus, we can find the speed of the object at a given position:

$$v_f(x) = \sqrt{\dfrac{b}{\pi m}F_0 \left(\cos \left(\dfrac{2\pi x_f}{b}\right) - 1\right)}.$$

But more importantly, we can derive a potential energy function for the lattice chain. We can write:

$$U(x) = -\int F(x) dx = \dfrac{b}{2\pi}F_0 \cos \left(\dfrac{2\pi x}{b}\right) + C.$$
where $C$ is a constant. We can choose $C$ so that $U(0) = 0$; only the difference in potential energy matter. Then we have:

$$U(x) = \dfrac{b}{2\pi}F_0 \cos \left(\dfrac{2\pi x}{b}\right).$$

This is just **another** conservative force.

### Conservative Forces

These forces occur frequently enough in physics and their properties are so important that they deserve their own attention. There are a few key properties of conservative forces that we should note:

1. if the work is independent of the path taken, then the force is conservative.
2. if the work done by the force is zero for a closed path, then the force is conservative.
3. if the curl of the force is zero, then the force is conservative.

It turns out that all of these statements are equivalent. And if any one of them is true, the rest hold, and we can develop a potential energy function for the force.

#### Why do these imply each other?

Let's start with the curl of the force. The [curl](https://en.wikipedia.org/wiki/Curl) of a vector field is a measure of the rotation of the field. It is a [vector differential operator](https://en.wikipedia.org/wiki/Vector_calculus_operator). Operationally, taking the curl amounts to a cross product of the del operator with the vector field. The curl of a vector field $\vec{F}$ is defined as:

$$\nabla \times \vec{F} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k} \\ \partial_x & \partial_y & \partial_z \\ F_x & F_y & F_z \end{vmatrix} = \left(\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}\right)\hat{i} + \left(\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}\right)\hat{j} + \left(\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}\right)\hat{k}.$$

In the event that the curl vanishes, we know that each term in the curl is zero. In this case, we can investigate what this implies about other aspects of the force. We write [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem) for the force as:

$$\iint_S (\nabla \times \vec{F})\cdot d\vec{S} = \oint_C \vec{F}\cdot d\vec{r}.$$

The left hand side is the integral of the curl of the force over some surface $S$ with boundary $C$. The right hand side is the line integral of the force around the boundary of the surface.  This theorem holds for any vector field with continuous first derivatives, so most of what we do.

Stokes's theorem tells us that for any choice of surface $S$ with boundary $C$, the line integral of the force around the boundary is equal to the integral of the curl of the force over the surface. If the curl vanishes, then the integral of the curl is zero. Thus, the line integral of the force around the boundary is zero.

$$\oint_C \vec{F}\cdot d\vec{r} = 0.$$

This is true for any closed path $C$. This is the second statement above.

We can equivalent write the integral of the force around a closed path as the work around a different path. The figure below shows these paths $C_1$ and $C_2$ that make up the first loop, and the paths $C_3$ and $C_4$ that make up the second loop. The work done by the force along each path is shown in the figure.

![Work done by a net force](/images/notes/week5/closed-path-work.png)

We can take the integral of both paths and write:

$$\oint_C \vec{F}\cdot d\vec{r} = \int_{C_1} \vec{F}\cdot d\vec{r} + \int_{C_2} \vec{F}\cdot d\vec{r} = \int_{C_3} \vec{F}\cdot d\vec{r} + \int_{C_4} \vec{F}\cdot d\vec{r} = 0.$$

Because both paths are closed and start and return to the same point, we can know that each contribution on each part of the path is equal and opposite. Thus, we can write:

$$\int_{C_n} \vec{F}\cdot d\vec{r} = -\int_{C_m} \vec{F}\cdot d\vec{r}.$$

This holds for any $n$ and $m$ where they make a closed path $C$. This is the first statement above.

## Summary of Results

We covered a lot fo ground. Let's remind ourselves of the key results.

The total energy of a system is the sum of the kinetic and potential energies:

$$E = T + V = K +U.$$

We use both $T$ and $K$ to represent kinetic energy, and both $U$ and $V$ to represent potential energy.

The conservation of energy is:

$$\dfrac{dE}{dt} = 0.$$

When all the forces are conservative, energy is conserved. Of course, we are limiting here to mechanical energy.

Conservative forces are those where the work done by the force is independent of the path taken. They have several key properties:

1. The forces are functions of position only $\vec{F}(\vec{r})$.
2. Their curl is zero: $\nabla \times \vec{F} = 0$.

We calculate the curl as:
$$\nabla \times \vec{F} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k} \\ \partial_x & \partial_y & \partial_z \\ F_x & F_y & F_z \end{vmatrix} = \left(\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}\right)\hat{i} + \left(\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}\right)\hat{j} + \left(\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}\right)\hat{k}.$$

3. The force is given by the negative gradient of the potential energy: $\vec{F} = -\nabla U$. This stems from the definition of the potential energy as the work done by the force.

We can calculate the gradient as:

$$\vec{F} = \langle F_x, F_y, F_z \rangle = -\nabla U = -\left(\dfrac{\partial U}{\partial x}\hat{i} + \dfrac{\partial U}{\partial y}\hat{j} + \dfrac{\partial U}{\partial z}\hat{k}\right).$$

4. The work done by a conservative force is path independent. We can write the work done by a conservative force as:

$$W = \int_{C} \vec{F}\cdot d\vec{r} = -\int_{C} \nabla U\cdot d\vec{r} = -\Delta U.$$

## Linear and Angular Momentum

We've talked about the central conservation laws of classical mechanics: 

* Conservation of energy - in a process, if energy is conserved, the total energy of the system is the same before and after the process. More strongly, in a closed system, the total energy is constant for any process ($dE_{sys}/dt=0$).
* Conservation of linear momentum - in a process, if momentum is conserved, the total momentum of the system is the same before and after the process. More strongly, in a closed system, the total *vector* momentum is constant for any process ($d\vec{p}_{sys}/dt=0$).
* Conservation of angular momentum - in a process, if angular momentum is conserved, the total angular momentum of the system is the same before and after the process. More strongly, in a closed system, the total *vector* angular momentum is constant for any process ($d\vec{L}_{sys}/dt=0$).

We've worked with the conservation of energy a lot because it's a fundamental concept in physics and it lends itself to a scalar equation analysis. This can be quite a bit simpler in many cases, but an energy only view of the world can be limiting.

### Linear Momentum

As we move into the formal study of linear momentum, we will start with a reminder of the definition of momentum, and the mathematical form of the conservation of momentum.

Linear momentum is a vector quantity defined as the product of an object's mass and its velocity. It is denoted by the symbol $\vec{p}$ and is defined as:

$$\vec{p} = m\vec{v}$$

where $m$ is the mass of the object and $\vec{v}$ is the velocity of the object. The SI unit of momentum is kg m/s. As we later came to understand with [Einstein's special theory of relativity](https://en.wikipedia.org/wiki/Special_relativity), this definition of momentum is the classical limit of the relativistic momentum:

$$\vec{p} = \gamma m\vec{v}$$

where $\gamma$ is the Lorentz factor,

$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}.$$

As you can calculate, the relativistic momentum reduces to the classical momentum when the velocity is much less than the speed of light. As $v/c \rightarrow 0$, $\gamma \rightarrow 1$, and the relativistic momentum reduces to the classical momentum.


#### Linear Momentum and Newton's Second Law

You have seen in our discussion of Newton's Second Law that the net force on a system is equal to the mass of the system times the acceleration of the system. This can be written as:

$$\vec{F}_{net}=m\vec{a}.$$

However, this definition and our thinking here with it is a bit limited. What about systems of objects that are interacting with each other? What about deformable systems? What happens if something is shedding mass, like a rocket or jet? 

Newton's definition from [the Principia](https://en.wikipedia.org/wiki/Philosophi%C3%A6_Naturalis_Principia_Mathematica) is a bit more general. He defines the force in terms of the rate of change of the body's momentum:

$$\vec{F}_{net}=\frac{d\vec{p}}{dt}.$$

We can extend that definition to a system of objects, where the net force on the system is equal to the rate of change of the total momentum of the system:

$$\vec{F}_{net}=\frac{d\vec{p}_{sys}}{dt}.$$

The second step might not be obvious, but by working through a few examples we can see how this is a more useful and general definition of force.

#### Forces internal to a system zero out

Consider an abstract system of $N$ particles. You might think of them as point particles but they could be extended objects. They experience outside forces and internal forces; i.e., we go a tag all the particles in our system and we can tell which ones are interacting with each other. We can also tell which ones are interacting with the outside world. This is a bit silly, but it can help us visualize what we are arguing below.

The total force on the system is given by the sum of all the masses times the acceleration of each particle:

$$\vec{F}_{total} = \sum_{i=1}^{N} m_i\vec{a}_i = \sum_{i=1}^{N} \vec{F}_i$$

where the last term is the net force on the $ith$ particle. For a given object, $i$, the net force is the sum of all the forces acting on it, both internal and external,

$$\vec{F}_{i} = \vec{F}_{i}^{int} + \vec{F}_{i}^{ext}.$$

Here these internal forces are pairwise interactions between the particle $i$ and every other particle in the system, 

$$\vec{F}_{i}^{int} = \sum_{j\neq i}^{N} \vec{F}_{ij},$$

where the sum is over all particles that are not $i$ because there's no force between a particle and itself. 

Cool, what happens to the internal force equation when we sum over all particles in the system?

#### Concrete Examples

We have a generic setup, let's see what happens when we apply this to a few examples: 2 particles, 3 particles, and then N particles.

##### Two Particles

With two particles the sum is easy to write out fully.

$$\vec{F}_{int} = \sum_{i=1}^{2} \vec{F}_{i}^{int}$$

$$\vec{F}_{int} = \sum_{i=1}^2 \sum_{j\neq i}^{2} \vec{F}_{ij}$$

$$\vec{F}_{int} = \vec{F}_{12} + \vec{F}_{21} = 0$$

By Newton's Third Law, the force of particle 1 on particle 2 is equal and opposite to the force of particle 2 on particle 1. The internal forces cancel out and the net force on the system is the sum of the external forces.

$$\vec{F}_{12} = -\vec{F}_{21}$$

So here the internal forces sum to zero.

$$\vec{F}_{int} = 0$$


##### Three Particles

We can write this out in a similar way.

$$\vec{F}_{int} = \sum_{i=1}^{3} \vec{F}_{i}^{int}$$

$$\vec{F}_{int} = \sum_{i=1}^3 \sum_{j\neq i}^{3} \vec{F}_{ij}$$

$$\vec{F}_{int} = \vec{F}_{12} + \vec{F}_{13} + \vec{F}_{23} + \vec{F}_{21} + \vec{F}_{31} + \vec{F}_{32}$$

We can group these terms by Newton's Third Law pairs.

$$\vec{F}_{int} = (\vec{F}_{12} + \vec{F}_{21}) + (\vec{F}_{13} + \vec{F}_{31}) + (\vec{F}_{23} + \vec{F}_{32}) = 0$$

Every interaction on body $i$ has a corresponding equal and opposite interaction on body $j$, and the internal forces are again zero.

$$\vec{F}_{int} = 0$$


##### N Particles

Clearly, there seems to be a pattern here. Namely that the internal forces are always zero. We can write out the sum for $N$ particles in a way that suggests this is always true.

$$\vec{F}_{int} = \sum_{i=1}^{N} \vec{F}_{i}^{int}$$

$$\vec{F}_{int} = \sum_{i=1}^N \sum_{j\neq i}^{N} \vec{F}_{ij}$$

And where we make a switch  in the sum terms, so we can counting the force from each interaction in each term in the sum to make it clear why the internal forces sum to zero.

$$\vec{F}_{int} = \sum_{i=1}^N \sum_{j>i}^{N} \left(\underbrace{\vec{F}_{ij} + \vec{F}_{ji}}_{\mathrm{always}\,0}\right) = 0$$

Internal forces will always appear as third law pairs, so the internal interactions will always sum to zero. This is a very powerful result. 

$$\vec{F}_{int} = 0\,\mathrm{,\,always}$$

**For a given system, only external forces can change the momentum.**

#### Mathematical Form of Conservation of Linear Momentum

Let's look back at the system momentum,

$$\vec{p}_{sys} = \sum_{i=1}^{N} m_i\vec{v}_i = \sum_{i=1}^{N} \vec{p}_i.$$

If we take the time derivative of the system momentum, and assume we have point particles, so the masses are not changing,

$$\dfrac{d\vec{p}_{sys}}{dt} = \sum_{i=1}^{N} m_i\dfrac{d\vec{v}_i}{dt} = \sum_{i=1}^{N} m_i\vec{a}_i = \sum_{i=1}^{N} \vec{F}_i$$

The net force on the system is given by,

$$\vec{F}_{net} = \vec{F}_{int} + \vec{F}_{ext}.$$

Should there be no external forces, then,

$$\vec{F}_{net} = \vec{F}_{int} = 0.$$

And thus there is no change momentum of the system,

$$\dfrac{d\vec{p}_{sys}}{dt} = 0.$$

So if the system has no external forces, the total momentum of the system is conserved. We can propose a discrete extension to this form above where 

$$\dfrac{d\vec{p}_{sys}}{dt} \approx \dfrac{\Delta\vec{p}_{sys}}{\Delta t} = 0.$$

And thus, it's easy to see:

$$\Delta \vec{p}_{sys} = \vec{p}_{sys,f} - \vec{p}_{sys,i} = 0.$$

If there are external forces, then we also have a prediction equation for how the energy will change in a small time step $\Delta t$:

$$\Delta \vec{p}_{sys} = \vec{p}_{sys,f} - \vec{p}_{sys,i} = \sum_{i=1}^{N} \vec{F}_{ext,i}\Delta t,$$

so that,

$$\vec{p}_{sys,f} = \vec{p}_{sys,i} + \vec{F}_{ext}\Delta t.$$

### Angular Momentum

[Angular momentum](https://en.wikipedia.org/wiki/Angular_momentum) is a complex and rich quantity that has deep connections to the shape and structure of a system. The "configuration" or how it is distributed in space can have a big impact on the dynamics of a system. Our study of classical angular momentum will be a stepping stone to our study of [quantum angular momentum](https://en.wikipedia.org/wiki/Angular_momentum_operator) and the [spin]([https://en.wikipedia.org/wiki/Spin_(physics)]) of particles. 

{{< admonition type="admonition" title="Quantum Mechanical Spin" class="information" >}}
[Spin](https://en.wikipedia.org/wiki/Spin_(physics)) is a quantum mechanical property that is not related to the rotation of a particle, but it is a form of angular momentum, and it's essential to the structure of the universe - it tells us if we have [fermionic](https://en.wikipedia.org/wiki/Fermion) or [bosonic](https://en.wikipedia.org/wiki/Boson) particles, it is what gives us the [Pauli Exclusion Principle](https://en.wikipedia.org/wiki/Pauli_exclusion_principle), and it is what gives us the [Zeeman Effect](https://en.wikipedia.org/wiki/Zeeman_effect) and the [Stark Effect](https://en.wikipedia.org/wiki/Stark_effect).
{{< /admonition >}}

For the moment, we will limit ourselves to classical angular momentum and we will focus on the abstract case of a single particle. As we work through the semester, we will revisit angular momentum and introduce how to work with distributions of mass and extended objects.

#### Definition of Angular Momentum

For a particle with a momentum $\vec{p}$, the angular momentum is defined as the cross product of the position vector $\vec{r}$ and the momentum vector $\vec{p}$,

$$\vec{L} = \vec{r} \times \vec{p} = m \left(\vec{r} \times \vec{v}\right).$$

This is a quantity that depends on the location of the particle relative origin of coordinates. This means you have some latitude in choosing the origin of coordinates, and you can choose the origin to simplify the problem.

This also means the angular momentum is a vector quantity, and it points in the direction perpendicular to the plane defined by the position and momentum vectors. 

#### When is Angular Momentum Conserved?

We can ask this by computing the time derivative of the angular momentum,

$$\dfrac{d\vec{L}}{dt} = \dfrac{d}{dt}\left(\vec{r} \times \vec{p}\right) = 0?$$

We did a calculation like this on a homework where we computed

$$\dfrac{d}{dt}\left(\vec{a}\times\vec{b}\right) = \vec{a}\times\dfrac{d\vec{b}}{dt} + \dfrac{d\vec{a}}{dt}\times\vec{b}.$$

Let's apply it here:

$$\dfrac{d\vec{L}}{dt} = \dfrac{d}{dt}\left(\vec{r} \times \vec{p}\right) = \dfrac{d\vec{r}}{dt} \times \vec{p} + \vec{r} \times \dfrac{d\vec{p}}{dt}.$$

If we assume that $\dot{m}=0$, then we can write the time derivative of the momentum as,

$$\dfrac{d\vec{p}}{dt} = \dfrac{d}{dt}\left(m\vec{v}\right) = m\dfrac{d\vec{v}}{dt}$$

We group the terms in the time derivative of the angular momentum,

$$\dfrac{d\vec{L}}{dt} = m \underbrace{\dfrac{d\vec{r}}{dt} \times \vec{v}}_{=0} + m\vec{r} \times \dfrac{d\vec{v}}{dt}.$$

The first term the cross product of the velocity with itself $\vec{v}\times\vec{v}$, and is zero, and the second term is the cross product of the position vector with the acceleration,

$$\dfrac{d\vec{L}}{dt} = m\vec{r} \times \dfrac{d\vec{v}}{dt} = \vec{r}\times m\vec{a}.$$

So the time derivative of the angular momentum is the net torque on the system!

$$\vec{\tau}_{net} = \vec{r} \times \vec{F}_{net}.$$

$$\dfrac{d\vec{L}}{dt} = \vec{r}\times m\vec{a} = \vec{r} \times \vec{F}_{net}$$

$$\dfrac{d\vec{L}}{dt} = \vec{\tau}_{net}.$$

If the net torque on the system is zero, then the angular momentum is conserved, and it is a constant of the motion.

$$\dfrac{d\vec{L}_{sys}}{dt} = 0.$$

$$\Delta \vec{L}_{sys} = \vec{L}_{sys,f} - \vec{L}_{sys,i} = 0.$$

If there's a net torque, we have a discrete update equation for the angular momentum,

$$\vec{L}_{sys,f} = \vec{L}_{sys,i} + \vec{\tau}_{net}\Delta t.$$

### Are we sure there are no internal torques that matter?

We can ask the same question we asked about internal forces. Are there internal torques that matter?  As before, let us define the total force on particle $i$ as the sum of internal and external forces,

$$\vec{F}_{i} = \vec{F}_{i}^{int} + \vec{F}_{i}^{ext}.$$

We assume there are no external forces, and so the net force on the system is the sum of the internal forces,

$$\vec{F}_{net} = \vec{F}_{int}.$$

For given object, we observe an angular momentum $\vec{l}_i$ that is the cross product of the position vector and the momentum vector. So the time derivative of the $i$th particle's angular momentum is,

$$\dfrac{d\vec{l}_i}{dt} = \vec{r}_i \times \vec{F}_i.$$

If the total angular momentum of the system is the sum of the angular momenta of the particles,

$$\vec{L} = \sum_{i=1}^{N} \vec{l}_i,$$

then the time derivative of the total angular momentum is,

$$\dfrac{d\vec{L}}{dt} = \sum_{i=1}^{N} \dfrac{d\vec{l}_i}{dt} = \sum_{i=1}^{N} \vec{r}_i \times \vec{F}_i.$$

Recall that $\vec{F}_i = \sum_{j\neq i}^{N} \vec{F}_{ij}$. So we can rewrite the time derivative of the total angular momentum as,

$$\dfrac{d\vec{L}}{dt} = \sum_{i=1}^{N} \sum_{j\neq i}^{N} \vec{r}_i  \times \vec{F}_{ij} = \sum_{i=1}^N \sum_{j >i}^{N} \left(\vec{r}_i \times \vec{F}_{ij} + \vec{r}_j \times \vec{F}_{ji}\right)$$

But note that $\vec{r}_i \times \vec{F}_{ij} = -\vec{r}_j \times \vec{F}_{ji}$, so the resulting expression gives us,

$$\dfrac{d\vec{L}}{dt} =\sum_{i=1}^N \sum_{j>i}^{N} \left(\vec{r}_i - \vec{r}_j\right)\times \vec{F}_{ij}.$$

So if the internal forces are parallel to the separation between the particles, then the internal torques sum to zero, and the total angular momentum of the system is conserved. So things like the gravitational force, the electric force, and spring forces are all internal forces that do not contribute to the net torque on the system.

And thus,

$$\dfrac{d\vec{L}_{sys}}{dt} = 0.$$

- Understand the conditions under which the total momentum of a system is conserved.
- Derive and apply the discrete update equation for momentum in the presence of external forces.
- Define angular momentum for a single particle and understand its dependence on the choice of the origin.
- Explore the relationship between angular momentum and torque, and derive the conditions for angular momentum conservation.
- Analyze the role of internal forces and torques in the conservation of angular momentum.
- Understand how forces like gravity, electric forces, and spring forces contribute to the net torque on a system.
- Practice deriving time derivatives of angular momentum and interpreting their physical significance.
- Use vector calculus to analyze the dynamics of systems with multiple particles.
- Understand the principle of energy conservation and its application to physical systems.
- Derive and apply equations for energy changes in systems with external forces.
- Analyze the interplay between kinetic, potential, and total energy in dynamic systems.
