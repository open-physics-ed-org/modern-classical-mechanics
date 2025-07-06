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


    
![png](images/08_notes_08_notes_1_0.png)
    


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

![Complex Conjugates](images/08_notes_conjugates_graph.png)

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


    
![png](images/08_notes_08_notes_6_0.png)
    



    
![png](images/08_notes_08_notes_6_1.png)
    



    
![png](images/08_notes_08_notes_6_2.png)
    


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


    
![png](images/08_notes_08_notes_9_0.png)
    


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


    
![png](images/08_notes_08_notes_11_0.png)
    


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


    
![png](images/08_notes_08_notes_13_0.png)
    

