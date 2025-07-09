<!-- HTML file automatically generated from DocOnce source (https://github.com/doconce/doconce/)
doconce format html hw5.do.txt --no_mako -->
<!-- dom:TITLE: PHY321: Classical Mechanics 1 -->

# Homework 8 (Due 18 Apr)

**Due 18 Apr (midnight)**

Total points: 120


```python
import numpy as np
from math import *
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
plt.style.use('seaborn-v0_8-colorblind')
```

## Exercise 1 (10pt) Paths along a curved surface

We have shown by minimizing the path length on a 2D flat surface that we have generated a linear equation, which illustrates the shortest distance between two points is a straight line. On a curved surface, the shortest distance will be a curve of some kind. In the exercise you will be asked to show that the shortest distance between two points on a sphere and a cylinder, both of fixed radii.

A step in spherical coordinates is given by:

$$d\vec{s} = dr \hat{r} + r d\theta \hat{\theta} + r \sin\theta d\phi \hat{\phi}.$$

A step in cylindrical coordinates is given by:

$$d\vec{s} = d\rho \hat{\rho} + \rho d\phi \hat{\phi} + dz \hat{z}.$$

1. (5 pt) Demonstrate the integral for the shortest distance between two points on a sphere of radius $R$ is given by:

$$L = R \int_{\theta_1}^{\theta_2} \sqrt{1 + \left(\sin^2\theta\right) \left(\frac{d\phi}{d\theta}\right)^2} d\theta$$

where $\theta$ is the polar angle and $\phi$ is the azimuthal angle. Note that you want to travel from ($\theta_1, \phi_1$) to ($\theta_2, \phi_2$) at fixed $R$.

2. (5 pt) Construct the integral for the shortest distance between two points on a cylinder of radius $R$ and height $h$. The coordinates are $(R, \phi_1, z_1)$ and $(R, \phi_2, z_2)$ in the cylindrical coordinate system, where $\rho$ is the radial difference, $\phi$ is the azimuthal angle, and $z$ is the height.

## Exercise 2 (15pt) Snell's Law

We can develop Snell's Law by minimizing the time it takes for light to travel between two points in different media. We note that the speed of light in a media is given by $v = c/n$, where $c$ is the speed of light in a vacuum and $n$ is the refractive index of the media. The time it takes for light to travel between two points is given by $t = L/v$, where $L$ is the distance between the two points.

Let a light ray travel in a medium with refractive index $n_1$ into another medium with refractive index $n_2$. 

1. (5 pt) Sketch the problem and indicate the relevant angles and distances in your figure. Recall that the angle of incidence is $\theta_1$ and the angle of refraction is $\theta_2$. It is ok to use a 2D sketch.


2. (5 pt) Set up the "integral" for the time it takes for light to travel between two points in different media. Use the fact that the speed of light in a media is given by $v = c/n$. Your answer needs to include the angles $\theta_1$ and $\theta_2$ and the refractive indices $n_1$ and $n_2$.



3. (5 pt) Minimize the time it takes for light to travel between two points in different media to derive Snell's Law.

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

## Exercise 3 (15pt) Lagrangian Examples

Constructing the Lagrangian for a system can be a bit tricky. In this exercise you will be asked to construct the Lagrangian for a few systems and quickly find equations of motion to illustrate the process.

1. (2 pt) Construct the Lagrangian in 3D for a projectile subject to no air resistance in a uniform gravitational field. The coordinates are $(x, y, z)$ in the Cartesian coordinate system. Find the 3 equations of motion.

2. (2 pt) Construct the Lagrangian for a one-dimensional simple harmonic oscillator ($F=-kx$). The coordinate is $x$ in the Cartesian coordinate system. Find the equation of motion.

3. (3 pt) A mass moves in a potential well $U(x,y) = \frac{1}{2}k(x^2 + y^2)$. Construct the Lagrangian in 2D. The coordinates are $(x, y)$ in the Cartesian coordinate system. Find the 2 equations of motion.

It's common to use coordinates that are convenient for the problem. In these cases, you will need to write down the kinetic and potential energy in terms of the coordinates you choose. The single particle kinetic energy in these coordinates are commonly used.

4. (4 pt) Write or derive the velocity vector in spherical coordinates. The coordinates are $(r, \theta, \phi)$ in the spherical coordinate system. Show the kinetic energy is given by $T = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2 + r^2\sin^2\theta\dot{\phi}^2)$.

5. (4 pt) Write or derive the velocity vector in cylindrical coordinates. The coordinates are $(\rho, \phi, z)$ in the cylindrical coordinate system. Show the kinetic energy is given by $T = \frac{1}{2}m(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + \dot{z}^2)$.

## Exercise 4 (25pt) Changing Coordinates

Consider two particles with masses $m_1=m_2=m$ connected by a spring with spring constant $k$. They sit on a frictionless surface but are constrained to the $x$-axis. The location of the first particle is $x_1$ and the location of the second particle is $x_2$. The spring is at equilibrium when the particles are a distance $L$ apart. Assume the spring is massless and that the left mass never changes position with the right mass (i.e., the spring is always horizontal).

1. (3 pt) Write down the kinetic and potential energy for this system in terms of $x_1$ and $x_2$ and their associated velocities.

2. (4 pt) Write down the Lagrangian for this system in terms of $x_1$ and $x_2$ and their associated velocities $\mathcal{L}(x_1, x_2, \dot{x}_1, \dot{x}_2)$. Find the 2 equations of motion.

3. (5 pt) Now consider a new coordinate system where the center of mass is at $x_{cm} = \frac{1}{2}(x_1 + x_2)$ and the relative coordinate is $x = x_1 - x_2$. Write down the kinetic and potential energy in terms of $x_{cm}$ and $x$ and their associated velocities.

4. (8 pt) Write down the Lagrangian for this system in terms of the center of mass coordinate ($x_{cm}$) and the spring's extension ($x$) and the associated velocities $\mathcal{L}(x_{cm}, x, \dot{x}_{cm}, \dot{x})$. Find the 2 equations of motion.
5. (5 pt) Find $x_{cm}(t)$ and $x(t)$ for the system for some generic initial conditions of your choosing. Describe the motion of the system.

In this problem we are changing the coordinates to explore a different aspect of the problem (and to make the math easier). This is a common technique that will not always be obvious. But practice will help us identify when it is useful.

## Exercise 5 (35 pt) Motion inside a paraboloid

Let's figure out the motion of a particle stuck inside a paraboloid. The potential energy of the bead is given by $U = mgz$, where $m$ is the mass of the bead, $g$ is the acceleration due to gravity. The coordinates are $(x, y, z)$ in the Cartesian coordinate system.

1. (5 pt) Write down the Lagrangian for the system in terms of $x$, $y$, and $z$ and their associated velocities $\mathcal{L}(x, y, z, \dot{x}, \dot{y}, \dot{z})$. Find the 3 equations of motion.

2. (15 pt) The bead is constrained by the paraboloid $z = \frac{1}{2}k(x^2 + y^2)$. Find the constraint equation and use it to eliminate one of the coordinates from the Lagrangian. Find the 2 equations of motion. Here it can be useful to change to cylindrical coordinates $(\rho, \phi, z)$. Hint it should be that the Lagrangian is a function of $\rho$ and $\phi$ and their associated velocities, $\mathcal{L}(\rho, \dot{\rho}, \phi, \dot{\phi})$.

3. (15 pt) For an initial condition where the bead is moving relative to the parabolic at some height above the bottom of the paraboloid, numerically solve the equations of motion (i.e., for $\rho(t)$ and $\phi(t)$) and plot the the motion of the bead. Does it stick to the paraboloid?

## Exercise 6 (20pt), Project Check-in 3

This is the last of three check-ins for your final project. This week, you should be preparing to finish your computational essay. Following the posted [rubric](../resources/computational-essay-rubric.md) for the computational essay, you should reflect on your progress and update your project. This is a chance to evaluate where you are in the process of completing your computational essay.

* 5a (5 pts). Review your project in the context of the rubric. What have you been able to accomplish so far? What were you unable to do in the time you had? Be honest in your evaluation of your progress. What do you have left to do? (at least 250 words)
* 5b (5 pts). What problems did you encounter in doing you work? What questions came up and how did you resolve them? Are there any unresolved questions? (at least 250 words)
* 5c (5 pts). Provide an artifact from your project. This could be a plot, a code snippet, a data set, or a figure. Explain what this artifact is and how it fits into your project. (at least 100-200 words)
* 5d (5 pts). Update your project timeline and milestones. How will you adjust your timeline to account for the work you have done and the work you have left to do? How will you meet the expectations from the rubric? (at least 100-200 words)

## Extra Credit - Integrating Classwork With Research

This opportunity will allow you to earn up to 5 extra credit points on a Homework per week. These points can push you above 100% or help make up for missed exercises.
In order to earn all points you must:

1. Attend an MSU research talk (recommended research oriented Clubs is  provided below)

2. Summarize the talk using at least 150 words

3. Turn in the summary along with your Homework.

Approved talks:
Talks given by researchers through the following clubs:
* Research and Idea Sharing Enterprise (RAISE)​: Meets Wednesday Nights Society for Physics Students (SPS)​: Meets Monday Nights

* Astronomy Club​: Meets Monday Nights

* Facility For Rare Isotope Beam (FRIB) Seminars: ​Occur multiple times a week


