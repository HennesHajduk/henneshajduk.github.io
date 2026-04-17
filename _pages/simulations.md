---
title: "Computational Results"
permalink: /simulations/
---

Below you can find snapshots and videos produced by some of my numerical simulations.

This site is still under development. More information and numerical results will follow soon.

<style>
.sim-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
  margin-top: 30px;
}

.sim-grid figure {
  margin: 0;
  text-align: center;
}

.sim-grid img, .sim-grid video {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.sim-grid figcaption {
  margin-top: 8px;
  font-size: 0.9em;
  color: #555;
}
</style>

<div class="sim-grid">

  <figure>
    <a href="/simulation-data/bc_inst.mp4">
      <img src="/simulation-data/bi-init.png" alt="Baroclinic instability">
    </a>
    <figcaption>
      Breakup of unstable Rossby waves in a two-layer quasi-geostrophic model. 1024x1024 grid using a semi-spectral model with hyperviscosity stabilization. Click to watch video.
    </figcaption>
  </figure>

  <figure>
    <img src="/simulation-data/sbi.png" alt="Shock-bubble interaction">
    <figcaption>
      Snapshot of an artificial shock–bubble interaction setup for the compressible Euler equations 1024x1024 grid using a positivity-preserving discontinuous Galerkin method.
    </figcaption>
  </figure>

  <figure>
    <img src="/simulation-data/khi.png" alt="Kelvin–Helmholtz instability">
    <figcaption>
      Snapshot of a Kelvin–Helmholtz instability for the compressible Euler equations 1024x1024 grid using a positivity-preserving discontinuous Galerkin method.
    </figcaption>
  </figure>

</div>

<!-- Wide figures -->
<div style="margin-top:40px;">

  <figure style="text-align:center;">
    <img src="/simulation-data/slope.png" alt="Critical slope" style="max-width:80%;">
    <figcaption>
      Ratio of topographic and critical slopes away from the equatorial region.
    </figcaption>
  </figure>

</div>
