# Week 6 - Notes: Linear and Angular Momentum



We've talked about the central conservation laws of classical mechanics: 

* Conservation of energy - in a process, if energy is conserved, the total energy of the system is the same before and after the process. More strongly, in a closed system, the total energy is constant for any process ($dE_{sys}/dt=0$).
* Conservation of linear momentum - in a process, if momentum is conserved, the total momentum of the system is the same before and after the process. More strongly, in a closed system, the total *vector* momentum is constant for any process ($d\vec{p}_{sys}/dt=0$).
* Conservation of angular momentum - in a process, if angular momentum is conserved, the total angular momentum of the system is the same before and after the process. More strongly, in a closed system, the total *vector* angular momentum is constant for any process ($d\vec{L}_{sys}/dt=0$).

We've worked with the conservation of energy a lot because it's a fundamental concept in physics and it lends itself to a scalar equation analysis. This can be quite a bit simpler in many cases, but an energy only view of the world can be limiting.

## Linear Momentum

As we move into the formal study of linear momentum, we will start with a reminder of the definition of momentum, and the mathematical form of the conservation of momentum.

Linear momentum is a vector quantity defined as the product of an object's mass and its velocity. It is denoted by the symbol $\vec{p}$ and is defined as:

$$\vec{p} = m\vec{v}$$

where $m$ is the mass of the object and $\vec{v}$ is the velocity of the object. The SI unit of momentum is kg m/s. As we later came to understand with [Einstein's special theory of relativity](https://en.wikipedia.org/wiki/Special_relativity), this definition of momentum is the classical limit of the relativistic momentum:

$$\vec{p} = \gamma m\vec{v}$$

where $\gamma$ is the Lorentz factor,

$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}.$$

As you can calculate, the relativistic momentum reduces to the classical momentum when the velocity is much less than the speed of light. As $v/c \rightarrow 0$, $\gamma \rightarrow 1$, and the relativistic momentum reduces to the classical momentum.


### Linear Momentum and Newton's Second Law

You have seen in our discussion of Newton's Second Law that the net force on a system is equal to the mass of the system times the acceleration of the system. This can be written as:

$$\vec{F}_{net}=m\vec{a}.$$

However, this definition and our thinking here with it is a bit limited. What about systems of objects that are interacting with each other? What about deformable systems? What happens if something is shedding mass, like a rocket or jet? 

Newton's definition from [the Principia](https://en.wikipedia.org/wiki/Philosophi%C3%A6_Naturalis_Principia_Mathematica) is a bit more general. He defines the force in terms of the rate of change of the body's momentum:

$$\vec{F}_{net}=\frac{d\vec{p}}{dt}.$$

We can extend that definition to a system of objects, where the net force on the system is equal to the rate of change of the total momentum of the system:

$$\vec{F}_{net}=\frac{d\vec{p}_{sys}}{dt}.$$

The second step might not be obvious, but by working through a few examples we can see how this is a more useful and general definition of force.

### Forces internal to a system zero out

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

### Mathematical Form of Conservation of Linear Momentum

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

## Angular Momentum

[Angular momentum](https://en.wikipedia.org/wiki/Angular_momentum) is a complex and rich quantity that has deep connections to the shape and structure of a system. The "configuration" or how it is distributed in space can have a big impact on the dynamics of a system. Our study of classical angular momentum will be a stepping stone to our study of [quantum angular momentum](https://en.wikipedia.org/wiki/Angular_momentum_operator) and the [spin]([https://en.wikipedia.org/wiki/Spin_(physics)]) of particles. 

:::{admonition} Quantum Mechanical Spin
:class: information
[Spin](https://en.wikipedia.org/wiki/Spin_(physics)) is a quantum mechanical property that is not related to the rotation of a particle, but it is a form of angular momentum, and it's essential to the structure of the universe - it tells us if we have [fermionic](https://en.wikipedia.org/wiki/Fermion) or [bosonic](https://en.wikipedia.org/wiki/Boson) particles, it is what gives us the [Pauli Exclusion Principle](https://en.wikipedia.org/wiki/Pauli_exclusion_principle), and it is what gives us the [Zeeman Effect](https://en.wikipedia.org/wiki/Zeeman_effect) and the [Stark Effect](https://en.wikipedia.org/wiki/Stark_effect).
:::

For the moment, we will limit ourselves to classical angular momentum and we will focus on the abstract case of a single particle. As we work through the semester, we will revisit angular momentum and introduce how to work with distributions of mass and extended objects.

### Definition of Angular Momentum

For a particle with a momentum $\vec{p}$, the angular momentum is defined as the cross product of the position vector $\vec{r}$ and the momentum vector $\vec{p}$,

$$\vec{L} = \vec{r} \times \vec{p} = m \left(\vec{r} \times \vec{v}\right).$$

This is a quantity that depends on the location of the particle relative origin of coordinates. This means you have some latitude in choosing the origin of coordinates, and you can choose the origin to simplify the problem.

This also means the angular momentum is a vector quantity, and it points in the direction perpendicular to the plane defined by the position and momentum vectors. 

### When is Angular Momentum Conserved?

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


```python

```


```python

```


