---
title: "Visualizations"
permalink: /simulations/
---

This page presents a selection of visualizations from my research. While these simulations are certainly enjoyable to look at, they also showcase the numerical methods, software, and computational techniques developed throughout my work. They highlight challenging problems ranging from shock-dominated compressible flows to large-scale geophysical fluid dynamics, illustrating the scope of my research and the capabilities of the numerical methods I develop.

<style>
.row {
  display: flex;
  justify-content: center;
  gap: 25px;
  margin-top: 30px;
  flex-wrap: wrap;
}

figure {
  text-align: center;
  margin: 0;
}

figure img, figure video {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

figcaption {
  margin-top: 8px;
  font-size: 0.9em;
  color: #555;
}
</style>

<div class="row">
  <figure style="max-width: 800px;">
    <video controls poster="/simulation-data/vst.png">
      <source src="/simulation-data/vst.mp4" type="video/mp4">
    </video>
  <figcaption>
    <strong>Viscous shock tube (compressible Navier–Stokes equations).</strong>
    A benchmark problem illustrating the interaction of shocks, boundary layers, and reflecting walls. The simulation demonstrates stabilized continuous finite elements with nonlinear limiting for convection-dominated parabolic problems.
  </figcaption>
  </figure>
</div>

<div class="row">
  <figure style="max-width: 800px;">
    <video controls poster="/simulation-data/bc_inst.png">
      <source src="/simulation-data/bc_inst.mp4" type="video/mp4">
    </video>
    <figcaption>
      <strong>Baroclinic instability (two-layer quasi-geostrophic model).</strong>
      Evolution of unstable Rossby waves computed with a semi-spectral discretization. This example highlights numerical methods for large-scale geophysical fluid dynamics.
    </figcaption>
  </figure>
</div>

<div class="row">
  <figure style="max-width: 350px;">
    <video controls poster="/simulation-data/sbi.png">
      <source src="/simulation-data/sbi.mp4" type="video/mp4">
    </video>
    <figcaption>
      <strong>Shock–bubble interaction (compressible Euler equations).</strong>
      Interaction of a strong shock wave with a light-density bubble. The simulation demonstrates element-based limiting techniques for continuous finite element discretizations of compressible flows.
    </figcaption>
  </figure>

  <figure style="max-width: 350px;">
    <video controls poster="/simulation-data/khi.png">
      <source src="/simulation-data/khi.mp4" type="video/mp4">
    </video>
    <figcaption>
      <strong>Kelvin–Helmholtz instability (compressible Euler equations).</strong>
      Formation of vortical structures driven by velocity shear. This example showcases discontinuous Galerkin discretizations together with nonlinear limiting for both volume and interface contributions.
    </figcaption>
  </figure>
</div>

<div class="row">
  <figure style="max-width: 800px;">
    <img src="/simulation-data/slope.png" alt="Critical slope">
    <figcaption>
      <strong>Global ocean diagnostics.</strong>
      Visualization of the ratio between topographic and critical slopes derived from observational ocean data. This example illustrates scientific data processing, large-scale visualization, and the analysis of geophysical data sets.
    </figcaption>
  </figure>
</div>
