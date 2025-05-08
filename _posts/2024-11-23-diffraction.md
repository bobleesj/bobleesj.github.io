---
layout: post
title: Learning about diffraction
categories: coursework
---

The following content is acquired from the course content of MSAE 4100 at Columbia University and Solid State Physics by Ashcroft/Mermin. The content is primarily consumsed for my own learning.

Here, the goal is to use our imagination to be able to create our own mindmap.

First, how do you generate X-ray? The theory behind is extremely intriguing. It requires an imagination.

Same speed as ligh in vacuum

Why do peaks occur?

The angle at the top is theta, half the angle between the incident and scattered beams. The long side is the distance between the atomic planes. The short side is the one half of a wavelength.

Te oscilalting electrons emit an electromagnetic in all directions.

What is Thomson Scattering?

What are the Three Laue equations?

As a result, constructive interference occurs at certain angles.

Q. What is a zeroth order Laue zone? It is a layer that contains th eorigin of the reciprocal lattice.

Q. What does Bragg's law tell you?
It tells you the geometric conditions required to observe diffraction from sets of lattice planes in the crystal.

$$
\begin{align}
    sin \theta &= \frac{{\lambda/2}}{d} \\
    2d  \sin \theta &=\lambda
\end{align}
$$

This is Bragg's Law in 1915 Nobel prize winner.

Imagine two parrallel electrons hitting two atoms the sample respectively. Assume the resulting angle change is
identicial.

Each atom has a nucleus, surrounding by a cloud of electrons.

The wavelenght of an X-ray is similiar to the distance between atoms in a crystal.

When waves are aligned, the signal is amplified. This is "constructive interference".

$$
\begin{align}
    E(x,t) = A e^{2 \pi i kx} e^{i 2 \pi \nu t} \\
\end{align}
$$

where

$$
\begin{align}
    \lambda \nu = c
\end{align}
$$

In solid state literatuure, the magnitude of wave vector is defined as $2 \pi /\lambda$ but in crystallography it can be denoted as $1/\lambda$.

### Phase difference

$$
\begin{equation}
    \phi = \left(2 \pi \frac{∆x}{\lambda}\right)
\end{equation}
$$

Hence, to represent the new amplitude with the phase,

$$
\begin{equation}
    A(x) = \cos\left(2\pi \frac{x}{\lambda} + \phi\right)
\end{equation}
$$

An X-ray wave

Elastic scattering, an X-ray is encountered by an atom by it is then must be re-emitted by the atom, without losing any energy. This is called "elastic scattering".

An electron in one of the shells is thermally "excited" to the next shell. When the electron magically returns to back to the original shell level, it emits X-rays.

It turns out these x-rays are electrically neurtral.

0.01 to 1,0 nm

The electron hits the anode, where 90 percent is disspiated as heat but some of them are converted to x-rays.

### Single crystal X-ray diffraction

A single crystall is highly ordred with crystal lattice.

### What is Electron Diffraction?

### What is polyatomic crystal?

## Electron Diffraciton

Why but do we need electron diffractio when we have X-ray diffraction?

X-rays can penetrate relatively deep into most materials (tens of micrometers to millimeters. However, this is not always ideal when you want to study very thin samples or surface layers. Electrons have shallower depth, so it is useful for studying thin flims, surfaces. Furthermore, the resolutino is lower for X-ray. The wavelnght of 0.1 to 100 nm is not enough to study indivdual atomic positions or defects. Electron beams have the De Broglie wavelength of 0.01 nm.

## Why do you need Si-N?

They are used for making ultrathin membranes (few nanometers thick). Si-N is designed to be electron-transparent, minimizing interference with the electron beam. It is also thermally and chemically stable.

Electron as a particle has a charge and a mass. Due to its low mass, it can be accelerated.

$$
\begin{equation}
    \lambda = \frac{h}{m \nu} = \frac{h}{\sqrt{2 m_o e V \left(1 + \frac{e}{2m_o c^2 V}\right)}}= \frac{1226.36}{\sqrt{V + 0.97845 \times 10^6 V^2}}
\end{equation}
$$

where $V$ is the acclerating volage, $e$ is the electron charge, and $m_o$ is the electron rest mass. From the equation, at 200 $V$, $\lambda$ is 2.508 pm and at 100 $V$, 3.701 pm.

The electron is a charged particle, so it complicates the diffraction process but it strongly interactis with other charges.

What is atomix scattering factor?

What is the structure factor?

A beam of electrons shone through a thin sample and captures the transmitted electrons to form an image. The electron changes direction in the sample without losing any energy.

## What is the dfiference between TEM and STEM?

## What is the difference between STEM and 4D-STEM?

## What is ptychography?

Ptychography - the goal is to capture interfering diffraction patterns, use advanced mathemtical algorthsm to reconstract the ful image of the sample.

It recovers phase information.

Q. What is phase information?

The position of the wave in the oscillatory cycle. Phase changes can highliyh fine structures that might not show up in intensity data alone. The phase can directly link with samples’ thickness, density and compositon.

Q. so my unerstnadinfg is that4D stem gives 4D info per reach real space and the difrraction pattern but the thing is that we want to do not only look at individual but take a whole and we want to recover the phase? like diffraction interfering?

4D STEM itself gives a wealth of data, but ptychography **enhances** it by leveraging **overlap** in the beam positions to recover the phase information. Here's how it works:

Now, in situ expeimrentsl require holders, like Si3N4 membrances but these membranes also scatter and produce noise in the ata.

Q. How does Ptchography help fliter out

DSTEM multislice ptychography for in situ

Q. whatn do you this in situ, how long does it tpyically take ?

**Computational Burden**: Ptychography involves iterative reconstruction algorithms (e.g., phase retrieval), which can take hours or even days depending on, dataset size (4D datasets are massive),

### What is the difference between synchrotron light source vs. regular STEM light source?

For STEM, thermionic (tungsten filament), emits electrons rather than electromagnetic waves. The synchortron, charged particles accelerated at near light-speed and produces broad spectrum of electromagnetic radiation. So The synchortron can be

Q. What is the limitation of 4D STEM otherwise that can be done by Syncrhtroton?

For 4D STEM, the sample must be thin so that the electrons can pass through without significant scattering or absoprtions

Q. Why do we need an node?

### Why do we want to use Synchrotron?

Synchrotron emits a broad spectrum of wavelenght lights. It can study bulk samples.

- Synchrotron uses X-ray so it passes throgh the X-ray and does not affct the sample. ALso, it can do 3D imaging capability (Tomograph) through multiple angles. Therefore, it is useful for Archaeology, biomedical,

Yes, if low-dose electron techniques in 4D STEM can achieve high-quality imaging without damaging sensitive samples, it would indeed be revolutionary

Allow us to study biological systems, sensitive materials (organic semiconductors) without degradation. Many samples degrade over time when exposed to an electron beam, making it difficult to observe real-time processes (e.g., chemical reactions or phase transitions).

Q. What is the concept of zone axis?

Q. What those recirpocal values provided in the diffraction images?
If you see a diffraction spot labeled 002, it corresponds to the family of planes in real space with Miller indices
(002) They are related to real-space planes via Miller indices.

Q. What is the brightness important?

Q. What can Syncrhtron do that STEM-4D cannot do?

Q. How can you get can crystal strain, electric/magnetic fields, phase images from 4D images?

Q. Why do you need synchotron source?

Q. What is the difference between TEM and STEM?
In TEM, beam of electrons illuminate the entire sample simultanoeusly. In STEM, electrons are scattered one point at a time.

Q. What motivatde to use STEM instead of TEM?

Q. How does STEM provide higher resolution at atomic scale?

Q. What is Energy-Dispersion X-ray Spectroscopy (EDS)?

It determine the elemental composition by detecting X-rays emitted during STEM. The incoming electron excites by "kncoking" electrons out oft he inner shell. To fill the valancym electrosn from higher energy levels drop down nad this produces X-rays...

Q. What is Electron Energy Loss Spectroscopy (EELS) and why important?

It gives you information about the amount of energy lost due to inelastic scattering, better for light elements (C, O, H). STEM (Scanning Transmission Electron Microscopy) allows you to perform EDS (Energy-Dispersive X-ray Spectroscopy) and EELS (Electron Energy Loss Spectroscopy) at each scanned position on the sample

### 4D-STEM

Q. How is 4D-STEM different from STEM and why is it important?
Regular STEM detects intensity from a single detector while the FUll 2D patterns is detected in each scan positions. Regular STEM uses annular detects to maesure integrated signal while 4D STEM use pixelated detectros to capture 2D diffraction maps.

Q. How is it possible you get get detailed crystallographic strain, phase information from 4D STEM?

from the Braggs diffraciton spots produced from 4D STem you can identify lattice parameters in each point.

Q. How do you determine lattice parameters from diffract 2D images?

$$
\begin{equation}
    \frac{1}{d_{hkl}^2} = h^2 \frac{1}{a^2} + k^2 \frac{1}{b^2} + l^2 \frac{1}{c^2}
\end{equation}
$$

$$
\begin{equation}
    \bold{g}_{khl} = h \bold{a}^* = k \bold{b}^* + l \bold{c}^*
\end{equation}
$$

Q. How does Ptychography filter out contributions from Si-N membranes?

### Geometry of electorn diffraction

Assume 200 kV electorns, with the wavelenght of 0.0002508 nm, and with d= 0.2 nm, then the difffractino angle is only 0.36 degresss. So often $\lambda \approx 2d \th$

What is synchrotron-based X-ray Absorption Spectroscopy (XAS)?

### Whaare the the types of electron diffraction?

- Selected area electron diffraction (SAED)
- Kikuchi diffraction patterns
- Convergent beam electron diffraction (CBED)
- Precession electron diffraction (PED)
- Back scatter electron diffraction (EBSD)
- Refletino high energy electrion diffraction (RHEED)
- Low energy electron diffraction (LEED)

## PDF (Pair distribution function)

Great videos

- Single crystal X-ray diffraction: https://www.youtube.com/watch?v=xBA09PXPPR4
- https://www.youtube.com/watch?v=QHMzFUo0NL8

Q. What is energy filter?
Filter electrons based on their energy after interacted with the sample. The key idea is to isolate the energy losses characteristic of Si-N and exclude them from the data you collect.

Q. What is the concept of multi slice in ptchography?

Q. Why is multislice important?
When a sample is thick, the sample is no longer modeled as a single, uniform object.

Q. Wat is multislice?
TheReconstruct the final 3D image of the sample

Q. What is Ptychography?
Diffraction patterns recorded across a region is combined to reconstruct the high-resolution real-space image of the sample

Q. What is the concept of “thick” here?
Several micrometers.

Q. Why do you need a phase retrieval algorithms (iterative phase retrieval)?

Q. Why do we need multi splice ptychography in real-life?
We can study thick biological samples and we study imaging nano materials, multilayers structures, composition material in materials science.

Q. What does it mean by the prove interacts with the sample as a whole?

Q. What is the traditional single-slice ptychography assumption?
The entire sample is a single, homogenous object. It assumes it has no different materials ad layers. This assumption works well for thin or relatively homogenous samples when the scattering does not vary significantly with depth or layer. But it breaks down for multi-layered materials and heterogeneous samples since probe scatter differently in different layers of the sample. Multiple scattering events occur within the sample.

Q. Multislice approach?
Each slice of the sample is considered differently and combined to form the overall diffraction pattern

Q. What is the still remaining assumption in multi-slice?
It has multislice approximation, meaning it treats the sample as a series of thin layer or slices, and for each slice, the scattering effects and phase shifts are modeled.

Q. How do you determine the initial phase of the electron?
It is well defined from the electron gun source.

Q. What information does the phase contain?
It contains fine features, boundaries, and defects.

Q. How do you use the phase information and intensity to construct real space imaging?

Q. So how can Ptschography separate Si-N?
Ptchography excels at capturing detailed phase image and useful how material modify the phase of the electron beam, these phases can reveal difference between materials that are not apparent in traditional amplitude-based images.

Q. Now that you have multis lace ptychography for in situ, how can you reconstruct , it inherently lends to 3D reconstruction

Q. What information is needed to guess and get refined later?
You need to set the amplitude, meaning how much wave’s intensity is reduced by the sample. Them,

Q. So what is the algorithm about?
The goal is to utilize the diffraction patterns recorded to reconstruct the real-space structure of the sample. Ptchography captures both amplitude and phase information, so the phase retrieval algorithm is crucial for obtaining the phase of the exit wave at each point in the sample.

Q. How do you acquire the phase information?
You start with the initial sample’s structure and guess intensity and phase of the sample’s Elton wave at each point. After diffraction, it gives you amplitude, not the phase. Then, the diffraction patterns obtained from the simulation ad then compared with the experimental diffraction data. We are primarily interested in the phase after the electron has scattered.

Q, How does the phase tell you information about the structure?

Q. Also do you model a single electron and the phase associated with the electron?

Q. But again, why are we doing this instead of using just regular 3D? Why can’t we just use the microscope to observe he 2D and then eventually form 3D by combining 2D images?
If you use a flat 2D project to build a 3D structure, the full depth information is hard to acquire. Even

Q. What is tomography?
It is a technique to build a 3D reconstruction from 2D images. For thick samples, scattering events become more complex. In 2D imaging, phase information can be important but is lost while ptchography allows you to reconstruct amplitude and phase from the diffraction data, allowing high-resolution reconstruction of the 3D structure.

Q. How do you sum this technique?
So basically the goal is to create a model and then construct modeled “real-space image” of the sample as a model but it does far better and we can remove signals but utizling phase information that we want to acquire.

Q. Why not just observe he sampled directly?
It is limited by light and maxim resolution. Many oil the details are not visible via direct observation.

## Literature

> Electron ptychography of 2D materials to deep sub-ångström resolution (2018, Nature)
