---
title: 04 - Why does fluid drag complicate things?
weight: 4
date: '2026-01-09'
math: true
---

[![Report Issues](https://img.shields.io/badge/report%20issues-GitHub-blue)](https://github.com/dannycab/phy321msu/issues) 
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Learning Goals

{{< admonition type="admonition" title="After studying Lesson 04, you should be able to:" class="note" >}}
* Differentiate between the two primary forms of fluid drag ($F \sim v$ and $F \sim v^2$) and identify their applications in real-world scenarios.
* Explain the concept of the Reynolds number and its significance in characterizing fluid flow regimes.
* Describe the differences between low Reynolds number (laminar) and high Reynolds number (turbulent) flows, including their physical implications.
* Analyze the equations of motion for systems with linear and quadratic drag forces in one and two dimensions.
* Solve analytically the equations of motion for systems with linear drag and explain why quadratic drag systems often require numerical methods.
* Develop and interpret free body diagrams for objects experiencing fluid drag in two dimensions.
* Apply Newton's Second Law to derive coupled differential equations for systems with drag forces and explain the challenges in solving them.
* Discuss the significance of the simple harmonic oscillator and gravitational bound systems as base models for more complex physical systems.
{{< /admonition >}}

As an object moves through the fluid, the molecules of the fluid collide with the object and exert a force on it. This collision changes the momentum of the object just a little bit. The collision does so in a random way, but the average effect of all those collisions is to exert a force on the object that is proportional to a function of the object's velocity, $F(v)$. In some cases those collisions occur such that they make an impact; other times they might approach the object more slowly and slide over it in familiar frictional interaction. These two behaviors are both fluid drag, but they are different forms.

The first form ($F \sim v^2$) describes the behavior of things like a skydiver falling, a high-speed car, or a baseball thrown through the air. But it can also be valid for the movement of fish in water, or a submarine moving through the ocean.  Through those collisions, the distribution of those forces can cause intra-body forces, which can result in damage or deformation of the object. However, we often model the body as solid and focus on the way this form of air resistance changes the motion. 

This form of air resistance cannot describe the behavior of objects approaching the speed of sound in the fluid. Objects moving a speeds that high can produce [shock fronts](https://en.wikipedia.org/wiki/Shock_wave) that forces the fluid to go through abrupt changes in density, pressure, and temperature. Below is a figure of a shock front produced the nose of a jet flying at supersonic speeds.


{{< figure src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Schlierenfoto_Mach_1-2_Pfeilfl%C3%BCgel_-_NASA.jpg" caption="A shock front from a supersonic jet. Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:Schlierenfoto_Mach_1-2_Pfeilfl%C3%BCgel_-_NASA.jpg)" >}}

The second form ($F \sim v$) describes the flow of a viscous fluid around a solid object. You might think of this as pulling an object through some viscous oil, honey, or even molasses. The movement of the fluid around the object exerts a force and slows the motion of the object.  In water, this form can explain the motion of some of the smallest creatures on Earth, like the [water bear](https://en.wikipedia.org/wiki/Tardigrade), an amoeba, or a paramecium. 

What is interesting here is that these creatures have had to adapt to this form of fluid drag. [Edward Purcell](https://en.wikipedia.org/wiki/Edward_M._Purcell) wrote a paper in 1977 called [Life at Low Reynolds Number](../docs/papers/purcell_AJP_1977.pdf)[^fairuse] that describes the motion of these creatures. He demonstrates that the physics in this regime requires creature to have adapted forms of locomotion that can take advantage of that environment. The figure below is reproduced from Purcell showing the decreasing physical scale and, thus, lower [Reynold's numbers](https://en.wikipedia.org/wiki/Reynolds_number).


{{< figure src="/images/notes/week4/purcell_fig3.png" caption="An illustration of the Reynold's number for different bodies in water. Source: [Purcell's, *Life at Low Reynolds Number*, Figure 3](https://pubs.aip.org/aapt/ajp/article/45/1/3/1043148/Life-at-low-Reynolds-number)" >}}


## Why do we often neglect air resistance?

We're in the business of making models of physical systems using the concepts and tools of Classical Mechanics. We've focused on Newton's Laws, which are a formulation of mechanics that starts from the concept of the force. 

We often start with that approach because the mathematical tools that we have available to us when we are first learning physics are geometry and algebra. Forces are a vector concept and Newton's Second Law is a vector equation that holds in each of the three dimensions of space. This formulation lends itself to a decomposing problems often into two or three separate problems, one for each dimension, and then using some algebra to solve the problems. However, that mathematics limits the kinds of explorations we can do.

This is one reason why we neglect [air resistance](https://en.wikipedia.org/wiki/Air_resistance) in our first explorations of motion. Our models of air resistance are more complicated and require more advanced mathematics to solve. The equations of motion can be coupled and non-linear. In some cases, we cannot solve the equations of motion analytically and must resort to numerical methods like [Euler's method](https://en.wikipedia.org/wiki/Euler_method), or the more often used [Runge-Kutta method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods).

[^fairuse]: Posted for educational access under [fair use](https://en.wikipedia.org/wiki/Fair_use) and will direct to original article when course is archived.

### The Reynolds Number

The different forms of fluid drag are often described by a dimensionless number called the [Reynolds Number](https://en.wikipedia.org/wiki/Reynolds_number). The Reynolds number is a ratio of the inertial forces to the viscous forces in a fluid. 

* **What are inertial forces?** They are the ones associated with resistance to motion, the mass of the object. The more massive the object in a given setup, the higher the inertial contribution.
* **What are viscous forces?** They are the ones associated with the interaction of the fluid with the object. The more viscous the fluid - the harder it for is to flow under the same conditions, the higher the viscous contribution.

The Reynolds number is defined as:

$$Re = \frac{\rho v L}{\mu}$$

where $\rho$ is the density of the fluid, $v$ is the velocity of the object in that fluid, $L$ is a characteristic length of the object, and $\mu$ is the dynamic viscosity of the fluid. 

You can probably see who the Reynolds number characterizes the system of the object and the fluid as their are properties of both the object and the fluid in the equation. The Reynolds number can be measured quite accurately in a lab because the laboratory setups are typically designed to make the measurement of the Reynolds number easier. We will often estimate it in theoretical physics.

#### What is a characteristic length?

This length is a generic length scale associated with the flow, this can be the order of magnitude size of the object, or, in the absence of an object, the same for the pipe or channel in which the flow is occurring. If it's an airplane, it can be the wingspan, or the length of the fuselage. If it's a car, it can be the length of the car. If it's a sphere, it can be the radius, and so on. 

#### What is dynamic viscosity?

Viscosity is the measure of the fluid's resistance to flow. It's how the fluid slides past itself. It's a bit of a harder quantity to describe, but you can think of it as the "stickiness" of the fluid. The higher the viscosity, the more sticky the fluid is -- really, for a given setup, the more viscous fluid will flow more slowly. The lower the viscosity, the higher tendency for a fluid to flow. Compare honey to water in the same vessel and temperature, and you'll observe the difference in viscosity.

##### Measuring viscosity

We can sometimes measure viscosity with a [viscometer](https://en.wikipedia.org/wiki/Viscometer), which uses a [capillary tube](https://en.wikipedia.org/wiki/Capillary_tube) to measure the time it takes for a fluid to flow through a tube of known dimensions. However, this works best for [Newtonian fluids](https://en.wikipedia.org/wiki/Newtonian_fluid), which are fluids that have a constant viscosity. 

{{< admonition type="admonition" title="Non-Newtonian fluids (in your kitchen; 1 minute video)" class="tip" >}}
Not all fluids are Newtonian, and some fluids have a viscosity that changes with the rate of flow. These [non-Newtonian fluids](https://en.wikipedia.org/wiki/Non-Newtonian_fluid) can be [shear thinning](https://en.wikipedia.org/wiki/Shear_thinning) or [shear thickening](https://en.wikipedia.org/wiki/Shear_thickening). Shear thinning fluids become less viscous when they are stirred or shaken, while shear thickening fluids become more viscous when they are stirred or shaken.

Below is a video from [America's Test Kitchen](https://www.americastestkitchen.com/) that demonstrates the behavior of a non-Newtonian fluid. The fluid is made from cornstarch and water, and it's called [oobleck](https://en.wikipedia.org/wiki/Oobleck). 

{{< youtube FrLh1GILomc >}}

- *Source: <https://www.youtube.com/watch?v=FrLh1GILomc>*

The physics of cooking is fascinating and covers the field of [soft matter physics](https://en.wikipedia.org/wiki/Soft_matter). There's a free course on the subject offered by [Harvard and EdX](https://pll.harvard.edu/course/science-cooking-haute-cuisine-soft-matter-science-physics).
{{< /admonition >}}

### Low Reynolds Number Flows

A low Reynolds number flow is a flow where the viscous forces dominate the inertial forces. The object is moving slowly, or the fluid is very viscous, or the object is very small. We typically think of these flows as being in the range of $Re < 1$. In these flows, the motion of the fluid is typically laminar; it flows in fairly smooth and parallel layers. Low Reynolds number flows can produce dynamics that is counterintutive. Below are a couple videos that explain the physics of low Reynolds number flows.

{{< admonition type="admonition" title="Physics of Life - Life at Low Reynolds Number (15 minute video)" class="tip" >}}
This video focuses on the biological aspects of the problem as the physics of low Reynolds numbers is important for understanding the motion of microorganisms. 

> Some YouTube videos are unable to be embedded in Jupyter Books. Click the image below to watch the video on YouTube.

{{< youtube gZk2bMaqs1E >}}

- *Source: <https://youtube.com/watch?v=gZk2bMaqs1E>*
{{< /admonition >}}

{{< admonition type="admonition" title="G.I. Taylor's Low Reynolds Number Flows (32 minute video)" class="tip" >}}
This video is a classic from [G.I. Taylor](https://en.wikipedia.org/wiki/Geoffrey_Ingram_Taylor) who was a physicist interested in sharing the conceptual beauty of physics with the general public. He was also a pioneer in the field of fluid mechanics. In fact, Taylor's [groundbreaking paper](../docs/papers/taylor_1922.pdf)[^fairuse] on the stability of fluid flows between two rotating cylinders set off studies into turbulence. The [Taylor-Couette flow](https://en.wikipedia.org/wiki/Taylor%E2%80%93Couette_flow) is a critical tool for [studies of turbulence](https://pubmed.ncbi.nlm.nih.gov/20365623/).

{{< youtube 8Dst6V4CQME >}}

- *Source: <https://youtube.com/watch?v=8Dst6V4CQME>*
{{< /admonition >}}

### High Reynolds Number Flows

In high Reynolds number flows, the inertial forces dominate the viscous forces. The object is moving quickly, or the fluid is not very viscous, or the object is very large. We typically think of these flows as being in the range of $Re > 1000$. In these flows, the motion of the fluid is typically [turbulent](https://en.wikipedia.org/wiki/Turbulence). Turbulent flows are characterized by chaotic and irregular motion. The fluid moves in a complex and unpredictable way, with eddies and vortices forming and dissipating. Turbulent flows can be very difficult to predict and model, but they are also very common in nature.

{{< admonition type="admonition" title="Von Kármán's Vortex Street (2 minute video)" class="tip" >}}
The [von Kármán vortex street](https://en.wikipedia.org/wiki/Von_K%C3%A1rm%C3%A1n_vortex_street) is a pattern of alternating vortices that can form when a fluid flows past a "bluff" body, such as a cylinder or a sphere. The vortices are shed from the body in a regular pattern, creating a repeating pattern of alternating vortices. The von Kármán vortex street is an example of a high Reynolds number flow, and it can be used to study the behavior of turbulent flows. Below is a video of a von Kármán vortex street simulation.

{{< youtube f3LmjJ1N7YE >}}

- *Source: <https://youtube.com/watch?v=f3LmjJ1N7YE>*
{{< /admonition >}}

{{< admonition type="admonition" title="Turbulent Flow (24 minute video)" class="tip" >}}
Turbulence is a major research area in science. We don't fully understand it. We are trying to determine what triggers it, how to control it, and how to predict if and when it will occur. The problem of turbulence is frequently multi-scale such that behavior at one time or length scale is not well explained or connected to another scale. Additionally, the mathematics of turbulence is very difficult. It makes for an interesting and challenging research area. Below is a video that explains the some of the physics of turbulence. The first 4 minutes or so are at least worth watching.

{{< youtube RkewD966Y90 >}}

- *Source: <https://youtube.com/watch?v=RkewD966Y90>*
{{< /admonition >}}



## Developing Equations of Motion

As you might have noticed in the last few weeks, our principal work is using models to develop equations of motion. Those equations of motion can then be analyzed, integrated, and plotted to understand the behavior of the system. This week, we will focus on the equations of motion for a few different systems. 

We will set up the equations of motion for a 2D quadratic drag system and show it's intractable analytically. Here is where our use of [Euler-Cromer integration](https://en.wikipedia.org/wiki/Euler%E2%80%93Cromer_method) can get us out of trouble. We will also develop the analytical solution to the 2D drag case when the drag is linear, which will show us how to solve these problems and compare them things we know.We will then quickly introduce two additional systems that are very common "base models" for more complex systems: (1) the gravitational bound planet system (a proxy for other central force systems) and (2) the simple harmonic oscillator (a common proxy for many oscillatory systems).


### Two-Dimensional Quadratic Drag

The drag force in 2D can be written in terms of the velocity vector of the object as:

$$\vec{F}_{drag} = -D |\vec{v}| \vec{v}$$

where $D$ is the drag coefficient and $\vec{v}$ is the velocity vector. Note that this force is written entirely using velocity, there is no dependence on position. However, the velocity vector is also function of time, $\vec{v} = \vec{v}(t)$.


#### Define the Coordinate System

To start this analysis, we need to define a coordinate system. Below, we draw the particle at some random time with the vecolicty vector shown. The axes are typical: $x$ is horizontal and $y$ is vertical. The drag force is always opposite to the velocity vector, so it will always be in the opposite direction of the velocity vector. 


{{< figure src="/images/notes/week4/2d-falling-ball.png" caption="Coordinate system choice for the 2D falling ball." >}}

{{< admonition type="caution" >}}
Redraw vector figure and post SVG
{{< /admonition >}}

In this coordinate system, the properties of the particle are:

$$\vec{r} = x \hat{x} + y \hat{y} = \langle x, y \rangle$$
$$\vec{v} = v_x \hat{x} + v_y \hat{y} = \langle v_x, v_y \rangle$$
$$\vec{a} = a_x \hat{x} + a_y \hat{y} = \langle a_x, a_y \rangle$$

where $\hat{x}$ and $\hat{y}$ are the unit vectors in the $x$ and $y$ directions, respectively. And the magnitude of the velocity vector is $|\vec{v}| = \sqrt{v_x^2 + v_y^2}$ as you might imagine.

The free body diagram at the point in time shown above is shown below. You see the gravitational force pointing directly downward and the drag force pointing in the opposite direction of the velocity vector. We continue to apply our coordinate system to the forces.


{{< figure src="/images/notes/week4/2d-falling-ball-fbd.png" caption="Free Body Diagram for the 2D falling ball." >}}

{{< admonition type="caution" >}}
Redraw vector figure and post SVG
{{< /admonition >}}

#### Apply Newton's Second Law

We now apply Newton's Second Law to the particle in the chosen coordinate system. The forces acting on the particle are the gravitational force and the drag force. 

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

##### Why can't we solve these equations?

We cannot form a solution because they are coupled and non-linear. Sometimes, we can decouple these equations (as we will see later) and produce partial differentials of the form:

$$f_1(v_x)dv_x = g_1(t)dt$$
$$f_2(v_y)dv_y = g_2(t)dt$$

These lead to independent equations of motion. We can use separation of variables to try to solve them. This is not possible in all cases, so functions are still not integrable analytically. But we cannot even form these partials, so an analytical solution is not possible in this case.

### Linear Drag in Two-Dimensions

As we saw above, the quadratic drag case is intractable. However, the linear drag case is analytically solvable. The drag force in 2D can be written in terms of the velocity vector of the object as:

$$\vec{F}_{lin} = -m \gamma \vec{v}$$

where $\gamma$ is a proxy for the drag coefficient. The linear drag force is proportional to the velocity vector.

We have the same set up as before and same FBD.


{{< figure src="/images/notes/week4/2d-falling-ball.png" caption="Coordinate System for the 2D falling ball." >}}

{{< admonition type="caution" >}}
Redraw vector figure and post SVG
{{< /admonition >}}

And thus the same coordinate system. The properties of the particle are the same as above. 

#### Apply Newton's Second Law

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

#### Solve the Equations

We can try to solve these equations by integrating them. We can integrate the first equation to get the velocity in the $x$ direction as a function of time.

##### Velocity in the $x$ direction

$$\dot{v}_x = -\gamma v_x$$

We separate the variables and integrate:

$$\frac{dv_x}{v_x} = -\gamma dt$$

We integrate from $v_{0,x}$ to $v_x$ and from $0$ to $t$:

$$\int_{v_{0,x}}^{v_x} \frac{dv_x}{v_x} = -\gamma \int_{0}^{t} dt$$

$$\ln(v_x) - \ln(v_{0,x}) = -\gamma t$$

$$v_x(t) = v_{0,x} e^{-\gamma t}$$

We see an exponential decay in the velocity in the $x$ direction.

##### Velocity in the $y$ direction

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

#### Trajectories

One of the main concepts we will discuss the trajectory of a system. We borrow that language and idea from projectile motion --  the location of the particle as a function of time is the trajectory. In this class, we will consider the word trajectory to mean the evolution of any property of the system as a function of time. This connects strongly to the concept of phase space, which we will discuss in the future.

In the prior example, we found the trajectory of the velocity in the $x$ and $y$ directions. 

$$v_x(t) = v_{0,x} e^{-\gamma t}$$
$$v_y(t) = \dfrac{g}{\gamma}\left(e^{-\gamma t} - 1\right) + v_{0,y} e^{-\gamma t}$$

We can expound on that work to find the trajectory of the position of the particle as a function of time. We can integrate the velocity to get the position.

Those integrals are doable, but they can be a little messy. We won't do them here, but quote the results consistent with the above equations.

$$x(t) = x_0 + \dfrac{1}{\gamma}v_{0,x}\left(1 - e^{-\gamma t}\right)$$
$$y(t) = y_0 - \dfrac{g}{\gamma}t + \dfrac{1}{\gamma}\left(\dfrac{g}{\gamma} + v_{0,y}\right)\left(1 - e^{-\gamma t}\right)$$

### 2D Gravitational Bound System

Consider a massive object (a large star) and a smaller satellite (a moon or small planet). We know that [Newton's Universal Law of Gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation) tells us the force between two objects that interact gravitationally is:

$$F = \dfrac{G m_1 m_2}{r^2}$$

where $G$ is the gravitational constant, $m_1$ and $m_2$ are the masses of the objects, and $r$ is the distance between the objects.

But we need to be more clear about the forces and the vector relationships. Consider the figure below with the massive object at the origin and the satellite at some distance $r$ from the origin. What is the vector $\vec{r}$ that describes the location of the satellite?

{{< figure src="/images/notes/week4/grav_01.png" caption="Gravitationally bound system with one body at the origin." >}}

{{< admonition type="error" >}}
Draw vector figure and post SVG
{{< /admonition >}}


If we move the sun from the origin a little, we can start to see what $\vec{r}$ is. The vector $\vec{r}$ is the vector from the sun to the satellite. See the figure below to see the sketch.

{{< figure src="/images/notes/week4/grav_02.png" caption="Gravitationally bound system with neither body at the origin." >}}

{{< admonition type="error" >}}
Draw vector figure and post SVG
{{< /admonition >}}

So if the location of the sun is $\vec{r}_{sun}$ and the Earth is $\vec{r}_{earth}$, then the vector $\vec{r}$ is:

$$\vec{r} = \vec{r}_{earth} - \vec{r}_{sun}$$

Let's return to the simplified model with the sun at the origin, and consider the earth at some distance $r$ from the origin. The force on the earth is:

$$\vec{F}_{grav} = -G \dfrac{M_{sun} M_{earth}}{|\vec{r}|^3} \vec{r}$$

where $M_{sun} = 2\times10^{30} \mathrm{kg}$ is the mass of the sun and $M_{earth} = 6 \times 10^{24} \mathrm{kg}$ is the mass of the earth. 

#### Define the Coordinate System

In the figure below, we show the earth at some distance $r$ from the origin at an angle $\phi$ from the $x$-axis. This distance is about $1.5 \times 10^{11}\;\mathrm{m}$ or $1\;\mathrm{A.U.}$ ([astronomical unit](https://en.wikipedia.org/wiki/Astronomical_unit)). While not entirely obvious, the scale of these numbers allow us to assume the Sun is at the origin, and doesn't move. Although this is not a good assumption for the real solar system, the sun orbits the [barycenter](https://en.wikipedia.org/wiki/Barycenter) of the solar system, which is about 1 solar radii from the center of the sun.


{{< figure src="/images/notes/week4/grav_03.png" caption="Vector analysis for a gravitationally bound system with neither body at the origin." >}}

{{< admonition type="error" >}}
Draw vector figure and post SVG
{{< /admonition >}}

Let's use the standard $x$ and $y$ axes to write the equations of motion. We can apply Newton's Second Law to the earth in the chosen coordinate system. 

$$\vec{F}_{net} = \vec{F}_{gravity} = m\vec{a} = m\langle a_x, a_y \rangle$$ 

So that the forces in the $x$ and $y$ directions are:

$$F_x = -G \dfrac{M_{sun} M_{earth}x}{(x^2+y^2)^{3/2}} \qquad F_y = -G \dfrac{M_{sun} M_{earth}y}{(x^2+y^2)^{3/2}}$$

and thus the acceleration of the Earth in the $x$ and $y$ directions are:

$$a_x = -G \dfrac{M_{sun} x}{(x^2+y^2)^{3/2}} \qquad a_y = -G \dfrac{M_{sun} y}{(x^2+y^2)^{3/2}}$$

This gives us a set of coupled differential equations.

$$\ddot{x} = -G \dfrac{M_{sun} x}{(x^2+y^2)^{3/2}} \qquad \ddot{y} = -G \dfrac{M_{sun} y}{(x^2+y^2)^{3/2}}$$

#### How do we then get the trajectories?

We can't solve these equations without more information. We need to know the initial conditions of the system (the initial position and velocity of the Earth). We can then integrate these equations to get the position of the Earth as a function of time.

We have three potential ways to solve these EOMs:

1) **Direct Integration:** We can integrate the equations of motion directly. This is possible in some cases where the equations are simple enough; think about the falling ball without air resistance, or the linear 1D drag case.
2) **Decouple and Solve:** We try to solve the coupled differential equations by decoupling them. This is possible in some cases, but not all. We can frequently decouple the equations by writing them in terms of the velocity, or by making a change of position variables.
3) **Numerical Integration:** We use numerical methods to predict the motion in small time steps. This is the most common method for solving complex systems.

### The Simple Harmonic Oscillator (SHO)

In 1D, the simple harmonic oscillator is a system where the force is proportional to the displacement from the equilibrium position. The force is given by:

$$F = -ks$$

where $k$ is the spring constant and $s$ is the displacement from the equilibrium position, $x-L_0$. The quantity $L_0$ is the relaxed length of the spring. The figure below shows the typical horizontal spring system.

{{< figure src="/images/vector-graphics/simple_harmonic_oscillator_setup_1D_horizontal.png" caption="Free Body Diagram of a Simple Harmonic Oscillator; the arrows label the direction of forces acting on the mass. [SVG File](../images/vector-graphics/simple_harmonic_oscillator_setup_1D_horizontal.svg)" >}}

We can typically choose to measure the displacement from the equilibrium position, and write the force instead as:

$$F = m a_x = m \dot{v}_x  = m\ddot{x} = -kx$$

So the equation of motion that we will try to solve is:

$$\ddot{x} = -\dfrac{k}{m}x$$

#### How do we solve this?

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


