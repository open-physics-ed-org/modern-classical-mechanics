# Week 12 - Notes: Introduction to Lagrangian Mechanics 




## Deriving Newton's Second Law in Plane Polar Coordinates

To get started with Lagrangian mechanics, we will start by deriving Newton's second law in plane polar coordinates. This is not a necessary step for anything we will do in Lagrangian mechanics, but it is a good way to get comfortable with the coordinate system. And it will also help us see how we can think about forces in a coordinate system that is not Cartesian because Lagrangian mechanics can be used with [generalized coordinates](https://en.wikipedia.org/wiki/Generalized_coordinates).

We start by sketching the location of a particle in plane polar coordinates, as shown below:

![Position vector in polar coordinates](../../images/notes/week12/coordinate-system.png)

The red arrow represents the position vector $\vec{r}$, which is a length $r$ from the origin at an angle $\phi$ from the $x$-axis. At the tip of the vector we have drawn the Cartesian unit vectors $\hat{x}$ and $\hat{y}$ in blue, and the polar unit vectors $\hat{r}$ and $\hat{\phi}$ in green. Notice that the polar unit vectors are rotated by an angle $\phi$ from the Cartesian unit vectors. We can simply write the position vector in terms of these unit vectors as:

$$\vec{r} = r \hat{r}\;\text{where}\;r = |\vec{r}|.$$

We start by taking the derivative of the position vector $\vec{r}$ with respect to time $t$ to find the velocity $\vec{v}$. Using the product and chain rules, we have:

$$\dfrac{d\vec{r}}{dt} = \frac{d}{dt}(r \hat{r}) = \dot{r} \hat{r} + r \frac{d\hat{r}}{dt}.$$

What is $\frac{d\hat{r}}{dt}$? 

We note that the green unit vectors for $\hat{r}$ and $\hat{\phi}$ are not constant, they change direction as the particle moves. We can write them in terms of the Cartesian unit vectors, which do not change with time, as follows:

$$\hat{r} = \cos(\phi) \hat{x} + \sin(\phi) \hat{y},\;\;\;\;\;\; \hat{\phi} = -\sin(\phi) \hat{x} + \cos(\phi) \hat{y}.$$


So now,we can differentiate $\hat{r}$ with respect to time $t$ using the chain rule:

$$\begin{align*}
\frac{d\hat{r}}{dt} &= \frac{d}{dt}(\cos(\phi) \hat{x} + \sin(\phi) \hat{y}) \\
&= \frac{d}{dt}(\cos(\phi)) \hat{x} + \cos(\phi) \frac{d\hat{x}}{dt} + \frac{d}{dt}(\sin(\phi)) \hat{y} + \sin(\phi) \frac{d\hat{y}}{dt} \\
&= -\sin(\phi) \dot{\phi} \hat{x} + \cos(\phi) \dot{\phi} \hat{y} \quad (\text{since } \frac{d\hat{x}}{dt} = 0 \text{ and } \frac{d\hat{y}}{dt} = 0) \\
&= \dot{\phi} \hat{\phi}
\end{align*}$$

And so our expression for the velocity $\vec{v} = \frac{d\vec{r}}{dt}$ becomes:

$$\vec{v} = \dot{r} \hat{r} + r \dot{\phi} \hat{\phi}.$$

We differentiate again to find the acceleration $\vec{a} = \frac{d\vec{v}}{dt}$. Using the product and chain rules again, we have:

$$\begin{align*}
\frac{d\vec{v}}{dt} &= \frac{d}{dt}(\dot{r} \hat{r} + r \dot{\phi} \hat{\phi}) \\
&= \frac{d}{dt}(\dot{r} \hat{r}) + \frac{d}{dt}(r \dot{\phi} \hat{\phi}) \\
&= \ddot{r} \hat{r} + \dot{r} \frac{d\hat{r}}{dt} + \dot{r} \dot{\phi} \hat{\phi} + r \ddot{\phi} \hat{\phi} + r \dot{\phi} \frac{d\hat{\phi}}{dt} \\
\end{align*}$$

We found $\frac{d\hat{r}}{dt} = \dot{\phi} \hat{\phi}$ in the previous step, and we also need to find $\frac{d\hat{\phi}}{dt}$. We can differentiate $\hat{\phi}$ in a similar way:

$$\begin{align*}
\frac{d\hat{\phi}}{dt} &= \frac{d}{dt}(-\sin(\phi) \hat{x} + \cos(\phi) \hat{y}) \\
&= \frac{d}{dt}(-\sin(\phi)) \hat{x} + (-\sin(\phi)) \frac{d\hat{x}}{dt} + \frac{d}{dt}(\cos(\phi)) \hat{y} + \cos(\phi) \frac{d\hat{y}}{dt} \\
&= -\cos(\phi) \dot{\phi} \hat{x} - \sin(\phi) \dot{\phi} \hat{y} \quad (\text{since } \frac{d\hat{x}}{dt} = 0 \text{ and } \frac{d\hat{y}}{dt} = 0) \\
&= -\dot{\phi} \hat{r} \quad (\text{since } \hat{r} = \cos(\phi) \hat{x} + \sin(\phi) \hat{y}).\\
\end{align*}$$

We return to our expression for the acceleration $\vec{a}$:

$$\begin{align*}
\vec{a} &= \ddot{r} \hat{r} + \dot{r} \frac{d\hat{r}}{dt} + \dot{r} \dot{\phi} \hat{\phi} + r \ddot{\phi} \hat{\phi} + r \dot{\phi} \frac{d\hat{\phi}}{dt} \\
&= \ddot{r} \hat{r} + \dot{r} (\dot{\phi} \hat{\phi}) + \dot{r} \dot{\phi} \hat{\phi} + r \ddot{\phi} \hat{\phi} + r \dot{\phi} (-\dot{\phi} \hat{r}) \\
&= \ddot{r} \hat{r} + \dot{r} \dot{\phi} \hat{\phi} + \dot{r} \dot{\phi} \hat{\phi} + r \ddot{\phi} \hat{\phi} - r \dot{\phi}^2 \hat{r}.\\
&= \left(\ddot{r} - r \dot{\phi}^2\right) \hat{r} + \left(2 \dot{r} \dot{\phi} + r \ddot{\phi}\right) \hat{\phi}.
\end{align*}$$

Using Newton's second law, we know that the acceleration $\vec{a}$ is equal to the net force $\vec{F}$ divided by the mass $m$ of the particle:

$$\vec{a} = \frac{\vec{F}}{m}.$$

Equating the two expressions for $\vec{a}$, we have:

$$\vec{F}_{net} = m\left[\left(\ddot{r} - r \dot{\phi}^2\right) \hat{r} + \left(2 \dot{r} \dot{\phi} + r \ddot{\phi}\right) \hat{\phi}\right]$$
$$\vec{F}_{net} = \vec{F}_{r} + \vec{F}_{\phi}$$

Where we can identify the radial and angular components of the net force as:

$$\vec{F}_{r} = m\left(\ddot{r} - r \dot{\phi}^2\right) \hat{r}$$
$$\vec{F}_{\phi} = m\left(2 \dot{r} \dot{\phi} + r \ddot{\phi}\right) \hat{\phi}$$

This gives us the net force in terms of the radial and angular components in polar coordinates.



### Skateboard Example

Let's see the utility of using polar coordinates by applying it to a skateboarder moving on a circular track. In this case, the skateboarder is constrained to move along a circular path of radius $r$. Consider a skateboarder moving on that circular track as shown below:

![Skateboarder on a circular track](../../images/notes/week12/skateboard.png)

At this point in the track, we can draw the free body diagram of the skateboarder. The forces acting on the skateboarder are the Earth's gravitational force and the normal force of the ramp.

![Free body diagram of skateboarder](../../images/notes/week12/skateboard-free-body.png)

We can use Newton's law in polar coordinates to analyze the forces acting on the skateboarder. This is because the normal force is always perpendicular to the surface of the ramp and will only have a radial component in polar coordinates. Thus we need only decompose the gravitational force into its radial and angular components.

The sum of all forces in the radial direction are given by:

$$\sum F_r = ma_r = -F_{ramp} + mg \cos(\phi) = m\left(\ddot{r} - r \dot{\phi}^2\right)$$

We note that $r=R$, that is the radius is fixed, so 

$$\ddot{r} = 0$$. 

Therefore, we can simplify the equation to:

$$-F_{ramp} + mg \cos(\phi) = -mR \dot{\phi}^2.$$

In the tangential direction, we have:

$$\sum F_{\phi} = ma_{\phi} = -mg \sin(\phi) = m\left(2 \dot{r} \dot{\phi} + r \ddot{\phi}\right)$$

Because $r=R$ is constant, we have $\dot{r} = 0$. Thus, the equation simplifies to:

$$-mg \sin(\phi) = mR \ddot{\phi}$$

Or, we can express this as:

$$\ddot{\phi} = -\frac{g}{R} \sin(\phi).$$

#### The Normal Force as a Function of Time

We can solve this equation using numerical methods to find $\phi(t)$, the angular position of the skateboarder as a function of time. This can be used to then find the normal force as a function of time by substituting $\phi(t)$ back into the radial equation we derived above:

$$F_{ramp} = mg \cos(\phi(t)) + mR \dot{\phi}^2(t).$$

Note that this force is a [force of constraint](https://en.wikipedia.org/wiki/Constraint_force) because it is not an external force acting on the skateboarder but rather a force that arises from the constraint of the circular track. These forces are important in mechanics and can be analyzed using Lagrangian mechanics as well. They are not typically conservative forces and do not have a potential energy associated with them. 

#### Simple Harmonic Motion

If we consider small angles, i.e., $\sin(\phi) \approx \phi$, then the equation of motion for $\ddot{\phi}$ becomes:

$$\ddot{\phi} \approx -\frac{g}{R} \phi.$$
on (SHM) with angular frequency $\omega = \sqrt{\frac{g}{R}}$. Thus, for small angles, the motion of the skateboarder on the circular track will exhibit SHM. The solution to this equation will be:

$$\phi(t) = A \cos(\omega t) + B \sin(\omega t),$$

where $A$ and $B$ are constants determined by the initial conditions of the problem.

### Newton's Laws and Equations of Motion

So far you have studied the work of physics from the perspective of Newtonian Mechanics, which is based on forces and their effects on motion. The idea behind using Newton's Laws is that:

1. We can identify all the interactions with a body (i.e., all the forces and torques acting on it).
2. We can write models of those interactions as mathematical expressions (i.e., force laws like $\vec{F} = -k \vec{x}$ for a spring or $b v^2$ for drag).
3. We can vectorially sum all the individual interactions to find the net result (i.e., $\sum \vec{F}_i = \vec{F}_{net}$).
4. We can then use Newton's second law to find the acceleration of the body, $\vec{a} = \frac{\vec{F}_{net}}{m}$.

This process has produced our **[equations of motion](https://en.wikipedia.org/wiki/Equation_of_motion)** for a system. Which we then investigated in detail throughout the course. 

```{admonition} Spring Example
We have solved the spring problem many times using Newton's Laws. The spring ($k$) is attached to a block of mass $m$ on a frictionless surface. There is a dashpot connected to the block with a damping coefficient $b$. We know the drag force is opposite the motion. We can write:

$$F_{spring} = -k x$$

$$F_{drag} = -b v$$

Thus, the net force on the block is:

$$F_{net} = F_{spring} + F_{drag} = -k \vec{x} - b \vec{v}$$


We can then substitute this into Newton's second law to find the acceleration of the block:

$$a = \frac{F_{net}}{m} = -\frac{k}{m} x - \frac{b}{m} v$$

And thus our equation of motion for the block is:

$$\ddot{x} = -\frac{k}{m} x - \frac{b}{m} \dot{x}$$
```

## Lagrangian Mechanics

The Lagrangian Formulation is rooted in classical optimization, but it is equivalent to Newton's work. However, it uses energy (a scalar) to do so. This means we can exploit coordinate transformations that do not change the scalar value of the energy.

Epistemologically, Lagrange's approach is an exploration of phase space to determine paths the dynamical system can take. You can think of this as one level of abstraction above plotting the known phase space, because we don't yet have the equations of motion. 

Let's try an example we have seen before, the spring-mass system. 

### Example: Spring-Mass System

As you will learn, to get the EOM for a non-dissipative system, we form a function called the **Lagrangian**:

The Lagrangian is defined as:

$$
\mathcal{L} = T - V
$$

Where:
- $T$ is the **kinetic energy** of the system.
- $V$ is the **potential energy** of the system.

For a 1D spring-mass system, we have:

$$T = \frac{1}{2} m \dot{x}^2 \quad V = \frac{1}{2} k x^2$$

Now we follow the optimization routine, which is applying the Euler-Lagrange equations to the Lagrangian. The Euler-Lagrange equation for $\mathcal{L}(x,\dot{x},t)$ is given by:

$$
\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) - \frac{\partial \mathcal{L}}{\partial x} = 0.
$$

Our Lagrangian for the spring-mass system is:

$$\mathcal{L}(x, \dot{x}) = T - V = \frac{1}{2} m \dot{x}^2 - \frac{1}{2} k x^2$$

Now we can compute the necessary derivatives:

$$\frac{\partial \mathcal{L}}{\partial \dot{x}} = m \dot{x}$$
$$\frac{\partial \mathcal{L}}{\partial x} = -k x$$

Now we can substitute these into the Euler-Lagrange equation:

$$
\frac{d}{dt} \left( m \dot{x} \right) - (-k x) = 0
$$

$$m\ddot{x} + kx = 0$$

This is the same equation of motion we derived using Newton's laws for the spring-mass system.

$$\ddot{x} = -\frac{k}{m} x$$
This shows that Lagrangian mechanics can reproduce the same equations of motion as Newtonian mechanics, but it does so by focusing on the energy of the system rather than forces directly. 

### Why does this work?

Lagrangian mechanics works because it is based on the [principle of least action](https://en.wikipedia.org/wiki/Action_principles) (or stationary action). This principle states that the actual path taken by a system between two points in phase space is the one that [minimizes (or makes stationary) the action](https://en.wikipedia.org/wiki/Hamilton%27s_principle), which is the integral of the Lagrangian over time.

This is not magic, it's an application of the [calculus of variations](https://en.wikipedia.org/wiki/Calculus_of_variations). The action is a functional, and the Euler-Lagrange equations provide a way to find the stationary points of that functional. By applying these equations to the Lagrangian, we can derive the equations of motion for a system.

We can think of this as a system that evolves in time, but does so in a way that is optimal in some sense. The approach allows us to find the path the system will take by exploiting [Hamilton's principle](https://en.wikipedia.org/wiki/Hamilton%27s_principle): *The path taken by a dynamical system between two points in phase space is the one that minimizes the time integral of the Lagrangian*. 

Mathematically, 

$$\delta \int_{t_1}^{t_2} \mathcal{L}(x(t), \dot{x}(t), t) dt = 0$$

Where $\delta$ indicates that we are looking for a stationary point of the action integral. This is precisely the formulation of the calculus of variations, which allows us to find the path that minimizes (or makes stationary) the action integral.

So, we know that the equation that will produce the $\mathcal{L}$ that minimizes the action integral is given by the Euler-Lagrange equations. 

$$\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) - \frac{\partial \mathcal{L}}{\partial x} = 0$$

In fact, this approach holds in each Cartesian coordinate, so that the equations of motion can be derived in any coordinate system. 

$$\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}_i} \right) - \frac{\partial \mathcal{L}}{\partial x_i} = 0$$

where $x_i$ can be $x, y, z$ if $\mathcal{L}(x,y,z,\dot{x},\dot{y},\dot{z},t)$.


### Generalized Coordinates

As it turns out, our approach can make use of an phase coordinate $(\theta, \phi, x, y, \rho, z, \ldots)$ and their first derivatives $(\dot{\theta}, \dot{\phi}, \dot{x}, \dot{y}, \dot{\rho}, \dot{z}, \ldots)$. In fact, we can do so for any set of [generalized coordinates](https://en.wikipedia.org/wiki/Generalized_coordinates) that describe the configuration of a system. Generalized coordinates are a set of coordinates that uniquely define the configuration of a system relative to some reference configuration. We denote them as $q_i$ where $i$ runs from 1 to $n$, and their time derivatives as $\dot{q}_i$.

The generalized position is given by:

$$\vec{q} = (q_1, q_2, \ldots, q_n)$$

And the generalized velocity (or time derivative of the generalized coordinates) is given by:

$$\vec{\dot{q}} = \left(\dot{q}_1, \dot{q}_2, \ldots, \dot{q}_n\right)$$

These $N$ coordinates would give tise to a set of $N$ equations of motion (subject to potential reductions due to constraints). The Lagrangian can be expressed in terms of these generalized coordinates and velocities:

$$
\mathcal{L} = \mathcal{L}(q_1, q_2, \ldots, q_n, \dot{q}_1, \dot{q}_2, \ldots, \dot{q}_n, t)
$$

The Euler-Lagrange equations can then be applied to each generalized coordinate $q_i$:

$$
\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{q}_i} \right) - \frac{\partial \mathcal{L}}{\partial q_i} = 0, \quad i = 1, 2, \ldots, n
$$

## Example: Plane Pendulum

To get some intuition for how Lagrangian mechanics works, let's consider an example we have seen before: the plane pendulum.

A pendulum bob of mass $m$ is attached to a fixed point by a rod of length $l$. The bob swings in a vertical plane under the influence of gravity as shown below. We define $U=0$ at the top of ceiling where the rod is attached.

![Pendulum Diagram](../../images/notes/week12/plane-pendulum.png)

The location of the bob is $\langle x, y \rangle$. We can use the $x,y$ coordinates to "naively" setup the Lagrangian and see what happens.

The kinetic energy $T$ of the pendulum bob is given by:

$$T(\dot{x}, \dot{y}) = \frac{1}{2} m (\dot{x}^2 + \dot{y}^2).$$

The potential energy $V$ of the pendulum bob is given by:

$$V(x,y) = +mgy.$$

Note $y$ is negative in the downward direction.

So we can write the Lagrangian $\mathcal{L}$ as:

$$
\mathcal{L}(x, y, \dot{x}, \dot{y}) = T - V = \frac{1}{2} m (\dot{x}^2 + \dot{y}^2) - mgy
$$

We will get two equations of motion from the Euler-Lagrange equations, one for $x$ and one for $y$. For $x$, we have:

$$\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) - \frac{\partial \mathcal{L}}{\partial x} = 0$$
$$\frac{d}{dt} \left( m \dot{x} \right) = 0.$$

This suggests that the momentum in the $x$-direction ($p_x= m\dot{x}$) is conserved, which cannot be correct for a pendulum. 

For $y$, we have:

$$\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{y}} \right) - \frac{\partial \mathcal{L}}{\partial y} = 0$$
$$\frac{d}{dt} \left( m \dot{y} \right) - (-mg) = 0$$
$$m\ddot{y} + mg = 0$$
$$\ddot{y} = -g.$$

There's no tension force? That can't be right. 

**We failed to include the constraint of the pendulum!** The pendulum is constrained to move along a circular arc of radius $l$. This means that the coordinates $x$ and $y$ are not independent, and we cannot just use $x,y$ as coordinates. This is a classic example of why we need to use generalized coordinates in Lagrangian mechanics.

The constraint for the pendulum is given by:

$$x^2 + y^2 = l^2$$

This tells us that,

$$\dot{x}^2 + \dot{y}^2 = \dot{r}^2 + r^2 \dot{\phi}^2 = l^2 \dot{\phi}^2$$

where $r=l$ is constant. So the constraint tells us that the motion of the pendulum is constrained to a circle of radius $l$ and it provides a relationship between the velocities $\dot{x}$ and $\dot{y}$.

So as you might have guessed, we need to use a different coordinate system to describe the motion of the pendulum. We can use **plane polar coordinates** $(r, \phi)$ where $r=l$ is constant and $\phi$ is the angle from the vertical.

$$\mathcal{L}(x, y, \dot{x}, \dot{y}) \rightarrow \mathcal{L}(r, \phi, \dot{r}, \dot{\phi})$$

The kinetic energy $T$ in polar coordinates is given by:

$$T = \frac{1}{2} m \left( \dot{x}^2 + \dot{y}^2 \right) = \frac{1}{2} ml^2\dot{\phi}^2 = T(\dot{r}, \dot{\phi}).$$

The potential energy $V$ becomes:

$$V = mgy = - mg l \cos(\phi) = V(r, \phi)$$

Now we can write the Lagrangian $\mathcal{L}$ in terms of the polar coordinates:

$$
\mathcal{L}(r, \phi, \dot{r}, \dot{\phi}) = T - V = \frac{1}{2} m l^2 \dot{\phi}^2 + mgl \cos(\phi)
$$

Notice that it is actually only a function of $\phi$ and $\dot{\phi}$, because $r=l$ is constant.

$$\mathcal{L}(l, \phi, \dot{\phi}) = \frac{1}{2} m l^2 \dot{\phi}^2 - mgl \cos(\phi)$$

Thus, we have a 1D equation of motion. This makes sense because the pendulum is constrained to move in a circular arc, and we can describe its motion using just one coordinate $\phi$.

Now we can apply the Euler-Lagrange equation to find the equation of motion for $\phi$:

$$
\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{\phi}} \right) - \frac{\partial \mathcal{L}}{\partial \phi} = 0
$$

$$-mgl \sin(\phi) + \frac{d}{dt} (ml^2 \dot{\phi}) = 0$$

And thus the $\phi$ equation of motion becomes:

$$ml^2 \ddot{\phi} + mgl \sin(\phi) = 0$$

or,

$$\ddot{\phi} = - \frac{g}{l} \sin(\phi).$$

As we have seen, for small $\phi$, this reduces to simple harmonic motion:

$$\ddot{\phi} \approx -\frac{g}{l} \phi \quad \text{for small } \phi.$$






