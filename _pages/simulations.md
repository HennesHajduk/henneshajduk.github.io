---
title: "Computational Results"
permalink: /simulations/
---

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

<!-- Row 1 (full width) -->
<div class="row">
  <figure style="max-width: 350px;">
    <video controls>
      <source src="/simulation-data/vst.mp4" type="video/mp4">
    </video>
    <figcaption>
      Shock tube problem for the compressible Navier-Stokes equations: Viscous boundary layers and reflecting boundaries influence the flow behavior. Click to watch video.
    </figcaption>
  </figure>

  <figure style="max-width: 350px;">
    <video controls>
      <source src="/simulation-data/bc_inst.mp4" type="video/mp4">
    </video>
    <figcaption>
      Breakup of unstable Rossby waves in a two-layer quasi-geostrophic model. 1024x1024 grid using a semi-spectral model with hyperviscosity stabilization. Click to watch video.
    </figcaption>
  </figure>
</div>

<!-- Row 2 (two snapshots) -->
<div class="row">
  <figure style="max-width: 350px;">
    <img src="/simulation-data/sbi.png" alt="Shock-bubble interaction">
    <figcaption>
      Snapshot of an artificial shock–bubble interaction setup for the compressible Euler equations 1024x1024 grid using a positivity-preserving discontinuous Galerkin method.
    </figcaption>
  </figure>

  <figure style="max-width: 350px;">
    <img src="/simulation-data/khi.png" alt="Kelvin–Helmholtz instability">
    <figcaption>
      Snapshot of a Kelvin–Helmholtz instability for the compressible Euler equations 1024x1024 grid using a positivity-preserving discontinuous Galerkin method.
    </figcaption>
  </figure>
</div>

<!-- Row 3 (full width) -->
<div class="row">
  <figure style="max-width: 800px;">
    <img src="/simulation-data/slope.png" alt="Critical slope">
    <figcaption>
      Ratio of topographic and critical slopes away from the equatorial region.
    </figcaption>
  </figure>
</div>
