---
title: 03 - What is Mathematical Modeling?
weight: 3
date: '2026-01-09'
math: true
---

[![Report Issues](https://img.shields.io/badge/report%20issues-GitHub-blue)](https://github.com/dannycab/phy321msu/issues) 
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Learning Goals

{{< admonition type="admonition" title="After studying Lesson 03, you should be able to:" class="note" >}}
* Define the concept of a "model" in physics and explain its role in predicting and explaining natural phenomena.
* Differentiate between various types of observations (e.g., qualitative, quantitative, historical) and their significance in building models.
* Develop equations of motion (EOM) for simple physical systems, such as a falling object or a simple harmonic oscillator.
* Analyze the iterative process of refining models based on experimental observations and theoretical predictions..
{{< /admonition >}}

Nature reveals itself to us through interactions. We can tell from observations that it is nature's interactions that lead to its evolution. Explaining how nature can change and predicting how it will change in the future is our work as scientists. In this our work, we observe nature and its interactions to make models of those observations. We aim to predict and explain our observations of nature through building and testing mathematical models.

In physics, our goals are typically to explain and predict observations of physical phenomenon. Here, we focus ourselves to those canonical things that physicists concern themselves with: motion, fields, waves, atoms, nuclei, and so on. 

{{< admonition type="admonition" title="Why the word \"observation\"?" class="hint" >}}
We intentionally use the word "observation" in our discussion of modeling, because we are not simply talking about what we can see with our eyes. The visible spectrum is limited to a small portion of the [electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum). 

These observations can come in the form of light, but also as sound, voltage, or current. For example, most instrumentation in laboratories will report only voltages or currents -- rather voltages and currents are what the equipment will measure precisely and report as measurements as different as [distance](https://en.wikipedia.org/wiki/Laser_rangefinder) and [shear stress response](https://en.wikipedia.org/wiki/Rheometer). 

We also use "observation" because it includes the historical science that conducted qualitative investigations and conceptual observations. It is also inclusive of the work of early humans and indigenous people who made observations and constructed ways of knowing and explaining the world around them. 

The word observation respects the common human endeavor of trying to understand and explain the natural world; an activity that all human civilizations and cultures have participated in for millennia.
{{< /admonition >}}

## What is a model?

Physics is a science that builds models. Typically, these models are represented mathematically in the form of equations or formula, but we can use charts, graphs, and animations to represent our models. Models used in physics are often constructed by a community of scientists who have agreed on the model's utility and accuracy. Physics is, after all, a social endeavor -- a global activity in which humans exchange and evaluate ideas and perform labor to produce new knowledge and practices. Experimental observations are used to validate these models. This experimental evidence can be table-top work conducted at the scale of a single lab or small set of experiments, or a big scientific endeavor with many moving parts and people such as DUNE, the LHC or LIGO.

Modeling is the process of constructing a model. This process is often iterative where the initial ideas and assumptions are used to formulate a model. It is then tested against observations, experience, and expectations, and, later refined. This process is repeated until the model is accurate enough to be useful. Physicists are model builders and model users. There is an enormous body of literature in natural philosophy, history of science, science education, and elsewhere covering the idea of a model and concepts and practices of modeling. 

Suffice to say, academics can spend a lot of time talking about the things that we are doing everyday. 

### History and Philosophy of Science

If you would like to dive deeper into models and modeling, there's excellent work in the [history and philosophy of science](https://en.wikipedia.org/wiki/History_and_philosophy_of_science). The field studies how science develops knowledge, practice, culture, and so on. It studies important events and provides critical information on important and, often, overlooked folks who do science. For example, historian and gender studies professor [Sharon Traweek](https://en.wikipedia.org/wiki/Sharon_Traweek) studies the high energy physics field. Her book, [Beamtimes and Lifetimes: The World of High Energy Physicists](https://en.wikipedia.org/wiki/Beamtimes_and_Lifetimes) is excellent.

{{< admonition type="admonition" title="Dame Nancy Cartwright (philosopher of science)" class="note" >}}
One of the more interesting scholars is [Dame Nancy Cartwright](https://en.wikipedia.org/wiki/Nancy_Cartwright_(philosopher)) who wrote a lot about the 'practice of science.' Her philosophical work informed many of the innovations in physics and broader science education -- including many science courses at MSU. 

Her writing is very interesting, but the style of writing can be a challenge to read. This is the nature of academic writing in different disciplines. Her book called "How The Laws of Physics Lie" is worth a read. Here's a link to the [first chapter](http://www.generativescience.org/papers/nature/Cartwright-_1983.pdf).
{{< /admonition >}}

{{< admonition type="admonition" title="Short Film on Modeling in Science (8 minutes)" class="tip" >}}
Geoscientist [John Aiken](https://mnky9800n.github.io/) made this short video when he was a graduate student at Georgia Tech. John cut clips from a lecture [Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman) gave. In this lecture, Feynman talks about the nature of models and the process of science.  John also interviewed different science researchers and teachers about their understanding of what a model is. 

{{< youtube dkTncoPqo5Y >}}

- *Source: <https://www.youtube.com/watch?v=dkTncoPqo5Y>*
{{< /admonition >}}

{{< admonition type="admonition" title="Feynman on the Process of Science (10 minutes)" class="warning" >}}
[Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman) was a physicist who made significant contributions to physics, especially in the field of quantum mechanics. He was awarded the [Nobel Prize in Physics in 1965](https://www.nobelprize.org/prizes/physics/1965/feynman/) for his work in quantum electrodynamics. In his time, he was known as a great teacher and communicator of physics. And [his lectures](https://www.feynmanlectures.caltech.edu/) are still used in physics education today -- even for planning our classes.

Feynman was a gifted communicator; his lectures are lively and conceptual. Here's the longer version of the lecture he gave on the nature of models and the process of science.

{{< youtube EYPapE-3FRw >}}

- *Source: <https://www.youtube.com/watch?v=EYPapE-3FRw>*


While we acknowledge the importance of Feynman's contributions to physics and physics teaching, we should remind ourselves that he was not a perfect person. Feynman was also known for his [sexist behavior and comments](https://thebaffler.com/outbursts/surely-youre-a-creep-mr-feynman-mcneill). (*Trigger warning*: this link recounts instances of harassment) 

**We should not ignore this aspect of his life, and remind ourselves that we can learn from his physics and make a welcoming space for all people.** These are not mutually exclusive positions to hold.
{{< /admonition >}}

:::

## Making Classical Models

The central enterprise of physics is making and testing models of physical systems. These models we developed are based on the assumptions we make about the physical systems we are studying. As we characterize the system, we make simplifying assumptions that allow us to describe the system in terms of a few key quantities. These quantities are often called the ["degrees of freedom"](https://en.wikipedia.org/wiki/Degrees_of_freedom_(physics_and_chemistry)) of the system.

In Classical Mechanics, we will use formulations of physics, such as [Newton's Laws](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion), to describe the motion of particles. We can also use the [Lagrangian](https://en.wikipedia.org/wiki/Lagrangian_mechanics) and [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) formulations of mechanics. These formulations are mathematical expressions of the physical laws that govern the motion of particles. They borrow from the idea that Newton's Laws are but an expression of a deeper principle, that nature works to [minimize the "action"](https://en.wikipedia.org/wiki/Action_principles). This is not energy! The action, as we will learn, is a quantity that provides theoretical constraints on the ways that a system may travel through all possible points in its phase space. And if this reads like a word salad, that's ok for now. We will get there.

Typically, the models we develop are expressed as [differential equations](https://en.wikipedia.org/wiki/Differential_equation) that describe how the system evolves in time. Our work in classical mechanics is to develop techniques and tools that let us investigate the solutions (later, families of solutions and qualitative different phases spaces) to these equations. These differential equations are commonly called [equations of motion](https://en.wikipedia.org/wiki/Equations_of_motion) (EOM). An equation of motion describes the evolution of the agents (particles) as they interact with their surroundings and each other.

#### What is Dynamics?

Dynamics is the study of the time evolution of any system in question. In classical mechanics, dynamics is the study of the motion of particles and the forces that cause that motion. In other physics, dynamics can refer to the study of the evolution of a system in time and space. And here, space might be an abstraction, such as a [phase space](https://en.wikipedia.org/wiki/Phase_space). We study phase spaces later.

Dynamics is a general term used frequently to mean the same thing in fields as distinct as economics, education, political science, engineering, biology, and chemistry. You might have read about [population models](https://en.wikipedia.org/wiki/Population_model), [voter pattern evolution](https://www.pewresearch.org/politics/2025/06/26/voting-patterns-in-the-2024-election/), or even [chemical kinetics](https://en.wikipedia.org/wiki/Chemical_kinetics). All of these are examples of dynamics of various systems.

{{< admonition type="admonition" title="When studying dynamics goes wrong" class="hint" >}}
Interestingly, we can, in part, blame the [2008 financial crisis](https://en.wikipedia.org/wiki/2008_financial_crisis) on how dynamics were modeled, not just on the presence of complex mathematics. Quantitative analysts—often with training in physics or mathematics—were solving partial differential equations and related models to describe market behavior, but these tools were transplanted from well-understood physical systems into a domain with far less control over assumptions and data. The techniques themselves were powerful; the problem was that they rested on fragile, poorly examined initial conditions and idealizations about correlations, liquidity, and rare events, turning elegant equations into dangerously misleading guides.

Crucially, these modeling failures did not occur in a vacuum. They unfolded inside a financial system organized around extracting value from the expertise, experience, and labor of working people while channeling gains upward to corporations and billionaires. In that context, models became part of a pipeline of exploitation: they were used to justify complex financial products, aggressive lending, and high leverage, while masking the risks that would eventually be offloaded onto workers through foreclosures, unemployment, and cuts to public services. 

The issue is not simply “too many physicists in finance,” but that technically sophisticated modeling was enlisted—often uncritically and sometimes incompetently—to serve a system whose deepest impacts were borne by those with the least power to shape it.
{{< /admonition >}}

### Newtonian Examples of Classical Models

From a Newtonian perspective, our equations of motion are often second-order differential equations. This stems from the fact that Newton's second law relates the acceleration of a particle to the forces acting on it and that the second derivative of position is acceleration. The second law is given by the equation:

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

where $\vec{x}$ is the position vector and $\ddot{\vec{x}}=\frac{d^2\vec{x}}{dt^2}$ is the acceleration vector. Thus, Newton's second law is a general EOM that describes the dynamics of a particle of mass, $m$:

$$\frac{d^2\vec{x}}{dt^2} = \dfrac{\vec{F}_{\text{net}}}{m}$$

#### Example: Falling Ball with No Air Resistance

Consider a ball of mass $m$ falling down. We define the positive $y$ direction to be down as in the figure showing the FBD of the ball. 

{{< figure src="/images/vector-graphics/falling_ball_no_air_resistance_fbd.png" caption="Free Body Diagram of a falling ball; the arrows label the direction of forces acting on the ball. [SVG File](../images/vector-graphics/falling_ball_no_air_resistance_fbd.svg)" >}}

We can apply Newton's laws to obtain the specific EOM for the ball.

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

This is a 1D case in the $y$ direction,

$$F_{\text{net,y}} = W = mg = m \ddot{y}$$

Thus,

$$\ddot{y} = g$$

is the specific EOM for the ball. 

#### Example: Simple Harmonic Oscillator

We will spend a lot of time studying the [simple harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator) (SHO). The SHO is a system that oscillates back and forth around an equilibrium position. It is a very common system in physics and is used a base model for many more complex systems. Consider a mass, $m$, attached to a spring with spring constant, $k$, sitting on a frictionless horizontal plane as in the figure below.

{{< figure src="/images/vector-graphics/simple_harmonic_oscillator_setup_1D_horizontal.png" caption="Free Body Diagram of a Simple Harmonic Oscillator; the arrows label the direction of forces acting on the mass. [SVG File](../images/vector-graphics/simple_harmonic_oscillator_setup_1D_horizontal.svg)" >}}

The EOM for the SHO can be derived form Newton's Second Law.

$$\vec{F}_{\text{net}} = m \vec{a} = m\ddot{\vec{x}}$$

This is a 1D case in the $x$ direction,

$$F_{\text{net,x}} = F_{\text{spring}} = -kx = m \ddot{x}$$

And thus,

$$\ddot{x} = -\dfrac{k}{m}x$$

is the specific EOM for the SHO. As we will learn, this restoring force causes the mass to oscillate back and forth around the equilibrium position, with a well known frequency, $\omega = \sqrt{\dfrac{k}{m}}$.

## Turning Observations into Models

One of the more challenging aspects of physics is how we work to make models of the observations we have. This a long and challenging process in general, but if we have a general schematic, we can make progress. The hand drawn figure below provides such a schematic.

{{< figure src="/images/vector-graphics/turning_observations_into_models_diagram.png" caption="Framework for making models: Schematic diagram showing the process of turning observations into models in physics. [SVG File](../images/vector-graphics/turning_observations_into_models_diagram.svg)" >}}

In the schematic, our observations are the starting point. Using our framework for physics (e.g., Newton's Laws) and making the appropriate assumptions (in blue), we can develop a model (in red) of the system. By conducting analysis and investigating the evolution of the model, we produce predictions (in green). We can then compare those predictions to our observations to evaluate how well our model describes the system.

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

Let's return to an example you have seen before: the falling ball.

### Example: Falling Ball in 1D

Consider a ball of mass $m$ falling with air resistance. Here, we have already done some of the work above. We have identified the phenomenon, and started to indicate the interactions. 

{{< figure src="/images/vector-graphics/falling_ball_framework_applied.png" caption="FBD of a falling ball with air resistance. [SVG file](../images/vector-graphics/falling_ball_framework_applied.svg)" >}}

In the figure above, we have identified the forces acting on the ball. We have the gravitational force, $W = mg$, and the air resistance, $F_{\text{air}}$. We have chosen the linear model for air-resistance, which is a choice of model given the assumption that the ball moves very slowly -- *this is not a good assumption in this case*, but makes the mathematical analysis simpler. We also selected the gravitational interaction model as a constant force near the surface of the Earth, thus neglecting variations in $g$ with height or location.

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

{{< admonition type="admonition" title="Kinematic equations" class="important" >}}
In this analysis we produced kinematic equations for an object experiencing a constant force in one dimension:

$$v(t) = v_0 + at$$
$$y(t) = y_0 + v_0 t + \dfrac{1}{2}at^2$$

This result is really useful, but is contingent on finding or knowing the anti-derivative of the functions that we are integrating. For the case of a constant force, it is the case that these kinematic equations are always representative.

But, finding an appropriate anti-derivative is not always possible. What might we do if we weren't sure that we could find the anti-derivative?
{{< /admonition >}}

### Discrete Formulation of Newtonian Mechanics

Most of our experience so far has been solving problems where we can find continuous functions that are the anti-derivatives of the functions we are integrating. This leads to standard formulae that we can use to predict or plot our results. 

However, there are very few systems for which we can write down EOMs that have known analytical solutions. In these cases, we need to turn to numerical methods to solve the equations of motion. To do this, we need a discrete formulation of the EOMs. 

For now, let's focus on 1D:

$$\dfrac{d^2y}{dt^2} = \dfrac{F}{m}$$

We can write this as a pair of first-order differential equations:

$$\dfrac{dy}{dt} = v \quad \textrm{and} \quad \dfrac{dv}{dt} = \dfrac{F}{m}$$

Let's allow ourselves to consider instead a small time interval of the evolution, $\Delta t$. We can then write the velocity equation as:

$$\dfrac{dv}{dt} = \dfrac{\Delta v}{\Delta t}= \dfrac{v(t+\Delta t) - v(t)}{\Delta t} = \dfrac{F}{m}$$

We can turn this into a discrete equation by multiplying through by $\Delta t$: 

$$v(t+\Delta t) - v(t) = \dfrac{F}{m}\Delta t$$


And then use that to make a prediction of the velocity at the next time step:

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

{{< admonition type="admonition" title="Choosing $v_{\textrm{avg}}$" class="tip" >}}
The idea that we have to pick a value for $v_{\textrm{avg}}$ is a key point in numerical methods. It might seem silly or overly subtle and it is certainly the latter. We can select $v(t)$, $v(t+\Delta t)$, or some average of the two. The choice of $v_{\textrm{avg}}$ is the key to the accuracy of the method.

As we will show in a later homework, the best choice is $v(t+\Delta t)$ as it preserves the energy of the system.
{{< /admonition >}}

#### Euler-Cromer Step

Taking the definition of $v_{avg}$ to be the predicted velocity, we obtain the [Euler-Cromer](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method) step for the position and velocity:

$$v(t+\Delta t) = v(t) + \dfrac{F(t)}{m} \Delta t$$
$$y(t+\Delta t) = y(t) + v(t+\Delta t) \Delta t$$

This method was accidentally discovered by a high energy physics student called Abby Aspel. It was later explored by [Alan Cromer](https://en.wikipedia.org/wiki/Alan_Cromer) who wrote up this [method in the American Journal of Physics](https://aapt.scitation.org/doi/10.1119/1.10903). 

In three-dimensions, this method is simply written in a vector form:

$$\vec{v}(t+\Delta t) = \vec{v}(t) + \dfrac{\vec{F}(t)}{m} \Delta t$$
$$\vec{r}(t+\Delta t) = \vec{r}(t) + \vec{v}(t+\Delta t) \Delta t$$


{{< admonition type="admonition" title="Erasing Contributions in Physics" class="warning" >}}
This method is called the Semi-Implicit Euler method or the Euler-Cromer method. It should be called the Euler-Aspel-Cromer method because Euler started it, Aspel improved it, and Cromer formalized it. 

It is not called that because physics and physicists tend to erase the contributions of marginalized groups including young people, women, and folks from non-dominant groups. 

**Don't believe it?**

Read about the [history of the MIT physics department](https://physics.mit.edu/about-physics/our-history/) and try to find the contributions of the many technical staff, non-tenure track faculty, and students who have made the department what it is today.

Abby Aspel deserves recognition for her discovery as much as Alan Cromer does for writing up a readable, useful, and well-cited article on the method. To Alan Cromer's credit, he quite clearly identifies Abby as having discovered the method while working on Kepler problems.
{{< /admonition >}}

## Analytical Solutions to the Air-Resistance Problem

While we have made a big deal about numerical solutions, it turns out that we can solve the air-resistance problem analytically, at least, in one-dimension with up to $v^2$ drag. 

We start with the EOM for velocity that we derived previously

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

As $t \rightarrow \infty$, the $\tanh$ will tend to 1, and thus the system approaches the terminal velocity,


$$\lim_{t\rightarrow \infty} v(t) = v_{\text{term}} = \sqrt{\dfrac{mg}{c}}$$






