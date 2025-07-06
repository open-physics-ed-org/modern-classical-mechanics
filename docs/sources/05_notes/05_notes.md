# Week 5 - Notes: Conservation of Energy

One expression of a conservation law is the [conservation of energy](https://en.wikipedia.org/wiki/Conservation_of_energy). For an isolated and closed system, the total energy is conserved. That is, before and after any process, we can account for all the energy in the system and it is the same. More generally, conservation of energy accounts for the energy "lost" to the surroundings. All of the changes to the system must be accounted for in changes the surroundings. 

For a given choice of system that interacts with its surroundings, the change in energy of the system is equal to the work done on the system and any heat exchanged with the surroundings. This is a statement of the [first law of thermodynamics](https://en.wikipedia.org/wiki/First_law_of_thermodynamics). We can write that statement mathematically as:

$$\Delta E_{\text{system}} = W + Q$$


where $\Delta E_{\text{system}}$ is the change in energy of the system, $W$ is the work done on the system, and $Q$ is the heat exchanged with the surroundings.

:::{admonition} Sign conventions
:class: warning

Note that the signs of the work done and heat exchanged are important. But we can remember them by asking if the system is going to increase its energy. 

If we add energy into the system by heating it, then $Q$ is positive because $\Delta E_{\text{system}}$ is positive. If the remove energy from the system through an exchange of heat, then $Q$ is negative.

If the system does work on the surroundings, for example, by exerting a force on an external object over some displacement, then $W$ is negative because $\Delta E_{\text{system}}$ is negative. If instead the surroundings do work on the system, then $W$ is positive.

:::

We can rewrite this energy equation as an update equation for the energy of the system:

$$E_{\text{system,f}} = E_{\text{system,i}} + W + Q$$

From this equation, we can see that the final state of the system's energy is determined by the sum of its initial energy, the work done on the system, and the heat exchanged with the surroundings.

## The Work-Energy Theorem

We often model a system as a single object that interacts with its surroundings. In this case, it's often beneficial to select the object alone to be the system of interest. Then all of our work is to explain and predict the dynamics of the object.

This simplification allows us to employ a more specialized case of the general energy equation. We can write the work-energy theorem as:

$$\Delta E_{\text{object}} = W_{\text{net}}$$
where $\Delta E_{\text{object}}$ is the change in energy of the object and $W_{\text{net}}$ is the net work done on the object.

More specifically, we often focus only on the changes to the object's motion. This is because we use often use the model of a [point particle](https://en.wikipedia.org/wiki/Point_particle) to describe the object. In this case, the object has no internal structure and thus no internal energy. The only energy we need to consider is the object's kinetic energy, $K$. 

:::{admonition} Limitation of this model

The point particle model where we focus on the kinetic energy of an object is an obvious simplification. But it might not be so obvious how quickly it is to break down.

Consider pushing a block across the floor. The block is a point particle and we model it as such. It comes to a stop and we argue the block's kinetic energy was converted to heat in the floor. 

But what about the block itself? Would it's surface temperature increase? It does, but we don't account for it.

A great account of these kinds of situations is from my colleague [Bruce Sherwood](https:/brucesherwood.net/).  Bruce's paper, [*Pseudowork and real work*, American Journal of Physics (1982)](https://pubs.aip.org/aapt/ajp/article-abstract/51/7/597/1052185/Pseudowork-and-real-work?redirectedFrom=fulltext), is an important read about the limitation of the point particle model. You can find a PDF copy [here](https://brucesherwood.net/wp-content/uploads/2017/06/Pseudowork1983.pdf).
:::

### Kinetic Energy

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

## Developing the Work-Energy Theorem

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

### Overall Effect of the Forces

Consider that we are looking at the changes in the object's motion over a longer period of space and time. This discrete model above helps us understand the relationship between the work done on the object and the change in its kinetic energy in a small interval, but what about the overall effect of the forces on the object?

Consider a discrete set of $n$ spatial intervals, $\Delta x_i$, where $i$ is the index of the interval. 

$$x = {x_0, x_1, x_2, \ldots, x_n}$$

At each of these spatial intervals, we experience a different net force, like in the figure below.

![Work done by a net force](../images/notes/week5/discrete-force-intervals.png)

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

### Work done in more than one dimension

Consider a path $C$ that we have discretized into $n$ intervals. The object starts at $\vec{r}_0$ and ends at $\vec{r}_n$. Each interval is $\Delta \vec{r}_i$ and the net force is $\vec{F}_{net,i}$. The figure below shows the work done by the net force in each interval.

![Work done by a net force](../images/notes/week5/path-integral-work.png)


The work done by the net force is:

$$W_{\text{net}} = \sum_{i=0}^{n} \vec{F}_{net,i}\cdot\Delta \vec{r}_i.$$

as $\Delta \vec{r}_i \rightarrow 0$ and $n \rightarrow \infty$, we have a continuous function of the net force. We can write that as:

$$W_{\text{net}} = \int_{C} \vec{F}_{net}\cdot d\vec{r}.$$

The work can be positive, if the force and displacement are in the same direction, or negative, if they are in opposite directions. It can also be zero, if the force is perpendicular to the displacement.

If the force is **always** perpendicular to the displacement, then the work done by the force is zero. This is because the dot product of two perpendicular vectors is zero. But what kind of motion is possible?

## Example: The Simple Harmonic Oscillator

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



## Example: A Lattice Chain

A less obivous example that produces a potential energy function is a [lattice chain](https://en.wikipedia.org/wiki/Lattice_chain). Here we model an electron moving in 1D near but not too near a long chain of atoms. The picture below shows the model.

![Lattice chain model](../images/notes/week5/lattice-chain.png)

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

## Conservative Forces

These forces occur frequently enough in physics and their properties are so important that they deserve their own attention. There are a few key properties of conservative forces that we should note:

1. if the work is independent of the path taken, then the force is conservative.
2. if the work done by the force is zero for a closed path, then the force is conservative.
3. if the curl of the force is zero, then the force is conservative.

It turns out that all of these statements are equivalent. And if any one of them is true, the rest hold, and we can develop a potential energy function for the force.

### Why do these imply each other?

Let's start with the curl of the force. The [curl](https://en.wikipedia.org/wiki/Curl) of a vector field is a measure of the rotation of the field. It is a [vector differential operator](https://en.wikipedia.org/wiki/Vector_calculus_operator). Operationally, taking the curl amounts to a cross product of the del operator with the vector field. The curl of a vector field $\vec{F}$ is defined as:

$$\nabla \times \vec{F} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k} \\ \partial_x & \partial_y & \partial_z \\ F_x & F_y & F_z \end{vmatrix} = \left(\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}\right)\hat{i} + \left(\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}\right)\hat{j} + \left(\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}\right)\hat{k}.$$

In the event that the curl vanishes, we know that each term in the curl is zero. In this case, we can investigate what this implies about other aspects of the force. We write [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem) for the force as:

$$\iint_S (\nabla \times \vec{F})\cdot d\vec{S} = \oint_C \vec{F}\cdot d\vec{r}.$$

The left hand side is the integral of the curl of the force over some surface $S$ with boundary $C$. The right hand side is the line integral of the force around the boundary of the surface.  This theorem holds for any vector field with continuous first derivatives, so most of what we do.

Stokes's theorem tells us that for any choice of surface $S$ with boundary $C$, the line integral of the force around the boundary is equal to the integral of the curl of the force over the surface. If the curl vanishes, then the integral of the curl is zero. Thus, the line integral of the force around the boundary is zero.

$$\oint_C \vec{F}\cdot d\vec{r} = 0.$$

This is true for any closed path $C$. This is the second statement above.

We can equivalent write the integral of the force around a closed path as the work around a different path. The figure below shows these paths $C_1$ and $C_2$ that make up the first loop, and the paths $C_3$ and $C_4$ that make up the second loop. The work done by the force along each path is shown in the figure.

![Work done by a net force](../images/notes/week5/closed-path-work.png)

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


