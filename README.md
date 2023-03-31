# The V Model under the unifie Master equation

We will first consider a simple implementation of the V model with a jump unravelling for a single bath. We will consider the model that is explicity studied in 

https://arxiv.org/pdf/2212.11307.pdf

The Hamiltonian of this model is a 3 level system given by 
\begin{equation}
    H = (\nu - \Delta)\ket{2}\bra{2} + \nu \ket{3}\bra{3}\,,
\end{equation}
where $\nu$ is the energy level and $\Delta$ parameterises the degeneracy between the two levels. 
There are two extreme limits in this model; the first corresponding to the Unified master equation which occurs when $\Delta$ is very small, and the the Secular approximation when $\Delta$ is larger. 

In the former case we will have two dissipators acting on the system coupled to the Left reservoir

$$
L_{-} = \gamma(\nu)(\ket{1}\bra{2} + \ket{1}\bra{3}) \quad \text{and} \quad L_{+} = \gamma(-\nu)(\ket{2}\bra{1} + \ket{3}\bra{1})\,,
$$

where $\gamma(\omega) = \mathcal{J}(\omega)[n(\omega)+1]$ and $\gamma(-\omega) =  \mathcal{J}(\omega)n(\omega)$ are the dissipation rates of the downward and upward channels respectively, $\mathcal{J}(\omega)= a \omega$ is a Ohmic spectral density, and $n(\omega ) = (e^{\beta \omega} - 1)^{-1}$ is the Bose-Einstein distribution. 
We will further have the two dissipators coupling to the Right reservoir given by 
$$R_{-} = \gamma(\nu)(\ket{1}\bra{2} + \alpha \ket{1}\bra{3}) \quad \text{and} \quad R_{+} = \gamma(-\nu)(\ket{2}\bra{1} + \alpha \ket{3}\bra{1})\,,$$
Under the Unified master equation (Eq. 10 in the paper) these clustered noise operators can be rewritten in the Schrodinger picture using a slight change of basis in the following form

$$
\frac{d \rho}{dt} = -i[H, \rho] + \mathcal{D}[L_{-}]\rho + \mathcal{D}[L_{+}]\rho +  \mathcal{D}[R_{-}]\rho + \mathcal{D}[R_{+}]\rho \,.
$$

Given that we have this in Lindblad form, we can easily write this as an unravelled master equation for quantum jumps, where we associate a jump with either $L_{-}$ or $L_{+}$. It is important to note that these jumps do not distinguish which transition the jump came from i.e ($\ket{1}\bra{2}$ or $\ket{1}\bra{3}$) thus erasing any 'which way' information.

The Secular approximation is valid when the energy difference between the two levels $\Delta$ is large. This ensures that there is now a clear distinction between the energy levels creating which way information. As such the each of the dissipators is split up into seperate dissipators and we obtain

$$
L_{2-} = \gamma(\nu - \Delta)\ket{1}\bra{2}\,, \quad L_{3-} = \gamma(\nu) \ket{1}\bra{3} \quad \text{and} \quad L_{2+} = \gamma(\Delta-\nu)\ket{2}\bra{1} \quad L_{3+} = \gamma(-\nu) \ket{3}\bra{1}\,,
$$

and likewise for the $R$ operators. Therefore under the Secular approximation, there is a clear distinction between the energy levels and which way information is preserved. As such, each of the $L$ operators and $R$ operators can be split into separate dissipators, resulting in a total of four noise operators for the system coupled to each reservoir.
