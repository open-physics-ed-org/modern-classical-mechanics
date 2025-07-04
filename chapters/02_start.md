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

[![YouTube thumbnail](https://img.youtube.com/vi/-M6lANfzFsM/hqdefault.jpg)](https://youtube.com/watch?v=-M6lANfzFsM)

Source: <https://www.youtube.com/watch?v=-M6lANfzFsM>

## A Critical Perspective on Computing

While the history of computing is often celebrated as a story of innovation, it is deeply entangled with systems of power, exploitation, and violence. Computing technologies have not only been tools of scientific progress but also instruments for surveillance, war, and perpetuation of systemic biases.

```{admonition} Humans as Computers
:class: note

Of course, the development of electronic computers was a huge development for science. Prior to that, humans were employed to do the calculations that we now do with computational algorithms. This work occurred in a wide variety of labs where data were entered into tables, calculations were done by hand, and the results were tabulated manually. 

Frequently the work was done by those with less power in the laboratory and broader society (e.g., women, immigrants, and folks of color). A notable and well-known example is the work of the [Harvard Computers](https://en.wikipedia.org/wiki/Harvard_Computers) in the late 19th and early 20th centuries where women were employed to do the calculations that led to significant discoveries in astronomy. 

![Harvard Computers](../images/notes/week2/harvard-computers.png)

One of the most important examples is the work done by African-American women at NASA in the 1960s, as depicted in the book and movie [Hidden Figures](https://en.wikipedia.org/wiki/Hidden_Figures).

![Hidden Figures](../images/notes/week2/nasa-computers-hidden-figures.png)

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
| [George Dyson’s *Turing’s Cathedral*](https://www.penguinrandomhouse.com/books/44425/turings-cathedral-by-george-dyson/) ![Turing's Cathedral](../images/notes/week2/dyson.png) | Chronicles the origins of the modern computer, focusing on [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) and his team at Princeton in the 1940s. This book delves into the intersection of mathematics, physics, and computation, highlighting the development of the first stored-program computers and their role in shaping the digital age. |
| [James Gleick’s *The Information*](https://www.penguinrandomhouse.com/books/60765/the-information-by-james-gleick/) ![The Information](../images/notes/week2/gleick.png) | Explores the transformative impact of information theory on science, technology, and culture. From the invention of writing to the digital age, Gleick highlights key figures like Michigander [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon), who revolutionized communication with his groundbreaking mathematical theory of information. |
| [Steven Levy’s *Hackers*](https://www.stevenlevy.com/hackers-heroes-of-the-computer-revolution) ![Hackers](../images/notes/week2/levy.png) | Chronicles the rise of hacker culture, from early computer pioneers to the creators of the personal computer revolution. Levy examines the "hacker ethic," emphasizing creativity, open access, and the joy of problem-solving, which shaped the tools and technologies we use today. |
| [Cathy O’Neil’s *Weapons of Math Destruction*](https://www.penguinrandomhouse.com/books/241363/weapons-of-math-destruction-by-cathy-oneil/) ![Weapons of Math Destruction](../images/notes/week2/oneill.png) | Explores how algorithms, often marketed as objective, exacerbate inequality in policing, hiring, and credit scoring. O’Neil critically examines the dangers of data-driven systems that disproportionately harm marginalized communities while remaining opaque and unregulated. |
| [Ruha Benjamin’s *Race After Technology*](https://www.ruhabenjamin.com/race-after-technology) ![Race After Technology](../images/notes/week2/benjamin.png) | Analyzes how algorithms and technologies reinforce systemic racism under the guise of neutrality. Benjamin introduces the concept of the “New Jim Code,” highlighting the ways in which technological tools amplify inequities while appearing fair and impartial. |
| [Simone Browne’s *Dark Matters*](https://www.dukeupress.edu/dark-matters) ![Dark Matters](../images/notes/week2/browne.png) | Examines how surveillance technologies are deeply rooted in practices of racialized social control. Browne connects historical practices like slave surveillance to modern tools like facial recognition and predictive policing, revealing the persistence of systemic inequities in new forms. |
| [Kate Crawford’s *Atlas of AI*](https://katecrawford.net/atlas) ![Atlas of AI](../images/notes/week2/crawford.png) | Explores the hidden costs of artificial intelligence, from resource extraction to labor exploitation and military applications. Crawford critiques AI as an extractive industry that reshapes power dynamics and perpetuates global inequalities while causing significant environmental damage. |
| [Shoshana Zuboff’s *The Age of Surveillance Capitalism*](https://shoshanazuboff.com/book/about/) ![Age of Surveillance Capitalism](../images/notes/week2/zuboff.png) | Investigates how corporations and governments exploit personal data for profit and control. Zuboff coins the term "surveillance capitalism" to describe how the tech industry commodifies human behavior, eroding privacy and autonomy while reshaping society’s power structures. |



