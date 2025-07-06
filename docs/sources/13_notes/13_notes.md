# Week 13 - Notes: Examples of Lagrangian Mechanics



We've seen the Lagrangian formulation of mechanics, and we have seen how to use it to derive the equations of motion for a system. We will cover a few common examples of Lagrangian mechanics and point out some of the subtleties that arise in each case.

## Example: The Atwood Machine

The [Atwood machine](https://en.wikipedia.org/wiki/Atwood_machine) consists of two masses, $M$ and $m$, connected by a massless string that passes over a massless pulley. The system is subject to gravity alone. The figure below shows the system along with a choice of coordinates $y_1$ and $y_2$ for the two masses. 

![Atwood Machine](../images/notes/week13/atwood.png)

These coordinates are measured from the center of the pulley and positive $y_1$ and $y_2$ are taken to be upward. Let's try to use the Lagrangian formalism to find the equations of motion for this system.

$$V = + Mgy_1 + mgy_2$$

$$T = \dfrac{1}{2}M\dot{y}_1^2 + \dfrac{1}{2}m\dot{y}_2^2$$

### Equation of Constraint

But notice that $y_1$ and $y_2$ are no independent coordinates. If we unravel the string that is over the pulley, we find that (assume length of string is $l$):

$$y_1 + \pi R + y_2 = l$$

where $R$ is the radius of the pulley. That is shown in the figure below.

![Unraveled String](../images/notes/week13/string-unraveled.png)

The equation above is called an **equation of constraint**. It relates the coordinates $y_1$ and $y_2$ to each other. We can use this equation to eliminate one of the coordinates. Let's eliminate $y_2$:

$$l = y_1 + \pi R + y_2 \rightarrow y_1 = (l - \pi R) - y_2$$ 

This constraint has implications for velocities,

$$\dfrac{dy_1}{dt} = \dfrac{d}{dt}\left((l-\pi R) - y_2\right) = -\dfrac{dy_2}{dt}$$

$$\dot{y}_1 = -\dot{y}_2.$$

This is likely what we could have expected, that the two masses move in opposite directions at the same speed.

### Constructing the Lagrangian

Let's use this constraint to reduce the number of coordinates in the Lagrangian. 

$$\mathcal{L}(y_1, y_2, \dot{y}_1, \dot{y}_2) \rightarrow \mathcal{L}(y_1, \dot{y}_1)$$

We can do this by substituting $y_2$ in terms of $y_1$ into the energy equations:

$$T(y_1, \dot{y}_1) = \dfrac{1}{2}M\dot{y}_1^2 + \dfrac{1}{2}m\dot{y}_2^2 = \dfrac{1}{2}(M+m)\dot{y}_1^2 = T(\dot{y}_1)$$

$$\begin{align}
V(y_1, y_2) &= +Mgy_1 + mgy_2 \\
& = Mgy_1 + mg((l-\pi R) - y_1) \\
& = (M-m)g y_1 + mg(l-\pi R) \\
V(y_1) & = (M-m)g y_1 + U_0
\end{align}$$

where $U_0 = mg(l-\pi R)$ is a constant and will not affect the equations of motion.

$$\mathcal{L}(y_1, \dot{y}_1) = T(\dot{y}_1) - V(y_1) = \dfrac{1}{2}(M+m)\dot{y}_1^2 - (M-m)g y_1$$

$$\dfrac{\partial \mathcal{L}}{\partial y_1} = -(M-m)g$$

$$\dfrac{\partial \mathcal{L}}{\partial \dot{y}_1} = (M+m)\dot{y}_1$$

These derivatives give the following equation of motion:

$$-(M-m) g - \dfrac{d}{dt}\left((M+m)\dot{y}_1\right) = 0$$

#### Generalized Force

Notice that the first term in the above equation is the force on the mass $M$ in the Newtonian picture: the weight of $M$ minus the weight of $m$. That makes sense because the Lagrangian formalism is supposed to reproduce Newton's laws, and the spatial derivative of the Lagrangian produces a [generalized force](https://en.wikipedia.org/wiki/Generalized_force).

$$\dfrac{\partial \mathcal{L}}{\partial q_i} = -\dfrac{\partial V}{\partial q_i} = F_i$$

The kinetic term has no spatial dependence, so it does not contribute to the generalized force.

#### Generalized Momentum

The second term in the above equation is the time derivative of the momentum of the system using $y_1$ as the coordinate:

$$(M+m)\dot{y}_1 = M\dot{y}_1 - m\dot{y}_2 = p_{y_1}$$

Again, that is a sensible result because the Lagrangian formalism is supposed to reproduce Newton's laws, and the generalized force is related to the time derivative of the [generalized momentum](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline)/07%3A_Symmetries_Invariance_and_the_Hamiltonian/7.02%3A_Generalized_Momentum).

$$\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) = \dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{q}_i}\right) = \dfrac{dp_{q_i}}{dt}$$

### Equation of Motion

The equation of motion can be written as

$$(M=m)\ddot{y}_1 = -(M-m)g$$
$$\ddot{y}_1 = -\dfrac{(M-m)}{(M+m)}g.$$

With $M > m$, this acceleration is downward as the larger mass $M$ accelerates down. With $\dot{y}_1 = -\dot{y}_2$, we know $$\ddot{y}_2 = -\ddot{y}_1$$, so that:

$$\ddot{y}_2 = \dfrac{(M-m)}{(M+m)}g$$

Again, with $M > m$, this acceleration is upward as the smaller mass $m$ accelerates up.

## Example: Atwood Machine with Rotating Pulley

In the previous example, we didn't take into account the energy needed to rotate the pulley. Let's do that now. Beucase the rope cannot slip, any small rotation $Rd\phi$ of the pulley give a change $dy_1$ in the position of mass $M$. This is the [no slip constraint](https://en.wikipedia.org/wiki/No-slip_condition).

If the pulley has a mass $M_p$ and radius $R$, then we must introduce it's kinetic energy:

$$T_{pulley} =  \dfrac{1}{2} I \omega^2$$

where $I$ is the [moment of inertia](https://en.wikipedia.org/wiki/List_of_moments_of_inertia) of the pulley and $\omega$ is the angular velocity of the pulley, $\omega = \dot{\phi}$. This angular velocity is related to the linear velocities of the masses.

$$I = \dfrac{1}{2}M_p R^2$$

$$T_{pulley} =  \dfrac{1}{2} \left(\dfrac{1}{2}M_p R^2\right) \dot{\phi}^2$$
$$T_{pulley} =  \dfrac{1}{4}M_p R^2 \dot{\phi}^2$$

We now map this additional kinetic energy into the problem.

$$T(\dot{y}_1, \dot{\phi}) = \dfrac{1}{2}(M+m)\dot{y}_1^2 + \dfrac{1}{4}M_p R^2 \dot{\phi}^2$$

But the constraint is such that, 

$$\dot{y}_1 = Rd\phi \rightarrow y_1 = R\phi +\underbrace{R\phi_0}_{\textrm{const.}}$$

$$\dot{y}_1 = R\dot{\phi}$$

We work these back into $T$, $V$, and $\mathcal{L}$.

$$\begin{align}
T(\dot{\phi}) &= \dfrac{1}{2}(M+m)\dot{y}_1^2 + \dfrac{1}{4}M_p R^2 \dot{\phi}^2\\
&= \dfrac{1}{2}(M+m+\frac{1}{2}M_p)R^2 \dot{\phi}^2\\
\end{align}$$

$$\begin{align}
V(\phi) &= (M-m)gy_1 + U_0 \\
&= (M-m)g(R\phi + R\phi_0) + U_0\\
&= (M-m)gR\phi + \tilde{U}_0\\
\end{align}$$

where $\tilde{U}_0 = (M-m)gR\phi_0 + U_0$ is another constant that will not affect the equations of motion.

$$\begin{align}
\mathcal{L}(\phi, \dot{\phi}) &= T(\dot{\phi}) - V(\phi)\\
& = \dfrac{1}{2}(M+m+\frac{1}{2}M_p)R^2 \dot{\phi}^2 - (M-m)gR\phi\\
\end{align}$$

### Torque and Angular Momentum

Our generalized coordinate is $\phi$ and our generalized velocity is $\dot{\phi}$. We apply the Euler-Lagrange equation. We obtain the generalized force:

$$\dfrac{\partial \mathcal{L}}{\partial \phi} = -(M-m)gR = F_{\phi}$$

Notice that in this case, the generalized force is not the same as the force on mass $M$ in the Newtonian picture. It's a torque around the pulley.

We can find the generalized momentum in a similar way:

$$\dfrac{\partial \mathcal{L}}{\partial \dot{\phi}} = (M+m+\frac{1}{2}M_p)R^2\dot{\phi} = p_{\phi}$$

This is the angular momentum of the system about the axle. We can see that by breaking down each part and adding them up.

$$\vec{L}_{total} = \vec{L}_{disk} + \vec{L}_{M} + \vec{L}_{m}$$

$$\vec{L}_{disk} = I_{disk}\omega = \dfrac{1}{2}M_p R^2 \dot{\phi}\,\text{(out of the page)}$$

$$\vec{L}_{M} = M\vec{r}_{M}\times \vec{v}_{M} = M(R\hat{r})\times (R\dot{\phi}\hat{\phi}) = MR^2 \dot{\phi}\,\text{(out of the page)}$$

$$\vec{L}_{m} = M\vec{r}_{m}\times \vec{v}_{m} = m(R\hat{r})\times (R\dot{\phi}\hat{\phi}) = mR^2 \dot{\phi}\,\text{(out of the page)}$$

Add them up:

$$\vec{L}_{total} = \left(\dfrac{1}{2}M_p + M + m\right)R^2 \dot{\phi}\,\text{(out of the page)}$$

Or the magnitude:

$$L_{total} = \left(\dfrac{1}{2}M_p + M + m\right)R^2 \dot{\phi}$$
$$p_{\phi} = L_{total}$$

### Equation of Motion

We return to the diffeferential equation of motion:

$$-(M-m)gR - \dfrac{d}{dt}((M+m+\frac{1}{2}M_p)R^2\dot{\phi} = 0$$
$$-(M-m)gR - (M+m+\frac{1}{2}M_p)R^2\ddot{\phi} = 0$$

which produces the following equation of motion:

$$\ddot{\phi} = -\dfrac{g}{R}\dfrac{(M-m)}{(M+m+\frac{1}{2}M_p)}$$

which is a constant acceleration.

## Example: Bead in a Parabolic Bowl

A bead of mass $m$ is constrained to move along a parabolic bowl. There is a gravitational force acting on the bead. The bowl is symmetric about the $z$-axis and the bead is constrained to move along the surface without friction or rolling. The bowl is described by the equation:

$$z = \dfrac{1}{2}c(x^2 + y^2)$$

where $c$ is a constant that describes the curvature of the bowl. The figure below shows the system.

![Bead in a Parabolic Bowl](../images/notes/week13/paraboloid.png)

In this case the system is better solved in cylindrical coordinates. The coordinates are $(r, \phi, z)$, where $r$ is the distance from the $z$-axis, $\phi$ is the angle around the $z$-axis, and $z$ is the height above the $xy$-plane as shown above.

With $\langle \rho, \phi, z\rangle$ as the coordinates, equation for the constraint is:

$$z = \dfrac{1}{2}c(x^2 + y^2) = \dfrac{1}{2}c\rho^2.$$

Note that $c$ has units.

$$[z] = m \quad [\rho^2] = m^2 \quad [c] = \dfrac{1}{m}$$

The speed in cylindrical coordinates can be derived from the expressions in Cartesian coordinates, but we quote the result here:

$$v^2 = \dot{\rho}^2 + \rho^2\dot{\phi}^2 + \dot{z}^2.$$

### Constructing the Lagrangian

We write the kinetic and potential energy of the bead in terms of the coordinates $(r, \phi, z)$.

$$T = \dfrac{1}{2}m\left(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + \dot{z}^2\right)$$

$$V = mgz$$

In principle, the Lagrangian can depend on all three coordinates and all three velocities. 

$$\mathcal{L}(\rho, \dot{\rho}, \phi, \dot{\phi}, z, \dot{z}, t) = T - V$$

There is no explicit time dependence, so we can ignore $t$. When the Lagrangian has no explicit time dependence, we should expect the energy to be conserved. This form of Lagrangian analysis does not account for dissipation.

$$\mathcal{L}(\rho, \dot{\rho}, \phi, \dot{\phi}, z, \dot{z})$$

Moreover, with the symmetry of the problem, we can expect no $\phi$ dependence. That is the gravitational potential energy only depends on $z$ and not on $\phi$. This is a consequence of the symmetry of the problem and indicates that $\phi$ is a [cyclic coordinate](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline)/07%3A_Symmetries_Invariance_and_the_Hamiltonian/7.05%3A_Cyclic_Coordinates). We thus expect angular momentum to be conserved about the $z$-axis.

$$\mathcal{L}(\rho, \dot{\rho}, \dot{\phi}, z, \dot{z})$$

Lastly, the constraint equation gives us $z$ in terms of $\rho$:

$$z = \dfrac{1}{2}c\rho^2$$

And thus we can find the time derivative of $z$:

$$\dot{z} = 2c\rho\dot{\rho}.$$

So the Lagrangian can be simplified three variables:

$$\mathcal{L}(\rho, \dot{\rho}, \dot{\phi}) = T - V$$

$$\mathcal{L}(\rho, \dot{\rho}, \dot{\phi}) = \dfrac{1}{2}m\left(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + 4c^2\rho^2\dot{\rho}^2\right) - mg\dfrac{1}{2}c\rho^2$$

### Equations of Motion

We can now apply the Euler-Lagrange equations to find the equations of motion. We will do this for each coordinate. Let's start with $\phi$ because there is only one term in the Lagrangian that depends on $\dot{\phi}$.

$$\underbrace{\dfrac{\partial \mathcal{L}}{\partial \phi}}_0 - \dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot{\phi}}\right) = 0$$

$$\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot{\phi}}\right) = \dfrac{d}{dt}\underbrace{\left(m\rho^2\dot{\phi}\right)}_{L_z} = 0$$

This equation of motion indicates that the angular momentum about the $z$-axis is conserved, as we expected from the symmetry of the problem.

For the coordinate $\rho$, we have:

$$\dfrac{\partial \mathcal{L}}{\partial \rho} - \dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot{\rho}}\right) = 0$$

$$\dfrac{\partial \mathcal{L}}{\partial \rho} = m\rho\dot{\phi}^2 + 4c^2m\rho\dot{\rho}^2 - 2mgc\rho$$

$$\dfrac{\partial \mathcal{L}}{\partial \dot{\rho}} = m\dot{\rho} + 4mc^2\rho^2\dot{\rho}$$

$$\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot{\rho}}\right) = m\ddot{\rho} + 8mc^2\rho\dot{\rho}^2 + 4mc^2\rho^2\ddot{\rho}$$

We can now write the equation of motion:

$$m\rho\dot{\phi}^2 + 4c^2m\rho\dot{\rho}^2 - 2mgc\rho - m\ddot{\rho} - 8mc^2\rho\dot{\rho}^2 - 4mc^2\rho^2\ddot{\rho} = 0$$

We can clean this up a little bit:

$$\ddot{\rho}(1+4c^2\rho^2) + 8c^2\rho\dot{\rho}^2 = \rho\dot{\phi}^2 + 4c^2\rho\dot{\rho}^2 - 2gc\rho$$

$$\ddot{\rho}(1+4c^2\rho^2) + 4c^2\rho\dot{\rho}^2 - \rho\dot{\phi}^2 + 2gc\rho = 0$$

We try to write both equations in terms of their accelerations. We have:

$$\ddot{\rho} = -\dfrac{4c^2\rho\dot{\rho}^2 - \rho\dot{\phi}^2 + 2gc\rho}{1+4c^2\rho^2}$$

$$\ddot{\phi} = - \dfrac{2\rho\dot{\rho}\dot{\phi}}{\rho^2}$$

For which we can develop a solution anywhere away from the origin ($\rho \neq 0$). 

### Preparing for Numerical Solution

We need to write these equations in a form that is ready for numerical solution. We can do this by writing the equations in terms of the first derivatives. Let $\omega = \dot{\phi}$ and $v = \dot{\rho}$. We get 4 1st order equations:

$$\dot{\rho} = v$$
$$\dot{\phi} = \omega$$
$$\dot{v} = -\dfrac{4c^2\rho v^2 - \rho\omega^2 + 2gc\rho}{1+4c^2\rho^2}$$
$$\dot{\omega} = - \dfrac{2 v\omega}{\rho^2}$$





