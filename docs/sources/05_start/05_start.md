# Week 5 - Conservation Laws



We started with Newton's Laws of Motion because they provide a framework for us to develop the equations of motion. However, there is a broader framework that can help us understand and organize our knowledge of physics. These are [conservation laws](https://en.wikipedia.org/wiki/Conservation_law).

Conservation laws are principles that state that certain properties of a system remain constant over time. These properties are called conserved quantities. In classical mechanics, there are three main conservation laws:

1. **Conservation of Energy**: The total energy of an isolated system remains constant over time.
2. **Conservation of Momentum**: The total momentum of an isolated system remains constant over time.
3. **Conservation of Angular Momentum**: The total angular momentum of an isolated system remains constant over time.

We will discuss them briefly below, before we dive into the details of conservation of energy. The concept of energy is so important and complimentary to our understanding of motion that we will focus on it before returning to momentum and angular momentum.

## Conservation of Energy

[Energy](https://en.wikipedia.org/wiki/Energy) is a central concept of science. It is also a very challenging conceptual idea. Physicists are known to say things like, 

> *"I can't tell you what energy is, but I can tell you how to calculate it."*

Richard Feynman is known to have had a disdain for the wildly different units of energy that we use in physics.

### Feynman on the units of energy (2 minute video)

[![Feynman on the units of energy](images/05_start_roX2NXDUTsM.jpg)](https://youtube.com/watch?v=roX2NXDUTsM)

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

[![The Big Misconception About Electricity](images/05_start_bHIhgxav9LY.jpg)](https://youtube.com/watch?v=bHIhgxav9LY)

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

[![Point Particle and Real Models](images/05_start_fbiNKrqVajM.jpg))](https://www.youtube.com/watch?v=fbiNKrqVajM)

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




