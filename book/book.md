# Week 1 - Notes: Introduction to Classical Mechanics

## How do we formulate Classical Mechanics?

In the past, you have learned about [Newton's Laws of Motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion). These laws are the foundation of classical mechanics. They are used to describe the motion of objects in the universe. In this course, we will use these laws to describe the motion of particles and rigid bodies. As we progress, we will learn other formulations of classical mechanics, such as the [Lagrangian](https://en.wikipedia.org/wiki/Lagrangian_mechanics) and [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) reformulations.

Newton's Laws of Motion are a vector formulation of classical mechanics. The laws are as follows:
1. **First Law**: An object at rest will remain at rest, and an object in motion will remain in motion at a constant velocity unless acted upon by an external force.
2. **Second Law**: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. The direction of the acceleration is in the direction of the net force.
3. **Third Law**: For every action, there is an equal and opposite reaction.

These are the classic laws of motion that you have learned in other courses. How we formulate these laws mathematically is the subject of this course.

## Newton's Second Law

[Newton's Second Law](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion#Newton's_second_law) provides the mathematical foundation for classical mechanics. It provides a vector relationship between the net force acting on an object and its acceleration. The law is given by the equation:

$$\vec{F}_{net} = m\vec{a}$$

where $\vec{F}_{net}$ is the net force acting on the object, $m$ is the mass of the object, and $\vec{a}$ is the acceleration of the object. This equation is a vector equation, meaning that it must be satisfied in each direction. 

$$\begin{aligned}
F_{net,x} &= m a_x \\
F_{net,y} &= m a_y \\
F_{net,z} &= m a_z
\end{aligned}$$

Each push in a Cartesian direction results in a proportional response -- an acceleration in the same direction of the net push. Let's go through a common example to illustrate this relationship.

### Example: A Block on an Inclined Ramp

Consider the box (mass, $m$) above on an inclined ramp (angle, $\theta$). The box is at rest subject to static friction, $\mu_s$. _What angle of inclination will cause the box to start sliding down the ramp?_

We start by drawing the [Free Body Diagram](https://en.wikipedia.org/wiki/Free_body_diagram) (FBD) of the box. 

![Free Body Diagram of Box on a Inclined Ramp; the arrows label the direction of forces acting on the box](images/notes/week1/box_fbd.png)<br>
[Source: homework.study.com](images/notes/week1/box_fbd_remote.png)

The FBD is a diagram that shows all the forces acting on the object. In this case, the forces acting on the box are:
- The force of gravity, $mg$, acting downwards.
- The force due to the ramp, which is both perpendicular to the ramp surface (normal) and parallel to it (friction).

We tilt our coordinate system to align with the ramp. This makes the normal force, $N$, act in the $y$-direction and the frictional force, $f$, act in the $x$-direction. The force of gravity is split into two components: $mg\sin(\theta)$ and $mg\cos(\theta)$.

The net force acting on the box is the sum of the forces acting on it, and is zero up to the point where the box starts sliding. At this point, the frictional force is at its maximum value, $\mu_s N$. Taking the sum of the forces acting on the box in each direction we have:

$$\vec{F}_{net} = \vec{f} + \vec{N} + \vec{F}_{gravity} = 0$$

$$\sum F_{x,i} = f - mg\sin(\theta) = 0$$
$$\sum F_{y,i} = N - mg\cos(\theta) = 0$$

Thus, 

$$f = mg\sin(\theta)$$
$$N = mg\cos(\theta)$$

At the point where the box starts sliding, the frictional force is at its maximum value, $\mu_s N$. Thus, the box starts sliding when:

$$f = \mu_s N$$

Substituting the expressions for $f$ and $N$ into the equation above, we have:

$$mg\sin(\theta) = \mu_s mg\cos(\theta)$$

Solving for $\theta$:

$$\tan(\theta) = \mu_s$$
$$\theta = \tan^{-1}(\mu_s)$$

Thus, the box starts sliding when the angle of inclination is equal to the arctangent of the coefficient of static friction. 

```{admonition} Check
We can check this with some numbers. Steel as a static friction coefficient of about 0.16, and rubber is closer to 0.8. Thus, the angle of inclinations for steel and rubber are:

$$\theta_{steel} = \tan^{-1}(0.16) \approx 9^\circ$$
$$\theta_{rubber} = \tan^{-1}(0.8) \approx 39^\circ$$

It seems quite reasonable that rubber would have a higher angle of inclination before sliding than steel.
```
```{tip}
A few things to note about this problem:
1. This was a static problem, such that $\vec{F}_{net} = 0$.
2. We rotated our coordinate system to align with the ramp. This is a common technique in classical mechanics to simplify the problem.
3. We still used Cartesian coordinates to solve the problem. This is because the forces could be easily decomposed in the titled coordinate system.
```

Let's work an example that is dynamic, where the net force is not zero.

### Example: Falling Object in One Dimension

Consider an object of mass $m$ falling, but it is subject to air resistance. The free body diagram of the object shows that the forces acting on the object are:
- The force of gravity/weight, $W=mg$, acting downwards.
- The force due to air resistance, $F_{air}$, acting upwards.

![Free Body Diagram of Falling Object; the arrows label the direction of forces acting on the object](images/notes/week1/falling_object.png)<br>
[Source: ibphysicsguide.weebly.com](images/notes/week1/falling_object_remote.gif)

Here we have chosen positive $y$ to be the downward direction. We want to predict the motion ($a$, $v$, $y$) of the object as a function of time. This is a very common problem for classical mechanics.

#### Air Drag?

First, we notice that we do not know the force due to [air resistance](https://en.wikipedia.org/wiki/Drag_(physics)). We do know that the force is related to the velocity of the object. So let's start by writing the air resistance force as a function of velocity:

$$F_{air} = F(v)$$

where $F(v)$ is some function of velocity. 

#### Taylor Series Expansion

Because we know that the objects move slowly in classical mechanics, we can assume that the function can be expanded using a [Taylor Series](https://en.wikipedia.org/wiki/Taylor_series).  In general, the Taylor Series of a function $f(x)$ about a point $a$ is given by:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

where $f^{(n)}(a)$ is the $n$-th derivative of $f(x)$ evaluated at $x=a$. We can write the first few terms out,

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \ldots$$

Because we know that the object is moving slowly, we can expand the function $F(v)$ about $v=0$:

$$F(v) = F(0) + F'(0)v + \frac{F''(0)}{2!}v^2 + \ldots$$

We can assume that the first term is zero, $F(0)=0$, because there is no air resistance when the object is at rest. Thus, the force due to air resistance is approximately:

$$F(v) \approx F'(0)v + \frac{F''(0)}{2!}v^2$$

We call the first term the **linear drag** term and the second term the **quadratic drag** term. The linear drag term is proportional to the velocity of the object, and the quadratic drag term is proportional to the square of the velocity of the object. We also typically replace the evaluated derivatives with constants, $b$ and $c$ -- because they are constants that depend on the object and the fluid it is moving through. And thus,

$$F_{air} \approx bv + cv^2$$



#### Back to Newton's Second Law

In the $y$-direction, the net force acting on the object is:

$$F_y = W - F_{air} = mg - bv - cv^2$$

And thus, the acceleration of the object is:

$$a = g - \frac{b}{m}v - \frac{c}{m}v^2$$

This [differential equation]((https://en.wikipedia.org/wiki/Differential_equation)) can be written in a variety of ways. One common way is to write the equation as a [second-order differential equation](https://math.libretexts.org/Bookshelves/Differential_Equations/Introduction_to_Partial_Differential_Equations_(Herman)/12:_B_-_Ordinary_Differential_Equations_Review/12.02:_Second_Order_Linear_Differential_Equations). 

$$\frac{d^2y}{dt^2} = g - \frac{b}{m}\frac{dy}{dt} - \frac{c}{m}\left(\frac{dy}{dt}\right)^2$$

Note that this is a nonlinear differential equation (i.e., there's a $(d^ny/dt^n)^m$ term where $m > 1$), which are notoriously difficult to solve in general. We can write it using the dot notation for derivatives (i.e., $\dot{y} = dy/dt$, $\ddot{y} = d^2y/dt^2$):

$$\ddot{y} = g - \frac{b}{m}\dot{y} - \frac{c}{m}\dot{y}^2$$

We can also use the velocity as the independent variable, $v = \dot{y}$. Both equations below are equivalent:

$$\frac{dv}{dt} = g - \frac{b}{m}v - \frac{c}{m}v^2$$
$$\dot{v} = g - \frac{b}{m}v - \frac{c}{m}v^2$$

```{tip}
A few things to note:
1. This is a dynamic one-dimensional problem, such that $\vec{F}_{net} \neq 0$.
2. This is a nonlinear problem, such that the acceleration is a function of the velocity of the object.
3. We are stuck with a differential equation that we need to solve, and don't have a simple algebraic solution (e.g., a simple antiderivative).
```

**How do we solve this equation to find the motion of the object as a function of time?**  We will come back to this, but solving differential equations is the primary tool of classical mechanics. We will learn how to solve these equations analytically and numerically in this course.


# Week 1 - Overture: What is Classical Physics?

There are many different fields of physics; they are both distinct and overlapping. If we were to take a view of what kinds of physical systems that we wanted to investigate with different physics, we could organize them based on the system's size and speed of change:

- [Classical physics](https://en.wikipedia.org/wiki/Classical_physics): large, slow systems

- [Statistical](https://en.wikipedia.org/wiki/Statistical_mechanics) and [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics): small, slow systems

- [General relativity](https://en.wikipedia.org/wiki/General_relativity): large, fast systems

- [Quantum field theory](https://en.wikipedia.org/wiki/Quantum_field_theory): small, fast systems

These are not hard and fast rules, and, in fact, we often bring physics from different spaces together to solve complex problems. For examples, the fields of [climate modeling](https://en.wikipedia.org/wiki/Climate_model), [non-linear dynamics](https://en.wikipedia.org/wiki/Nonlinear_system), [astrophysics](https://en.wikipedia.org/wiki/Astrophysics), and [particle physics](https://en.wikipedia.org/wiki/Particle_physics) use physical models and tools for each of the fields above. How we organize physics for ourselves depends on how we decide we want to look at it. However the first view where we organize the field by size and speed is a useful way to think about the different kinds of physics that we have developed thus far. The figure below shows how we might organize physics by size and speed.

![Physics by size and speed](images/notes/week1/640px-Modernphysicsfields.svg.png)<br>
*Source: [Wikipedia](images/notes/week1/File:Modernphysicsfields.svg)*

Classical Physics is the physics that we developed before discovering relativity and quantum mechanics. It typically covers both mechanical systems and electromagnetic systems. It is also [the physics that we read about historically](https://en.wikipedia.org/wiki/History_of_physics), which has its [roots in ancient astronomy](https://en.wikipedia.org/wiki/History_of_astronomy) and has existed across many different cultures. 

```{admonition} Wherever there were people, there was Classical Physics.
:class: note

You might have heard of the development physics in the [Hellensitic age](https://en.wikipedia.org/wiki/Science_in_classical_antiquity#Hellenistic_age) where the Greeks used mathematics to study astronomical objects, or how [Newton's Laws of motion](https://en.wikipedia.org/wiki/Newton's_laws_of_motion) came to be. These are both examples of classical physics. 

But there are many more including [astronomical analyses in Sub-Saharan Africa](https://www.science.org/doi/10.1126/science.200.4343.766) in 300 BCE, massive [scientific expansion in China](https://en.wikipedia.org/wiki/Science_and_technology_of_the_Song_dynasty) during the Song dynasty, and studies that pushed the fields of optics, mechanics, and astronomy in the [Islamic Golden Age](https://en.wikipedia.org/wiki/Islamic_Golden_Age). 

While we do not often present it, much to the detriment of our own field, [physics and astronomy were a large part of indigenous cultures](https://en.wikipedia.org/wiki/Indigenous_astronomy) across the world including in what become the United States. 
```

## Classical Mechanics

When we define [Classical Mechanics](https://en.wikipedia.org/wiki/Classical_mechanics), at least for the purposes of this class, we will define it as the physics of large, slow, mechanical systems.

- **Large** - Systems are typically big enough that we can see them with our eyes, or maybe with some reasonably simple optical tools. We're typically excluding the microscopic world of atoms and molecules.
- **Slow** -- Systems for which we can observe their motion and track them "visually"; that is they move much slower than the speed of light. This is a critical assumption that we make in classical mechanics.
- **Mechanical** -- Systems where the fields of electromagnetism don't come into play. We relax this is bit when we think of a particle in a classical E&M field, but the focus is still on modeling the particle and not the field.

### Modeling Large, Slow, Mechanical Systems

**Classical mechanics is a physics that allows us to model these large, slow, mechanical systems.**

It helps us develop an understanding of that process of making models and how we can use models to make predictions. It is a physics that results typically in [deterministic models](https://en.wikipedia.org/wiki/Determinism), where we can predict the future of a system given its current state. This is because the language of Classical Mechanics is [differential equations](https://en.wikipedia.org/wiki/Differential_equation), which describe how a system changes as a result of influences from it's environment. It is often a [vector-based physics](<https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)>) as it describes the pushes and pulls on a system in a given direction. However, we can often develop scalar models or systems of scalar equations that describe the motion of a system.

Ultimately, Classical Mechanics is a physics that allows us to interrogate the behavior of these systems and describe their [dynamics](<https://en.wikipedia.org/wiki/Dynamics_(mechanics)>). Through Classical Mechanics, we can describe the present state of a system, how it will evolve, and then use that information to make predictions about the future. What we learn from Classical Mechanics can become a set of powerful tools that we can use in many contexts.


## Applications of Classical Mechanics

While it might appear there's little room for using Classical Mechanics in research or in industry now, it turns out there's tons of room. It is still the physics that enables us to understand fluid systems, nonlinear mechanical effects, continuum mechanics, animal locomotion, and many other systems. Below are several examples of how Classical Mechanics is used in research and industry. We encourage to watch these videos as they demonstrate how the physics we will learn in class is really central to continuing to understand nature.

### Fluid Mechanics at LANL (6 minute video)

[Researchers at Los Alamos National Lab](https://www.lanl.gov/org/ddste/aldsc/theoretical/fluid-dynamics-solid-mechanics/index.php) do a variety of research using fluid mechanics models.

[![](images/notes/week1/youtube_myuD81326_o.jpg)](https://youtube.com/watch?v=myuD81326_o)

Source: <https://www.youtube.com/watch?v=myuD81326_o>

### Biologically-Inspired Robotics (2 minute video)


A [research lab at Georgia Tech](https://crablab.gatech.edu/) uses Classical Mechanics to model the motion of animals and then uses that information to build robots that can move like animals.


[![](images/notes/week1/youtube_Qme07fA3Fj4.jpg)](https://youtube.com/watch?v=Qme07fA3Fj4)


Source: <https://www.youtube.com/watch?v=Qme07fA3Fj4>

## Classical Mechanics in this Class

Classical mechanics is a topic which has been taught intensively over
several centuries. It is, with its many variants and ways of
presenting the educational material, normally the first physics
course many of us meet and it lays the foundation for further physics
studies. Many of the equations and ways of reasoning about the
underlying laws of motion and pertinent forces, shape our approaches and understanding
of the scientific method and discourse, as well as the way we develop our insights
and deeper understanding about physical systems.


There are a wealth of
well-tested (from both a physics point of view and a pedagogical
standpoint) exercises and problems which can be solved
analytically. However, many of these problems represent idealized and
less realistic situations. The large majority of these problems are
solved by paper and pencil and are traditionally aimed
at what we normally refer to as continuous models from which we may find an analytical solution. As a consequence,
when teaching mechanics, it implies that we can seldomly venture beyond an idealized case
in order to develop our understandings and insights about the
underlying forces and laws of motion.

On the other hand, numerical algorithms call for approximate discrete
models and much of the development of methods for continuous models
are nowadays being replaced by methods for discrete models in science and
industry, simply because **much larger classes of problems can be addressed** with discrete models, often by simpler and more
generic methodologies. For example, [numerical integration](https://en.wikipedia.org/wiki/Numerical_integration) is an enormously important tool in physics, and it is a method that is based on discrete models.

### Analytical and Numerical Models Compliment Each Other

As we will this semester, when properly scaling the equations at hand,
discrete models open up for more advanced abstractions and the possibility to
study real life systems, with the added bonus that we can explore and
deepen our basic understanding of various physical systems

Analytical solutions are as important as before. In addition, such
solutions provide us with invaluable benchmarks and tests for our
discrete models. Such benchmarks, as we will see, allow us
to discuss possible sources of errors and their behaviors. And
finally, since most of our models are based on various algorithms from
numerical mathematics, we have a unique opportunity to gain a deeper
understanding of the mathematical approaches we are using.

### Computing is an Essential Tool for Physics

With computing and data science as important elements in essentially
all aspects of a modern society, we could then try to define Computing as
**solving scientific problems using all possible tools, including
symbolic computing, computers and numerical algorithms, and analytical
paper and pencil solutions**.
Computing provides us with the tools to develop our own understanding of the scientific method by enhancing algorithmic thinking.

The way we will teach this course reflects
this definition of computing. The course contains both classical paper
and pencil exercises as well as computational projects and exercises. The
hope is that this will allow you to explore the physics of systems
governed by the degrees of freedom of classical mechanics at a deeper
level, and that these insights about the scientific method will help
you to develop a better understanding of how the underlying forces and
equations of motion and how they impact a given system. Furthermore, by introducing various numerical methods
via computational projects and exercises, we aim at developing your competences and skills about these topics.

These competences will enable you to

- understand how algorithms are used to solve mathematical problems,

- derive, verify, and implement algorithms,

- understand what can go wrong with algorithms,

- use these algorithms to construct reproducible scientific outcomes and to engage in science in ethical ways, and

- think algorithmically for the purposes of gaining deeper insights about scientific problems.

All these elements are central for maturing and gaining a better understanding of the modern scientific process _per se_.

### What We Hope You Will Learn

The power of the scientific method lies in identifying a given problem
as a special case of an abstract class of problems, identifying
general solution methods for this class of problems, and applying a
general method to the specific problem (applying means, in the case of
computing, calculations by pen and paper, symbolic computing, or
numerical computing by ready-made and/or self-written software). This
generic view on problems and methods is particularly important for
understanding how to apply available, generic software to solve a
particular problem.

_However, verification of algorithms and understanding their limitations requires much of the classical knowledge about continuous models._

# Week 2 - Notes: Mathematical Preliminaries

We need a few things to get us started with making models of classical phenomenon. A few of those topics might be familiar to you; things like vectors, and derivatives. But we'll also need to introduce some new concepts, like the concept of [Discretization](https://en.wikipedia.org/wiki/Discretization). In particular, we will introduce a powerful method for solving all forms of Differential Equations -- Euler-Cromer Integration. We start by introducing the concept of Euler Discretization, and then we'll move on to Euler-Cromer Integration later in the course.

## Euler Discretization

Another useful formulation of Classical Mechanics uses discrete points in time to make approximate predictions of the motion. This is called the [Euler Method](https://en.wikipedia.org/wiki/Euler_method). The Euler Method is a simple numerical method to solve ordinary differential equations. The method is based on the idea of approximating the derivative of a function by a finite difference.

We posit discrete time, like snapshots of the motion where a given measure of time $t_i$ exists in a discrete set of times between $t_0$ and $t_f$. That is, $t_i \in \{t_0, t_1, t_2, \ldots, t_f\}$. We conceive of the motion as discrete like the points in the figure below.

In this case, the points are equally spaced in time, such that $t_{i+1} - t_i = \Delta t$. This gives a simple table of the motion of the object at each time step:

| time | position |
|------|----------|
| $t_0$ | $y_0$ |
| $t_1$ | $y_1$ |
| $t_2$ | $y_2$ |
| $\ldots$ | $\ldots$ |

where $y_i$ is the position of the object at time $t_i$. Here, $t_i = t_0 + i\Delta t$ -- equal time spacing -- and $y(t_i) = y_i$ indicates the position of the object at time $t_i$.

### Predicting the Motion

This formulation can be used to predict the motion of the object.  Let's first define the average velocity over a time step, $\Delta t$, like this:

$$v(t) = \dfrac{y(t+\Delta t) - y(t)}{\Delta t}$$

Now, we know that at time, $t_i$, the velocity is $v_i$: $v(t_i) = v_i$ If we make the time step small, $\Delta t \rightarrow 0$, then the average velocity is approximately the velocity at time $t_i$. Thus, we can write the velocity at time $t_{i}$ as:

$$v_{i} = \dfrac{y_{i+1} - y_i}{\Delta t}$$

**Note** If we take the limit that $\Delta t \rightarrow 0$, then the average velocity becomes the instantaneous velocity. This stems from the [Fundamental Theorem of Calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus).

$$\lim_{\Delta t \rightarrow 0} \dfrac{y(t+\Delta t) - y(t)}{\Delta t} = \dfrac{dy}{dt} = \dot{y}$$

What about the acceleration? We can use the same idea to approximate the acceleration. The average acceleration is given by:

$$a(t) = \dfrac{v(t+\Delta t) - v(t)}{\Delta t}$$

And thus, the acceleration at time $t_i$ is:

$$a_i = \dfrac{v_{i+1} - v_i}{\Delta t}$$

Again, if we take the limit that $\Delta t \rightarrow 0$, then the average acceleration becomes the instantaneous acceleration:

$$\lim_{\Delta t \rightarrow 0} \dfrac{v(t+\Delta t) - v(t)}{\Delta t} = \dfrac{dv}{dt} = \dot{v}$$

### Video Summary (13 minutes)

There's many videos covering the topic of Euler's method. Here's a video that covers the basics of Euler's method and how it can be used to solve differential equations. It somewhat follows the notes above, but it's always good to hear another perspective.

- Direct Link: [https://youtube.com/watch?v=_0mvWedqW7c](https://youtube.com/watch?v=_0mvWedqW7c)


```python
from IPython.display import YouTubeVideo

YouTubeVideo('_0mvWedqW7c', width=720, height=405)
```





<iframe
    width="720"
    height="405"
    src="https://www.youtube.com/embed/_0mvWedqW7c"
    frameborder="0"
    allowfullscreen

></iframe>




## Discretizing Newton's Second Law

We can use the Euler Method to discretize Newton's Second Law, and this allows us to predict the motion of the object using iterative methods. These methods are well-suited for computers, and we will learn how to implement them in this course.

Let there be a 1D net force acting the x-direction on an object of mass $m$, $F(x)$. Here the force changes with position. We can discretize this force as a function of position, $F(x_i)$. The net force acting on the object is:

$$F(x_i) = F_i$$

Using Newton's Second Law, we can write the acceleration of the object as:

$$a_i = \dfrac{F_i}{m}$$

But the definition of the average acceleration gives:

$$a_i = \dfrac{v_{i+1} - v_i}{\Delta t}$$

Or in terms of the predicted velocity, $v_{i+1}$:

$$v_{i+1} = v_i + a_i\Delta t$$

Or in terms of the net force:

$$v_{i+1} = v_i + \dfrac{F_i}{m}\Delta t$$

**This is the Euler formulation for predicting the velocity of the object in the next time step -- given the velocity at the current time step.**

We pause here and will return to this formulation later, but this discretization is the basis for many numerical methods in classical mechanics, and we can apply it to solve the falling object problem above.

### Looking Ahead

The development of the forward Euler scheme is the basis for many numerical methods in physics, and especially in classical mechanics. The video below is a longer introduction to the Euler Method and how it can be used to solve differential equations. It's a bit more advanced than the previous video, but it's a good introduction to the topic. We will revisit this topic a number of times, and you will have a chance to implement these methods in Python. *This video will be posted again when we cover numerical methods in more detail.*

- Direct Link: [https://www.youtube.com/watch?v=MstPeOTCVzQ](https://www.youtube.com/watch?v=MstPeOTCVzQ)


```python
from IPython.display import YouTubeVideo

YouTubeVideo('MstPeOTCVzQ', width=720, height=405)
```





<iframe
    width="720"
    height="405"
    src="https://www.youtube.com/embed/MstPeOTCVzQ"
    frameborder="0"
    allowfullscreen

></iframe>




## Additional Mathematical Preliminaries

As you have noticed, much of what we do in classical mechanics involves solving differential equations. We will explore how to solve these equations in this course. But also notice that most of the work involves vector manipulation and/or decomposition. Thus, we will need to be comfortable with vectors. Below are some mathematical concepts of vectors that we will use in this course.

### Vectors and Coordinates

The figure below shows a vector in two dimensions. 

![Vector in Two Dimensions; the vector is defined by its magnitude, $A$, and its direction, $\theta$](../../images/notes/week2/2dvector.png)

The vector is defined by its magnitude, $A$, and its direction, $\theta$. The vector can be decomposed into two components, $A_x$ and $A_y$, in the $x$ and $y$ directions, respectively.

The magnitude of the vector is given by the Pythagorean theorem:

$$|\vec{A}| = A = \sqrt{A_x^2 + A_y^2}$$

The angle of the vector is given by the tangent of the angle:

$$\theta = \tan^{-1}\left(\dfrac{A_y}{A_x}\right)$$

We can find the *vector components* using the magnitude and angle:

$$A_x = A\cos(\theta)$$
$$A_y = A\sin(\theta)$$

It's important to note that the vector components are the projections of the vector onto the $x$ and $y$ axes. The vector components are scalars, and the vector is a sum of the components. We can write the vector in several common forms:

$$\vec{A} = A_x\hat{x} + A_y\hat{y}  = A_x\hat{i} + A_y\hat{j} = A_x\hat{e}_x + A_y\hat{e}_y.$$

#### Unit Vectors

The unit vectors, $\hat{x}$, $\hat{y}$, $\hat{i}$, $\hat{j}$, $\hat{e}_x$, and $\hat{e}_y$, are the basis vectors in the $x$ and $y$ directions. The unit vectors are used to define the vector components. 

Interestingly, the angle of the vector is not needed to write the vector in Plane Polar Coordinates ($r$, $\theta$). The vector can be written as:

$$\vec{A} = A\hat{A}$$

where $\hat{A}$ is the unit vector in the direction of $\vec{A}$. Let's check that works out:

$$\vec{A} = A_x\hat{x} + A_y\hat{y}$$

$$|\vec{A}| = A = \sqrt{A_x^2 + A_y^2}$$

$$\hat{A} = \dfrac{\vec{A}}{|\vec{A}|} = \dfrac{A_x\hat{x} + A_y\hat{y}}{\sqrt{A_x^2 + A_y^2}}$$

Such that,

$$\vec{A} = A\hat{A} = A_x\hat{x} + A_y\hat{y}$$

Cartesian unit vectors are fixed in space and time when in an inertial reference frame. However, the unit vectors in Plane Polar Coordinates are not fixed in space and time. They rotate with the vector. This is a common source of confusion when working with vectors in different coordinate systems, which we will come back to later.

The magnitude of a unit vector is always one, $|\hat{A}| = 1$. And unit vectors are orthogonal to each other, $\hat{x} \cdot \hat{y} = 0$.



```python

```

### Multiplication of Vectors

#### Dot (Scalar) Product

A dot product of two vectors is a scalar quantity. The dot product of two 3D vectors, $\vec{a}$ and $\vec{b}$, is given by:

$$\vec{a} \cdot \vec{b} = a_xb_x + a_yb_y + a_zb_z$$

This product is also equal to the product of the magnitudes of the vectors and the cosine of the angle between them:

$$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos(\phi).$$ 

The figure below shows the relationship between the vectors and the angle.

![Dot Product of Two Vectors; the dot product is the product of the magnitudes of the vectors and the cosine of the angle between them](../../images/notes/week2/Dot-product.png) 

<br>
Source: [Wikipedia](images/notes/week1/File:Dot-product-1.svg)

Much like scalar multiplication, a dot produce is distributive:

$$\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$$

Here's the proof:

$$\vec{a} \cdot (\vec{b} + \vec{c}) = a_x(b_x + c_x) + a_y(b_y + c_y) + a_z(b_z + c_z)$$

$$= a_xb_x + a_xc_x + a_yb_y + a_yc_y + a_zb_z + a_zc_z$$

$$= \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$$

#### Cross (Vector) Product

The cross product of two vectors is a vector quantity. The cross product of two 3D vectors, $\vec{a}$ and $\vec{b}$, is given by:

$$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}$$

This results in a vector that has the following components:

$$\vec{a} \times \vec{b} = (a_yb_z - a_zb_y)\hat{x} - (a_xb_z-a_zb_x)\hat{y} + (a_xb_y - a_yb_x)\hat{z}$$

A few notes about cross products:

1. $\vec{a} \times \vec{b}$ always produces a vector and never a scalar.
2. $(\vec{a} \times \vec{b})_i$ denotes the $i$-th component of the cross product.
3. $\vec{a} \times \vec{b} \neq \vec{b} \times \vec{a}$; order matters.

What is the relationship between $\vec{a} \times \vec{b}$ and $\vec{a} \cdot \vec{b}$? The right-hand rule gives the direction of the cross product. The magnitude of the cross product is given by:

$$|\vec{a} \times \vec{b}| = |\vec{a}||\vec{b}|\sin(\phi)$$
$$|\vec{b} \times \vec{a}| = |\vec{a}||\vec{b}|\sin(\phi)$$

And thus both magnitudes are the same, however, the directions are opposite. 

$$\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$$

## Units

In classical mechanics, we will use the [International System of Units (SI)](https://en.wikipedia.org/wiki/International_System_of_Units). The SI units are the standard units used in science and engineering. The primary units we will use in this course are related to the motion of objects:

- **Length**: The meter, $m$, is the standard unit of length, $[r] = \mathrm{length}$.
- **Mass**: The kilogram, $kg$, is the standard unit of mass, $[m] = \mathrm{mass}$.
- **Time**: The second, $s$, is the standard unit of time, $[t] = \mathrm{time}$.


From these basic units, we can derive the other units. We also use velocity, acceleration, force, momentum, and energy. 

- **Velocity**: The meter per second, $m/s$, is the standard unit of velocity, $[v] = \mathrm{length/time}$.
- **Acceleration**: The meter per second squared, $m/s^2$, is the standard unit of acceleration, $[a] = \mathrm{length/time^2}$.
- **Force**: The Newton, $N$, is the standard unit of force, $[F] = \mathrm{mass*length/(time)^2}$.
- **Momentum**: The kilogram meter per second, $kg\cdot m/s$, is the standard unit of momentum, $[p] = \mathrm{mass*length/time}$.
- **Energy**: The Joule, $J$, is the standard unit of energy, $[E] = \mathrm{mass*length}^2/\mathrm{time}^2$.

### Example: What are the units of the drag coefficients?

Recall the drag force, $F_{air} = bv + cv^2$. The units of the drag coefficients, $b$ and $c$, can be found by examining the units of the force. The units of the force are:

$$[F_{air}] = [b][v] + [c][v^2]$$

$$\mathrm{mass*length/(time)^2} = [b]*\mathrm{length/time}+ [c]*(\mathrm{length/(time)})^2$$

The units need to match on both sides of the equation. Thus, the units of the drag coefficients are:

Thus, the units of the drag coefficients are:

$$[b] = \mathrm{mass*length/(time)^2} * \mathrm{time/length} = \mathrm{mass/time}$$

$$[c] = \mathrm{mass*length/(time)^2} * (\mathrm{time/(length)})^2 = \mathrm{mass/length}$$




# Week 2 - Computing as a tool for science



One of the first ideas that we developed was a model of a falling ball in one-dimension. We obtained the following differential equation that described the motion of the ball:

$$\ddot{y} = g - \dfrac{b}{m}\dot{y} - \dfrac{c}{m}\dot{y}^2.$$

This *nonlinear* second-order differential equation is the **equation of motion** for the ball. It is nonlinear because the term $\dot{y}^2$ appears in the equation. 

**Can you think of an anti-derivative for this equation?** *Probably not.*

We can change the equation to a system of first-order differential equations by defining a new variable $v = \dot{y}$, so that the equation becomes:

$$\begin{aligned}
\dot{y} &= v, \\
\dot{v} &= g - \dfrac{b}{m}v - \dfrac{c}{m}v^2.
\end{aligned}$$

But the equation for $v$ is still nonlinear. Clearly we need a different approach to solving this problem. In fact, we need a more generic approach to investigate equations of motion for systems like this. Most models of physical systems cannot be solved in closed analytical form. But, this approach to writing $N$th order differential equations as a system of $N$ first-order differential equations is a powerful tool in computational physics.



```{admonition} Limitations of only working with analytically solvable problems
:class: note

The problems that we often present in physics classes lend themselves to analytical solutions because we (collectively as a physics community) decided on the kinds of illustrative problems for students to work and solve. We did this at a time when computing was inaccessible and less pervasive in society, but also when we knew little about how people learn.

The choices we made in the past convey a false impression that most physics problems can be solved analytically. But more importantly, our choices convey that finding the solution is the goal of physics. This is not the case. The goal of physics is to understand the world around us. When we continue to focus exclusively on systems that can be solved analytically, we continue to perpetuate those impressions. 

There's a movement of physics instructors across the world building these forward-looking pedagogies and curricula. They work loosely through a collective called the [Partnership for Integration of Computation into Undergraduate Physics (PICUP)](https://www.compadre.org/PICUP/). 

In our class, we aim to build a set of investigative tools and approaches that we can use in Classical Mechanics.
```

## Scientific Computing

In this course, we will explore a broad class of problems using plotting and numerical integration as principal tools. These techniques and algorithms, along with the software we use, fall within the broader field of [scientific computing](https://en.wikipedia.org/wiki/Scientific_computing). Scientific computing focuses on developing mathematical models and numerical methods to solve problems in the natural sciences and engineering.

For historical context, the [Timeline of the Development of Scientific Computing](https://en.wikipedia.org/wiki/Timeline_of_scientific_computing) provides an excellent overview. The roots of this field trace back to significant advancements long before modern electronic devices. Much of the foundational mathematics, such as [Euler’s Method](https://en.wikipedia.org/wiki/Euler_method) for solving differential equations, was developed in the 18th century by [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler). Implementing these algorithms on computers was a natural progression in scientific problem-solving.

### History of Computing

The history of scientific computing is deeply intertwined with the evolution of computing itself, a fascinating and complex narrative encompassing technical, social, political, and economic perspectives. Contributions to computing originated worldwide, starting with tools like the [abacus](https://en.wikipedia.org/wiki/Abacus) in ancient China. Mechanical innovations such as [Pascal’s adding machine](https://en.wikipedia.org/wiki/Pascal%27s_calculator) and [Babbage’s Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine) marked significant milestones leading toward the modern computer.

To get an introductory overview, the video below from Futurology is a helpful resource, but it is by no means comprehensive or critical.

[![](images/notes/week1/hqdefault.jpg)](https://youtube.com/watch?v=-M6lANfzFsM)

Source: <https://www.youtube.com/watch?v=-M6lANfzFsM>

## A Critical Perspective on Computing

While the history of computing is often celebrated as a story of innovation, it is deeply entangled with systems of power, exploitation, and violence. Computing technologies have not only been tools of scientific progress but also instruments for surveillance, war, and perpetuation of systemic biases.

```{admonition} Humans as Computers
:class: note

Of course, the development of electronic computers was a huge development for science. Prior to that, humans were employed to do the calculations that we now do with computational algorithms. This work occurred in a wide variety of labs where data were entered into tables, calculations were done by hand, and the results were tabulated manually. 

Frequently the work was done by those with less power in the laboratory and broader society (e.g., women, immigrants, and folks of color). A notable and well-known example is the work of the [Harvard Computers](https://en.wikipedia.org/wiki/Harvard_Computers) in the late 19th and early 20th centuries where women were employed to do the calculations that led to significant discoveries in astronomy. 

![Harvard Computers](../../images/notes/week2/harvard-computers.png)

One of the most important examples is the work done by African-American women at NASA in the 1960s, as depicted in the book and movie [Hidden Figures](https://en.wikipedia.org/wiki/Hidden_Figures).

![Hidden Figures](../../images/notes/week2/nasa-computers-hidden-figures.png)

Women highlighted in this work include: [Williamina Fleming](https://en.wikipedia.org/wiki/Williamina_Fleming), [Florence Cushman](https://en.wikipedia.org/wiki/Florence_Cushman), [Katherine Johnson](https://en.wikipedia.org/wiki/Katherine_Johnson), [Dorothy Vaughan](https://en.wikipedia.org/wiki/Dorothy_Vaughan), and [Mary Jackson](https://en.wikipedia.org/wiki/Mary_Jackson).
```

The algorithms driving modern computing are not neutral—they reflect the biases of the societies that create them. In [Cathy O’Neil’s *Weapons of Math Destruction*](https://www.penguinrandomhouse.com/books/241363/weapons-of-math-destruction-by-cathy-oneil/), the author explores how algorithms used in areas like policing, hiring, and education often reinforce systemic inequality, disproportionately harming marginalized communities. Similarly, [Ruha Benjamin’s *Race After Technology*](https://www.ruhabenjamin.com/race-after-technology) examines how race and technology intersect, showing how seemingly “objective” systems encode and perpetuate racial biases.

The use of AI in policing is another area of concern. [Simone Browne’s *Dark Matters*](https://www.dukeupress.edu/dark-matters) highlights how surveillance technologies, from facial recognition to predictive policing, are rooted in practices of racialized social control, extending systems of oppression into the digital realm.

The militarization of AI is one of the most alarming developments in computing. AI-driven drones and autonomous weapons, often described as the future of warfare, raise profound ethical and humanitarian concerns. [Shoshana Zuboff’s *The Age of Surveillance Capitalism*](https://shoshanazuboff.com/book/about/) discusses how the same technologies used for corporate profit are repurposed for state surveillance and military applications, blurring the lines between civilian and combatant spaces.

Additionally, [Peter Asaro’s work on lethal autonomous weapons](https://peterasaro.org/writing/Asaro%20Oxford%20AI%20Ethics%20AWS.pdf) questions the morality and legality of machines making life-and-death decisions. Meanwhile, [Kate Crawford’s *Atlas of AI*](https://katecrawford.net/atlas) explores how AI systems, from mining rare earth materials to deployment in warfare, are deeply intertwined with colonial exploitation and ecological destruction.

The tech industry's focus on profit has devastating environmental and social impacts. Computing relies on the extraction of rare materials, energy-intensive processes, and exploitative labor practices. [Naomi Klein’s *This Changes Everything*](https://thischangeseverything.org/) examines how capitalism exacerbates climate change, with insights into the environmental toll of computing technologies. [Yarden Katz’s *Artificial Whiteness*](https://cup.columbia.edu/book/artificial-whiteness/9780231194914) connects the development of AI to broader systems of capitalist and racial oppression.

## Additional Resources for Exploration

For deeper dives into these ideas, consider the following materials:

| Resource | Description |
|----------|-------------|
| [George Dyson’s *Turing’s Cathedral*](https://www.penguinrandomhouse.com/books/44425/turings-cathedral-by-george-dyson/) ![Turing's Cathedral](../../images/notes/week2/dyson.png) | Chronicles the origins of the modern computer, focusing on [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) and his team at Princeton in the 1940s. This book delves into the intersection of mathematics, physics, and computation, highlighting the development of the first stored-program computers and their role in shaping the digital age. |
| [James Gleick’s *The Information*](https://www.penguinrandomhouse.com/books/60765/the-information-by-james-gleick/) ![The Information](../../images/notes/week2/gleick.png) | Explores the transformative impact of information theory on science, technology, and culture. From the invention of writing to the digital age, Gleick highlights key figures like Michigander [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon), who revolutionized communication with his groundbreaking mathematical theory of information. |
| [Steven Levy’s *Hackers*](https://www.stevenlevy.com/hackers-heroes-of-the-computer-revolution) ![Hackers](../../images/notes/week2/levy.png) | Chronicles the rise of hacker culture, from early computer pioneers to the creators of the personal computer revolution. Levy examines the "hacker ethic," emphasizing creativity, open access, and the joy of problem-solving, which shaped the tools and technologies we use today. |
| [Cathy O’Neil’s *Weapons of Math Destruction*](https://www.penguinrandomhouse.com/books/241363/weapons-of-math-destruction-by-cathy-oneil/) ![Weapons of Math Destruction](../../images/notes/week2/oneill.png) | Explores how algorithms, often marketed as objective, exacerbate inequality in policing, hiring, and credit scoring. O’Neil critically examines the dangers of data-driven systems that disproportionately harm marginalized communities while remaining opaque and unregulated. |
| [Ruha Benjamin’s *Race After Technology*](https://www.ruhabenjamin.com/race-after-technology) ![Race After Technology](../../images/notes/week2/benjamin.png) | Analyzes how algorithms and technologies reinforce systemic racism under the guise of neutrality. Benjamin introduces the concept of the “New Jim Code,” highlighting the ways in which technological tools amplify inequities while appearing fair and impartial. |
| [Simone Browne’s *Dark Matters*](https://www.dukeupress.edu/dark-matters) ![Dark Matters](../../images/notes/week2/browne.png) | Examines how surveillance technologies are deeply rooted in practices of racialized social control. Browne connects historical practices like slave surveillance to modern tools like facial recognition and predictive policing, revealing the persistence of systemic inequities in new forms. |
| [Kate Crawford’s *Atlas of AI*](https://katecrawford.net/atlas) ![Atlas of AI](../../images/notes/week2/crawford.png) | Explores the hidden costs of artificial intelligence, from resource extraction to labor exploitation and military applications. Crawford critiques AI as an extractive industry that reshapes power dynamics and perpetuates global inequalities while causing significant environmental damage. |
| [Shoshana Zuboff’s *The Age of Surveillance Capitalism*](https://shoshanazuboff.com/book/about/) ![Age of Surveillance Capitalism](../../images/notes/week2/zuboff.png) | Investigates how corporations and governments exploit personal data for profit and control. Zuboff coins the term "surveillance capitalism" to describe how the tech industry commodifies human behavior, eroding privacy and autonomy while reshaping society’s power structures. |



# Week 3 - Notes: Making Classical Models

The central enterprise of physics is making and testing models of physical systems. These models we developed are based on the assumptions we make about the physical systems we are studying. As we characterize the system, we make simplifying assumptions that allow us to describe the system in terms of a few key quantities. These quantities are often called the ["degrees of freedom"](https://en.wikipedia.org/wiki/Degrees_of_freedom_(physics_and_chemistry)) of the system.

In Classical Mechanics, we will use formulations of physics, such as [Newton's Laws](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion), to describe the motion of particles. We can also use the [Lagrangian](https://en.wikipedia.org/wiki/Lagrangian_mechanics) and [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) formulations of mechanics. These formulations are mathematical expressions of the physical laws that govern the motion of particles.

Typically, those expressions are [differential equations](https://en.wikipedia.org/wiki/Differential_equation) that describe how the system evolves in time. Our work in classical mechanics is to develop techniques and tools that let us investigate the solutions to these equations. These differential equations are commonly called [equations of motion](https://en.wikipedia.org/wiki/Equations_of_motion) (EOM). An equation of motion describes the evolution of the agents (particles) as they interact with their surroundings and each other.

## Newtonian Examples of Classical Models

From a Newtonian perspective, our equations of motion are often second-order differential equations. This stems from the fact that Newton's second law relates the acceleration of a particle to the forces acting on it. The second law is given by the equation:

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

where $\vec{x}$ is the position vector and $\ddot{\vec{x}}=\frac{d^2\vec{x}}{dt^2}$ is the acceleration vector. Thus, Newton's second law is a general EOM that describes the dynamics of a particle of mass, $m$:

$$\frac{d^2\vec{x}}{dt^2} = \dfrac{\vec{F}_{\text{net}}}{m}$$

```{admonition} What is Dynamics?

Dynamics is the study of the time evolution of a system in question. In classical mechanics, dynamics is the study of the motion of particles and the forces that cause that motion. In other physics, dynamics can refer to the study of the evolution of a system in time and space. And here, space might be an abstraction, such as a [phase space](https://en.wikipedia.org/wiki/Phase_space). We study phase spaces later in the term.
```

### Example: Falling Ball with No Air Resistance

Consider a ball of mass $m$ falling down. We define the positive $y$ direction to be down as in the figure showing the FBD of the ball. 

![FBD of a falling ball](../../images/notes/week3/1d-ball-fbd.png)

We can apply Newton's laws to obtain the specific EOM for the ball.

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

This is a 1D case in the $y$ direction,

$$F_{\text{net,y}} = W = mg = m \ddot{y}$$

Thus,

$$\ddot{y} = g$$

is the specific EOM for the ball. 

### Example: Simple Harmonic Oscillator

We will spend a lot of time studying the [simple harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator) (SHO) in this course. The SHO is a system that oscillates back and forth around an equilibrium position. It is a very common system in physics and is used a base model for many more complex systems. Consider a mass, $m$, attached to a spring with spring constant, $k$, sitting on a frictionless horizontal plane as in the figure below.

![FBD of a simple harmonic oscillator](../../images/notes/week3/sho_horizontal.png)

The EOM for the SHO can be derived form Newton's Second Law.

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

This is a 1D case in the $x$ direction,

$$F_{\text{net,x}} = F_{\text{spring}} = -kx = m \ddot{x}$$

And thus,

$$\ddot{x} = -\dfrac{k}{m}x$$

is the specific EOM for the SHO. As we will learn, this restoring force causes the mass to oscillate back and forth around the equilibrium position, with a well known frequency, $\omega = \sqrt{\dfrac{k}{m}}$.

## Turning Observations into Models

One of the more challenging aspects of physics is how we work to make models of the observations we have. This a long and challenging process in general, but if we have a general schematic, we can make progress. The hand drawn figure below provides such a schematic.

![Framework for making models](../../images/notes/week3/prelim_framework.png)

In the schematic, our observations are the starting point. Using our framework for physics (e.g., Newton's Laws) and making the appropriate assumptions (in blue), we can develop a model (in red) of the system. By conducting analysis and investgating the evolution of the model, we produce predictions (in green). We can then compare tose predictions to our observations to evaluate how well our model describes the system.

In this class, we mostly focus on the elements circled in purple where we develop models, and use them to predict. The core part of this class is the orange circled elements of modeling and predicting. We will spend a lot of time developing the tools and techniques to make these predictions.

### Modeling Process

Making models of physical systems is greatly helped by considering the following steps:

- Identify the phenomenon or system of interest.
- Identify the interactions the system has with its surroundings.
- Choose an appropriate physics framework to investigate the system (Newton? Lagrange? Hamilton? Continuous or Discrete?).
- Sketch the system and identify the interactions, name them, and assign them to the appropriate framework.
- Choose your coordinate system and define your variables.
- Apply the appropriate physics framework to the system.
- **Obtain the equations of motion**, and make predictions.

Let's turn to an example you have seen before: the falling ball.

### Example: Falling Ball in 1D

Consider a ball of mass $m$ falling with air resistance. Here, we have already done some of the work above. We have identified the phenomenon, and started to indicate the interactions. 

![FBD of a falling ball with air resistance](../../images/notes/week3/1d-ball-fbd-air.png)

In the figure above, we have identified the forces acting on the ball. We have the gravitational force, $W = mg$, and the air resistance, $F_{\text{air}}$. We have chosen the linear mode for air-resistance, which is a choice of model given the assumption that the ball moves very slowly -- *this is not a good assumption in this case*, but makes the mathematical analysis simpler.

We have also chosen our coordinate system, with the positive $y$ direction pointing down.

We choose a Newtonian framework for our physics because we are familiar with it. And thus, we can develop the EOM:

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

In 1d,

$$F_{\text{net,y}} = W - F_{\text{air}} = mg - bv = m \ddot{y}$$

So that the EOM is,

$$\ddot{y} = g - \dfrac{b}{m}v$$

#### Question: What happens with $\ddot{y} = 0$?

Once the ball has no acceleration, the two forces are balanced. This is the terminal velocity of the ball. We can solve for this by setting $\ddot{y} = 0$:

$$0 = g - \dfrac{b}{m}v_{\text{term}}$$

$$v_{\text{term}} = \dfrac{mg}{b}$$

This is the terminal velocity of the ball for linear drag. When the ball reaches this speed (and does so asymptotically), the forces are balanced and the ball will fall at a constant speed.

#### Question can we solve this differential equation?

The differential equation $\ddot{y} = g - \dfrac{b}{m}v$ is a second-order differential equation for $y$. We can solve this equation analytically by recasting it as a first-order differential equation for $v$, which we solve for and then integrate to find $y(t)$.

$$\dot{v} = g - \dfrac{b}{m}v$$

We will do that later, for now, let's hack off the drag bit and return to the simple falling ball. Our simplified EOM is:

$$\ddot{y} = g$$

Note this is written as a second order ODE for $y$:

$$\dfrac{d^2y}{dt^2} = g$$

It is possible also to recast these kinds of second-order differential equations as a pair of 1st order differential equations for $y$ and $v$:

$$\dfrac{dv}{dt} = g \qquad \dfrac{dy}{dt} = v$$

This is a common technique in physics and engineering to solve second-order differential equations. Let's solve this for completeness.

$$\dfrac{dv}{dt} = g \longrightarrow \textrm{a constant}$$

We can integrate:

$$\int_{v_0}^{v(t)} dv = \int_{0}^{t} g dt$$

$$v(t) - v_0 = gt$$

We obtain the velocity as a function of time for constant acceleration:

$$v(t) = v_0 + gt$$

Now we can integrate the velocity to obtain the position as a function of time:

$$\dfrac{dy}{dt} = v \longrightarrow \textrm{a function of time}$$

$$\int_{y_0}^{y(t)} dy = \int_{0}^{t} v_0 + gt dt$$

$$y(t) - y_0 = v_0 t + \dfrac{1}{2}gt^2$$

We obtain the position as a function of time for constant acceleration, the standard kinematic equation:

$$y(t) = y_0 + v_0 t + \dfrac{1}{2}gt^2$$

Why the 'plus' sign on the last term? Because we choose positive $y$ to be down, and the ball is accelerating down.

```{note}
This is really useful, but is contingent on finding or knowing the anti-derivative of the functions we are integrating. That is not always possible. What might we do if we weren't sure that we could find the anti-derivative?
```

## Discrete Formulation of Newtonian Mechanics

Most of our experience so far has been solving problems where we can find continuous functions that are the anti-derivatives of the functions we are integrating. This leads to standard formulae that we can use to predict or plot our results. 

However, there are very few systems for which we can write down EOMs that have known solutions. In these cases, we need to turn to numerical methods to solve the equations of motion. To do this, we need a discrete formulation of the EOMs. 

Let's focus on 1D:

$$\dfrac{d^2y}{dt^2} = \dfrac{F}{m}$$

We can write this as a pair of first-order differential equations:

$$\dfrac{dy}{dt} = v \quad \textrm{and} \quad \dfrac{dv}{dt} = \dfrac{F}{m}$$

Let's allow ourselves to consider instead a small time interval of the evolution, $\Delta t$. We can then write the velocity equation as:

$$\dfrac{dv}{dt} = \dfrac{\Delta v}{\Delta t}= \dfrac{v(t+\Delta t) - v(t)}{\Delta t} = \dfrac{F}{m}$$

We can turn this into a discrete equation by multiplying through by $\Delta t$: prediction of the velocity at the next time step:

$$v(t+\Delta t) = v(t) + \dfrac{F}{m} \Delta t$$

This is the "velocity update" equation, or more generally, the [Euler step](https://en.wikipedia.org/wiki/Euler_method) for velocity. Given the information at time $t$, $F(t)$, $m$, and $v(t)$, we can predict the velocity at the next time step.

$$v(t+\Delta t) = v(t) + \dfrac{F(t)}{m} \Delta t$$

Great! But that is just for velocity, can we do the same for position?

**Yes**

We can use the same logic to predict the position at the next time step:

$$\dfrac{dy}{dt} = v$$

If we discretize this, we realize we just have the definition of the average velocity:

$$\dfrac{dy}{dt} = v_{\textrm{avg}}$$

We can then write the position update equation:

$$y(t+\Delta t) = y(t) + v_{\textrm{avg}} \Delta t$$


What is left is to determine what should be the estimate for $v_{\textrm{avg}}$. 

```{admonition} Choosing $v_{\textrm{avg}}$
:class: note

The idea that we have to pick a value for $v_{\textrm{avg}}$ is a key point in numerical methods. It might seem silly or overly subtle and it certainly the latter. We can select $v(t)$, $v(t+\Delta t)$, or some average of the two. The choice of $v_{\textrm{avg}}$ is the key to the accuracy of the method.

As we will show in a later homework, the best choice is $v(t+\Delta t)$ as it preserves the energy of the system. 
```


### Euler-Cromer Step

Taken together, we obtain the [Euler-Cromer](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method) step for the position and velocity:

$$v(t+\Delta t) = v(t) + \dfrac{F(t)}{m} \Delta t$$
$$y(t+\Delta t) = y(t) + v(t+\Delta t) \Delta t$$

This method was accidentaly discovered by a high physics student called Abby Aspel. It was later explored by [Alan Cromer](https://en.wikipedia.org/wiki/Alan_Cromer) whote wrote up this [method in the American Journal of Physics](https://aapt.scitation.org/doi/10.1119/1.10903). 


In three-dimensions, this method is simply written in a vector form:

$$\vec{v}(t+\Delta t) = \vec{v}(t) + \dfrac{\vec{F}(t)}{m} \Delta t$$
$$\vec{r}(t+\Delta t) = \vec{r}(t) + \vec{v}(t+\Delta t) \Delta t$$


```{admonition} Erasing Contributions in Physics
:class: note
This method should be called the Euler-Aspel-Cromer method because Euler started it, Aspel discovered it, and Cromer formalized it. 

It is not because physics and physicists tend to erase the contributions of marginalized groups including young people, women, and folks from non-dominant groups.

**Don't believe it?**

Read about the [history of the MIT physics department](https://physics.mit.edu/about-physics/our-history/) and try to find the contributions of the many technical staff, non-tenure track faculty, and students who have made the department what it is today.
```

## Analytical Solutions to the Air-Resistance Problem

We can solve the air-resistance problem analytically. We have the EOM for velocity:

$$\dot{v} = g - \dfrac{b}{m}v - \dfrac{c}{m}v^2$$

### Linear Drag

Let's take the linear limit first, $c=0$. 

$$\dot{v} = g - \dfrac{b}{m}v$$

We can solve this equation by separating variables:

$$\dfrac{dv}{g - \dfrac{b}{m}v} = dt$$

We can integrate both sides:

$$\int \dfrac{dv}{g - \dfrac{b}{m}v} = \int dt$$

$$-\dfrac{m}{b} \ln|g - \dfrac{b}{m}v| = t + C$$

We can solve for $v(t)$:

$$g - \dfrac{b}{m}v = e^{-\dfrac{b}{m}t - C}$$

$$v(t) = \dfrac{mg}{b} - e^{-\dfrac{b}{m}t - C}$$

We can solve for the constant $C$ by using the initial condition $v(0) = v_0$:

$$v_0 = \dfrac{mg}{b} - e^{-C}$$

$$e^{-C} = \dfrac{mg}{b} - v_0$$

$$v(t) = \dfrac{mg}{b} - \left(\dfrac{mg}{b} - v_0\right)e^{-\dfrac{b}{m}t}$$

When $v_0 = 0$, we find:

$$v(t) = \dfrac{mg}{b}\left(1 - e^{-\dfrac{b}{m}t}\right)$$

And as $t \to \infty$, we find the terminal velocity:

$$v_{\text{term}} = \lim_{t \to \infty} v(t) = \dfrac{mg}{b}$$

### Quadratic Drag

In the case of quadratic drag, we have:

$$\dot{v} = g - \dfrac{c}{m}v^2$$

We can find the terminal velocity by setting $\dot{v} = 0$:

$$0 = g - \dfrac{c}{m}v_{\text{term}}^2$$

$$v_{\text{term}} = \sqrt{\dfrac{mg}{c}}$$


Thus, we recast the problem in terms of the terminal velocity:

$$\dot{v} = g\left(1 - \dfrac{v^2}{v_{\text{term}}^2}\right)$$

We can separate variables and integrate:

$$\int \dfrac{dv}{1 - \dfrac{v^2}{v_{\text{term}}^2}} = \int g dt$$

#### Assume we start at rest, $v(0) = 0$

We can solve for $v(t)$, by using the proper limits:

$$\int_{0}^{v(t)} \dfrac{dv}{1 - \dfrac{v^2}{v_{\text{term}}^2}} = \int_{0}^{t} g dt$$

This is a known integral and yields:

$$\dfrac{v_{\text{term}}}{2}\ln\left|\dfrac{v_{\text{term}} + v}{v_{\text{term}} - v}\right| = gt$$

With the initial condition $v(0) = 0$, we find:

$$\dfrac{v_{\text{term}}}{g} \tanh^{-1}\left(\dfrac{v}{v_{\text{term}}}\right) = t$$

And thus, we find the velocity as a function of time:

$$v(t) = v_{\text{term}}\tanh\left(\dfrac{gt}{v_{\text{term}}}\right)$$




```python

```


# Week 3 - What is Mathematical Modeling?

Nature reveals itself to us through interactions. We can tell from observations that it is nature's interactions that lead to its evolution. How nature is changing and predicting how it will change in the future is the work of science. In this work, we observe nature and its interactions to make models of those observations. We aim to predict and explain our observations of nature through this building of models.

In physics, our goals are typically to explain and predict observations of physical phenomenon. Here, we focus ourselves to those canonical things that physicists concern themselves with: motion, fields, waves, atoms, nuclei, and so on. 

```{admonition} Why the word "observation"?
:class: note

We intentionally use the word observations here, because we are not simply talking about what we can see with our eyes. The visible spectrum is limited to a small portion of the [electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum). 

These observations can come in the form of light, but also as sound, voltage, or current. For example, most instrumentation in laboratories will report only voltages or currents -- rather voltages and currents are what the equipment will measure precisely and report as measurements as different as [distance](https://en.wikipedia.org/wiki/Laser_rangefinder) and [shear stress response](https://en.wikipedia.org/wiki/Rheometer). 

Lastly, we use "observation" because it includes the historical science that conducted qualitative investigations and conceptual observations. It is also language that includes the work of early cultures who made observations and constructed ways of knowing and explaining the world around them. 
```

## What is a model?

Physics is a science that builds models. Typically, these models are represented mathematically in the form of equations or formula, but we can use charts, graphs, animations, and so on to represent our models. Models used in physics are often constructed by a community of scientists who have agreed on the model's utility and accuracy. Experimental observations are used to validate these models.

Modeling is the process of constructing a model. This process is often iterative where the initial ideas and assumptions are used to formulate a model. It is then tested against observations and refined. This process is repeated until the model is accurate enough to be useful. Physicists are model builders and model users. 

Geoscientist [John Aiken](https://mnky9800n.github.io/) made this short video when he was a graduate student at Georgia Tech. John cut clips from a lecture [Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman) gave. In this lecture, Feynman talks about the nature of models and the process of science.  John also interviewed different science researchers and teachers about their understanding of what a model is. 

[![](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=dkTncoPqo5Y)

Source: <https://www.youtube.com/watch?v=dkTncoPqo5Y>



### Feynman on the Process of Science

[Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman) was a physicist who made significant contributions to physics, especially in the field of quantum mechanics. He was awarded the [Nobel Prize in Physics in 1965](https://www.nobelprize.org/prizes/physics/1965/feynman/) for his work in quantum electrodynamics. In his time, he was known as a great teacher and communicator of physics. And [his lectures](https://www.feynmanlectures.caltech.edu/) are still used in physics education today -- even for planning this class.

Feynman was a gifted communicator; his lectures are lively and conceptual. Here's the longer version of the lecture he gave on the nature of models and the process of science.

[![](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=EYPapE-3FRw)

Source: <https://www.youtube.com/watch?v=EYPapE-3FRw>

```{admonition} Richard Feynman's Legacy
:class: warning

While we acknowledge the importance of Feynman's contributions to physics and physics teaching, we should remind ourselves that he was not a perfect person. Feynman was also known for his [sexist behavior and comments](https://thebaffler.com/outbursts/surely-youre-a-creep-mr-feynman-mcneill). (*Trigger warning*: this link recounts instances of harassment) 

We should not ignore this aspect of his life, and remind ourselves that we can learn from his physics and make a welcoming space for all people.
```

### History and Philosophy of Science

If you would like to dive deeper into models and modeling, there's excellent work in history and philosophy of science. The field studies how science develops knowledge, practice, culture, and so on. It studies important events and provides critical information on important and, often, overlooked folks who do science. For example, historian and gender studies professor [Sharon Traweek](https://en.wikipedia.org/wiki/Sharon_Traweek) studies the high energy physics field. Her book, [Beamtimes and Lifetimes: The World of High Energy Physicists](https://en.wikipedia.org/wiki/Beamtimes_and_Lifetimes) is excellent.

```{admonition} Dame Nancy Cartwright (philosopher of science)
:class: note

One of the more interesting scholars is [Dame Nancy Cartwright](https://en.wikipedia.org/wiki/Nancy_Cartwright_(philosopher)) who wrote a lot about the 'practice of science.' Her philosophical work informed many of the innovations in physics and broader science education -- including many science courses at MSU. 

Her writing is very interesting, but the style of writing can be a challenge to read. This is the nature of academic writing in different disciplines. Her book called "How The Laws of Physics Lie" is worth a read. Here's a link to the [first chapter](http://www.generativescience.org/papers/nature/Cartwright-_1983.pdf).
```
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


# Week 4 - Why does fluid drag complicate things?

As an object moves through the fluid, the molecules of the fluid collide with the object and exert a force on it. This collision changes the momentum oof the object just a little bit. The collision does so in a random way, but the average effect of all those collisions is to exert a force on the object that is proportional to a function of the object's velocity, $F(v)$. In some cases those collisions occur such that they make an impact; other times they might approach the object more slowly and slide over it in a more frictional interaction. These two behaviors are both fluid drag, but they are different forms.

The first form ($F \sim v^2$) describes the behavior of things like a skydiver falling, a high-speed car, or a baseball thrown through the air. But it can also be valid for the movement of fish in water, or a submarine moving through the ocean.  Through those collisions, the distribution of those forces can cause intra-body forces, which can result in damage or deformation of the object. However, we often model the body as solid and focus on the way this form of air resistance changes the motion. 

This form of air resistance cannot describe the behavior of objects approaching the speed of sound in the fluid. Objects moving a speeds that high can produce [shock fronts](https://en.wikipedia.org/wiki/Shock_wave) that forces the fluid to go through abrupt changes in density, pressure, and temperature. Below is a figure of a shock front produced the nose of a jet flying at supersonic speeds.

![A shock front from a supersonic jet](images/notes/week1/Schlierenfoto_Mach_1-2_Pfeilfl%C3%BCgel_-_NASA.jpg)

The second form ($F \sim v$) describes the flow of a viscous fluid around a solid object. You might think of this as pulling an object through some viscous oil, honey, or even molasses. The movement of the fluid around the object exerts a force and slows the motion of the object.  In water, this form can explain the motion of some of the smallest creatures on Earth, like the [water bear](https://en.wikipedia.org/wiki/Tardigrade), an amoeba, or a paramecium. 

What is interesting here is that these creatures have had to adapt to this form of fluid drag. [Edward Purcell](https://en.wikipedia.org/wiki/Edward_M._Purcell) wrote a paper in 1977 called [Life at Low Reynolds Number](../../docs/papers/purcell_AJP_1977.pdf) that describes the motion of these creatures. He demonstrates that the physics in this regime requires creature to have adapted forms of locomotion that can take advantage of that environment.



## Why do we often neglect air resistance?

We're in the business of making models of physical systems using the concepts and tools of Classical Mechanics. We've focused on Newton's Laws, which are a formulation of mechanics that starts from the concept of the force. 

We often start with that approach because the mathematical tools that we have available to us when we are first learning physics are geometry and algebra. Forces are a vector concept and Newton's Second Law is a vector equation that holds in each of the three dimensions of space. This formulation lends itself to a decomposing problems often into two or three separate problems, one for each dimension, and then using some algebra to solve the problems. However, that mathematics limits the kinds of explorations we can do.

This is one reason why we neglect [air resistance](https://en.wikipedia.org/wiki/Air_resistance) in our first explorations of motion. Our models of air resistance are more complicated and require more advanced mathematics to solve. The equations of motion can be coupled and non-linear. In some cases, we cannot solve the equations of motion analytically and must resort to numerical methods like [Euler's method](https://en.wikipedia.org/wiki/Euler_method), or the more often used [Runge-Kutta method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods).

## The Reynolds Number

The different forms of fluid drag are often described by a dimensionless number called the [Reynolds Number](https://en.wikipedia.org/wiki/Reynolds_number). The Reynolds number is a ratio of the inertial forces to the viscous forces in a fluid. 

* What are inertial forces? They are the ones associated with resistance to motion, the mass of the object. The more massive the object in a given setup, the higher the inertial contribution.
* What are viscous forces? They are the ones associated with the interaction of the fluid with the object. The more viscous the fluid - the harder it for is to flow under the same conditions, the higher the viscous contribution.

The Reynolds number is defined as:

$$Re = \frac{\rho v L}{\mu}$$

where $\rho$ is the density of the fluid, $v$ is the velocity of the object in that fluid, $L$ is a characteristic length of the object, and $\mu$ is the dynamic viscosity of the fluid. 

You can probably see who the Reynolds number characterizes the system of the object and the fluid as their are properties of both the object and the fluid in the equation. The Reynolds number can be measured quite accurately in a lab because the laboratory setups are typically designed to make the measurement of the Reynolds number easier. We will often estimate it in theoretical physics.

### What is a characteristic length?

This length is a generic length scale associated with the flow, this can be the order of magnitude size of the object, or, in the absence of an object, the same for the pipe or channel in which the flow is occurring. If it's an airplane, it can be the wingspan, or the length of the fuselage. If it's a car, it can be the length of the car. If it's a sphere, it can be the radius, and so on. 

### What is dynamic viscosity?

Viscosity is the measure of the fluid's resistance to flow. It's how the fluid slides past itself. It's a bit of a harder quantity to describe, but you can think of it as the "stickiness" of the fluid. The higher the viscosity, the more sticky the fluid is -- really, for a given setup, the more viscous fluid will flow more slowly. The lower the viscosity, the higher tendency for a fluid to flow. Compare honey to water in the same vessel and temperature, and you'll observe the difference in viscosity.

#### Measuring viscosity

We can sometimes measure viscosity with a [viscometer](https://en.wikipedia.org/wiki/Viscometer), which uses a [capillary tube](https://en.wikipedia.org/wiki/Capillary_tube) to measure the time it takes for a fluid to flow through a tube of known dimensions. However, this works best for [Newtonian fluids](https://en.wikipedia.org/wiki/Newtonian_fluid), which are fluids that have a constant viscosity. 

#### Non-Newtonian fluids (in your kitchen)

Not all fluids are Newtonian, and some fluids have a viscosity that changes with the rate of flow. These [non-Newtonian fluids](https://en.wikipedia.org/wiki/Non-Newtonian_fluid) can be [shear thinning](https://en.wikipedia.org/wiki/Shear_thinning) or [shear thickening](https://en.wikipedia.org/wiki/Shear_thickening). Shear thinning fluids become less viscous when they are stirred or shaken, while shear thickening fluids become more viscous when they are stirred or shaken.

Below is a video from [America's Test Kitchen](https://www.americastestkitchen.com/) that demonstrates the behavior of a non-Newtonian fluid. The fluid is made from cornstarch and water, and it's called [oobleck](https://en.wikipedia.org/wiki/Oobleck). 

[![America's Test Kitchen Non-Newtonian Fluids](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=FrLh1GILomc)

Source: <https://www.youtube.com/watch?v=FrLh1GILomc>

The physics of cooking is fascinating and covers the field of [soft matter physics](https://en.wikipedia.org/wiki/Soft_matter). There's a free course on the subject offered by [Harvard and EdX](https://pll.harvard.edu/course/science-cooking-haute-cuisine-soft-matter-science-physics).

### Low Reynolds Number Flows

A low Reynolds number flow is a flow where the viscous forces dominate the inertial forces. The object is moving slowly, or the fluid is very viscous, or the object is very small. We typically think of these flows as being in the range of $Re < 1$. In these flows, the motion of the fluid is typically laminar; it flows in fairly smooth and parallel layers. Low Reynolds number flows can produce dynamics that is counterintutive. Below are a couple videos that explain the physics of low Reynolds number flows.

#### Physics of Life - Life at Low Reynolds Number (15 minute video)

This video focuses on the biological aspects of the problem as the physics of low Reynolds numbers is important for understanding the motion of microorganisms. 

[![Physics of Life - Life at Low Reynolds Number](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=gZk2bMaqs1E)

Source: <https://youtube.com/watch?v=gZk2bMaqs1E>

#### G.I. Taylor's Low Reynolds Number Flows (32 minute video)

This video is a classic from [G.I. Taylor](https://en.wikipedia.org/wiki/Geoffrey_Ingram_Taylor) who was a physicist interested in sharing the conceptual beauty of physics with the general public. He was also a pioneer in the field of fluid mechanics. In fact, Taylor's [groundbreaking paper](../../docs/papers/taylor_1922.pdf) on the stability of fluid flows between two rotating cylinders set off studies into turbulence. The [Taylor-Couette flow](https://en.wikipedia.org/wiki/Taylor%E2%80%93Couette_flow) is a critical tool for [studies of turbulence](https://pubmed.ncbi.nlm.nih.gov/20365623/).

[![G.I. Taylor's Low Reynolds Number Flows](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=8Dst6V4CQME)

Source: <https://youtube.com/watch?v=8Dst6V4CQME>

### High Reynolds Number Flows

In high Reynolds number flows, the inertial forces dominate the viscous forces. The object is moving quickly, or the fluid is not very viscous, or the object is very large. We typically think of these flows as being in the range of $Re > 1000$. In these flows, the motion of the fluid is typically [turbulent](https://en.wikipedia.org/wiki/Turbulence). Turbulent flows are characterized by chaotic and irregular motion. The fluid moves in a complex and unpredictable way, with eddies and vortices forming and dissipating. Turbulent flows can be very difficult to predict and model, but they are also very common in nature.

#### Von Kármán's Vortex Street (2 minute video)

The [von Kármán vortex street](https://en.wikipedia.org/wiki/Von_K%C3%A1rm%C3%A1n_vortex_street) is a pattern of alternating vortices that can form when a fluid flows past a "bluff" body, such as a cylinder or a sphere. The vortices are shed from the body in a regular pattern, creating a repeating pattern of alternating vortices. The von Kármán vortex street is an example of a high Reynolds number flow, and it can be used to study the behavior of turbulent flows. Below is a video of a von Kármán vortex street simulation.

[![Von Karman's Vortex Street](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=f3LmjJ1N7YE)

Source: <https://youtube.com/watch?v=f3LmjJ1N7YE>

#### Turbulent Flow (24 minute video)

Turbulence is a major research area in science. We don't fully understand it. We are trying to determine what triggers it, how to control it, and how to predict if and when it will occur. The problem of turbulence is frequently multi-scale such that behavior at one time or length scale is not well explained or connected to another scale. Additionally, the mathematics of turbulence is very difficult. It makes for an interesting and challenging research area. Below is a video that explains the some of the physics of turbulence. The first 4 minutes or so are at least worth watching.

[![Turbulence](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=RkewD966Y90)

Source: <https://youtube.com/watch?v=RkewD966Y90>


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

![Work done by a net force](../../images/notes/week5/discrete-force-intervals.png)

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

![Work done by a net force](../../images/notes/week5/path-integral-work.png)


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

![Lattice chain model](../../images/notes/week5/lattice-chain.png)

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

![Work done by a net force](../../images/notes/week5/closed-path-work.png)

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

[![Feynman on the units of energy](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=roX2NXDUTsM)

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

[![The Big Misconception About Electricity](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=bHIhgxav9LY)

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

[![Point Particle and Real Models](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=fbiNKrqVajM)

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


# Week 6 - Notes: Stability and Energy


You have likely already heard of the concept of stability in other classes or contexts. The idea that something is "stable" is a well understood concept in everyday language, but here we mean to put some precision on the statement. 

* What do we mean by stable?
* And what forms of stability are there? 
* What are the implications of stability for the behavior of a system?

We will start this from the perspective of force and then relate it to the potential energy. Ultimately, we will develop a toolkit for understanding the stability of a system and how to analyze it.

Further, we will introduce the idea of [fixed points](https://en.wikipedia.org/wiki/Fixed_point_(mathematics)) and how they relate to stability. These fixed points, or equilibrium points, are the points where the system is at rest, or it would be if it were not disturbed. They are important to identify because they are the first concept in the larger narrative of stability. Later, we will see how systems can produce other structures like [limit cycles](https://en.wikipedia.org/wiki/Limit_cycle) and [chaotic attractors](https://en.wikipedia.org/wiki/Attractor). Indeed, in some cases, we can parameterize the system, by choosing a tuneable variable, to produce any of these structures.

## What is an equilibrium point?

This might have an obvious answer to you if you think about a vertical pendulum. Obviously, the bottom of the swing has some special meaning, and it is the point that the pendulum will return to if it is not disturbed. As, surely, you can surmise, this is an equilibrium point for this system.

But what about the location at the top of the swing? The location directly opposite the bottom of the swing? It turns out that is also an equilibrium point. But there is something very different about these two points. 

The bottom of the swing is a stable equilibrium point, while the top of the swing is an unstable equilibrium point. This basic idea that we can identify points in the system where the system is at rest is a powerful concept. Moreover, we already have some intuition about the stability of these points; for example, the bottom of the swing is a lower potential energy state, while the top of the swing is a higher potential energy state.

## How can we identify equilibrium points?

Starting from Newton's second law, we can write the equation of motion for a system. This equation will be a differential equation that describes how the system evolves in time. For the pendulum without a small angle approximation, we have the following equation of motion:

$$m L \ddot{\theta} = -m g \sin(\theta)$$

Where $m$ is the mass of the pendulum, $L$ is the length of the pendulum, $g$ is the acceleration due to gravity, and $\theta$ is the angle of the pendulum from the vertical; measured from the bottom of the swing.

To find the equilibrium points we search for the points where $\ddot{\theta} = 0$. This is the point where the system is at rest, or instantaneously at rest. In this case, we have:

$$0 = -g \sin(\theta),$$

$$\sin(\theta) = 0.$$

Now, we know that the angle theta here is measurable around the entire circles as we did not make the small angle approximation. Thus, we find that the equilibrium points are at:

$$\theta = 0\;\mathrm{and}\;\theta = \pi,$$

corresponding to the bottom and top of the swing, respectively. There are in fact an infinite number of equilibrium points for this system, but these are the only unique points. The others would correspond to multiple rotations around the circle.

### What is happening here? Where does energy come into play?

What we've done is use the equation of motion to find the points where the system is at rest. But we can also think of this in terms of the potential energy of the system. The strength of the potential energy view is that there's another representation of the system that can be used to understand the stability of the equilibrium points, namely the graph of the potential energy. We can use this energy landscape to help us see the stability of the equilibrium points.

The potential energy of the pendulum that we have been discussing is given by:

$$U(\theta) = -m g L \cos(\theta).$$

Let's graph this potential energy and see what it looks like.


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('seaborn-v0_8-colorblind')

theta = np.linspace(-np.pi, np.pi, 1000)
U = -9.8 * np.cos(theta)


fig = plt.figure(figsize=(8, 6))

plt.plot(theta, U)

plt.xlabel(r'$\theta$')
plt.ylabel(r'$U(\theta)$')

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-10, -5, 0, 5, 10], ['-10', '-5',  '0', '5', '10'])

plt.title('Potential Energy of a Pendulum')

plt.grid()
plt.tight_layout()
plt.show()
```


    
![png](06_notes_files/06_notes_4_0.png)
    


We can see where the equilibrium points are by noticing they are the minima and maxima of the potential energy. In fact, these fixed points are the extrema of the potential energy. The bottom of the swing is a minimum, while the top of the swing is a maximum. This is a general property of fixed/equilibrium points that are derived from a potential energy function.

We also can see then how we might find these points by looking at the potential energy. Given a potential energy function, we can find the equilibrium points by finding the extrema of the potential energy. 

Let's return to the pendulum example. 

$$U(\theta) = -m g L \cos(\theta).$$

The first derivative of the potential energy is:

$$\frac{dU}{d\theta} = m g L \sin(\theta).$$

Setting this equal to zero, we find the equilibrium points:

$$\sin(\theta) = 0,$$

$$\theta = 0\;\mathrm{and}\;\theta = \pi.$$

This is the same result we found from the equation of motion. This approach is generally applicable to potential energy functions because the equation of motion is derived from the potential energy through it's gradient. In 1D,

$$m a = F = -\frac{dU}{dx}.$$

Or in 3D,

$$m \mathbf{a} = \mathbf{F} = -\nabla U.$$

In the case of the pendulum, we have:

$$m L \ddot{\theta} = -\frac{dU}{d\theta},$$

$$m L \ddot{\theta} = -m g L \sin(\theta).$$

## How can we determine the stability of an equilibrium point?

Clearly from our intuition, the bottom of the swing is a stable equilibrium point, while the top of the swing is an unstable equilibrium point. But how can we determine this mathematically? We have found that the equilibrium points are at $\theta = 0$ and $\theta = \pi$. 

Let's plot the potential energy again and include the equilibrium points. We know which are stable and which are unstable, but let's see if we can determine this from the potential energy.


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('seaborn-v0_8-colorblind')

theta = np.linspace(-np.pi, np.pi, 1000)
U = -9.8 * np.cos(theta)


fig = plt.figure(figsize=(8, 6))

plt.plot(theta, U)
plt.plot(0, -9.8, 'C2*', label='stable', markersize=20)
plt.plot(-np.pi, 9.8, 'C3*', label='unstable', markersize=20)
plt.plot(+np.pi, 9.8, 'C3*', markersize=20)


plt.xlabel(r'$\theta$')
plt.ylabel(r'$U(\theta)$')

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-10, -5, 0, 5, 10], ['-10', '-5',  '0', '5', '10'])

plt.title('Potential Energy of a Pendulum')
plt.legend()

plt.grid()
plt.tight_layout()
plt.show()
```


    
![png](06_notes_files/06_notes_7_0.png)
    


So it's clear that the equilibrium points are the extrema of the potential energy. We can determine their stability in the same way we identified them. We look at the local curvature of the potential energy at the equilibrium points. If we find that the second derivative of the potential energy is positive, then the equilibrium point is stable. If the second derivative is negative, then the equilibrium point is unstable.

Let's calculate the second derivative of the potential energy for the pendulum:

$$U(\theta) = -m g L \cos(\theta),$$

$$\frac{dU(\theta)}{d\theta} = m g L \sin(\theta),$$

$$\frac{d^2U(\theta)}{d\theta^2} = m g L \cos(\theta).$$

At the bottom of the swing, $\theta = 0$, we have:

$$\frac{d^2U(\theta = 0)}{d\theta^2} = m g L > 0.$$

At the top of the swing, $\theta = \pm\pi$, we have:

$$\frac{d^2U(\theta = \pm\pi)}{d\theta^2} = -m g L < 0.$$

Thus, we have confirmed that the bottom of the swing is a stable equilibrium point, while the top of the swing is an unstable equilibrium point.

## Our new toolkit

We now have a set of tools to help us understand the stability of a system. We can find the equilibrium points by setting the acceleration to zero, or by setting the first derivative of the potential energy to zero. We can determine the stability of these points by looking at the curvature of the potential energy at these points. 

If we have a system that can be described fully by a potential energy function, we can use this toolkit to understand the stability of the system. We will develop a broader class of tools for when the system is not fully described by a potential energy function, or for multi-dimensional systems. But this is a good start.

1. Write out the potential energy function for the system, $U(x)$.
2. Find all the extrema, $x^*$, of the potential energy by setting the first derivative to zero, $\frac{dU}{dx} = 0$. These are the equilibrium points.
3. Evaluate the second derivative of the potential energy at each of these points, $\frac{d^2U(x=x^*)}{dx^2}$. If this is positive, the equilibrium point is stable. If it is negative, the equilibrium point is unstable. If it's zero, it might be [metastable](https://en.wikipedia.org/wiki/Metastability).


# Week 6 - Stability and Equilibria

We have shown that we can develop trajectories of different physical systems by solving the differential equations that describe them. This is a useful approach, but it often means we are focused on a single trajectory. This might be fine if all the trajectories are the same or roughly so, say like the 1D falling ball, or the simple harmonic oscillator. 

Systems can produce multiple families of trajectories depending on the parameter choices, and the initial conditions associated with the problem you are solving. A more general approach that starts us down the road of characterizing the many potential behaviors that a physical system can exhibit is to consider [stability](https://en.wikipedia.org/wiki/Stability_theory). As we will build the toolkit to investigate classical systems, understanding equilibrium points and their stability is a useful step. 


## Why do we study stability and equilibria?

First, because nature is often moving towards a state of equilibrium because those states are associated, as we will see, with the lowest local energy state. It takes energy to move away from stable equilibrium, and physical systems tend to minimize their energy -- because those configurations are often quite stable. 

Much of the physics that we do today focuses on [non-equilibrium systems](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics). These are systems that are typically driven by external interactions to ensure the system remains out of equilibrium. The responses of these systems to this driving and how they might relax to equilibrium are often studied.

Second, we can often start from the equilibrium points of a system and then perturb the system to see how it responds. We know how to solve problems around equilibrium points, and working with fully non-equilibrium systems is often much harder. 

We have gotten much better at working in non-equilibrium spaces, especially as we have developed computing tools that can help us simulate the behavior of systems that are far from equilibrium.

## The Simple Harmonic Oscillator Models Many Systems

You have used the simple harmonic oscillator frequently. 

There's a reason for that. 

It provides the simplest example of a system that exhibits periodic motion. It also is a system with one of the simplest energy landscapes -- a parabola; and it has a global stable equilibrium point at the bottom of the potential well.

There are many systems that we can transform into a simple harmonic oscillator. And it is not because the world is full of springs and masses. It is because the simple harmonic oscillator is a good model for many systems near their local equilibrium points. In fact, as you will see, it is the leading (non-constant) term in every Taylor expansion of a 1D potential energy function near a local minimum.

### Another SHO Example - A Pendulum

Consider a pendulum of mass $m$ and length $L$ that is displaced from the vertical by an angle $\theta$. We can show that the complete equation of motion (without drag) is:

$$mL\ddot{\theta} = - mg\sin \theta,$$

$$\ddot{\theta} = -\frac{g}{L}\sin \theta.$$

Typically we limit to small angles, so $\sin \theta \approx \theta$, and the equation becomes: 

$$\ddot{\theta} = -\frac{g}{L}\theta.$$

This is a second order differential equation that we have solved before. The general EOM for a simple harmonic oscillator is:

$$\ddot{x} = -\omega^2 x.$$

A general solution to this equation is:

$$x(t) = A\cos(\omega t + \phi),$$

where $A$ is the amplitude of the oscillation, $\omega$ is the angular frequency of the oscillation, and $\phi$ is the phase of the oscillation.

This model of an SHO works with many systems, not just pendulums. Here's some examples along with the equivalent natural oscillation frequency, $\omega^2$, for each system:

| System | Equation of motion | $\omega^2$ |
|--------|--------------------|------------|
| Mass-spring system | $m\ddot{x} = -kx$ | $k/m$ |
| Pendulum | $\ddot{\theta} = -\frac{g}{L}\theta$ | $g/L$ |
| LC circuit | $L\ddot{q} = -\frac{q}{C}$ | $1/LC$ |
| Water in a U-shaped tube | $\ddot{h} = -\frac{2g\rho A}{M} h$| $\frac{2g\rho A}{M}$ |


### Stability of the SHO

Regardless of the choice of physical model, the SHO equation is the same second order differential equation, which we write in general as:

$$\frac{d^2 x}{dt^2} = -\omega^2 x$$

For a given system, this results in a potential energy that is proportional to the square of the variable $x$ (the "stretch") and to the square of the frequency $\omega$. This potential energy is always positive, and it can have a non-zero minimum.

$$U(x) = \frac{1}{2} \xi \omega^2 x^2 + U_0$$

where $\xi$ is a positive constant (with units!) of proportionality. In the case of a mass on a spring, $\xi = m$. We can find the equilibrium points by setting taking the first derivative of the potential energy and setting it to zero.

$$\frac{dU}{dx} = \xi \omega^2 x = 0$$

This gives us the equilibrium point at $x = 0$. We might have expected this, as the potential energy is a parabola, and the minimum of a parabola is at the vertex. We can also determine the stability of this equilibrium point by looking at the second derivative of the potential energy, and evaluating it at the equilibrium point.

$$\frac{d^2U}{dx^2} = \xi \omega^2 > 0$$

This number is always positive, indicating that for an SHO, the equilibrium point is stable. This is a general result for the SHO, and it is true for all the systems listed above.

## Interpreting your Analysis

Above, we completed an analysis of the simplest system that we will work with. It lead us to find a global minimum in the potential energy, so that suggests a few things for us to think about:

1. **The SHO is a conservative system - the total energy of the system is conserved.** So any trajectory will oscillate between kinetic and potential energy, but the total energy will remain constant. This is not something that will always be true.
2. **The SHO has a global minimum in potential energy - a globally stable equilibrium point.** Oscillations will always occur around this point. Global stability is a very strong form of stability; it is also rare in that most systems have multiple equilibrium points: some are stable, some are not, and some are [metastable](https://en.wikipedia.org/wiki/Metastability).
3. **If the SHO starts at rest at the equilibrium point, it will remain there.** It will take energy put into the system to move away from the equilibrium point. Because this a global minimum, all trajectories will oscillate around this point. However, in systems with local equilibrium points, the system can be perturbed away from the equilibrium point, and end up in a different equilibrium point. This is a common feature of many systems.
4. **If there are interactions that remove energy from the system, the system will eventually come to rest at the equilibrium point.** This is a common feature of many systems.


## Where are we going?

This work we are doing to understand equations of motion, stability, and equilibrium points is foundational. Some of the most exciting physics we see today is rooted in understanding how systems move away from equilibrium, and how they respond to external driving. [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory) is a field that has grown out of understanding how systems can be very sensitive to initial conditions, and how they can exhibit complex behavior. 

We will start to use these ideas from this week into next week as we build a set of additional tools like [phase space diagrams](https://en.wikipedia.org/wiki/Phase_space) and using asymptotic behavior to investigate and explain the behavior of physical systems. 

To introduce some of those initial ideas here are two videos from different physics perspectives on the topic of chaos.


### Veritasium - THe Butterfly Effect and Chaotic Systems (13 minute video)

In this video, Derek Muller uses the typical example of the Butterfly Effect to introduce the idea of chaos theory. The philosophical aspects of the butterfly effect are interesting, but not real in any physical sense. Instead, it's a metaphor for the idea that small changes in initial conditions can lead to large changes in the system. Muller contrasts our understanding of determinism with uncertainty; he introduces the concepts of sensitivity to initial conditions and discusses the idea of an attractor. 

[![Chaos Theory](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=fDek6cYijxI)

### University of Bristol - Chaos Theory and Randomness (8 minute video)

In this video, two researchers from the University of Bristol ([Jens Marklof](https://people.maths.bris.ac.uk/~majm/) and [Henna Koivusalo](https://people.maths.bris.ac.uk/~te20281/)) discuss the idea of chaos theory from a more mathematical perspective - remdining us of the differences between randomness and chaos. The overlap between physicists and mathematicians in the study of chaos is significant. One important contribution is [Dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system), which is a mathematical framework that is used to study these behaviors. The researchers who do this work are mathematicians, physicists, engineers, and computer scientists. They do experiments, but they also do a lot of mathematical modeling.

[![Chaos Theory](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=5fRhasVmcUE)


# Week 7 - Notes: Critical Points; Phase Space; Trajectories

Thus far, we have developed an approach to solving differential equations for particular trajectories of the different classical systems that we have studied. Typically, we work to develop the equations of motion for a system using Newton's Second Law. Those equations typically have the form

$$\ddot{\vec{x}} = f(\vec{x}, \dot{\vec{x}}, t),$$

where $\vec{x}$ is the position vector of the system, $\dot{\vec{x}}$ is the velocity vector of the system, and $f$ is some function that depends on the position, velocity, and time. In 1D, we have studied a number of systems where the equations of motion takes the form:

$$\ddot{x} = f(x, \dot{x}, t).$$

Our approach has been to find ways of solving these equations for a given set of initial conditions ($x_0$, $v_0$, at $t=t_0$) to get individual trajectories of the system.

$$x(t)\; \text{and}\; v(t)\; \text{for}\; t \geq t_0.$$

## Developing a General Understanding of Motion

However, some of the equations of motion we have developed (in fact, most) cannot be solved in a "closed form", which is what gives rise to analytical trajectories. In these cases, we have used numerical methods to solve the equations of motion.

It also seems pretty inefficient to have to solve the equations of motion for every possible set of initial conditions. It would be nice if we could develop a general understanding of the behavior of the system without having to solve the equations of motion for every possible set of initial conditions.

Finally, we often care less about particular trajectories and more about the general behavior of the system. For example, we might want to know if the system is stable, or if it will oscillate, or if it will spiral in or out. We seek to understand qualitatively different solutions to the equations of motion.

In this week, we will take a step back and consider the general structure of the solutions to these equations. We will introduce the concept of a critical point, and we will discuss how the phase space of a system can be used to understand the behavior of the system.  This approach will help us broaden our understanding of the solutions to differential equations and the behavior of classical systems. It also gives us a new set of tools and ways of thinking about the systems that we have been studying.

## Example: A Nonlinear 1st Order ODE

Consider the following first-order ordinary differential equation:

$$\dot{x} = \sin x.$$

Let's assume we want to find $x(t)$ for a given set of initial conditions $x_0$ at $t=t_0$. This equation is nonlinear, but we can make some progress by separating variables:

$$\frac{dx}{\sin x} = dt.$$

We can integrate both sides to get:

$$\int \frac{dx}{\sin x} = \int dt.$$

The integral on the left-hand side is one that we can look up:

$$\int \frac{dx}{\sin x} = \ln\left|\csc\left(x\right) + \cot\left(x\right)\right| + C.$$

Cool. So we have:

$$t-t_0 = \ln\left|\csc\left(x\right) + \cot\left(x\right)\right| - \ln\left|\csc\left(x_0\right) + \cot\left(x_0\right)\right|,$$

$$t-t_0 = \ln\left|\frac{\csc\left(x\right) + \cot\left(x\right)}{\csc\left(x_0\right) + \cot\left(x_0\right)}\right|.$$

Well how do solve for $x(t)$? That's not so easy. And a harder question is: what does the motion look like?

We need a new approach.

### A Geometric Analysis

Let us instead plot the equation $\dot{x} = \sin x$ in the [phase space](https://en.wikipedia.org/wiki/Phase_space) of the system. Here, we are plotting the velocity of the system as a function of the position of the system. This is a common approach to understanding the behavior of a system.

In 1D, this plot is called a 'Flow on a Line'. That is because we can characterize the behavior of the system by the direction of the flow of the system in the phase space. In this case, the flow is given by the function $\sin x$. A positive $\sin x$ means that the system is moving to the right, and a negative $\sin x$ means that the system is moving to the left. We plot it below with some additional information.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

x = np.linspace(-7/2*np.pi, 7/2*np.pi, 1000)
xdot = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, xdot, 'k', label=r'$\dot{x} = \sin(x)$')

ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)

plt.plot([-3*np.pi, -np.pi, np.pi, 3*np.pi], [0, 0, 0, 0], 
         'C1o', 
         markersize=12,
         label='Stable fixed points')

plt.plot([-2*np.pi, 0, 2*np.pi], [0, 0,  0], 
         'C2o', 
         markersize=12, 
         markerfacecolor='none',
         markeredgewidth=2,
         markeredgecolor='C2',
         label='Unstable fixed points')

plt.plot([-5/2*np.pi, -np.pi/2, 3*np.pi/2, 7/2*np.pi], [0, 0, 0, 0], 
         'k<', 
         markersize=12,
         label='Flow to the left')
plt.plot([-7/2*np.pi, -3/2*np.pi, np.pi/2, 5/2*np.pi], [0, 0, 0, 0], 
         'k>', 
         markersize=12,
         label='Flow to the right')

plt.legend(loc='upper right')

ax.set_xlabel(r'x')
ax.set_ylabel(r'$\dot{x}$', rotation=0)
ax.grid()
xticks = [-4*np.pi, -7*np.pi/2, -3*np.pi, -5*np.pi/2, -2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi, 7*np.pi/2, 4*np.pi]
xticks_labels = [r'$-4\pi$', r'$-\frac{7\pi}{2}$', r'$-3\pi$', r'$-\frac{5\pi}{2}$', r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$', r'$\frac{7\pi}{2}$', r'$4\pi$']
ax.set_xticks(xticks)
ax.set_xticklabels(xticks_labels)
plt.xlim(-7/2*np.pi, 7/2*np.pi)
plt.ylim(-2.5, 2.5)
plt.tight_layout()
```


    
![png](07_notes_files/07_notes_2_0.png)
    


The plot we have made is called a 'Phase Portrait'. It is a plot of the velocity of the system as a function of the position of the system. The arrows indicate the direction of the flow of the system. The critical points of the system are the points where the flow is zero. These are the points where the system is at rest (i.e., $\dot{x} = 0$).

In this case, the critical points are at $x = n\pi$, where $n$ is an integer. At these points, the system is at rest. The system will move to the right if $\dot{x} > 0$ and to the left if $\dot{x} < 0$. We have indicated that flow direction with arrows on the line.

From those flow directions, we can also find the 'critical points' of the motion. These are the points where the flow changes direction, and they are found by setting $\dot{x} = 0$. In this case, the critical points are at $x = n\pi$, where $n$ is an integer. In some cases, that point is stable (green solid circle) and in other cases, it is unstable (red open circle). You can see why from the flow directions; for stable points, the flow on both sides of the critical point is towards the critical point, and for unstable points, the flow on both sides of the critical point is away from the critical point.

### What does the motion look like?

We can see from the phase portrait, that motion that doesn't start on a critical point will eventually move towards the stable critical point. This is because the flow direction is always towards the stable critical point. We also can note that depending on the location of the particle to start, it will move to the left or right to reach the stable critical point. And we also notice that the motion is often accelerated up a to a maximum velocity and then decelerated down to zero velocity as it approaches the critical point -- this is the sinusoidal nature of the velocity function.

## Another Example: A Polynomial 1st Order ODE

Consider instead the following first-order ordinary differential equation:

$$\dot{x} = x^3 - x.$$

We can find the critical points of this system by setting $\dot{x} = 0$:

$$x^3 - x = 0,$$

$$x(x^2 - 1) = 0,$$

$$x(x-1)(x+1) = 0.$$

So that there are three critical points: $x = 0$, $x = 1$, and $x = -1$. We can plot the phase portrait of this system below along with a little more information.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

x = np.linspace(-7/2*np.pi, 7/2*np.pi, 1000)
xdot = x**3-x

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, xdot, 'k', label=r'$\dot{x} = x^3 - x$')

ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)

plt.plot([0], [0], 
         'C1o', 
         markersize=12,
         label='Stable fixed points')

plt.plot([-1, 1], [0,  0], 
         'C2o', 
         markersize=12, 
         markerfacecolor='none',
         markeredgewidth=2,
         markeredgecolor='C2',
         label='Unstable fixed points')

plt.plot([-1.5, 0.5], [0, 0], 
         'k<', 
         markersize=12,
         label='Flow to the left')
plt.plot([-0.5, 1.5], [0, 0], 
         'k>', 
         markersize=12,
         label='Flow to the right')

plt.legend(loc='upper left')
plt.xlim(-2, 2)
plt.ylim(-3, 3)
ax.set_xlabel(r'x')
ax.set_ylabel(r'$\dot{x}$', rotation=0)
ax.grid()

plt.tight_layout()
```


    
![png](07_notes_files/07_notes_5_0.png)
    


### What does the motion look like?

From the phase potrait, we can see that for $|x_0| > 1$, the solutions run off to $|x| \rightarrow |\pm \infty|$. Otherwise all solutions will approach the stable critical point at $x = 0$. 

Notice we did all this analysis without trying to solve the differential equation. We can understand the general behavior of the system by looking at the phase portrait. If we did try to solve it, we would find that the solutions are not easy to find in a closed form.

$$\dot{x} = x^3 - x,$$

$$\int \frac{dx}{x^3 - x} = \int dt,$$

$$\int_{x_0}^{x(f)} \frac{dx}{x^3 - x} = t - 0.$$

$$t = \dfrac{1}{2}\ln(1-x^2)|_{x_0}^{x(f)} -\ln(x)|_{x_0}^{x(f)},$$

$$t= \dfrac{1}{2}\ln\left(\dfrac{1-x(f)^2}{1-x_0^2}\right) - \ln\left(\dfrac{x(f)}{x_0}\right).$$

Again. OOF. That's a lot of work for a simple system.

### Summary

We still need some tools to deal with finding trajectories for systems that are not easy to solve. But let's pause for a minute and appreciate what we have done. Without solving the differential equation, we have could characterize all possible solutions.

Now, the next step is to do this with 2nd order differential equations. The analogy changes from a 'Flow on a line' to a 'Flow on a plane'. Let's introduce that with a simple example.


## The Harmonic Oscillator Gets a Bad Rap

We've shown that the harmonic oscillator is a simple system to solve. But let's consider the following 2nd order differential equation where the force is not linear. This is the classical pendulum equation of motion where we have removed the small angle approximation and dispensed with the parameters that control the motion ($\omega^2=1$).

$$\ddot{x} = -\sin x.$$

We will model this system in phase space, but let us first take the linear approximation of the system. We can do this by expanding the $\sin x$ term in a Taylor series:

$$\sin x \approx x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \dfrac{x^7}{7!} + \ldots.$$

If we keep only the first term, we get the linear harmonic oscillator:

$$\ddot{x} = -x.$$

Now, we transform the 2nd order differential equation into two 1st order differential equations:

$$\dot{x} = v,$$
$$\dot{v} = -x.$$

This gives us a description of the motion in phase space. We can plot the phase portrait of this system by considering that every point in phase space $\langle x, v\rangle$ has an arrow that is represented by the change that occurs at that location $\langle \dot{x}, \dot{v} \rangle = \langle v, -x\rangle$. This is a *strange* concept, but the logic is that how $x$ and $v$ change at a given point in phase space is given by the velocity vector at that point and it depends on the location that you are at in phase space. Let's plot this in parts below.

### The $x=0$ line

Let's first consider the vertical axis $x=0$. Note that we can directly compute this:

$$\langle \dot{x}, \dot{v} \rangle = \langle v,0 \rangle.$$

So in the phase space, the arrows will be completely horizontal and will get larger as you move away from the origin.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

def returnPhase(x, xdot):
    return (xdot, -x)

# Points along the vertical axis
v = np.linspace(-2, 2, 10)
x = np.zeros_like(v)

# Xompute the phase portrait
xdot, ydot = returnPhase(x, v)

# Plot the phase portrait as arrows
fig, ax = plt.subplots(figsize=(5, 5))
ax.quiver(x, v, xdot, ydot)
ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$\dot{x}$', rotation=0)
ax.grid()

```


    
![png](07_notes_files/07_notes_8_0.png)
    


### The $v=0$ line

Similarly, we can compute the arrows on the horizontal axis $v=0$:

$$\langle \dot{x}, \dot{v} \rangle = \langle 0,-x \rangle.$$

So these will be completely vertical and will get larger as you move away from the origin. The negative sign indicates that the arrows will point up on the left side and down on the right side. Let's plot that.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

def returnPhase(x, xdot):
    return (xdot, -x)

# Points along the horizontal axis
x = np.linspace(-2, 2, 10)
v = np.zeros_like(x)

# Xompute the phase portrait
xdot, ydot = returnPhase(x, v)

# Plot the phase portrait as arrows
fig, ax = plt.subplots(figsize=(5, 5))
ax.quiver(x, v, xdot, ydot)
ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$\dot{x}$', rotation=0)
ax.grid()

```


    
![png](07_notes_files/07_notes_10_0.png)
    


### Putting it all together

We could keep plotting like this and we will begin to connect the dots into a phase potrait. We have already built the code to do this in general above, but we need to make use of the 'meshgrid' function in numpy to make this work. [Meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) is a function that generates a grid of points in 2D space. We can use it to take our 2 arrays for the space we are interested in and generate a grid of points that we can use to compute the arrows at each point. Let's plot the full phase portrait of the system below.

We also introduce the [streamplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html) function in matplotlib. This function connects the lines a little more smoothly and gives a better representation of the flow of the system.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

def returnPhase(x, xdot):
    return (xdot, -x)

# Points along the horizontal axis
x = np.linspace(-2, 2, 10)
v = x

# Use meshgrid to create a grid
X, V = np.meshgrid(x, v)

# Compute the phase portrait
# NOTE WE ARE NOW USING X, V
xdot, ydot = returnPhase(X, V)

# Plot the phase portrait as arrows and using a streamplot

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.streamplot(X, V, xdot, ydot, color='k')
ax1.title.set_text('SHO Streamplot')
ax1.axhline(0, color='black', linewidth=2)
ax1.axvline(0, color='black', linewidth=2)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$\dot{x}$', rotation=0)
ax1.grid()

ax2.quiver(X, V, xdot, ydot)
ax2.title.set_text('SHO Quiver')
ax2.axhline(0, color='black', linewidth=2)
ax2.axvline(0, color='black', linewidth=2)
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$\dot{x}$', rotation=0)
ax2.grid()

plt.tight_layout()

```


    
![png](07_notes_files/07_notes_12_0.png)
    


### What does the motion look like?

Well, it's the simple harmonic oscillator. The motion is periodic and sinusoidal. It's bounded in ellipses of increasing energy as you go outwards. The critical points are at the origin, where the system is at rest, but no trajectory will ever reach the origin except for the one that starts there. The system will oscillate back and forth forever. Total energy for any trajectory is conserved (that's why the ellipses are concentric). Each loop characterizes a full period of the motion for a given set of initial conditions. All initial conditions will lead to periodic motion, and all can be characterized by the phase portrait.

#### How do we know the phase trajectories are ellipses?

The energy of the system is given by:

$$E = \dfrac{1}{2}mv^2 + \dfrac{1}{2}kx^2.$$

For any one trajectory, the energy is conserved. So we can write:

$$E = \dfrac{1}{2}mv^2 + \dfrac{1}{2}kx^2 = \text{constant}.$$

This is the equation of an ellipse. We can rewrite it as:

$$1 = \dfrac{v^2}{2E/m} + \dfrac{x^2}{2E/k}.$$

This ellipse is centered at the origin and has a semi-major axis of $\sqrt{2E/k}$ and a semi-minor axis of $\sqrt{2E/m}$. The energy of the system determines the size of the ellipse. The larger the energy, the larger the ellipse.

### Returning to the Pendulum

In the pendulum problem, we have a second order non linear differential equation, which we can write as two first order equations:

$$\dot{x} = v,$$
$$\dot{v} = -\sin x.$$

We can now use the infrastructure we have built to plot the phase portrait of the pendulum. We will plot the phase portrait of the pendulum below.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

def returnPhase(x, xdot):
    return (xdot, -np.sin(x))

# Points along the horizontal axis
x = np.linspace(-5, 5, 20)
v = x

# Use meshgrid to create a grid
X, V = np.meshgrid(x, v)

# Compute the phase portrait
# NOTE WE ARE NOW USING X, V
xdot, ydot = returnPhase(X, V)

# Plot the phase portrait as arrows and using a streamplot

fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

ax1.streamplot(X, V, xdot, ydot, color='k')
ax1.plot([0], [0], 'C1o', 
         markersize=12, 
         label='Stable fixed point')

ax1.plot([-np.pi, np.pi], [0, 0], 'C2o', 
         markersize=12, 
         markerfacecolor='none',
         markeredgewidth=4,
         label='Unstable fixed points')

ax1.title.set_text('Physical Pendulum Streamplot')
ax1.axhline(0, color='black', linewidth=2)
ax1.axvline(0, color='black', linewidth=2)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$\dot{x}$', rotation=0)
ax1.grid()
ax1.legend()

plt.tight_layout()
```


    
![png](07_notes_files/07_notes_15_0.png)
    


### What does the motion look like?

Now, we see a more complex picture of the pendulum. The motion is still oscillatory and periodic, but it is definitely not sinusoidal. For very small choices of initial conditions, the motion is sinusoidal; we can zoom in an see we get near ellipses.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

def returnPhase(x, xdot):
    return (xdot, -np.sin(x))

# Points along the horizontal axis
x = np.linspace(-0.5, 0.5, 20)
v = x

# Use meshgrid to create a grid
X, V = np.meshgrid(x, v)

# Compute the phase portrait
# NOTE WE ARE NOW USING X, V
xdot, ydot = returnPhase(X, V)

# Plot the phase portrait as arrows and using a streamplot

fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

ax1.streamplot(X, V, xdot, ydot, color='k')
ax1.plot([0], [0], 'C1o', 
         markersize=12, 
         label='Stable fixed point')

# ax1.plot([-np.pi, np.pi], [0, 0], 'C2o', 
#          markersize=12, 
#          markerfacecolor='none',
#          markeredgewidth=4,
#          label='Unstable fixed points')

ax1.title.set_text('Physical Pendulum Streamplot with zoom')
ax1.axhline(0, color='black', linewidth=2)
ax1.axvline(0, color='black', linewidth=2)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$\dot{x}$', rotation=0)
ax1.grid()
ax1.legend()

plt.tight_layout()
```


    
![png](07_notes_files/07_notes_17_0.png)
    


So we see that for small initial conditions, we recover the SHO. But for most initial conditions, we have oscillations that are not sinusoidal. Moreover, we have a series of high energy trajectories that are not bounded. These are the ones that continue to allow the pendulum to rotate over the top of itself. This is a new type of motion that we did not see in the SHO.

## What about damped motion?

We can also consider the case where we add a damping term to the pendulum equation of motion:

$$\ddot{x} = -\sin x - \gamma \dot{x}.$$

Or in the approximate form:

$$\ddot{x} = - x - \gamma \dot{x}.$$

In either case, we can write this as two first order equations:

**Exact Form**

$$\dot{x} = v,$$
$$\dot{v} = -\sin x - \gamma v.$$

**Approximate Form**

$$\dot{x} = v,$$
$$\dot{v} = -x - \gamma v.$$

When we plot this phase portrait we will find a new type of motion and a new type of critical point -- an attractor. This is a point in phase space that all trajectories will eventually approach. We leave that plot as an exercise.


# Week 7 - Nonlinear Dynamics

We have now built enough tools to tackle some challenging physical systems that have nonlinear equations of motion. The broader field of study that deals with these systems is called [Nonlinear Dynamics](https://en.wikipedia.org/wiki/Nonlinear_system). Nonlinear dynamics or nonlinear science is the study of systems that are described by nonlinear equations. These systems are often chaotic, meaning they are highly sensitive to initial conditions. In many cases, these systems are treated using [dynamical systems theory](https://en.wikipedia.org/wiki/Dynamical_system).

Nonlinear dynamics is the science that has helped us understand the dynamics of [fluids](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations), [water waves](https://en.wikipedia.org/wiki/Kadomtsev%E2%80%93Petviashvili_equation), [crystals and other optical systems](https://en.wikipedia.org/wiki/Nonlinear_optics), [radio waves](https://en.wikipedia.org/wiki/Li%C3%A9nard_equation), [the weather](https://en.wikipedia.org/wiki/Numerical_weather_prediction), and countless other systems. It has been used in [fluid dynamics](https://en.wikipedia.org/wiki/Turbulence), [plasma physics](https://en.wikipedia.org/wiki/Plasma_modeling), [mechanical systems](https://en.wikipedia.org/wiki/Double_pendulum), and many other fields. [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory) is associated with nonlinear dynamics and is a subset of the field. Recently, this work has extended to quantum systems, where the Hamiltonian is nonlinear. [Quantum chaos](https://en.wikipedia.org/wiki/Quantum_chaos) is a field that studies the quantum analog of classical chaotic systems.

## Nonlinear Differential Equations 

Differential equations are the language of classical mechanics. They describe how the systems we investigate evolve over time. They track the [state variables](https://en.wikipedia.org/wiki/State_variable) of the system, which are what define the system. For us, this is often the position components and the velocity components of the system. The video below gives a good overview of what differential equations are and why they are important for our study. It also provides an introduction to the concept of a [phase space](https://en.wikipedia.org/wiki/Phase_space), which is the space defined by all the state variables of the system.

### Differential equations, a tourist's guide (27 min)

[![Differential Equations](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=p_di4Zn4wz4)

Source: <https://www.youtube.com/watch?v=p_di4Zn4wz4>

## Phase Portraits

Solving non-linear equations can be quite difficult, and in most cases, we can't find an analytical solution. We can numerically integrate the equations to find specific trajectories. But this is a fairly inefficient approach, especially when nonlinear systems exhibit such complex behavior and are so sensitive to initial conditions. 

We can also use a technique called [phase portraits](https://en.wikipedia.org/wiki/Phase_portrait) to understand the behavior of these systems. A phase portrait is a graphical representation of the trajectories of a dynamical system in the phase space. That space is defined by the combination of all the state variables of the system. For example, a simple pendulum has two state variables: the angle and the angular velocity. The phase portrait of the pendulum is a plot of the angular velocity against the angle. Or for the harmonic oscillator, the phase portrait is a plot of the velocity against the position.

*Phase portraits are quite useful for second order differential equations (or any two-dimensional system) because we frequently use and interpret 2D graphs.* Notice that we focused on "2nd order differential equations" not "linear 2nd order." That is because, as we will see, **phase portraits are particularly useful for nonlinear 2nd order differential equations.**

We will go into the details of how to construct and develop phase portraits in class. This video from [Steve Brunton](https://www.me.washington.edu/facultyfinder/steve-brunton) is a good overview of the process. It's quite detailed and takes a mathematical perspective, so don't worry if you don't understand everything in the video. We have plenty of time to investigate how this works in practice.

### Drawing Phase Portraits for Nonlinear Systems (26 min)

[![Drawing Phase Portraits for Nonlinear Systems](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=vBwyD4JJlSs)

Source: <https://www.youtube.com/watch?v=vBwyD4JJlSs>


# Week 8 - Notes: Oscillators and Modeling Oscillations


We continue our study of physics phenomena that exhibits recurrent or periodic behavior. Some systems repeat their motion in a regular pattern, and we call them oscillators. 

We have met this behavior many times. This is because we often look at the behavior of stems just a little bit away from equilibrium. Systems with local stable equilibria will have oscillatory behavior in a region around that equilibrium point. Note below the made up example of a potential energy function that has local minima and maxima.

Near the local minima, the system will oscillate back and forth. The potential energy function will look like a parabola.


```python
## Make a plot of a potential energy function with 3 local minima

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

x = np.linspace(-2, 2, 100)
U = x**6 - 2*x**3 - 10*x**2 + x

plt.plot(x, U)
plt.xlabel('x')
plt.ylabel('Potential Energy')
plt.title('Potential Energy Function')
plt.grid(True)
plt.tight_layout()
plt.show()


```


    
![png](08_notes_files/08_notes_1_0.png)
    


## Why do we often see oscillations in physics?

Oscillatory behavior is common in physics because many systems have a stable equilibrium point. When we disturb the system from equilibrium, it will oscillate back and forth around that equilibrium point. Let's assume there's a given stable equilibrium point at $x=a$, we can write the potential energy function as a Taylor series expansion around that point:

$$U(x) \approx U(a) + \dfrac{dU}{dx}\bigg|_{x=a}(x-a) + \dfrac{1}{2}\dfrac{d^2U}{dx^2}\bigg|_{x=a}(x-a)^2 + \cdots$$

The linear term is zero because the equilibrium point is a minimum, $\dfrac{dU}{dx}\bigg|_{x=a}=0$. The quadratic term is remains as does the constant term. So up to the quadratic term, the potential energy function is a parabola.

$$U(x) \approx U(a) + \dfrac{1}{2}\dfrac{d^2U}{dx^2}\bigg|_{x=a}(x-a)^2$$

We can write the value of the second derivative as a constant $k$. It will just be the measure of the concavity of the potential energy function at the equilibrium point. So near $x=a$, the potential energy function will look like a parabola of the form:

$$U(x) \approx U(a) + \dfrac{1}{2}k(x-a)^2$$

Because only changes in potential energy are important, we can ignore the constant term $U(a)$. The change in potential energy is then:

$$\Delta U = \dfrac{1}{2}k(x_f-a)^2 - \dfrac{1}{2}k(x_i-a)^2$$
$$\Delta U = U_f - U_i$$

This is just the change in potential energy for any spring-mass system (any SHO) if $k>0$.

## The Exact Solution for the Simple Harmonic Oscillator

This potential $U=\frac{1}{2}kx^2$ is the potential for the simple harmonic oscillator when $k>0$ and we are modeling around a stable critical point. We know that this potential energy will produce a restoring force.

$$F = -\dfrac{dU}{dx} = -kx$$

Thus our equation of motion is:

$$m\ddot{x} = -kx,$$

Or

$$\ddot{x} = -\dfrac{k}{m}x.$$

The natural oscillation frequency of the SHO is:

$$\omega = \sqrt{\dfrac{k}{m}}.$$

And thus we obtain several forms of their general solution:

$$x(t) = A\cos(\omega t) + B\sin(\omega t)$$
$$x(t) = C\cos(\omega t + \phi)$$
$$x(t) = D\sin(\omega t + \phi)$$

Where $A$, $B$, $C$, $D$, and $\phi$ are constants that depend on the initial conditions of the system. The phase $\phi$ is the phase angle of the oscillation. Each solution is equivalent to the others and can be written as the other form. And each solution has two arbitrary constants that depend on the initial conditions of the system.

### Complex forms of the SHO solution

These forms are useful, but often lead to more complex algebra. We can write the solution in terms of complex exponentials, which have the advantage of simplifying the algebra. Let's try a complex form of the solution:

$$x(t) = e^{i\omega t}\;\textrm{where}\;i^2=-1$$

Take its derivatives:

$$\dot{x}(t) = i\omega e^{i\omega t}$$
$$\ddot{x}(t) = (i\omega)(i\omega) e^{i\omega t} = -\omega^2 e^{i\omega t} = -\omega^2 x(t)$$

Note that $e^{-i\omega t}$ is also a solution to the differential equation that will produce this same result. So the general solution is the linear combination of these two solutions:

$$x(t) = C_1 e^{i\omega t} + C_2 e^{-i\omega t}$$

where $C_1$ and $C_2$ are constants that depend on the initial conditions of the system and **can be complex**. We still have two arbitrary constants that depend on the initial conditions of the system, which is needed for a second-order differential equation.

### But the solution to the motion of the SHO is real!

Yes, that is true. The solution must be a real function of time. This puts conditions on the constants $C_1$ and $C_2$. Using the Euler formula:

$$e^{i\theta} = \cos(\theta) + i\sin(\theta)$$

we can apply this to the functional form of the solution, such that,

$$e^{\pm i\omega t} = \cos(\omega t) \pm i\sin(\omega t).$$

Applying this to the general solution:

$$x(t) = C_1(\cos(\omega t) + i\sin(\omega t)) + C_2(\cos(\omega t) - i\sin(\omega t))$$
$$x(t) = (C_1 + C_2)\cos(\omega t) + i(C_1 - C_2)\sin(\omega t).$$

We grouped the terms in the last line to define some constants $B_1$ and $B_2$:

$$B_1 = C_1 + C_2$$
$$B_2 = i(C_1 - C_2)$$

So that,

$$x(t) = B_1\cos(\omega t) + B_2\sin(\omega t).$$

But $B_1$ and $B_2$ must be real because the rest of the solution is real.  What does that mean? Let's write $C_1$ and $C_2$ in terms of $B_1$ and $B_2$:

$$C_1 = \dfrac{1}{2}\left(B_1-iB_2\right)$$
$$C_2 = \dfrac{1}{2}\left(B_1+iB_2\right)$$



## Complex Conjugates

These values of $C_1$ and $C_2$ are the complex conjugates of each other. The complex conjugate of a complex number $z=a+ib$ is $z^*=a-ib$. The complex conjugate of a complex number is the same as the original number, but with the sign of the imaginary part reversed.

We can draw these in the complex plane where the $x$-axis is the real part and the $y$-axis is the imaginary part.

![Complex Conjugates](../../images/notes/week8/conjugates_graph.png)

In the graph we can see that the complex conjugates are a reflection of each other. This is because the imaginary part of the complex conjugate is the negative of the original imaginary part.

The mathematics is quite useful for us. Consider the produce of two complex conjugates:

$$z = a + ib$$
$$z^* = a - ib$$

So that,

$$zz^* = (a+ib)(a-ib) = a^2 + b^2$$

The product of a complex number and its complex conjugate is always a real number. Moreover, we can define the magnitude of a complex number as:

$$|z| = \sqrt{zz^*} = \sqrt{a^2 + b^2},m$$

which is also real! Given that $C_1$ and $C_2$ are complex conjugates ($C_2 = C_1^*$), we can write the general solution to the SHO as:

$$x(t) = C_1 e^{i\omega t} + C_1^* e^{-i\omega t}$$

### What does that mean for the SHO?

There's a few more mathematical properties for complex conjugates that are useful for the SHO. The general solution to the SHO is. Let:

$$z = a + ib$$
$$z^* = a - ib$$

So that,

$$z+z^* = 2a,$$
$$z-z^* = 2ib.$$

We denote the Real Part of a complex number as $Re(z)$ and the Imaginary Part as $Im(z)$. So that,

$$Re(z) = Re(z^*) = a,$$
$$Im(z) = -Im(z^*) = b.$$

The real and imaginary parts of a complex number are real numbers. We can apply these properties to the general solution of the SHO:

$$x(t) = C_1 e^{i\omega t} + C_1^* e^{-i\omega t}$$
$$x(t) = C_1 e^{i\omega t} + \left(C_1 e^{i\omega t}\right)^*$$
$$x(t) = 2Re\left(C_1 e^{i\omega t}\right)$$

let $C = 2C_1$ so that,

$$x(t) = Re\left(C e^{i\omega t}\right).$$

This must be equal to a real function of time. For example,

$$x(t)= A\cos(\omega t-\delta),$$

which we can write as,

$$x(t) = Re\left(Ae^{i(\omega t - \delta)}\right) = Re\left(Ae^{-i\delta}e^{i\omega t}\right).$$

Thus, 

$$C = Ae^{-i\delta}.$$

This is a bit abstract, but let's try to graph this and make it a bit concrete. Below, we've plotted the solution to an oscillator that starts with a $\delta = \pi/4$ phase shift. The solution is plotted in the complex plane with rainbow colors to demonstrate time (from violet to red). The starting point is marked with a black square, and because the $omega$ is positive, the solution moves counter-clockwise in the plane.

Below that we trace the real part of the solution in the $t$-$x$ plane. This is not the same as a readout on something like an oscilloscope, or a time trace of the solution. But we can rotate the graph to be in the $x$-$t$ plane - and thus a real temporal solution. In all cases, the black square marks the starting point of the solution, and the rainbow of points marks the solution as it moves in time. 


```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.style.use('seaborn-v0_8-colorblind')

C1 = 1
delta = np.pi/4
omega = 1
t = np.linspace(0, 2*np.pi, 100)

x = C1*np.exp(1j*(omega*t - delta))

## Plot the trajectory in the complex plane

fig, ax = plt.subplots(1,1, figsize=(6, 6))
plt.scatter(x.real, x.imag, c=t, cmap=cm.rainbow, s=15)
plt.plot(x.real[0], x.imag[0], 'ks', markersize=15, label='Start')
plt.axhline(0, color='k', lw=2)
plt.axvline(0, color='k', lw=2)
plt.grid()
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.tight_layout()

## Plot the trajectory in the t-x plane
fig, ax = plt.subplots(1,1, figsize=(6, 6))
plt.scatter(x.real, t, c=t, cmap=cm.rainbow, s=15, label='Real Part')
plt.plot(x.real[0], t[0], 'ks', markersize=15, label='Start')
plt.axvline(0, color='k', lw=2)
plt.grid()
plt.xlabel('x')
plt.ylabel('t', rotation=0)
plt.tight_layout()

# Plot the trajectory in the x-t plane
fig, ax = plt.subplots(1,1, figsize=(6, 6))
plt.scatter(t, x.real, c=t, cmap=cm.rainbow, s=15, label='Real Part')
plt.plot(t[0], x.real[0], 'ks', markersize=15, label='Start')
plt.axhline(0, color='k', lw=2)
plt.grid()
plt.xlabel('t')
plt.ylabel('x', rotation=0)
plt.tight_layout()
```


    
![png](08_notes_files/08_notes_6_0.png)
    



    
![png](08_notes_files/08_notes_6_1.png)
    



    
![png](08_notes_files/08_notes_6_2.png)
    


## Damped Oscillations

The firs complication we can add to an oscillator is a bit of damping, or friction. It's common to see this in real systems. Here, we add a force that removes energy from the system. This is often modeled as a force that is proportional to the velocity of the system:
$$F_{damping} = -b\dot{x}$$

where $b$ is a constant that depends on the system. The equation of motion is then:

$$m\ddot{x} = -kx - b\dot{x}$$
or, rearranging terms,

$$m\ddot{x} + b\dot{x} + kx = 0$$

### Common simplifications

We often rewrite the equation in terms of $\ddot{x}$:

$$\ddot{x} + \dfrac{b}{m}\dot{x} + \dfrac{k}{m}x = 0$$

And then we define a few constants:

$$\omega_0 = \sqrt{\dfrac{k}{m}} \text{ (natural frequency)}$$
$$2\beta = \dfrac{b}{m} \text{ (damping constant)}$$

Thus we obtain:

$$\ddot{x} + 2\beta\dot{x} + \omega_0^2 x = 0$$

This is a second order, linear ODE, so if we find a solution, and it first our initial conditions, we can be sure it is the solution to the problem.

:::{admonition} Uniqueness of the solution
:class: tip

Linear ODEs have a very nice property: if you find a solution to the ODE, and it satisfies the initial conditions, then it is the unique solution to the problem. This stems from the [Picard-Lindelöf theorem](https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem).

That is you are guaranteed that if you find a solution, you can be sure it is the only solution.

There's a caveat to this, if you find multiple solutions and they are different, then your solution is the linear combination of those solutions.

We will exploit this property frequently.
:::

### Finding the solution

Let's assume a solution of the form and see where that gets us:

$$x(t) = e^{r t}$$

So that the derivatives are:

$$\dot{x}(t) = r e^{r t} \qquad \ddot{x}(t) = r^2 e^{r t}$$

Substituting these into the ODE gives us:

$$r^2 e^{r t} + 2\beta r e^{r t} + \omega_0^2 e^{r t} = 0$$

We can factor out the $e^{r t}$ term:

$$e^{r t} \left(r^2 + 2\beta r + \omega_0^2\right) = 0$$

Except for the trivial case of $e^{r t} = 0$, we can divide both sides by $e^{r t}$:

$$r^2 + 2\beta r + \omega_0^2 = 0$$

This is the so called [Auxilary Equation](https://en.wikipedia.org/wiki/Auxiliary_equation). This is a quadratic equation in $r$ and we can solve it using the quadratic formula:

$$r = \dfrac{-2\beta \pm \sqrt{(2\beta)^2 - 4\omega_0^2}}{2}$$

So that we obtain two roots:

$$r_1 = -\beta + \sqrt{\beta^2 - \omega_0^2}$$
$$r_2 = -\beta - \sqrt{\beta^2 - \omega_0^2}$$

As uniqueness guides us, we can write the general solution as a linear combination of the two solutions:

$$x(t) = A e^{r_1 t} + B e^{r_2 t}$$

Where $A$ and $B$ are constants that depend on the initial conditions of the system.

In full detail that solution is:

$$x(t) = e^{-\beta t}\left(A e^{\sqrt{\beta^2 - \omega_0^2} t} + B e^{-\sqrt{\beta^2 - \omega_0^2} t}\right).$$

## Case Studies of Damped Oscillations

Let's look a the three cases of damping. We can classify the system based on the value of $\beta$ and $\omega_0$.

### No Damping $\beta=0$

This is just the case of the SHO. The solution is:

$$x(t) = e^{-\beta t}\left(A e^{\sqrt{\beta^2 - \omega_0^2} t} + B e^{-\sqrt{\beta^2 - \omega_0^2} t}\right).$$

$$x(t) = e^0 \left(A e^{\sqrt{-\omega^2} t} + B e^{\sqrt{-\omega^2 t}}\right)$$

$$x(t) = C_1 e^{i\omega t} + C_2 e^{-i\omega t}$$

This is the same solution we had before. The system oscillates with a frequency $\omega_0$ and the amplitude is constant.

### Weak Damping $\beta^2 < \omega_0^2$

Technically, weak means $\beta^2 \ll \omega_0^2$, but whatever. Let's just work this out:

$$\beta^2 - \omega_0^2 < 0$$

So that

$$\sqrt{\beta^2 - \omega_0^2} = i\sqrt{\omega_0^2 - \beta^2} = i\omega_1.$$

We introduce a new frequency $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$, which is different from the natural frequency $\omega_0$. The solution is:

$$x(t) = e^{-\beta t}\left(C_1 e^{\sqrt{\beta^2 - \omega_0^2} t} + C_2 e^{-\sqrt{\beta^2 - \omega_0^2} t}\right)$$

So that with a change to $\omega_1$ we have:

$$x(t) = e^{-\beta t}\left(C_1 e^{i\omega_1 t} + C_2 e^{-i\omega_1 t}\right)$$

Or an equivalent form:

$$x(t) = Ae^{-\beta t}\cos(\omega_1 t + \delta)$$

This is an oscillator with a decay envelope that is decaying according to the factor $e^{-\beta t}$. We can graph it.

This is what we call an underdamped oscillator. The system oscillates with a frequency $\omega_1$ and the amplitude decays exponentially with time.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

A = 1
beta = 0.5
omega = 10
omega1 = np.sqrt(omega**2 - beta**2)
t = np.linspace(0, 2*np.pi, 1000)
x = A*np.exp(-beta*t)*np.cos(omega1*t)
upper_envelope = A*np.exp(-beta*t)
lower_envelope = -A*np.exp(-beta*t)

plt.plot(t, x, 'C0', label='Underdamped Oscillation')
plt.plot(t, upper_envelope, 'C1--', label='Upper Envelope')
plt.plot(t, lower_envelope, 'C1--', label='Lower Envelope')
plt.axhline(0, color='k', lw=2)
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Damped Oscillation with Decay Envelope shown')
#plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

```


    
![png](08_notes_files/08_notes_9_0.png)
    


### Strong Damping $\beta^2 > \omega_0^2$

Again, the assumption is really $\beta^2 \gg \omega_0^2$, but let's just work this out. In the case of strong damping, we have:

$$\beta^2 - \omega_0^2 > 0$$

So that $\sqrt{\beta^2 - \omega_0^2}$ is a real number. We can write the solution as:

$$x(t) = C_1 e^{(-\beta - \sqrt{\beta^2 - \omega_0^2})t} + C_2 e^{(-\beta + \sqrt{\beta^2 - \omega_0^2})t}$$

Let's consider $t \rightarrow \infty$. Both terms will decay to zero. This is overdamped motion. And typically there's a transient motion that quickly decays to zero. The system does not oscillate, but rather returns to equilibrium without oscillating. Let's graph it.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

C1 = 1
C2 = -1
omega = 10
beta = 100

t = np.linspace(0, 2*np.pi, 1000)

x = C1*np.exp(-1*(beta-np.sqrt(beta**2 - omega**2))*t) + C2*np.exp(-1*(beta+np.sqrt(beta**2 - omega**2))*t)

plt.plot(t, x, 'C0', label='Overdamped Oscillation')
plt.grid()
plt.axhline(0, color='k', lw=2)
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Overdamped Oscillation')

plt.tight_layout()
plt.show()
```


    
![png](08_notes_files/08_notes_11_0.png)
    


### Critical Damping $\beta^2 = \omega_0^2$

This is the case where we naively would find:

$$\sqrt{\beta^2 - \omega_0^2} = 0$$

so that,

$$x(t) \propto e^{-\beta t}$$

So the solution just decays to zero??

No! Our guess of $x(t) = e^{r t}$ is only a good guess unless $\beta = \omega_0$. In this case, we have a double root. We need to find a new solution. We can do this by multiplying our guess by $t$:
$$x(t) = t e^{-\beta t}$$

So the general solution is for critical damping is:

$$x(t) = e^{-\beta t}\left(C_1 + C_2 t\right)$$

And we plot that below.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

C1 = 1
C2 = -1
omega = 1
beta = 1

t = np.linspace(0, 2*np.pi, 1000)
x = np.exp(-beta*t)*(C1 + C2*t)

plt.plot(t, x, 'C0', label='Critically Damped Oscillation')
plt.axhline(0, color='k', lw=2)
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Critically Damped Oscillation')
plt.grid()
plt.tight_layout()
plt.show()
```


    
![png](08_notes_files/08_notes_13_0.png)
    

# Week 8 - Oscillations

Oscillatory or periodic behavior is a common phenomenon in nature. We see it in the motion of pendulums, springs, and other mechanical systems. But oscillations are not limited to mechanical systems; they can also be found in electrical circuits, biological systems, and even in the behavior of populations in ecology. The study of periodic motion is foundational to the understanding of many physical systems because many present themselves with local minima in their potential energy. Alternatively, some systems are confined in ways that lead to periodic motion. 

The most common of these is the simple harmonic oscillator, which is a system that experiences a restoring force proportional to its displacement from equilibrium. The motion of that system is not just periodic, but sinusoidal, a particular kind of periodicity in which we obtain a sinusoidal function with very nice properties.

## Reminder of the SHO

The simple harmonic oscillator (SHO) is a system that experiences a restoring force proportional to its displacement from equilibrium. The equation of motion for a simple harmonic oscillator is given by:

$$m\ddot{x} = -k x.$$

The associated potential energy is given by:

$$U(x) = \frac{1}{2} k x^2 + U_0.$$

It is this potential energy that leads to not only peridioc motion, but the sinusoidal nature of the motion. And because the approximation near a local minimum often yields a quadratic potential to leading order, 

$$U(x) \propto x^2,$$

we can use the SHO to approximate many systems. The solution to the SHO is well-established, and we can write the position of the oscillator as a function of time. We know there are several forms of the solution that are all valid, but they must have two free parameters to match the initial conditions. 

$$x(t) = A \cos(\omega t) + B \sin(\omega t),$$
$$x(t) = C \cos(\omega t + \phi),$$
$$x(t) = C_1 e^{i \omega t} + C_2 e^{-i \omega t}.$$

## Nonlinear oscillators

While the SHO is a well known and well-studied system, many systems are not simple harmonic oscillators. In fact, most systems are not simple harmonic oscillators. The potential energy of a system can be more complicated than a simple quadratic function. For example, the potential energy of a pendulum is given by:

$$U(\theta) = mgL(1 - \cos(\theta)).$$

The general motion of a pendulum is thus not simple harmonic motion, but it can be approximated as simple harmonic motion for small angles. 

There are other examples:

* The [Duffing Oscillator](https://en.wikipedia.org/wiki/Duffing_oscillator) is a nonlinear oscillator that can exhibit chaotic behavior. Typically it is driven by an external force, which can be periodic or random. The driven Duffing oscillator is given by:

$$\ddot{x} + \delta \dot{x} + \alpha x + \beta x^3 = F_0 \cos(\omega t)$$

* The [Van der Pol Oscillator](https://en.wikipedia.org/wiki/Van_der_Pol_oscillator) is a nonlinear oscillator that can exhibit [limit cycle behavior](https://en.wikipedia.org/wiki/Limit_cycle). 

$$\ddot{x} - \mu(1-x^2)\dot{x} + x = 0$$

* It can also be driven by an external force:

$$\ddot{x} - \mu(1-x^2)\dot{x} + x - A \sin(\omega t)$$

All of the tools we develop to investigate the SHO can be ported to these systems.

## Synchronization (21 minute video)

One of the most interesting aspects of an oscillator is that they can couple to each other. This leads to things like [beats](https://en.wikipedia.org/wiki/Beat_(acoustics)), where two oscillators with slightly different frequencies can create a new frequency that is the difference of the two. This is a common phenomenon in music, where two instruments playing slightly out of tune can create a new frequency that is the difference of the two.

But even more interesting is the phenomenon of [synchronization](https://en.wikipedia.org/wiki/Synchronization). 

How do fireflies end up blinking together? How do walking people end up moving in step? How does your heart physically push blood through your body? 

Each of these questions has to do with the physics of [synchronization](https://en.wikipedia.org/wiki/Synchronization). There's a lot of interesting physics in this space. The phenomenon of synchronization is rooted in the physics of [oscillations](https://en.wikipedia.org/wiki/Oscillation) and [waves](https://en.wikipedia.org/wiki/Wave). 

When oscillators couple (or influence each other), we begin to see behavior that is more complex than the sole oscillator. These "coupled oscillators" can demonstrate a wide variety of behaviors, including synchronization. They also form the basis for important technologies like [lasers](https://en.wikipedia.org/wiki/Laser) and [radio transmitters](https://en.wikipedia.org/wiki/Radio_transmitter).

 We will begin our study of oscillations with the [simple harmonic oscillator](https://en.wikipedia.org/wiki/Simple_harmonic_motion), then we add a little [damping](https://en.wikipedia.org/wiki/Damping) to the system, and then move to more complex systems (e.g., [the Duffing oscillator](https://en.wikipedia.org/wiki/Duffing_equation)).

 The video below is a good introduction to the topic of synchronization and worth a watch. 

[![The Surprising Secret of Synchronization](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=t-_VPRCtiUg)


# Week 9 - Notes: Driven Oscillations

We have seen that oscillators that have only a potential energy term will oscillate forever -- energy is conserved. While the oscillations can take any shape, they are periodic. 

Damped oscillators dissipate energy, and so the oscillations will eventually die out. With the damped harmonic oscillator, the oscillations are still periodic, but the amplitude decreases over time. For that model,

$$\ddot{x} + 2\beta \dot{x} + \omega_0^2 x = 0$$

we found that the relative strengths of $\beta$ and $\omega_0$ determined the type of oscillation. But the motion always died out because the damping removed energy from the system.

**What if we kept putting energy into the system?**

We can replenish the energy that is lost to damping by adding a driving force. These are driven oscillators, sometimes called forced oscillators. The driving force is a time dependent force that is added to the system.


:::{admonition} Time Dependent Force Not Periodic
:class : tip

Here we used time dependent force to mean a force that depends on nearly any function of time $F(t)$. The force does not have to be perdiodic, but it can be. 

Systems can be given a kick or pulse of energy (which we might model with a [delta function](https://en.wikipedia.org/wiki/Delta_function) or a [step function](https://en.wikipedia.org/wiki/Heaviside_step_function), or they can be driven by a periodic force.

For most of our examples, we will use a periodic driving force.
:::

## Driving the Oscillator

For the damped harmonic oscillator, we had
$$m\ddot{x} + b \dot{x} + k x = 0$$

Now we will add a driving force $F(t)$ to the system, so that the equation of motion becomes
$$m\ddot{x} +b \dot{x} + k x = F(t)$$

We can represent that setup in the picture below. The blue spring with spring constant $k$ is attached to a red mass $m$. There is a dashpot (damping) in green with damping constant $b=2\beta$. The driving force $F(t)$ is shown in black and called "driver".

![driven oscillator](../../images/notes/week9/driven_oscillator.png)

We write that differential equation as:

$$\ddot{x} + 2\beta \dot{x} + \omega_0^2 x = F(t)/m=f(t)$$

where $\omega_0^2 = k/m$ and $2\beta = b/m$. The function $f(t)$ is the driving force per unit mass.

**Note that this differential equation remains linear.**

Why? Because the "operations" on x(t) are linear.

## Linearity of Differential Equations

A linear differential equation has many nice properties. In particular, the superposition of solutions and the uniqueness of solutions. So it is worth knowing when you have one.

**Claim:** $\dfrac{d}{dt}$ is a linear operator.

What is an operator? It is simply a function that takes a function as an input and returns another function as an output. The derivative is a function that takes a function and returns another function, namely the slope of the tangent line to the original function everywhere it is defined and differentiable.

Let's prove that $\dfrac{d}{dt}$ is a linear operator. 

Let $x(t) = x_1(t) + x_2(t)$, where $x_1(t)$ and $x_2(t)$ are two functions. Then

$$\dfrac{dx(t)}{dt} = \dfrac{d}{dt} \left(x_1(t) + x_2(t)\right) = \dfrac{dx_1(t)}{dt} + \dfrac{dx_2(t)}{dt}$$

We can distribute the derivative across the sum of the two functions. Thus $\dfrac{d}{dt}$ is a linear operator.

This also suggests that constants and other simple derivatives are linear operators (e.g., $\dfrac{d^2}{dt^2}$ and $\dfrac{d^3}{dt^3}$). And because of the distributive property, any linear sum of linear operators is also a linear operator (e.g., $\dfrac{d^2}{dt^2} + \dfrac{d}{dt}$).

We can write the diffferential equation for the driven oscillator as

$$\dfrac{d^2x(t)}{dt^2} + 2\beta \dfrac{dx(t)}{dt} + \omega_0^2 x(t) = f(t).$$

We group the terms of the left hand side into a single operator, $\mathcal{D}$, so that

$$\mathcal{D} x(t) = \left(\dfrac{d^2}{dt^2} + 2\beta \dfrac{d}{dt} + \omega_0^2\right) x(t) = f(t)$$

The operator $\mathcal{D}$ is a linear differential operator. This compact notation expresses the linearity of the differential equation.

$$\mathcal{D} x(t) = f(t)$$

### Effect of a Linear Operator on our Solutions

Because $\mathcal{D}$ is a linear operator, we can distribute it. This results in our finding a linear combination of solutions to the differential equation. This is built up quite easily in three steps.

1. We can allow the operator to act on a function scaled by a scalar constant $a$: 

$$\mathcal{D} \left(a x(t)\right) = a \mathcal{D} x(t)$$

2. We can allow the operator to act on a sum of functions:

$$\mathcal{D} \left(x_1(t) + x_2(t)\right) = \mathcal{D} x_1(t) + \mathcal{D} x_2(t)$$

3. We can allow the operator to act on a linear combination of functions:

$$\mathcal{D} \left(a x_1(t) + b x_2(t)\right) = a \mathcal{D} x_1(t) + b \mathcal{D} x_2(t)$$

This is the superposition principle in action. But we have to be careful when we apply it. For example, when,

$$\mathcal{D} x(t) = f(t)$$

we must first solve the homogeneous equation, $\mathcal{D} x(t) = 0$.

## Homogeneous and Particular Solutions

The damped driven oscillator is a linear differential equation. But that means that any solution to the equation where the driving force is zero is a solution to the equation where the driving force is non-zero. And, thus must be added to the solution of the non-homogeneous equation. 

Let's use the language of differential operators to express this. We want to solve:

$$\mathcal{D} x(t) = f(t)$$

where $\mathcal{D}$ is a linear differential operator. But any solution to the homogeneous equation, $\mathcal{D} x_h(t) = 0$, is a solution to the non-homogeneous equation. 

We use the notation $x_h(t)$ to denote the solution to the homogeneous equation.

So let's use the superposition principle to write the solution to the non-homogeneous equation as a sum of two parts:

$$x(t) = x_h(t) + x_p(t)$$

where $x_p(t)$ is a particular solution to the non-homogeneous equation. We will get to the name of $x_p(t)$ in a moment. Let's the focus on the mathematical properties of the solution for a moment.

$$\mathcal{D} x(t) = \underbrace{\mathcal{D} x_h(t)}_0 + \mathcal{D} x_p(t) = f(t)$$

With the homogeneous solution, $\mathcal{D} x_h(t) = 0$, we have

$$\mathcal{D} x_p(t) = f(t)$$

That is what defines the particular solution. In our case, that it is specific to the driving force $f(t)$ we have chosen.

**Summary:** When solving $\mathcal{D} x(t) = f(t)$, the solution is the sum of the homogeneous solution $x_h(t)$ and a particular solution $x_p(t)$. We typically solve the homogeneous equation $\mathcal{D} x_h(t) = 0$ first. 

The solutions $x_h(t)$ satisfies the unknowns set by the initial conditions. The particular solution $x_p(t)$ is a solution to the non-homogeneous equation $\mathcal{D} x_p(t) = f(t)$, so it will not depend on the initial conditions, how it is particular to the driving force $f(t)$.

## Example: Sinusoidal Driving Force

Let's consider a sinusoidal driving force. We will use the following notation for the driving force:

$$f(t) = f_0 \cos(\omega t)$$

where $f_0$ is the amplitude of the driving force and $\omega$ is the angular frequency of the driving force. **Note that $\omega$ is not necessarily the same as $\omega_0$.**

So we can write the differential equation for the driven oscillator as

$$\mathcal{D} x(t) = f_0 \cos(\omega t)$$

where $\mathcal{D}$ is the linear differential operator

$$\mathcal{D} = \dfrac{d^2}{dt^2} + 2\beta \dfrac{d}{dt} + \omega_0^2$$

Note that if instead $f(t) = f_0 \sin(\omega t)$, then we would have

$$\mathcal{D} y(t) = f_0 \sin(\omega t)$$

where $y(t)$ is the solution to the differential equation with a sine driving force and $\mathcal{D}$ is the same linear differential operator. Writing both the $x(t)$ of $y(t)$ differential equations out, we have

$$\ddot{x} + 2\beta \dot{x} + \omega_0^2 x = f_0 \cos(\omega t)$$
$$\ddot{y} + 2\beta \dot{y} + \omega_0^2 y = f_0 \sin(\omega t)$$

### Two Birds, One Stone

We can cleverly combine these two equations into a singlle differential equation by using complex numbers.

$$z(t) = x(t) + i y(t).$$

We can similarly write $f(t)$ as a complex sum:

$$f(t) = f_0 \cos(\omega t) + i f_0 \sin(\omega t) = f_0 e^{i \omega t}.$$

Now because of linearity, we can write the differential equation for $z(t)$ as

$$\mathcal{D} z(t) = f_0 e^{i \omega t}.$$

Written out, we have

$$\ddot{z} + 2\beta \dot{z} + \omega_0^2 z = f_0 e^{i \omega t}.$$

### Particular Solution

We note the particular solution depends on the driving force. We can try one that follows the complex exponential form of the driving force.

$$z_p(t) = C e^{i \omega t}$$

where $C$ is a complex constant. We can find $C$ by substituting $z_p(t)$ into the differential equation.


$$\ddot{z}_p + 2\beta \dot{z}_p + \omega_0^2 z_p = f_0 e^{i \omega t}$$
$$\left(-\omega^2 + 2\beta i \omega + \omega_0^2\right) C e^{i \omega t} = f_0 e^{i \omega t}$$

We can cancel the $e^{i \omega t}$ terms on both sides of the equation, and we are left with

$$\left(-\omega^2 + 2\beta i \omega + \omega_0^2\right) C = f_0.$$

We can solve for $C$:

$$C = \dfrac{f_0}{\omega_0^2 - \omega^2 + 2\beta i \omega}.$$

We found $C$ and it is fully determined. But it is a complex number. Ultimately, we want a real valued solution, but we remember that 

$$Re(z(t)) = x(t) \qquad Im(z(t)) = y(t).$$

And we can write the coefficient $C$ as a magnitude $A$ and a phase $\delta$:

$$C = A e^{-i \delta}$$

### Writing the Complex Amplitude

Let's find that form of $C$.

$$A^2 = CC^*$$
$$A^2 = \left(\dfrac{f_0}{\omega_0^2 - \omega^2 + 2\beta i \omega}\right) \left(\dfrac{f_0}{\omega_0^2 - \omega^2 - 2\beta i \omega}\right)$$
$$A^2 = \dfrac{f_0^2}{\left(\omega_0^2 - \omega^2\right)^2 + 4\beta^2 \omega^2}$$

So the amplitude of the particular solution is

$$A = \dfrac{f_0}{\sqrt{\left(\omega_0^2 - \omega^2\right)^2 + 4\beta^2 \omega^2}}.$$

We can find the phase by looking at $C= A e^{-i \delta}$:

$$C = \dfrac{f_0}{\omega_0^2 - \omega^2 + 2\beta i \omega} = A e^{-i \delta}$$

$$f_0e^{i\delta} = A \left(\omega_0^2 - \omega^2 + 2\beta i \omega\right)$$

Note that both $f_0$ and $A$ are real numbers, so the complex phase of $\delta$ is determined by the complex number on the right side of the equation.

That is, the phase of the $e^{-i\delta}$ term and the phase of the complex number $\left(\omega_0^2 - \omega^2 + 2\beta i \omega\right)$ are the same. So we can write ratio of their imaginary and real parts as,

$$\tan(\delta) = \dfrac{2\beta \omega}{\omega_0^2 - \omega^2}$$

$$\delta = \arctan\left(\dfrac{2\beta \omega}{\omega_0^2 - \omega^2}\right)$$

Again, this number is fully determined without initial conditions.

### Back to the Particular Solution

We proposed a solution $z_p(t) = C e^{i \omega t}$, where $C$ is a complex constant. This became

$$z_p(t) = A e^{-i \delta} e^{i \omega t} = A e^{i(\omega t - \delta)}$$

where $A$ is a real number and $\delta$ is a real number. Note we can write the particular solutions for both $x(t)$ and $y(t)$ as

$$x_p(t) = Re\left(z_p(t)\right) = A \cos(\omega t - \delta)$$
$$y_p(t) = Im\left(z_p(t)\right) = A \sin(\omega t - \delta)$$

### General Solution

The proposed general solution was 

$$x(t) = x_h(t) + x_p(t)$$

And for our sinusoidal driving force, we have found the particular solution, so that we can write:

$$x(t) = x_h(t) + A \cos(\omega t - \delta)$$

where $x_h(t)$ is the solution to the homogeneous equation, $\mathcal{D} x_h(t) = 0$.

We propose a solution form for $x_h(t)$ that is a linear combination of two exponential functions (as we did before):

$$x_h(t) = C_1 e^{\lambda_1 t} + C_2 e^{\lambda_2 t}.$$

These are solutions to the damped oscillator, and we refer to them as the "transient" solutions. They are transient because they die out over time due to damping. 

For a weakly damped system, $\beta^2 < \omega_0^2$, which is the case that is most interesting to us, we can write the solution as,

$$x(t) = A \cos(\omega t - \delta) + A_{tr}e^{-\beta t} \cos(\omega_1 t - \delta_{tr})$$

where $A_{tr}$ is the amplitude of the transient solution, $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$ is the damped frequency (per usual), and $\delta_{tr}$ is the phase of the transient solution.


## Resonance and Tuning

A curious thing about the long term behavior (after the transients die out) is that we can observe large amplitudes at particular choices of driving. Consider the long term (stady state) solution to the driven damped harmonic oscillator:

$$x_{longterm}(t) = A \cos(\omega t - \delta)$$

where,

$$A^2 = \dfrac{f_0^2}{\left(\omega_0^2 - \omega^2\right)^2 + 4\beta^2 \omega^2}.$$

Let's allow $\beta$ to be small so that $4\beta^2 \omega^2$ is small. If we focus on the denominator, we can see that the amplitude will be small when $\omega$ is far from $\omega_0$. But if we choose $\omega$ to be close to $\omega_0$, then the denominator will be small, and the amplitude will be large.

The second result is a [resonance](https://en.wikipedia.org/wiki/Resonance) effect. The system will resonate at a particular frequency, $\omega_0$, and the amplitude of the oscillations will be large. Below is a sketch of the response of a driven damped harmonic oscillator to a sinusoidal driving force. The amplitude of the oscillations is plotted as a function of the driving frequency $\omega$.

![Resonance Sketch](../../images/notes/week9/resonance.png)

### Achieving Resonance

There's two ways that we can approach this. Let's focus on the denominator of the amplitude equation:

$$\left(\omega_0^2 - \omega^2\right)^2 + 4\beta^2 \omega^2$$

When that denominator is small, the amplitude will be large. There's two ways to make the denominator small.

**Case 1:** Tune the $\omega_0$ (the natural frequency of the system) to be close to $\omega$ (the driving frequency). This is how a car radio works. You change the resistance of the radio circuit to change the natural frequency of the radio circuit. You can then tune the radio to a particular station that is broadcasting at a particular frequency. This gives an amplified signal,

When $\omega_0 = \omega$, then the denominator is equal to $4\beta^2 \omega_0^2$. The amplitude is

$$A = \dfrac{f_0}{2\beta \omega_0}.$$

**Case 2:** Tune the driver ($\omega$) to be close to $\omega_0$. 

Because we are adjusting the driver, we are seeking the driving frequency that minizes the denominator. We can do this by setting the derivative of the denominator with respect to $\omega$ to zero.

$$\dfrac{d}{d\omega} \left(\left(\omega_0^2 - \omega^2\right)^2 + 4\beta^2 \omega^2\right) = 0$$

$$2\left(\omega_0^2 - \omega^2\right) \left(-2\omega\right) + 8\beta^2 \omega = 0$$

$$-4\omega_0^2 \omega + 4\omega^3 + 8\beta^2 \omega = 0$$

$$4\omega\left(\omega^2 - \omega_0^2 + 2\beta^2\right) = 0$$

$$\omega = 0 \qquad \text{or} \qquad \omega^2 - \omega_0^2 + 2\beta^2 = 0$$

Thie first solution is when there is no driver. But the second, $\omega_2$, is the frequency that minimizes the denominator. We can write that as

$$\omega_2 = \sqrt{\omega_0^2 - 2\beta^2}$$

We can a strong response when $\omega_0^2 \gg 2\beta^2$ or when $\omega_2 \approx \omega_0$.


```python

```




# Week 9 - Driven Oscillators and Resonance

Thus far, we have either worked with energy conserving systems or systems that dissipate energy to the point of stopping their motion. The primary examples have been conservative systems, potential energy oscillators, and systems with damping that extract all the kinetic energy from the system. [Driven Systems](https://en.wikipedia.org/wiki/Driven_oscillator) are systems that are driven by external forcing. We use "forcing" because it's not always a push or a pull. Radio systems use electromagnetic waves to drive the system. Climate systems are driven by thermal forcing. 

Driven oscillators are a specific type of driven system, we expect them to demonstrate recurrent bahevior. Driven ooscillators are quite common. Analog radios use a driven oscillator that is tuned to a specific frequency (99.5 FM is tuned to 99.5 MHz). When you dial the radio you are "tuning" the oscillator to the frequency of the broadcast. This is an illustration of the phenomenon of [resonance](https://en.wikipedia.org/wiki/Resonance). Resonance is a phenomenon where a system is driven at a frequency that matches (or closely matches) its natural frequency. When this happens, the amplitude of the oscillation can grow very large. Resonance is the phenomenon that caused the [collapse of the Tacoma Narrows Bridge](https://en.wikipedia.org/wiki/Tacoma_Narrows_Bridge_(1940)) in 1940. 

## Collapse of the Tacoma Narrows Bridge (9 minute video)

Resonance is the phenomenon that caused the [collapse of the Tacoma Narrows Bridge](https://en.wikipedia.org/wiki/Tacoma_Narrows_Bridge_(1940)) in 1940. The video below describes the collapse and how the bridge was rebuilt to avoid the same problem. 

[![Why the Tacoma Narrows Bridge Collapsed](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=mXTSnZgrfxM)

## Quantum Mechanical Resonance

You might have heard about resonance in the context of [quantum mechanics](https://en.wikipedia.org/wiki/Resonance_(quantum_mechanics)) or most likely in [particle physics](https://en.wikipedia.org/wiki/Particle_physics) or [nuclear physics](https://en.wikipedia.org/wiki/Nuclear_physics). In these cases, typically resonance is a phenomenon where a system is driven at a frequency that matches some natural spacing of energy levels. In quantum mechanics, frequency of light is related to it's energy by $E = h \nu$, where $h$ is Planck's constant and $\nu$ is the frequency of the light. 

The energy levels of a system are quantized, they are separated by discrete amounts. When a system is driven at a frequency that matches the energy level separation, the system can absorb energy from the driving force. This can cause the system to transition to a higher energy state. A quantum system also ejects an amount of energy as a photon (randomly) and transitions to a lower energy state.  

Probing these transitions can tell you about particle properties and reactions. This is a large field of study in particle and nuclear physics.

## Solving Linear Differential Equations

Much of the work we have done so far has been solving homogeneous linear differential equations. These are equations that have a form like this:

$$\frac{d^2 x}{dt^2} + 2\beta\frac{dx}{dt} + \omega_0^2 x = 0.$$

All of the driven systems that we will work with will be described by a linear differential equation. The general form of a linear differential equation is:

$$\frac{d^n x}{dt^n} + a_{n-1} \frac{d^{n-1} x}{dt^{n-1}} + a_{n-2} \frac{d^{n-2} x}{dt^{n-2}} + ... + a_1 \frac{dx}{dt} + a_0 x = f(t).$$

The $f(t)$ is the driving force. The $a_i$ are constants. The $n$ is the order of the differential equation.

We've never solved a driven differential equation before, but we have two powerful tools: superposition and uniqueness. Superposition tells us that we can solve the homogeneous part of the equation and then add a particular solution to get the full solution. Uniqueness tells us that if we have a solution that fits the driver and the initial conditions, then it is unique. 

As the homogenous solutions for our oscillators will typically die out, we will refer to them as transient solutions. The particular solution will be the steady state solution.


# Week 10 - Activity: Modeling Chaotic Systems

Chaotic systems are complex and unpredictable, often exhibiting sensitive dependence on initial conditions. This can make numerically simulating them challenging. We have used a variety of integrators and noticed that some are better than others for different problems. Here, we will use the built-in integrator from the `scipy` library to simulate our systems ([`solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)).

This integrator is designed to be robust and efficient, making it a good choice for a wide range of problems. We can also specify the integrator to use, which can be helpful for specific applications. In our case, we will use the default integrator, which is a good general-purpose integrator. However, we can also specify other integrators, such as `RK45`, `RK23`, `DOP853`, etc., depending on our needs. For the most part, these integrators are using different methods of estimating the slope of the function at each step, which can affect the accuracy and stability of the simulation. They also have different efficiency and performance characteristics, which can be important for large-scale simulations.

We start with a code that simulates a damped driven pendulum, and the plots we want to obtain. You will can use those to develop simulations of the [Duffing oscillator](https://en.wikipedia.org/wiki/Duffing_equation) and the [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system) later.

## Using solve_ivp to simulate chaotic systems

We have written a variety of integrators for solving ordinary differential equations (ODEs). In this activity, we will introduce the `solve_ivp` function from the `scipy.integrate` module, which is a versatile and powerful tool for solving ODEs. We will use it to simulate chaotic systems and explore its capabilities.

To set up a `solve_ivp` simulation, we need to define the system of ODEs we want to solve. Let's focus on the damped driven pendulum, a classic example that we will use to illustrate the process. 

### Damped Driving Pendulum

Consider a pendulum that can swing in a plane on a pivot. The pendulum hinge is driven by a horizontal oscillator that oscillates with a constant frequency and amplitude. The second order ODE that describes such a damped driven pendulum is:

$$
\frac{d^2\theta}{dt^2} + \beta \frac{d\theta}{dt} + \sin(\theta) = A \cos(\omega_D t)
$$

where $\theta$ is the angle of the pendulum, $\beta$ is the damping coefficient, $A$ is the amplitude of the driving force, and $\omega_D$ is the angular frequency of the driving force. We've absorbed some constants into the parameters for simplicity.

### Using solve_ivp

To use `solve_ivp`, we need to convert this second-order ODE into a system of first-order ODEs. We can do this by introducing a new variable for the angular velocity:

$$
\begin{align*}
\dot{\theta} &= \omega \\
\dot{\omega} &= -\sin(\theta) - \beta \omega + A \cos(\omega_D t)
\end{align*}
$$

where $\omega$ is the angular velocity of the pendulum NOT the driver.

Let's implement this system using `solve_ivp` and simulate its behavior over time.

📝 **Read over this code and run it.** Make sure you make sense of what each part does. You will need to modify it for the next part of the activity.


```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy.integrate import solve_ivp
plt.style.use('seaborn-v0_8-colorblind')

# Define the damped driven pendulum equations
# Note that they are first order ODEs
def damped_driven_pendulum(t, y, beta, A, omegaD=1):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -np.sin(theta) - beta * omega + A * np.cos(omegaD*t)
    return [dtheta_dt, domega_dt]

# Parameters that define the system
beta = 0.5         # Damping coefficient
A = 1.0             # Amplitude of driving force
omegaD = 2*np.pi  # Driving frequency
t_span = (0, 100)   # Time span for the simulation
y0 = [6, 0]     # Initial conditions: theta = pi, omega = 0; Note that solve_ivp takes a list of initial conditions
t_eval = np.linspace(t_span[0], t_span[1], 10000)  # Time points to evaluate; Note that solve_ivp takes a list of times to evaluate

# Solve the ODEs using solve_ivp
# Here we pass the function, time span, initial conditions, parameters, and time points to evaluate
# Any additional arguments to the function can be passed in args in the form of a tuple
# Note that the order of arguments in args must match the order of parameters in the function
solution = solve_ivp(damped_driven_pendulum, t_span, y0, args=(beta, A, omegaD), t_eval=t_eval)
```

### Plotting the resulting solution

The solution from `solve_ivp` gives us the values of $\theta$ and $\omega$ over time. We can use this data to create plots that help us visualize the behavior of the damped driven pendulum. These results are evaluated at discrete time points, so we can use them to create time series plots or phase space plots.

The solution object returned by `solve_ivp` contains several attributes, including `t` (the time points) and `y` (the values of the variables at each time point). We can use these to create our plots. Note that the first column of `y` corresponds to $\theta$ and the second column corresponds to $\omega$ because we defined them in that order in the `damped_driven_pendulum` function above.


```python
fig = plt.figure(figsize=(16, 4))
gs = gridspec.GridSpec(2, 2, figure=fig, height_ratios=[1, 1], width_ratios=[3, 1])


ax0 = fig.add_subplot(gs[0, 0])
ax0.plot(solution.t, solution.y[0])
plt.scatter(solution.t[0], solution.y[0][0], color='C1', marker='o', label='Start', s=50)
plt.scatter(solution.t[-1], solution.y[0][-1], color='C2', marker='s', label='End', s=50)
ax0.set_title('Time Series')
ax0.set_ylabel('Position')
ax0.legend()
ax0.grid()

ax1 = fig.add_subplot(gs[1,0])
ax1.plot(solution.t, solution.y[1])
plt.scatter(solution.t[0], solution.y[1][0], color='C1', marker='o', label='Start', s=50)
plt.scatter(solution.t[-1], solution.y[1][-1], color='C2', marker='s', label='End', s=50)
ax1.set_xlabel('Time')
ax1.set_ylabel('Velocity')
ax1.legend()
ax1.grid()

ax2 = fig.add_subplot(gs[:, 1])
ax2.plot(solution.y[0], solution.y[1])
ax2.set_title('Phase Space')
plt.scatter(solution.y[0][0], solution.y[1][0], color='C1', marker='o', label='Start', s=50)
plt.scatter(solution.y[0][-1], solution.y[1][-1], color='C2', marker='s', label='End', s=50)
ax2.set_xlabel('Position')
ax2.set_ylabel('Velocity')
ax2.legend()
ax2.grid()
plt.tight_layout()
```


    
![png](10_notes_files/10_notes_4_0.png)
    


📝 What do you notice about the behavior of this system? Both short and long term? How can you see that in your plots?

**Your Answer Here**

### Investigating Periodicity

As you recall, the damped driven oscillator has two solutions - a transient solution that decays to zero, and a steady-state solution that is periodic. You can see in the above plot that the system starts with a transient solution, but eventually settles into a periodic solution.  Let's truncate the time to see the periodic solution more clearly. Let's look at the last 40 seconds of the simulation. We used `t_eval` to only evaluate the solution at 1000 points, between 0 and 100. We don't need to recalculate the solution, we can just plot the last 40 seconds of the solution we already calculated.

To check the periodicity, we investigate if the time series returns to the same value after a certain period. We can do this by plotting the time series after the transients have decayed. If the system is periodic, we should see a repeating pattern in the plot. Using the physics of the driver, we can plot a point at every period of the driver to see if the system returns to the same value, $T = \frac{2\pi}{\omega}$.

We do that below to demonstrate that after the transient solution decays, the system settles into a single periodic solution. 

One route to chaos is [period-doubling bifurcation](https://en.wikipedia.org/wiki/Period-doubling_bifurcation), where the system goes from a single period to two periods. You can see that we are not at that point yet, but the [Duffing oscillator](https://en.wikipedia.org/wiki/Duffing_equation) is a classic example of a system that exhibits period-doubling bifurcation. 


```python
# Note this block runs the integration again but only returns the last 60 seconds of the simulation
startTime = 60
index = np.where(solution.t > startTime)[0][0]

solution_short_time = solution.t[index:]
solution_short_theta = solution.y[0][index:]
solution_short_omega = solution.y[1][index:]

# Indicies where solution repeats every 2pi/omegaD
period = 2*np.pi/omegaD
indices = np.where((solution_short_time % period) < 0.01)[0]


fig = plt.figure(figsize=(16, 4))
gs = gridspec.GridSpec(2, 2, figure=fig, height_ratios=[1, 1], width_ratios=[3, 1])


ax0 = fig.add_subplot(gs[0, 0])
ax0.plot(solution_short_time, solution_short_theta)
ax0.scatter(solution_short_time[0], solution_short_theta[0], color='C1', marker='o', label='Start', s=50)
ax0.scatter(solution_short_time[-1], solution_short_theta[-1], color='C2', marker='s', label='End', s=50)
ax0.scatter(solution_short_time[indices], solution_short_theta[indices], color='C3', marker='x', s=50)
ax0.set_title('Time Series')
ax0.set_ylabel('Position')
ax0.legend()
ax0.grid()

ax1 = fig.add_subplot(gs[1,0])
ax1.plot(solution_short_time, solution_short_omega)
ax1.scatter(solution_short_time[0], solution_short_omega[0], color='C1', marker='o', label='Start', s=50)
ax1.scatter(solution_short_time[-1], solution_short_omega[-1], color='C2', marker='s', label='End', s=50)
ax1.scatter(solution_short_time[indices], solution_short_omega[indices], color='C3', marker='x', s=50)
ax1.set_xlabel('Time')
ax1.set_ylabel('Velocity')
ax1.legend()
ax1.grid()

ax2 = fig.add_subplot(gs[:, 1])
ax2.plot(solution_short_theta, solution_short_omega)
ax2.set_title('Phase Space')
ax2.scatter(solution_short_theta[0], solution_short_omega[0], color='C1', marker='o', label='Start', s=50)
ax2.scatter(solution_short_theta[-1], solution_short_omega[-1], color='C2', marker='s', label='End', s=50)
ax2.scatter(solution_short_theta[indices], solution_short_omega[indices], color='C3', marker='x', s=50)
ax2.set_xlabel('Position')
ax2.set_ylabel('Velocity')
ax2.legend()
ax2.grid()
plt.tight_layout()
```


    
![png](10_notes_files/10_notes_7_0.png)
    


📝 How does this view of the long term solution help us see the periodicity of the motion? How could we check if the motion follows the driving frequency?

**Your Answer Here**

### A Period-1 Solution

While the specific location of the marked points might vary a little but, we can see that there's roughly a repeated location of those points. In the case of position or velocity, the pink ex marks the spot where the system returns to the same value. The phase space makes that more clear because we can see that the system returns to the roughly the same point in phase space. This is close to a period-1 solution. It might be that we still have some transient behavior, or that our integrator is not perfectly accurate, or that our scheme for selecting the time points is not perfect, but we can see that the system is close to periodic.

We can use this approach to investigate other chaotic systems and explore their behavior over time.

## Period Doubling with the Duffing Oscillator

The Duffing oscillator is a non-linear second-order differential equation that describes the motion of a damped and driven oscillator with a non-linear restoring force. Under certain conditions, it can exhibit chaotic behavior, including period-doubling bifurcations. There are many routes to chaos, but period-doubling is a classic example.

The model is given by:

$$\frac{d^2x}{dt^2} + \delta \frac{dx}{dt} + \alpha x + \beta x^3 = \gamma \cos(\omega t)$$

We can rewrite this as a system of first-order ODEs by introducing a new variable for the velocity:

$$
\begin{align*}
\dot{x} &= v \\
\dot{v} &= -\delta v - \alpha x - \beta x^3 + \gamma \cos(\omega t).
\end{align*}
$$

### 📝 Numerically Integrate the Duffing Oscillator

For our simulation we will observe the effect of the driving strength $\gamma$ on the behavior of the system. We start with the following parameters:

| Parameter | Value |
| --------- | ----- |
| $\delta$  | 0.2   |
| $\alpha$  | -1    |
| $\beta$   | 1     |
| $\gamma$  | 0.3   |
| $\omega$  | 1.2     |

Choose the initial conditions and time span for the simulation:
| Condition | Value |
| --------- | ----- |
| Initial $x$ | 1.0   |
| Initial $v$ | 0     |
| Time span | 100 cycles of the driver |
| Evaluation points | 10000 |

Below we've provided some of the code, but not the definition of the `duffing` function. You will need to write that function and fill in the missing code to complete the simulation.

📝 **Write the rest of the code necessary to simulate the Duffing oscillator.**

📝 **Plot the results of your simulation in the next cell.**


```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy.integrate import solve_ivp
plt.style.use('seaborn-v0_8-colorblind')
```


```python
## def duffing(t, y, delta, alpha, beta, gamma, omega):
    ## Your Code Here

# Parameters
delta = 0.3
alpha = -1.0
beta = 1.0
gamma = 0.2
omega = 1.2

# Time span and initial conditions
cycles = 100
tfinal = 2 * np.pi * cycles / omega
t_span = (0, tfinal)
t_eval = np.linspace(t_span[0], t_span[1], 10000)
y0 = [1.0, 0.0]

# Solve the ODEs using solve_ivp
## Your Code Here
```

### 📝 Plotting the results

Once you have simulated the Duffing oscillator, you can plot the results to visualize its behavior over time. Your plot should be similar to the one above where you plot at least the position $x$ over time, and then a phase space plot of $x$ vs. $v$. Make sure that you label your axes and include a title for your plot; add starting and ending points to your plot so you are sure about the direction of the motion.

This first set of plots should look similar to the one below.

![Duffing](../../images/notes/week10/first_duffing.png)


```python
## Plot the time series and phase space
## Your Code Here
```

### 📝 Investigating Periodicity

Now that you have this solution, look at only the last few cycles of the simulation. You can do this by plotting only the last 10 cycles of the simulation. Include a mark at every cycle of the driver, $T = \frac{2\pi}{\omega}$. This will help you see if the system is periodic or not.


```python
## Plot the time series and phase space
## Your Code Here
```

📝  What did you find the periodicity of this particular set up to be? How did you determine it?

**Your Answer Here**

### Period Doubling

Let's use the same code, or write this code in a new cell, or write a new function, to investigate the effect of increasing the driving strength $\gamma$ on the behavior of the system. 

You will **run the code multiple times**, changing the value of $\gamma$ each time. You can do this by changing the value in the code, or by writing a loop to run through a range of values. In either case, you will need to plot the long term behavior of the system for each value of $\gamma$, including the phase space plot. Your plot should also include a mark at every cycle of the driver, $T = \frac{2\pi}{\omega}$.


For choices of $\gamma$, please use the following values: 0.2, 0.28, 0.29, 0.37, 0.50, 0.68, 0.74, 0.75, 


```python
## Your Code Here
```

## Sensitivity to Initial Conditions with the Lorenz Attractor

The Lorenz attractor is a system of ordinary differential equations that model atmospheric convection. It is a classic example of a chaotic system that exhibits sensitive dependence on initial conditions. It also demonstrates the phenomenon of a [strange attractor](https://en.wikipedia.org/wiki/Strange_attractor). A strange attractor is a fractal structure in phase space that the system approaches asymptotically over time. For the Lorenz attractor, the strange attractor is a set of points in phase space that the system approaches as time goes to infinity - the butterfly shape that you might be familiar with. 

In this activity, we will simulate the Lorenz attractor using `solve_ivp` and explore how solutions diverge from each other based on small differences in initial conditions.

### Mathematical Model

The Lorenz model is given by:

$$\frac{dx}{dt} = \sigma (y - x)$$
$$\frac{dy}{dt} = x(\rho - z) - y$$
$$\frac{dz}{dt} = xy - \beta z$$

Where $\sigma$, $\rho$, and $\beta$ are system parameters. The canonical values are $\sigma = 10$, $\rho = 28$, and $\beta = \frac{8}{3}$.

### 📝 Numerically Integrate the Lorenz Attractor

In the cells below, we scaffold some of the code to simulate the Lorenz attractor. You will need to fill in the missing pieces. Once you plot the solution, you should be able to produce time series, and phase space plots of the Lorenz attractor. **Note that the phase space for the Lorenz attractor is 3D (x,y,z), so you will need to use a 3D plotting function or plot projections.**

For the parameters, we will use the canonical values of $\sigma = 10$, $\rho = 28$, and $\beta = \frac{8}{3}$. Choose initial conditions of $x=1$, $y=1$, and $z=1$ and simulate for 50 time units. If you do, your solution will look like the one below.

![Lorenz Time Series](../../images/notes/week10/lorenz-1.png)

![Lorenz Phase Space](../../images/notes/week10/lorenz-2.png)


```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy.integrate import solve_ivp
plt.style.use('seaborn-v0_8-colorblind')
```


```python
## def lorenz(t, y, sigma, beta, rho):
    ## Your Code Here

# Parameters for the Lorenz system
sigma = 10.0
beta = 8/3
rho = 28.0

# Time span and initial conditions
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)
y0 = [1.0, 1.0, 1.0]

# Solve the differential equations using solve_ivp
## Your Code Here

# Plotting your results
## Your Code Here
```

### 📝 Exploring Sensitivity to Initial Conditions

Noe that you have a solution to the Lorenz attractor, you can observe how trajectories that start from slightly different initial conditions diverge over time. This is a hallmark of chaotic systems, where small differences in initial conditions can lead to vastly different outcomes. We can visualize this as a bundle of trajectories that start from nearby points in phase space and then diverge over time. For the Lorenz attractor, this is often visualized as a butterfly-shaped structure in phase space.

For this activity, we will simulate the Lorenz attractor for two sets of initial conditions that are close together. We will then plot the trajectories in phase space to observe how they diverge over time.

**📝 Modify the code you wrote above to simulate the Lorenz attractor for two sets of initial conditions that are close together. Plot the trajectories in phase space to observe how they diverge over time. Do this as both a time series and in phase space.**


```python
## Your Code Here
```

### 📝 The Strange Attractor

The two trajectories that you plotted above should look like they are diverging over time. This is very common in chaotic systems. However, when you plot the trajectories in the phase space, they seem to occupy a bounded region of space - this is especially true as the trajectories evolve.

This bounded region is called a strange attractor. A strange attractor is a set of points in phase space that the system approaches asymptotically over time. For the Lorenz attractor, the strange attractor is a fractal structure that the system approaches as time goes to infinity.

Let's plot a ton of trajectories starting from different initial conditions to see the strange attractor. We can do this by looping over a range of initial conditions and plotting each trajectory in phase space. 

That will get very messy, so instead, let's integrate 100-1000 trajectories that are near the original trajectory. We will plot only the original and final location of each trajectory. This will give us a sense of the strange attractor without plotting every single trajectory.


```python
## Your Code Here
```
# Week 10 - Chaotic Dynamics

[Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory) is a branch of science that focuses on the study of systems that exhibit chaotic behavior. These systems are quite sensitive to their initial conditions, meaning that small changes or even errors in measurements can lead to vastly different outcomes. These systems tend have strange couplings and feedback loops, making them very difficult to predict. These systems are nonlinear, meaning that the mathematical tools we bring to bear are often more sophisticated. And, computing is often required to simulate and understand the behavior of these systems.

We will focus on classical chaos, where the systems are [deterministic](https://en.wikipedia.org/wiki/Deterministic_system); they follow specific laws or equations. There is no inherent randomness included in the system. In some cases, folks include [noise](https://en.wikipedia.org/wiki/Noise_(electronics)) in their system, but this is not required for a system to be chaotic. Even though they are fully deterministic, due to their sensitivity to initial conditions, classical chaotic systems can appear random and unpredictable over time. 

## Characteristics of Chaotic Systems

Chaotic systems exhibit several key characteristics that distinguish them from other types of [dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system)

### Sensitive Dependence on Initial Conditions

One of the hallmark features of chaotic systems is their sensitive dependence on initial conditions. Even tiny differences in the starting state of the system can lead to dramatically different outcomes. While in many cases this means that we cannot predict the long-term behavior of the system, in some cases we can still make accurate short-term predictions. This concept has been abstracted into the popular saying "a butterfly flapping its wings in Brazil can cause a tornado in Texas," illustrating how small changes can have far-reaching effects. But it is true that in weather systems, small changes in atmospheric conditions can result in significantly different weather patterns.

### Nonlinearity

Chaotic systems are typically [nonlinear](https://en.wikipedia.org/wiki/Nonlinear_system); simple linear equations and the properties of their solutions are not sufficient to describe their behavior. The couplings of different aspects of the system can lead to feedback loops and interactions that are not simply additive. The mathematical equations governing chaotic systems often involve nonlinear functions, and are thus require different tools to analyze. Moreover, these nonlinear behaviors can change dramatically with small changes in the system parameters. These can lead to [bifurcations](https://en.wikipedia.org/wiki/Bifurcation) in the system, where a small change in a parameter can cause a sudden and qualitative change in the system's behavior. This is just another reason why chaotic systems are so difficult to predict and control

### Strange Attractors

We have seen how systems can have fixed points - both stable and unstable - and we have seen periodic behavior. These are common in many dynamical systems. In our study of the harmonic oscillator, we observed that the system can exhibit periodic behavior when undamped or driven, but we also saw how it can settle to a stable fixed point when damped. As we move to study chaotic systems, we begin to see other kinds of behavior. Systems can have [limit cycles](https://en.wikipedia.org/wiki/Limit_cycle) - periodic orbits that are stable or unstable. Below we show the limit cycle of the [Van der Pol oscillator](https://en.wikipedia.org/wiki/Van_der_Pol_oscillator), 

![Limit Cycle](images/notes/week1/640px-VanDerPolPhaseSpace.png)


One of the most interesting types of [attractors](https://en.wikipedia.org/wiki/Attractor) in dynamical systems is the [strange attractor](https://en.wikipedia.org/wiki/Strange_attractor). These are fractal structures in phase space towards which the system evolves over time. Strange attractors are complex and often exhibit self-similarity, meaning they look similar at different scales. The [Lorenz attractor](https://en.wikipedia.org/wiki/Lorenz_system) is a famous example of a strange attractor, displaying a butterfly-shaped pattern.

![Lorenz Attractor](images/notes/week1/A_Trajectory_Through_Phase_Space_in_a_Lorenz_Attractor.gif)

### Long-term Unpredictability

While chaotic systems can be predictable in the short term, their long-term behavior is inherently unpredictable due to the exponential growth of errors in initial conditions. You can think about this in terms of taking a bundle of trajectories that all start with slightly different initial conditions. As time goes on, these trajectories will diverge from one another; they will do so exponentially in every direction. The direction in which they diverge most rapidly is called the [Lyapunov exponent](https://en.wikipedia.org/wiki/Lyapunov_exponent). Technically, there's an exponent for each direction in phase space, but we often just refer to the largest one. If the largest Lyapunov exponent is positive, then the system is chaotic. 



# Week 11 - Notes: The Euler-Lagrange Equation

As we will use it, the [Calculus of Variations](https://en.wikipedia.org/wiki/Calculus_of_variations) foucses on finding the conditions of extrema for quantities that can be expressed as an integral. This might be a very abstract concept, so we will start with a simple example.

This approach might seem a bit alien at first, but it turns out to be an interesting way to develop an equivalent formulation of mechanics. Moreover, the Calculus of Variations is a powerful tool in many fields, and forms the basis for [Lagrangian mechanics](https://en.wikipedia.org/wiki/Lagrangian_mechanics).

To do this, we will derive (in 1D) the [Euler-Lagrange equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation). This equation gives us a way to find the function that makes the integral of a given functional stationary (i.e., a local maximum or minimum).


## Canonical Conceptualization - Finding the Shortest Path in a Plane

Using the Calculus of Variations, we can show that the shortest path between two points in a plane is a straight line. This is a classic example, but it illustrates the concept well. Consider a general path in two-dimensional space that connects two points, say $s_1 = \langle x_1, y_1 \rangle$ and $s_2 = \langle x_2, y_2 \rangle$. We can represent this path as a function $y(x)$. The figure below illustrates the setup.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

x1, x2 = 1, 5 
xvals = np.linspace(x1, x2, 100)

ygeneric = np.sin((xvals - x1) / (x2 - x1) * np.pi/3) * (3) / 10 + (0 + 3) / 2 + 2*xvals**2
y1, y2 = ygeneric[0], ygeneric[-1]  

fig, ax = plt.subplots()

ax.plot(xvals, ygeneric, label=r'Generic Path, $y(x)$', color='C0')
ax.plot([x1, x2], [y1, y2], label='Shortest Path', color='C1', linestyle='--')
ax.plot(x1, y1, 'C2o')  # Point 1
ax.plot(x2, y2, 'C2o')  # Point 2

# blank ticks
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Shortest Path Between Two Points in a Plane')
# Add a legend to the plot
ax.legend()
# Show the plot
plt.grid(True)  # Add grid for better readability
plt.show()  # Display the plot
```


    
![png](11_notes_files/11_notes_2_0.png)
    


The blue solid line is the 'generic path' that connects the two points $s_1$ and $s_2$. The green dotted line is the solution that we expect to get when we ask, "what is the shortest path between these two points?" 

### Setup of the Problem

Let's take a generic segment of the path $ds$ and express it in terms of its differential elements:

$$ds = \sqrt{dx^2 + dy^2}.$$

The length of the path from $s_1$ to $s_2$ can be expressed as an integral:

$$l = \int_{s_1}^{s_2} ds$$

We want to minimize this length, $l$, which is the total length of the path. To do this, we are attempting to minimize the integral of $ds$ over the path. This is where the Calculus of Variations comes in.

Let's write the expression for $ds$ in a more convenient form. We can factor out the $dx$ term:

$$ds = \sqrt{dx^2 + dy^2} = dx \sqrt{1 + \left(\frac{dy}{dx}\right)^2} = dx = \sqrt{1 + y'(x)^2}$$

where $y'(x) = \frac{dy}{dx}$ is the derivative of $y$ with respect to $x$. So the integral for the length of the path becomes:

$$l = \int_{x_1}^{x_2} dx \sqrt{1 + y'(x)^2}.$$

The function $y(x)$ defines the path that minimizes the length $l$. To find this path, we assume an incorrect function $Y(x)$ that is close to the true path $y(x)$, and we can express the difference between them as $\alpha\eta(x)$:

$$Y(x) = \underbrace{y(x)}_{\textrm{correct}}+ \underbrace{\alpha\eta(x)}_{\textrm{minimize}}$$

Note that $Y(x_1) = y(x_1)$ and $Y(x_2) = y(x_2)$, so the endpoints of the path are fixed. The function $\eta(x)$ represents a small perturbation to the path, and $\alpha$ is a small parameter that we will use to control the size of the perturbation.



### Deriving the Euler-Lagrange Equation

The mathematical derivation involves extremizing the integral using a perturbation approach. The generic integral we are trying to minimize is for a function of the form:

$$f(y(x),y'(x),x)),$$

where $f$ is a function of $y$, its derivative $y'$, and the independent variable $x$. So that the integral we are minimizing can be expressed as:

$$S=\int_{x_1}^{x_2} f(y(x),y'(x),x) dx.$$

We assume $y(x)$ minimizes the integral $S$. So that any function $Y(x) = y(x) + \alpha\eta(x)$ produces a larger value for $S$,

$$\int_{s_1}^{s_2} f(Y(x),Y'(x),x) dx > \int_{s_1}^{s_2} f(y(x),y'(x),x) dx.$$

Because we are looking for a minimum, we notice that when $\alpha = 0$, we have $Y(x) = y(x)$, and the integral is at its minimum. To find the extremum, we can take the derivative of the integral with respect to $\alpha$ and set it to zero:

$$\dfrac{dS}{d\alpha}|_{\alpha=0} = 0.$$

We start that analysis by differentiating the integral with respect to $\alpha$:

$$\begin{align}
S &= \int_{x_1}^{x_2} f(Y(x),Y'(x),x) dx \\
&= \int_{x_1}^{x_2} f(y(x) + \alpha\eta(x), y'(x) + \alpha\eta'(x), x) dx.\\
\end{align}$$

We can now differentiate.

$$\begin{align}
\dfrac{dS}{d\alpha} &= \int_{x_1}^{x_2}\left[ \dfrac{\partial f}{\partial Y}\dfrac{dY}{d\alpha} + \dfrac{\partial f}{\partial Y'}\dfrac{dY'}{d\alpha}+ \dfrac{\partial f}{\partial x}\dfrac{dx}{d\alpha} \right] dx.\\
\end{align}$$

Let's take each term in turn. The first term is:

$$\dfrac{df}{dY}\dfrac{dY}{d\alpha}.$$

Let's focus on the second part of that term:

$$\dfrac{dY}{d\alpha} = \dfrac{d}{d\alpha}\left[y(x) + \alpha\eta(x)\right] = \eta(x).$$

Let's look at the second term:

$$\dfrac{dY'}{d\alpha}.$$

Again, let's focus on the second part of that term:

$$\dfrac{dY'}{d\alpha} = \dfrac{d}{d\alpha}\left[y'(x) + \alpha\eta'(x)\right] = \eta'(x).$$

Lastly, the third term:

$$\dfrac{\partial f}{\partial x}\dfrac{dx}{d\alpha}=0.$$

This term is a bit different. The $dx$ term is independent of $\alpha$, so we can treat it as a constant with respect to $\alpha$. Therefore, this term will not contribute to the derivative with respect to $\alpha$, and we can ignore it in our analysis.

Putting it all together, we have:

$$\begin{align}
\dfrac{dS}{d\alpha} &= \int_{x_1}^{x_2}\left[ \dfrac{\partial f}{\partial Y}\eta(x) + \dfrac{\partial f}{\partial Y'}\eta'(x) \right] dx.\\
\end{align}$$

Our expression is still in terms of $Y(x)$, the incorrect function. We want to express it in terms of $y(x)$, the correct function. Let's look at the derivatives $\dfrac{\partial f}{\partial Y}$ and $\dfrac{\partial f}{\partial Y'}$. We can use the chain rule to express these derivatives in terms of $y(x)$:

$$\begin{align}
\dfrac{\partial f}{\partial Y} &= \dfrac{\partial f}{\partial y}\dfrac{\partial y}{\partial Y} = \dfrac{\partial f}{\partial y},\\
\dfrac{\partial f}{\partial Y'} &= \dfrac{\partial f}{\partial y'}\dfrac{\partial y'}{\partial Y'} = \dfrac{\partial f}{\partial y'}.\\
\end{align}$$

**Why?** Because $\dfrac{\partial y}{\partial Y} = 1$ and $\dfrac{\partial y'}{\partial Y'} = 1$ when we are differentiating with respect to the correct function $y(x)$. This means that we can express the derivatives in terms of the correct function $y(x)$.

$$\begin{align}
\dfrac{dS}{d\alpha} &= \int_{x_1}^{x_2}\left[ \dfrac{\partial f}{\partial y}\eta(x) + \dfrac{\partial f}{\partial y'}\eta'(x) \right] dx.\\
\end{align}$$

We are seeking $\dfrac{dS}{d\alpha}$ at $\alpha = 0$, so we set the integral to zero:

$$\begin{align}
\int_{x_1}^{x_2}\left[ \dfrac{\partial f}{\partial y}\eta(x) + \dfrac{\partial f}{\partial y'}\eta'(x) \right] dx = 0.\\
\end{align}$$

#### Integration by Parts

Now to deal with the integral here, we can use integration by parts:

$$\int u'v dx = [uv] - \int u v' dx$$

The first term $[uv]$ is called the "surface term" because it is the result of the integral and is evaluated at the boundaries of the integral, $x_1$ and $x_2$. We will apply integration by parts only to the second term in the integral.

Here, we note $u = \eta(x)$ and $v = \dfrac{\partial f}{\partial y'}$. Then, we can express the second term in the integral as follows:

$$\begin{align}
\int_{x_1}^{x_2} \eta'(x) \dfrac{\partial f}{\partial y'} dx &= \underbrace{\left[ \eta(x) \dfrac{\partial f}{\partial y'} \right]_{x_1}^{x_2}}_{\eta(x_1)=\eta(x_2)=0} - \int_{x_1}^{x_2} \eta(x) \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right) dx\\
&= - \int_{x_1}^{x_2} \eta(x) \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right) dx
\end{align}$$

Notice that the surface term evaluates to zero because we have fixed the endpoints of the path, so $\eta(x_1) = \eta(x_2) = 0$.  We put this all together to get:

$$\begin{align}
\dfrac{dS}{d\alpha} &= \int_{x_1}^{x_2}\left[ \eta(x)\dfrac{\partial f}{\partial y} - \eta(x) \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right) \right] dx = 0.\\
& = \int_{x_1}^{x_2} \eta(x) \left[ \dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right) \right] dx = 0.\\
\end{align}$$

```{important}
The last statement is true for any arbitrary function $\eta(x)$, so we can conclude that the term in square brackets must be zero:

$$\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right) = 0.$$

This is the **[Euler-Lagrange equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation)** for a 1D problem.
```

### Back to the Shortest Path Example

Now let's apply the Euler-Lagrange equation to our original problem of finding the shortest path between two points in a plane. We have:

$$l = \int_{x_1}^{x_2} \sqrt{1 + y'(x)^2} dx.$$

Here, we can identify our function $f$ as:

$$f(y(x), y'(x), x) = \sqrt{1 + y'(x)^2}.$$

Let's apply the Euler-Lagrange equation to this function. 

$$\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right) = 0.$$

We take the derivatives:

$$\dfrac{\partial f}{\partial y} = 0$$

since $f$ does not depend on $y$, only on $y'$. Now let's compute the second term:

$$\begin{align}
\dfrac{\partial f}{\partial y'} &= \dfrac{\partial}{\partial y'}\left( \sqrt{1 + y'(x)^2} \right)\\
&= \dfrac{1}{2} \left(1 + y'(x)^2\right)^{-1/2} 2y'(x)\\
&= \frac{y'(x)}{\sqrt{1 + y'(x)^2}}.\\
\end{align}$$

Let's put all this together:

$$\begin{align}
0 &= \dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left( \dfrac{\partial f}{\partial y'} \right)\\
0 &= 0 - \dfrac{d}{dx}\left(\frac{y'(x)}{\sqrt{1 + y'(x)^2}}\right).\\
\end{align}$$

This means that,

$$\dfrac{d}{dx}\left(\frac{y'(x)}{\sqrt{1 + y'(x)^2}}\right) = 0$$

This implies that:

$$\frac{y'(x)}{\sqrt{1 + y'(x)^2}} = C = \textrm{a constant}.$$

Or rearranging gives us:

$$\begin{align}
y'(x) &= C\sqrt{1 + y'(x)^2}\\
y'(x)^2 &= C^2(1 + y'(x)^2)\\
(1 - C^2)y'(x)^2 &= C^2\\
y'(x)^2 &= \frac{C^2}{1 - C^2}\\
y'(x) &= \pm \sqrt{\frac{C^2}{1 - C^2}}\\
\end{align}$$

So that, $y'(x)$ is a constant, call it $m$, which produces a linear solution.

$$\dfrac{dy}{dx} = \sqrt{\frac{C^2}{1 - C^2}} = m$$

Integrating gives us:

$$y(x) = mx + b$$

where $b$ is a constant of integration. This is the equation of a straight line!

## Example: Snell's Law

Let's assume you are walking on the beach and need to get to a location in the water quickly. Where do you enter the water to minimize the time it takes to reach the location in the water? This is a classic problem in physics and can be solved using the Calculus of Variations.

Consider the picture below where you can move at a speed $v_1$ on the shore and a speed $v_2$ in the water. We know that $v_1 > v_2$, so you can move faster on the shore than in the water. We aim to minimize the time it takes to reach the point $\langle x_2, y_2 \rangle$ in the water from point $\langle x_1, y_1 \rangle$ on the shore. We take the shoreline to be a line at $x = 0$. and the location we cross the shoreline is $\langle 0, y \rangle$.

![Snell's Law Diagram](../../images/notes/week11/snells_shore.png)

Notice the angle that we approach the shoreline at, $\theta_1$, and the angle that we approach the target in the water, $\theta_2$.

The total time to travel from $\langle x_1, y_1 \rangle$ to $\langle 0, y \rangle$ and then to $\langle x_2, y_2 \rangle$ is:

$$T = t_1 + t_2 = \dfrac{d_1}{v_1} + \dfrac{d_2}{v_2}$$

where $d_1$ is the distance from $\langle x_1, y_1 \rangle$ to $\langle 0, y \rangle$, and $d_2$ is the distance from $\langle 0, y \rangle$ to $\langle x_2, y_2 \rangle$. We can write those distances in terms of the coordinates:

$$d_1 = \sqrt{x_1^2 + (y - y_1)^2}$$
$$d_2 = \sqrt{x_2^2 + (y_2 - y)^2}$$

This gives us:

$$T = \dfrac{\sqrt{x_1^2 + (y - y_1)^2}}{v_1} + \dfrac{\sqrt{x_2^2 + (y_2 - y)^2}}{v_2}.$$

We want to minimize this time, $T$, by choosing the optimal point $y$ where we cross the shoreline. We compute the derivative of $T$ with respect to $y$ and set it to zero:

$$\dfrac{dT}{dy} = 0$$

$$\begin{align}
\dfrac{dT}{dy} &= \dfrac{1}{2}\dfrac{1}{v_1}\left(x_1^2 + (y-y_1)^2\right)^{-1/2}(2)(y-y_1) + \dfrac{1}{2}\dfrac{1}{v_2}\left(x_2^2 + (y_2-y)^2\right)^{-1/2}(-2)(y_2-y) = 0\\
&= \dfrac{1}{v_1}\left(\dfrac{y-y_1}{\sqrt{x_1^2 + (y-y_1)^2}}\right) - \dfrac{1}{v_2}\left(\dfrac{y_2-y}{\sqrt{x_2^2 + (y_2-y)^2}}\right) = 0\\
&= \dfrac{1}{v_1}\left(\dfrac{y-y_1}{d_1}\right) - \dfrac{1}{v_2}\left(\dfrac{y_2-y}{d_2}\right) = 0\\
\end{align}$$

where the last step is just substituting in the expressions for $d_1$ and $d_2$. Notice that those expressions are related to the angles we defined earlier. We can rewrite the expression in terms of the angles $\theta_1$ and $\theta_2$:

$$\sin(\theta_1) = \frac{y - y_1}{d_1}$$
$$\sin(\theta_2) = \frac{y_2 - y}{d_2}$$

This gives us:

$$\dfrac{\sin(\theta_1)}{v_1} - \dfrac{\sin(\theta_2)}{v_2} = 0$$

```{important}
This is [**Snell's Law**](https://en.wikipedia.org/wiki/Snell%27s_law)! It tells us that the ratio of the sine of the angles to the velocities is constant. This is a classic result in optics, but it also applies to this problem of finding the shortest path in a plane.

$$\dfrac{\sin(\theta_1)}{v_1} = \dfrac{\sin(\theta_2)}{v_2}$$
```

## Example: Brachistochrone Problem

The [Brachistochrone problem](https://en.wikipedia.org/wiki/Brachistochrone_problem) is a classic problem in the Calculus of Variations. It asks the question: "What is the shape of the curve that a bead will follow under the influence of gravity to reach the bottom in the shortest time?"  Here's a great video from [Steven Strogatz](https://en.wikipedia.org/wiki/Steven_Strogatz) that explains the problem and its solution.

[![Youtube Video on the Brachistochrone Problem](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=Cld0p3a43fU)

Source: <https://www.youtube.com/watch?v=Cld0p3a43fU>

The setup is below, there's two points separated by a distance vertically and horizontally. What shape should we make a track so that a bead will roll down it in the shortest time?

![The Brachistochrone Problem](../../images/notes/week11/brachistochrone.png)

The time it takes for the bead to roll down the curve is given by:

$$T = \int_{1}^{2} \dfrac{ds}{v}$$

where $ds$ is the differential arc length along the curve, and $v$ is the velocity of the bead at that point. The generic step is the same as before:

$$ds = \sqrt{dx^2 + dy^2}.$$

#### Velocity of the Bead

What about $v$? Because the bead is moving under the influence of gravity, we can use conservation of energy to find the velocity. Note that we don't model the rolling of the bead, just the motion down the track. We also neglect all frictional forces. This is a major simplification, but it will give us an analytical solution.

$$\Delta K + \Delta U = 0$$

If the bead starts from rest, then $v_i = 0$, and we can write:

$$\dfrac{1}{2}mv^2 - \dfrac{1}{2}m(0)^2 + mg(\Delta y) = 0,$$

$$v = \sqrt{2g\Delta y}$$

where $\Delta y = y_1 - y_2 > 0$. This is the change in height of the bead as it rolls down the track. We can express this in terms of the coordinates of the two points, $y_1$ and $y_2$.

Let's move the origin to the top of the track and measure $+y$ downwards. Thus, for any point on the track, we have:

$$v = \sqrt{2gy}.$$

We can now write the integral again,

$$T = \int_{1}^{2} \dfrac{ds}{v} = \int_{1}^{2} \dfrac{\sqrt{dx^2 + dy^2}}{\sqrt{2gy}}.$$

We notice that we can factor out a $dy$ term from the square root in the numerator:

$$\sqrt{dx^2 + dy^2} = dy\sqrt{\left(\frac{dx}{dy}\right)^2 + 1} = dy \sqrt{x'^2 + 1}$$

where $x' = \frac{dx}{dy}$. This gives us:

$$T = \dfrac{1}{\sqrt{2g}}\int_{0}^{y_2} dy \dfrac{\sqrt{x'^2 + 1}}{\sqrt{y}}.$$

We can identify our function $f$ as:

$$f(x,x',y) = f(x',y) = \dfrac{\sqrt{x'^2 + 1}}{\sqrt{y}}.$$

Because $f$ does not depend on $x$, $\partial f/\partial x = 0$. So that the Euler-Lagrange equation simplifies to:

$$\dfrac{d}{dy}\left(\dfrac{\partial f}{\partial x'}\right) = 0.$$

Or that this partial derivative must be a constant:

$$\dfrac{\partial f}{\partial x'} = \textrm{a constant},$$

$$dfrac{\partial f}{\partial x'} = \dfrac{x'}{\sqrt{x'^2 + 1}\sqrt{y}} = \sqrt{C},$$

where $C$ is a constant. We square both sides to get:

$$\dfrac{x'^2}{(x'^2 + 1)y} = C.$$

Knowing the solution ahead of time, we choose the constant $C = \frac{1}{2a}$. This gives us:

$$\dfrac{x'^2}{(x'^2 + 1)y} = \frac{1}{2a}.$$

Some more algebra gives us:

$$2ax'^2 = y(x'^2 + 1),$$
$$(2a - y)x'^2 = y,$$
$$x'^2 = \frac{y}{2a - y},$$

where $x' = \frac{dx}{dy}$. We can now integrate this to find the shape of the curve:

$$x = \int \sqrt{\frac{y}{2a - y}} dy.$$

This integral will give us the shape of the curve $x(y)$, but to solve it we need to use a substitution. 

Let $y = a(1 - \cos(\theta))$. Thus, $dy = a\sin(\theta)d\theta$. This gives us:

$$\begin{align}
x(y(\theta)) &= \int \sqrt{\frac{y(\theta)}{2a - y(\theta)}} dy\\
&= \int \sqrt{\frac{a(1 - \cos(\theta))}{2a - a(1 - \cos(\theta))}} a\sin(\theta)d\theta\\
&= a \int \sqrt{\frac{(1-\cos\theta)}{(1+\cos\theta)}} \sin(\theta)d\theta.\\
\end{align}$$

Note that $\sin \theta = \sqrt{1 - \cos^2 \theta} = \sqrt{(1 - \cos\theta)(1 + \cos\theta)}$. This allows us to simplify the integral:

$$\begin{align}
x(y(\theta)) &= a \int \sqrt{\frac{(1-\cos\theta)^2(1+\cos\theta)}{(1+\cos\theta)}} d\theta\\
&= a \int \sqrt{(1 - \cos\theta)^2} d\theta\\
&= a \int (1 - \cos\theta) d\theta\\
&= a \left(\theta - \sin(\theta)\right) + C\\
\end{align}$$

where $C$ is a constant of integration. 

With initial conditions $x(0) = 0$ when $y(0) = 0$ at $t=0$ and $\theta = 0$, we find that $C = 0$. So the solution is:

$$x(\theta) = a\left(\theta - \sin(\theta)\right)$$
$$y(\theta) = a(1 - \cos(\theta)).$$

This is the "cycloid" curve that the bead will follow to minimize the time it takes to roll down the track. We can plot this curve to visualize it.

What is so interesting about this curve is that it is [isochronous](https://en.wikipedia.org/wiki/Isochronous), meaning that all beads released from rest at any point on the curve will reach the bottom at the same time, regardless of where they start.




```python
## Plot a cycloid path for comparison
## $$x(\theta) = a\left(\theta - \sin(\theta)\right)$$
## $$y(\theta) = a(1 - \cos(\theta)).$$

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

# Cycloid parameters
a = 1  # Radius of the rolling circle
theta = np.linspace(0, 3/2 * np.pi, 1000)  # Parameter for the cycloid

# Cycloid equations
x_cycloid = a * (theta - np.sin(theta))
y_cycloid = -a * (1 - np.cos(theta))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 4))  # Create a new figure and axis
ax.plot(x_cycloid, y_cycloid, color='C0')
ax.plot(0, 0, 'C1o', label='Start')  # Starting point of the cycloid
ax.plot(x_cycloid[-1], y_cycloid[-1], 'C2o', label='End')  # Ending point of the cycloid

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Cycloid Path')

ax.legend()  # Add a legend to the plot

# Show the plot
plt.grid(True)  # Add grid for better readability
plt.show()  # Display the plot
```


    
![png](11_notes_files/11_notes_10_0.png)
    



# Week 11 - Calculus of Variations

We are eventually going to develop some deep principles of classical mechanics that will connect for us the motion of particles and the forces they experience to the energy that moves between aspects of the system. This formulation of mechanics is called [Lagrangian Mechanics](https://en.wikipedia.org/wiki/Lagrangian_mechanics). It is a powerful and elegant way to describe the motion of particles and systems. It is based on the [Calculus of Variations](https://en.wikipedia.org/wiki/Calculus_of_variations), a field of mathematics that is concerned with finding the path that minimizes or maximizes (called "extremization") a certain quantity.

The conceptual idea of Lagrangian mechanics is to describe the motion of a system by defining a function called the **Lagrangian**. Under this framework, the stationary points (or paths) of the [action integral](https://en.wikipedia.org/wiki/Action_(physics)), which is the integral of the Lagrangian over time, correspond to the actual motion of the system. This means that if you can find the path that minimizes or maximizes this action, you can determine the equations of motion for the system. We will come back to this next week when we derive the Lagrangian equations of motion. But understand that we are seeking to extremize a particular integral to find the path that a system will take through configuration space. 

Our examples will start with simple systems, like the motion on a plane - where we will prove a line is the shortest path between two points (also known as a geodesic). We will also recover a form of [Snell's Law](https://en.wikipedia.org/wiki/Snell%27s_law) of refraction, which describes how light bends when it passes through different media. We will use running from the shoreline to a point in the water as an example of how to apply these principles. Lastly, we will look at the [Brachistochrone problem](https://en.wikipedia.org/wiki/Brachistochrone_problem), which is the problem of finding the curve down which a bead will slide (without friction) from one point to another in the shortest time. This is a classic problem in the calculus of variations and leads us to the cycloid curve.

This section is mathematically intensive and will require you to have a solid understanding of calculus, including differentiation and integration. This mathematics is also very powerful and underlies how we can develop equations of motion in particular systems. But is also describes the shape of surfaces like bubbles and droplets. The video below is a nice introduction to the concept of Calculus of Variations and it's relation to [minimal surfaces](https://en.wikipedia.org/wiki/Minimal_surface).

## The Brachistochrone Problem (16 minute video)

The Brachistochrone is a well known problem and its history is quite interesting. The video below discusses the problem and it history in detail. It's what helped spur the development of the calculus of variations and the work of Lagrange and others. The problem is deceptively simple: given two points in a vertical plane, find the curve down which a bead will slide (without friction) from one point to the other in the shortest time. The solution to this problem is not a straight line, but rather a cycloid curve.

[![Youtube Video on the Brachistochrone Problem](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=Cld0p3a43fU)

Source: <https://www.youtube.com/watch?v=Cld0p3a43fU>

## The Math of Bubbles (17 minute video)

In the video below, we learn about the [Soap Bubble Problem](https://en.wikipedia.org/wiki/Soap_bubble), which is another classic problem in the calculus of variations. The goal is to find the shape of a soap bubble that minimizes surface area for a given volume.

[![The Math of Bubbles: Minimal Surfaces & the Calculus of Variations](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=8SABptOYUVk))

Source: <https://youtube.com/watch?v=8SABptOYUVk>


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






# Week 12 - The Principle of Least Action

[Newtonian Mechanics](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion) is an incredibly useful model of the natural world. In fact, it wasn't until the mid 1970s that we were able to truly [test Einstein's gravity as a true replacement](https://en.wikipedia.org/wiki/Tests_of_general_relativity) for Newton. That being said, for most terrestrial situations (macroscopic objects moving at low speeds), Newton's mechanics is very good. However, the problem with Newton is that it requires a few things:

1. We must be able identify each interaction on the object or model an average behavior from many smaller interactions (e.g., models of friction vs. detailed E&M forces)
2. We must be able to mathematically describe the size and direction of the interaction at all times we want to model
3. We must be able to vectorially add the interactions to produce the net force $\sum_i \vec{F}_i = \vec{F}_{net}$.

In many cases, we can do this. But consider a bead sliding inside a cone. How would you write down the contact force between the cone and the bead for all space and time?

This is where [Lagrangian Mechanics](https://en.wikipedia.org/wiki/Lagrangian_mechanics) comes in. It is a powerful and elegant way to describe the motion of particles and systems. It is based on the [Calculus of Variations](https://en.wikipedia.org/wiki/Calculus_of_variations), a field of mathematics that is concerned with finding the path that minimizes or maximizes (called "extremization") a certain quantity. In the case of Lagrangian Mechanics, the quantity we are extremizing is the [action](https://en.wikipedia.org/wiki/Action_(physics)).

The video below discusses the concept of the Principle of Least Action, which is the foundation of Lagrangian Mechanics.

[![The Principle of Least Action](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=Q_CQDSlmboA)

Source: <https://youtube.com/watch?v=Q_CQDSlmboA>

## Introduction to Lagrangian Dynamics (10 minute video)

The concept of Lagrangian dynamics can be a bit abstract at first, especially if you are used to Newtonian mechanics. The basic idea is that instead of focusing on forces, we focus on the kinetic and potential energy of the system to derive the equations of motion. The procedure to compute the equations of motion is straghtforward, but the set up of these problems can be tricky at first. 

The basic steps are:
1. **Identify the generalized coordinates**: These are the variables that describe the configuration of the system (e.g., angles, distances).
2. **Write down the Lagrangian**: The Lagrangian $\mathcal{L}$ is defined as the difference between the kinetic energy $T$ and potential energy $V$ of the system: 
   $$ \mathcal{L} = T - V $$
3. **Apply the Euler-Lagrange equations**: The equations of motion are derived from the Lagrangian using the Euler-Lagrange equations:
    $$ \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{q}_i} \right) - \frac{\partial \mathcal{L}}{\partial q_i} = 0 $$
    where $q_i$ are the generalized coordinates and $\dot{q}_i$ are their time derivatives (velocities).

But we need practice applying these steps to get comfortable with the process. Parth G. has a lovely video below about the basics of Lagrangian Dynamics. We will do a lot of this in class and go over many examples. This video is a nice introduction to the concept.

[![Introduction to Lagrangian Dynamics](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=KpLno70oYHE)

Source: <https://youtube.com/watch?v=KpLno70oYHE>


# Week 13 - Lagrangian Mechanics

The Lagrangian formulation of mechanics allows us to describe the motion of a system in terms of its kinetic and potential energy, rather than its forces. This approach is particularly useful for systems with constraints or when dealing with generalized coordinates. There's a few general concepts that arise in Lagrangian mechanics that make it a powerful tool for analyzing mechanical systems.

First, the Lagrangian formulation emphasizes the idea of independent coordinates while also providing the flexibility to use any set of coordinates that are convenient for the problem at hand. This is in contrast to Newtonian mechanics, which often relies clearly structured position and velocity vectors. 

Because the Lagrangian uses this generalized coordinate system, it is often easier to analyze complex systems with many degrees of freedom. Moreover, when dealing with constraints, the Lagrangian formulation allows us to incorporate these constraints directly into the equations of motion, which reduces the dimensionality of the problem.

In addition, the Lagrangian formulation is particularly useful for systems with symmetries. By applying [Noether's theorem](https://en.wikipedia.org/wiki/Noether%27s_theorem), we can relate symmetries of the system to conserved quantities, which can simplify the analysis of the system's motion. For example, if a particular system is invariant under time translations (for us no explicit time dependence in $\mathcal{L}$), we can conclude that energy is conserved. If a coordinate is cyclic (e.g., no $x$ dependence in $\mathcal{L}$), we can conclude that the corresponding momentum (in this example, $p_x$) is conserved.

Lastly, the formalism produces [generalized forces](https://en.wikipedia.org/wiki/Generalized_force) that are not necessarily equal to the physical forces acting on the system, but have corresponding generalized momenta. These are always produced in our equations of motion, but they might not be forces or momenta that we can measure directly, or that we can even define as a "force", some are torques, for example. 

Consider an $N$ dimensional system with $N$ generalized coordinates $q_i$ and $N$ generalized velocities $\dot{q}_i$. The Lagrangian is defined as the difference between the kinetic energy $T$ and the potential energy $V$ of the system:

$$
\mathcal{L} = T(\dot{q}_1, \dot{q}_2, \dots, \dot{q}_N) - V(q_1, q_2, \dots, q_N)
$$

The derivative of the Lagrangian with respect to a generalized coordinate $q_i$ is given by:

$$\dfrac{\partial \mathcal{L}}{\partial q_i} = \dfrac{\partial V}{\partial q_i} = F_{q_i}$$

where $F_{q_i}$ is the generalized force conjugate to the coordinate $q_i$.

The derivative of the Lagrangian with respect to a generalized velocity $\dot{q}_i$ is given by:

$$\dfrac{\partial \mathcal{L}}{\partial \dot{q}_i} = \dfrac{\partial T}{\partial \dot{q}_i} = p_{q_i}$$

where $p_{q_i}$ is the generalized momentum conjugate to the coordinate $q_i$.

## The Standard Model Lagrangian (17 minute video)

An understanding of physics formulated through [Lagrangian Mechanics](https://en.wikipedia.org/wiki/Lagrangian_mechanics) is a powerful and elegant way to describe the motion of particles and systems. But it can be much more than that. Much of the work of particle physics is done in the context of the [Standard Model](https://en.wikipedia.org/wiki/Standard_Model). The Standard Model is a theory that describes the electromagnetic, weak, and strong nuclear interactions. The Standard Model is a [quantum field theory](https://en.wikipedia.org/wiki/Quantum_field_theory), which is formulated through a Lagrangian.

The video below provides an introduction to this equation and the Standard Model.

[![Standard Model Lagrangian](images/notes/week1//hqdefault.jpg)](https://youtube.com/watch?v=PHiyQID7SBs)



# Chapters Index

- [01_notes.md](01_notes.md)
- [01_start.md](01_start.md)
- [02_notes.md](02_notes.md)
- [02_start.md](02_start.md)
- [index.md](index.md)
- [01_notes.pdf](01_notes.pdf)
- [01_start.pdf](01_start.pdf)
- [02_notes.pdf](02_notes.pdf)
- [02_start.pdf](02_start.pdf)
- [01_notes.docx](01_notes.docx)
- [01_start.docx](01_start.docx)
- [02_notes.docx](02_notes.docx)
- [02_start.docx](02_start.docx)

## Images by Week

### week1
- images/notes/week1/640px-Modernphysicsfields.svg.png
- images/notes/week1/box_fbd_remote.png
- images/notes/week1/box_fbd.png
- images/notes/week1/falling_object_remote.gif
- images/notes/week1/falling_object.png
- images/notes/week1/File:Dot-product-1.svg
- images/notes/week1/File:Modernphysicsfields.svg
- images/notes/week1/hqdefault.jpg
- images/notes/week1/youtube_myuD81326_o.jpg
- images/notes/week1/youtube_Qme07fA3Fj4.jpg

### week10
- images/notes/week10/chen.png
- images/notes/week10/damped-long-term.png
- images/notes/week10/dei_talk.png
- images/notes/week10/duffing-chaos.png
- images/notes/week10/duffing.png
- images/notes/week10/first_duffing.png
- images/notes/week10/hellmo.gif
- images/notes/week10/lorenz-1.png
- images/notes/week10/lorenz-2.png
- images/notes/week10/lorenz-trajectories.png
- images/notes/week10/lorenz.png
- images/notes/week10/lyapunov.png
- images/notes/week10/sprott.png
- images/notes/week10/van-der-pol-limit-cycle.gif

### week11
- images/notes/week11/brachistochrone.png
- images/notes/week11/snells_shore.png
- images/notes/week11/soap_bubble.png

### week12
- images/notes/week12/coordinate-system.png
- images/notes/week12/newton-scared.jpg
- images/notes/week12/plane-pendulum.png
- images/notes/week12/skateboard-free-body.png
- images/notes/week12/skateboard.png
- images/notes/week12/standup.png

### week13
- images/notes/week13/action.001.png
- images/notes/week13/andy-lagrange.jpeg
- images/notes/week13/atwood.png
- images/notes/week13/era.png
- images/notes/week13/lion-lagrange.jpg
- images/notes/week13/march.png
- images/notes/week13/paraboloid.png
- images/notes/week13/string-unraveled.png

### week2
- images/notes/week2/2dvector.png
- images/notes/week2/benjamin.png
- images/notes/week2/browne.png
- images/notes/week2/crawford.png
- images/notes/week2/Dot-product.png
- images/notes/week2/dyson.png
- images/notes/week2/gleick.png
- images/notes/week2/harvard-computers.png
- images/notes/week2/levy.png
- images/notes/week2/nasa-computers-hidden-figures.png
- images/notes/week2/oneill.png
- images/notes/week2/zuboff.png

### week3
- images/notes/week3/1d-ball-fbd-air.png
- images/notes/week3/1d-ball-fbd.png
- images/notes/week3/ai_vote_s2025.png
- images/notes/week3/cq6-3.png
- images/notes/week3/drag.png
- images/notes/week3/prelim_framework.png
- images/notes/week3/quack.png
- images/notes/week3/sho_horizontal.png
- images/notes/week3/stokes.png
- images/notes/week3/trans_rally.png
- images/notes/week3/von_karman.png
- images/notes/week3/vortex-shedding.png

### week4
- images/notes/week4/2d-falling-ball-fbd.png
- images/notes/week4/2d-falling-ball.png
- images/notes/week4/grav_01.png
- images/notes/week4/grav_02.png
- images/notes/week4/grav_03.png
- images/notes/week4/numerical_integration.png
- images/notes/week4/paramecium-swimming.png

### week5
- images/notes/week5/closed-path-work.png
- images/notes/week5/conservation-of-energy.png
- images/notes/week5/conservative-forces.png
- images/notes/week5/cq_left_field.png
- images/notes/week5/cq_right_field.png
- images/notes/week5/discrete-force-intervals.png
- images/notes/week5/gravedigger.png
- images/notes/week5/lattice-chain.png
- images/notes/week5/path-integral-work.png

### week6
- images/notes/week6/cq15-5.png
- images/notes/week6/mexican-hat-potential.png
- images/notes/week6/pendulum-potential-energy.png
- images/notes/week6/quark-potential.png
- images/notes/week6/quarks.png
- images/notes/week6/resisting.png
- images/notes/week6/sho-potential-energy.png

### week7
- images/notes/week7/1st-order-ode-ex-1.png
- images/notes/week7/1st-order-ode-ex-2.png
- images/notes/week7/roessler.png

### week8
- images/notes/week8/conjugates_graph.png
- images/notes/week8/cq19-1a.png
- images/notes/week8/cq19-1b.png
- images/notes/week8/cq19-1c.png
- images/notes/week8/cq19-5.png
- images/notes/week8/cq19-6.png

### week9
- images/notes/week9/animated-driven-pendulum.gif
- images/notes/week9/car_shock.png
- images/notes/week9/complex_plane.png
- images/notes/week9/driven_oscillator.png
- images/notes/week9/large_angle_pendulum.png
- images/notes/week9/plane.png
- images/notes/week9/real_part.png
- images/notes/week9/resonance.png
- images/notes/week9/time_trace.png
- images/notes/week9/tuning-fork.png


## Figures

- ../docs/figures/640px-Modernphysicsfields.svg.png
- ../docs/figures/youtube_myuD81326_o.jpg
- ../docs/figures/youtube_Qme07fA3Fj4.jpg
