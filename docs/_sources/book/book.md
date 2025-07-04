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



