# Scalar Field Visualization
A Scalar Fields assigns a scalar to every point in a given space
For a 2D space, a scalar field is often just represented with color (and a 2d array)
**Pseudo-coloring** - coloring to denote continuous data
    * **chloropleth** the map of value to color

Two mapping options
* color table - discrete
* transfer function - continuous

## Designing a colormap
* Find valMin and valMax
* create an interpolation between two (or more colors)
    * linear
    * Don't forget gamma values for grayscale perception
* normalize and compute

* Don't use the rainbow for linear change (look up perceptually linear color map)
* EG:
    * Kindlmann Colormap
    * Black Body Colormap

**Diverging colormaps** 
Good for dilineate + and - as well as magnitude
Blue - white - Red

Colormaps for 3D surfaces
* Viridis and Cividis (optimized)

Keyed lookup tasks - getting the user to estimate data values from the chart
* color can help
* contour lines help too

Tips:
* Prefer interpolating values over interpolating colors
    * color interpolation can fall outside the colormap!
* Design for accessibility (no red green)
* Use your knowledge to your advantage
* Stick with a standard if this exists (over an optimal visualization)
* Prefer changes are lightness over changes in hue when possible