---
title: "Research"
permalink: /research/
---

My research focuses on finite element methods, in particular high-order approximations and discontinuous Galerkin (DG) discretizations. Building on these approaches, I develop nonlinear stabilization techniques that adaptively introduce numerical viscosity where needed.

These methods are applied to problems in geophysical fluid dynamics. While low-order, structure-preserving schemes ensure that key qualitative properties of the exact solution are retained at the discrete level, high-order methods provide superior accuracy in smooth regions. In my work, these paradigms are combined through limiting procedures that yield optimal accuracy in smooth regions while providing the necessary stabilization near strong gradients.

Some highlights of my research in this direction include limiting schemes for DG methods, applications to geophysical flow problems, and the combination of neural networks with limiters for continuous finite elements. Furthermore, I have worked on stabilization techniques based on weighted essentially non-oscillatory (WENO) schemes, residual distribution methods (in collaboration with colleagues at Lawrence Livermore National Laboratory, California), and enriched Galerkin methods, among others.

For more details, please check out my [publications](/publications/).

My team and I use the C++ [MFEM finite element library](https://mfem.org) in our daily work and highly recommend this software to anyone working in a similar field.
