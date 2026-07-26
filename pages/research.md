---
title: "Research"
permalink: /research/
---

My research focuses on finite element methods, in particular high-order approximations using continuous and discontinuous Galerkin (DG) discretizations. Building on these approaches, I develop nonlinear stabilization techniques that adaptively introduce numerical viscosity where needed while maintaining high accuracy elsewhere.

These methods are primarily applied to problems in geophysical fluid dynamics. While low-order, structure-preserving schemes ensure that key qualitative properties of the exact solution are retained at the discrete level, high-order methods provide superior accuracy in smooth regions. My research combines these complementary paradigms through limiting procedures that achieve optimal accuracy in smooth regions while providing robust stabilization near strong gradients.

My current research directions include limiting schemes for DG methods, applications to geophysical flow problems, and the integration of neural networks into limiter design for continuous finite element methods. In addition, I have worked on stabilization techniques based on weighted essentially non-oscillatory (WENO) schemes, residual distribution methods (in collaboration with colleagues at Lawrence Livermore National Laboratory, California), enriched Galerkin methods, and related approaches.

For more details, please explore my [publications](/publications/).

My team and I use the C++ [MFEM finite element library](https://mfem.org) extensively in our research for the development and implementation of new numerical methods. We highly recommend MFEM to researchers working in finite element methods and scientific computing.
