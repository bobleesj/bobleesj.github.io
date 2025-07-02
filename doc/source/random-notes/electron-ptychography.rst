Electron Ptychography
=====================

The goal is to reconstruct the transmission functions of a sample. The goal is to obtain phase and amplitude.

Why is it important to find the phase?
--------------------------------------

What's probe function?
----------------------

What's transmission function?
-----------------------------

The transmission function is the sample's effect on the probe function.


.. math::
    P(x,y) = Ae^{\frac{-x^2+y^2}{2\sigma^2}}e^{i\phi_p(x,y)}
    
Where :math:`A` is the amplitude and :math:`\sigma` is the beam width.

What's the PIE algorithm?
-------------------------

PIE stands for ptchogrpahic iterative engine. It is a phase retrieval algorithm that uses the probe function to reconstruct the transmission function of the sample. The algorithm iteratively refines the probe and sample functions until convergence is reached.

You model the exist wavefunctino is 

.. math::
    \psi(x,y) = P(x,y)T(x,y)
    
Where :math:`\psi` is the exit wavefunction, :math:`P` is the probe function, and :math:`T` is the transmission function.

Simulate the diffraciton pattern using Fouriter transform.

The electron's exit wavefunction encodes the information about the samples structure.

Using this wavefunction, you can reconstruct the transmission function of the sample.
