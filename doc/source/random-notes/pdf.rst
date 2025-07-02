Notes
=====

Disclaimer: Some may be inaccurate. They are used for my understanding.

Quantum particles
-----------------

Erwin Schrodinger 양자 세계를 파동으로 기술하는 방정식.

Werner Heisenberg 양자 세계를 입자로 기술하는 방정식.


If you had two slits, if the wave behaved like a particle like a bullet, then we'd see only two bands. 

But when a light passes through two slits, we pattern of light and dark bands on the screen instead. It's like droping two pebbles in a pond where the two waves overlap and create a unique pattern of new waves.

The bright and dark bands represnt the constructive and destructive interference of light waves.

In the early 20th century, Albert Einstein light behaves like a series of particles.

When a beam of light hits a metal surface, it can eject electrons from the surface. If the same color is used, even if the light is extremely bright, more electrosn were ejected but the same energy.

This is where it get extremely crazy. BUT! When scientists placed a measuring device before passing through the slit that the each photon passes through, the interference pattern disappered. It changed the behavior of the photons!!!

뉴턴은 우리가 양자역학을 이해하지 못하는 것처럼 중력을 이해하지 못했다. 
슐로딩어는 Quantum leap에 무슨일이 일어나는지 고민했다.
Copenhagen Interpretation - We can just see what we observe whether we try to define something or not is irrelevant.
파동함수가 하나의 점으로 '붕괴'하는데 확률로 나타난다. 고양이가 살아있을 수도, 죽어 있을 수도 있다. 살아있는지 죽었는지 하나로 결과값으로 '붕괴'되는 것은 상자를 열어보았을 때만 알 수 있다.

모든 입자는 항상 명확한 속성을 가지고 잇다. 카드처럼 말이다. 우리가 카드를 보지 않으면 그 카드를 알 수 없다.


What is BZ (The Brillouin zone)

    It is considered a "primitive cell" in reciprocal space. The rest is a translation of the BZ.

    Hence, BZ describes the possible wavevectors (k) that describe the motion of electrons in the periodic lattice.

What is a typical unit for a k-point?

    1/Angstrom (or Å⁻¹). It makes sense becuase the reciprocal space is the inverse of real space.

    A sound wave that the ear detects, in principle can be broken down into multiple waves of differnt phases. The way is to do it is using Fouirer transform where the unit is in frequencies (s⁻¹) using Fourier transform.

Why find the probaibility of finding the distance between two atoms?

    In a non-crystalline material, there is no longer a repeated atomic pattern defined by space group symmetry or translations. Therefore, it becomes important to use a statistical approach to better understand the overall structure of the material for humans. PDF serves this role.

What does PDF capture?

    It captures the short-range order.

How do you collect Bragg and diffuse scattering data differently?

It requires high-energy X-rays Q-range, usually > 50 keV.

Synchrotron

    Particles don't travel in a straight line then it produces x-ray radiation?

    Rotate electrons, wigglers and undulators? Electrons are wiggleds with magnetic fields circualting. The endulators emit x-ray radiation.

What's total scattering?

    Get diffraction over a wide range of momentum transfer.

The beam penetrates the sample. The sample is rotated to reduce the preferred orientation effects. 

Each image is exposed for a few seconds. If it is spinning, a single image averages over all orientations during that expore.

:math:`F(Q) = Q[S(Q) -1]`

where S(Q) is the total scattering.

X-ray captures the shadow of the bones. i

PDF

    Raw data, S(Q), then PDF G(r)

Solve macromolecular structure. 

What's the workflow?

    Colelct high-energy total scattering data at a synchrotron. Then reduce from 2D to 1, then get S(Q). Use Fourier transform to get G(r).

With PDF, how can you do with it?

    You can use PDF to reverse engineer the structure of a material.

The beam interactves with millions to millions of nanoparticles. The x-ray beam is like  wave rolling onto a beach. The wave doens't cover the entire beach but it engults a patch.

Why do we use reciprocal space?

    X-ray, neutron diffraction, electron diffraction, these are collected in reciprocal space (scattering data).
    
    Then it is transformed into real space.

Why do diffraction provide data in diffraction space?

    Detectors measure the angles and intensities of scattered waves.

    Reciprocal space is how certain spacings occurs 

    We don't see atoms directly. We only indirectly measure how waves bounce off them.
    
    The detector measures the angles of the bounced waves and the intensity.

What is "beam size"?

    The phyiscal cross-sectional area of the x-ray beam where it hits the sample.
    
Is the X-ray beam coherent?

    Lab-based X-ray tubes produce partially coherent x-rays. Synchrotron X-ras are highly coherent.in

Imagine a 2D plane, 3 by 3 atom sqaure. Horizontal spacing, vertical spacing maybe 2 Å but the diagonal spacing 2.83 Å and these are all picked up by the defector.

In 3D, there is interlayer spacings, 

Tossing a wave across a pond with pebbles. 

The wave hits a chunf of material. 

Here is how you :math:`n\lambda = 2d\sin\theta`

.. math::

   n\lambda = 2\sin\theta

TEM
---

How do you turn diffraciton data into a real space image?

    An inverse Fourifer transform is used. But the Fourier transformer phase information must be 
    retriverdf or approximated?

The incident is converged. It is usually 1 atom wide beam.

BF: Bright field 
ABF: Annular bright field
ADF: Annular dark field
HAADF: High angle annular dark field

Why is it knowing the phase retrival important?



The elctron wavelenght is aabout 0.02508 Å⁻¹ 

X-ray diffraction
-----------------

1912 - x-ray diffraciton laws, Bragg won the Nobel Prize in 1914
1986 was the first synchotron PDF emasurement Egami at Brookhaven

.. math:: 
    
    Q= \frac{4\pi}{\lambda} sin(\theta)

Longer wavelneght tend to penetrate deeper intot he sample because it has lower photon energy so it interactves less with the electrons in the atom.

Q. Why use schrotron beam?

    - High flux of photons
    - Coherent beam
    - Tune x-ray wavelneght

Visible light has 500 nm of wavelength.

Ptychography was invented and uses the interpreference of diffraction patternes to reconstruct the image of the sample. In 2021 0.5 amstroms to 0.2 amstroms by Muller at Cornell.

Multi-slice pytchography was developed by 2021 in the x-ray communit but the normal algorithm didn't work well for electrons due to much greater interactions. So "regularization" was introduced like including more layers due to multiple scattering.

How does TEM work?
- An electron beam is accelerated to 70% of the speed of light (210,000 km/s).
- The elctronmagnetic lenses focus, electrons scatter, then magnifieid by objetive and projected lenses, than 5 cm image is then detected by detectors.
- The wavelenght of an electron is 2.5 picometers.

What does ptychography attempt to find?

- Use the overalling regions to solve for the phase of the existing electron wave?

Why is finding the existing electron wave important?

What's a virtual detector?


What's the benefit of using a defocused probe?

- It increase the beam size so fwer scan positions are needed, lwoeirng the data acqusition and phase retrival time.

What is the working definition of a probe?

A probe refers to the collective electrons as a single wave function.

How can you desribe a probe as a single wavefunction?

- The assumption is coherence. The electonrs in the probe share a conssitent phase relationship. 

When we say "think" how thick isare we talking about?

- 50 namometers.

What's considered "low" dose in electron microscopy?

Why is theory ptschogrpyh is unaffected by lens aberrations?

Colin

- 256 x 256 probe positions. 
- 1920 x 1792 image pixels
- 225 billion pixels (420 GB) in 3 minutes.

Remaining questions

- Why did the 2018 paper use defocuse probe iterative ptychography?
- How does aperture work?
- What are the form-factors?
- What does aberration-correctecd mean?


.. plot::

  import matplotlib.pyplot as plt
  plt.plot([1, 2, 3], [4, 5, 6])
  plt.title("A plotting example")

Plot 1 import

.. plot:: plots/plot_one.py

  The plot caption.