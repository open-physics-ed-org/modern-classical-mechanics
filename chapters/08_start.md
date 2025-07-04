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

[![YouTube thumbnail](images/notes/week1//hqdefault.jpg)](https://www.youtube.com/watch?v=t-_VPRCtiUg)


