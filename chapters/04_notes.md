# Week 4 - Notes: Equations of Motion

As you might have noticed in the last few weeks, our principal work is using models to develop equations of motion. Those equations of motion can then be analyzed, integrated, and plotted to understand the behavior of the system. This week, we will focus on the equations of motion for a few different systems. 

We will set up the equations of motion for a 2D quadratic drag system and show it's intractable analytically. Here is where our use of [Euler-Cromer integration] can get us out of trouble. We will also develop the analytical solution to the 2D drag case when the drag is linear, which will show us how to solve these problems and compare them things we know.We will then quickly introduce two additional systems that are very common "base models" for more complex systems: (1) the gravitational bound planet system (a proxy for other central force systems) and (2) the simple harmonic oscillator (a common proxy for many oscillatory systems).


## Two-Dimensional Quadratic Drag

The drag force in 2D can be written in terms of the velocity vector of the object as:

$$\vec{F}_{drag} = -D |\vec{v}| \vec{v}$$

where $D$ is the drag coefficient and $\vec{v}$ is the velocity vector. Note that this force is written entirely using velocity, there is no dependence on position. However, the velocity vector is also function of time, $\vec{v} = \vec{v}(t)$.


### Define the Coordinate System

To start this analysis, we need to define a coordinate system. Below, we draw the particle at some random time with the vecolicty vector shown. The axes are typical: $x$ is horizontal and $y$ is vertical. The drag force is always opposite to the velocity vector, so it will always be in the opposite direction of the velocity vector. 

![Coordinate System](../../images/notes/week4/2d-falling-ball.png)

In this coordinate system, the properties of the particle are:

$$\vec{r} = x \hat{x} + y \hat{y} = \langle x, y \rangle$$
$$\vec{v} = v_x \hat{x} + v_y \hat{y} = \langle v_x, v_y \rangle$$
$$\vec{a} = a_x \hat{x} + a_y \hat{y} = \langle a_x, a_y \rangle$$

where $\hat{x}$ and $\hat{y}$ are the unit vectors in the $x$ and $y$ directions, respectively. And the magnitude of the velocity vector is $|\vec{v}| = \sqrt{v_x^2 + v_y^2}$ as you might imagine.

The free body diagram at the point in time shown above is shown below. You see the gravitational force pointing directly downward and the drag force pointing in the opposite direction of the velocity vector. We continue to apply our coordinate system to the forces.

![Free Body Diagram](../../images/notes/week4/2d-falling-ball-fbd.png)

### Apply Newton's Second Law

We now apply Newton's Seccond Law to the particle in the chosen coordinate system. The forces acting on the particle are the gravitational force and the drag force. 

$$\vec{F}_{net} = \vec{F}_{gravity} + \vec{F}_{drag}$$

How do we apply the coordinate system to the forces? We focus on the diagram above. We start by writing the sum of the forces. For this, we take $F_{gravity,x}$ to be a positive value, $mg$, where $g$ is the magnitude of the acceleration due to gravity. 

$$F_{net,x} =  F_{drag,x}$$
$$F_{net,y} =  F_{drag,y}-F_{gravity,y}$$

We can now write the forces in terms of the components of the vectors, and we introduce the acceleration vector, $\vec{a} = \langle a_x, a_y \rangle$.

$$m a_x = -D |\vec{v}| v_x$$
$$m a_y = -D |\vec{v}| v_y - mg$$

Let's clean this up a little in terms of the components:

$$\ddot{x} = -\frac{D}{m}  \dot{x}\sqrt{\dot{x}^2 + \dot{y}^2}$$
$$\ddot{y} = -\frac{D}{m} \dot{y}\sqrt{\dot{x}^2 + \dot{y}^2} - g$$

We can try to focus on the velocity instead to simplify the equations. Then we integrate those equations to get the position.

$$\dot{v}_x = -\frac{D}{m}  {v_x}\sqrt{{v_x}^2 + {v_y}^2}$$
$$\dot{v}_y = -\frac{D}{m} {v_y}\sqrt{{v_x}^2 + {v_y}^2} - g$$

Rats! There is no analytical solution to these equations.

These are called [coupled differential equations](https://math.libretexts.org/Bookshelves/Differential_Equations/Differential_Equations_(Chasnov)/07:_Systems_of_Equations/7.02:_Coupled_First-Order_Equations) because the equations are linked by the terms $\dot{x}$ and $\dot{y}$. This means that we cannot solve them independently. We need another approach to solve these equations.

#### Why can't we solve these equations?

We cannot form a solution because they are coupled and non-linear. Sometimes, we can decouple these equations (as we will see later) and produce partial differentials of the form:

$$f_1(v_x)dv_x = g_1(t)dt$$
$$f_2(v_y)dv_y = g_2(t)dt$$

These lead to independent equations of motion. We can use separation of variables to try to solve them. This is not possible in all cases, so functions are still not integrable analytically. But we cannot even form these partials, so an analytical solution is not possible in this case.





## Linear Drag in Two-Dimensions

As we saw above, the quadratic drag case is intractable. However, the linear drag case is analytically solvable. The drag force in 2D can be written in terms of the velocity vector of the object as:

$$\vec{F}_{lin} = -m \gamma \vec{v}$$

where $\gamma$ is a proxy for the drag coefficient. The linear drag force is proportional to the velocity vector.

We have the same set up as before and same FBD.

![Coordinate System](../../images/notes/week4/2d-falling-ball.png)

And thus the same coordinate system. The properties of the particle are the same as above. 

### Apply Newton's Second Law

We now apply Newton's Seccond Law to the particle in the chosen coordinate system. The forces acting on the particle are the gravitational force and the drag force.

$$\vec{F}_{net} = \vec{F}_{gravity} + \vec{F}_{lin}$$

Again, the gravitation force magnitude is $mg$, so we write the forces in terms of the components of the vectors:

$$F_{net,x} =  F_{lin,x}$$
$$F_{net,y} =  F_{lin,y}-F_{gravity,y}$$

In terms of the acceleration vector, $\vec{a} = \langle a_x, a_y \rangle$, we have:

$$m a_x = -m \gamma v_x$$
$$m a_y = -m \gamma v_y - mg$$

Notice that $v_x$ and $v_y$ are the components of the velocity vector; they can be positive, negative, or zero. We can clean this up in terms of the velocity components, and we have two linear, uncoupled differential equations:

$$\dot{v}_x = -\gamma v_x$$
$$\dot{v}_y = - \gamma v_y - g$$

### Solve the Equations

We can try to solve these equations by integrating them. We can integrate the first equation to get the velocity in the $x$ direction as a function of time.

#### Velocity in the $x$ direction

$$\dot{v}_x = -\gamma v_x$$

We separate the variables and integrate:

$$\frac{dv_x}{v_x} = -\gamma dt$$

We integrate from $v_{0,x}$ to $v_x$ and from $0$ to $t$:

$$\int_{v_{0,x}}^{v_x} \frac{dv_x}{v_x} = -\gamma \int_{0}^{t} dt$$

$$\ln(v_x) - \ln(v_{0,x}) = -\gamma t$$

$$v_x(t) = v_{0,x} e^{-\gamma t}$$

We see an exponential decay in the velocity in the $x$ direction.

#### Velocity in the $y$ direction

Now we can try to do the same for $v_y$:

$$\dot{v}_y = -\gamma v_y - g$$

We separate the variables and integrate:

$$\frac{dv_y}{v_y + \frac{g}{\gamma}} = -\gamma dt$$

Note that this integral will be of the form:

$$\int \frac{dx}{x + a} = \ln(x + a) + C$$

Again, we integrate from $v_{0,y}$ to $v_y$ and from $0$ to $t$:

$$\int_{v_{0,y}}^{v_y} \frac{dv_y}{v_y + \frac{g}{\gamma}} = -\gamma \int_{0}^{t} dt$$

$$\ln(v_y + \frac{g}{\gamma}) - \ln(v_{0,y} + \frac{g}{\gamma}) = -\gamma t$$

$$ln\left(\dfrac{v_y + \frac{g}{\gamma}}{v_{0,y} + \frac{g}{\gamma}}\right) = -\gamma t$$

Next we use exponentiation and do a little algebra to solve for $v_y$:

$$\left(\dfrac{g}{\gamma} + v_y\right) = \left(\dfrac{g}{\gamma} + v_{0,y}\right) e^{-\gamma t}$$

$$v_y(t) = \dfrac{g}{\gamma}\left(e^{-\gamma t} - 1\right) + v_{0,y} e^{-\gamma t}$$

In the $y$ direction, the story appears more complex.

### Trajectories

One of the main concepts we will discuss the trajectory of a system. We borrow that language and idea from projectile motion --  the location of the particle as a function of time is the trajectory. In this class, we will consider the word trajectory to mean the evolution of any property of the system as a function of time. This connects strongly to the concept of phase space, which we will discuss in the future.

In the prior example, we found the trajectory of the velocity in the $x$ and $y$ directions. 

$$v_x(t) = v_{0,x} e^{-\gamma t}$$
$$v_y(t) = \dfrac{g}{\gamma}\left(e^{-\gamma t} - 1\right) + v_{0,y} e^{-\gamma t}$$

We can expound on that work to find the trajectory of the position of the particle as a function of time. We can integrate the velocity to get the position.

Those integrals are doable, but they can be a little messy. We won't do them here, but quote the results consistent with the above equations.

$$x(t) = x_0 + \dfrac{1}{\gamma}v_{0,x}\left(1 - e^{-\gamma t}\right)$$
$$y(t) = y_0 - \dfrac{g}{\gamma}t + \dfrac{1}{\gamma}\left(\dfrac{g}{\gamma} + v_{0,y}\right)\left(1 - e^{-\gamma t}\right)$$

## 2D Gravitational Bound System

Consider a massive object (a large star) and a smaller satellite (a moon or small planet). We know that [Newton's Universal Law of Gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation) tells us the force between two objects that interact gravitationally is:

$$F = \dfrac{G m_1 m_2}{r^2}$$

where $G$ is the gravitational constant, $m_1$ and $m_2$ are the masses of the objects, and $r$ is the distance between the objects.

But we need to be more clear about the forces and the vector relationships. Consider the figure below with the massive object at the origin and the satellite at some distance $r$ from the origin. What is the vector $\vec{r}$ that describes the location of the satellite?

![Gravitational Bound System](../../images/notes/week4/grav_01.png)

If we move the sun from the origin a little, we can start to see what $\vec{r}$ is. The vector $\vec{r}$ is the vector from the sun to the satellite. See the figure below to see the sketch.

![Gravitational Bound System](../../images/notes/week4/grav_02.png)

So if the location of the sun is $\vec{r}_{sun}$ and the Earth is $\vec{r}_{earth}$, then the vector $\vec{r}$ is:

$$\vec{r} = \vec{r}_{earth} - \vec{r}_{sun}$$

Let's return to the simplified model with the sun at the origin, and consider the earth at some distance $r$ from the origin. The force on the earth is:

$$\vec{F}_{grav} = -G \dfrac{M_{sun} M_{earth}}{|\vec{r}|^3} \vec{r}$$

where $M_{sun} = 2\times10^{30} \mathrm{kg}$ is the mass of the sun and $M_{earth} = 6 \times 10^{24} \mathrm{kg}$ is the mass of the earth. 

### Define the Coordinate System

In the figure below, we show the earth at some distance $r$ from the origin at an angle $\phi$ from the $x$-axis. This distance is about $1.5 \times 10^{11}\;\mathrm{m}$ or $1\;\mathrm{A.U.}$ ([astronomical unit](https://en.wikipedia.org/wiki/Astronomical_unit)). While not entirely obvious, the scale of these numbers allow us to assume the Sun is at the origin, and doesn't move. Although this is not a good assumption for the real solar system, the sun orbits the [barycenter](https://en.wikipedia.org/wiki/Barycenter) of the solar system, which is about 1 solar radii from the center of the sun.

![Gravitational Bound System](../../images/notes/week4/grav_03.png)

Let's use the standard $x$ and $y$ axes to write the equations of motion. We can apply Newton's Second Law to the earth in the chosen coordinate system. 

$$\vec{F}_{net} = \vec{F}_{gravity} = m\vec{a} = m\langle a_x, a_y \rangle$$ 

So that the forces in the $x$ and $y$ directions are:

$$F_x = -G \dfrac{M_{sun} M_{earth}x}{(x+2+y^2)^{3/2}} \qquad F_y = -G \dfrac{M_{sun} M_{earth}y}{(x+2+y^2)^{3/2}}$$

and thus the acceleration of the Earth in the $x$ and $y$ directions are:

$$a_x = -G \dfrac{M_{sun} x}{(x+2+y^2)^{3/2}} \qquad a_y = -G \dfrac{M_{sun} y}{(x+2+y^2)^{3/2}}$$

This gives us a set of coupled differential equations.

$$\ddot{x} = -G \dfrac{M_{sun} x}{(x+2+y^2)^{3/2}} \qquad \ddot{y} = -G \dfrac{M_{sun} y}{(x+2+y^2)^{3/2}}$$

### How do we then get the trajectories?

We can't solve these equations without more information. We need to know the initial conditions of the system (the initial position and velocity of the Earth). We can then integrate these equations to get the position of the Earth as a function of time.

We have three potential ways to solve these EOMs:

1) Direct Integration: We can integrate the equations of motion directly. This is possible in some cases where the equations are simple enough; think about the falling ball without air resistance, or the linear 1D drag case.
2) Decouple and Solve: We try to solve the coupled differential equations by decoupling them. This is possible in some cases, but not all. We can frequently decouple the equations by writing them in terms of the velocity, or by making a change of position variables.
3) Numerical Integration: We use numerical methods to predict the motion in small time steps. This is the most common method for solving complex systems.



## The Simple Harmonic Oscillator (SHO)

In 1D, the simple harmonic oscillator is a system where the force is proportional to the displacement from the equilibrium position. The force is given by:

$$F = -ks$$

where $k$ is the spring constant and $s$ is the displacement from the equilibrium position, $x-L_0$. The quantity $L_0$ is the relaxed length of the spring. The figure below shows the typical horizontal spring system.

![SHO](../../images/notes/week3/sho_horizontal.png)

We can typically choose to measure the displacement from the equilibrium position, and write the force instead as:

$$F = m a_x = m \dot{v}_x  = m\ddot{x} = -kx$$

So the equation of motion that we will try to solve is:

$$\ddot{x} = -\dfrac{k}{m}x$$

### How do we solve this?

$$\dfrac{d^2x}{dt^2} = -\dfrac{k}{m}x = - \omega^2 x$$

where $\omega = \sqrt{\dfrac{k}{m}}$ is the natural oscillation frequency of the system. 

It might seem strange, but let's try the following potential solution to the differential equation:

$$x(t) = C e^{i\omega t}$$

where $C$ is a constant. We can take the second derivative of $x(t)$ with respect to time to see if it satisfies the differential equation.

$$\dot{x}(t) = i\omega C e^{i\omega t}$$
$$\ddot{x}(t) = -\omega^2 C e^{i\omega t} = -\omega^2 x(t)$$

This is a solution to the differential equation as long as $C$ is a constant, but it's a complex one ($C=a+ib$). We can also write the solution in terms of the cosine and sine functions because the exponential function can be written in terms of these functions.

$$e^{i\omega t} = \cos(\omega t) + i\sin(\omega t)$$

Thus, another general solution to this EOM that we can write is:

$$x(t) = A \cos(\omega t) + B \sin(\omega t)$$

where $A$ and $B$ are constants that depend on the initial conditions of the system. Let's see how that works:

$$\dot{x}(t) = -A \omega \sin(\omega t) + B \omega \cos(\omega t)$$
$$\ddot{x}(t) = -A \omega^2 \cos(\omega t) - B \omega^2 \sin(\omega t) = -\omega^2 x(t)$$

Another form that works is:

$$x(t) = D \cos(\omega t + \phi)$$

where $D$ is the amplitude of the oscillation and $\phi$ is the phase of the oscillation.  Let's check that again:

$$\dot{x}(t) = -D \omega \sin(\omega t + \phi)$$
$$\ddot{x}(t) = -D \omega^2 \cos(\omega t + \phi) = -\omega^2 x(t)$$

So we have several forms of the general solution to the simple harmonic oscillator. We can use these solutions to understand the behavior of the system. We can also use these solutions to understand the behavior of more complex systems that can be approximated by the simple harmonic oscillator. 

One critical aspect of these solutions is that they have 2 free parameters, $A$ and $B$, or $D$ and $\phi$. These parameters are determined by the initial conditions of the system. **There are N free parameters in the general solution to an Nth order differential equation.**


