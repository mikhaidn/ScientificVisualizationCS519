# 3D Computer Graphics for People in a Hurry
Visualization is to Graphics as Physics is to Math

## Rendering - How do you present a model?
* The same "model" can look different depending on how the application can "render an image"

* Modern GPUs are designed to render triangles

Rendering standards:
* Rasterization
    * Fast
    * Good for surface rendering
* Ray Tracing
    * highly detailed, captures shading
    * Good for volume visualization

## Rasterization - presenting information in "real time"
For each primitive (triangle)
* compute illumination
* project to image plane
* fill in pixels

**Pixel** - smallest controllable picture element in an image
**Raster** - grid of pixel values
**Rasterizaation** - The act of mapping a structure/shape of verticies and edges to a raster

### 3D Graphics pipeline
Vertex Processing -> Rasterization -> Fragment processing

Objects in a scene are usually represented with polygonal meshes
Done by GPU

Main Components of a GPU (there's more than just these steps in practice)
**NOTE** GPUs are highly parallelized, this is important to understand

* **Vertex Shader** -  coordinate transformations/ position calculation
    * Usually equivalent to a matrix transformation
    * Can also convert colors
    * **Changing Coordinate Systems**
        * Model Transformation - Move a model from isolated coordinate system to one in the "world"
        * Camera Transformation - Place camera at the origin and redefine the world based off of that 
        * Projection Transformation - Change coordinates so that 3D to 2D projection is done correctly (projection geometry 1/0 is valid - look it up)
        * Viewport Transformation - change from 2D corrdinates [-1,1] to pixel coorinates ( intX, intY )

* **Fragment Shader** - color/opacity calculation
    * Rasterizer fragments triagle primitives
    * Fragments are "potential pixels" with their own location, color, and depth attributes.
    * Vertex attributes are interpolated across fragments

## Shading
Deterrmining the color for a pizel during the rendering process

**TLDR on light** - Light hits a surface and scatters IRL
### Light source models
    * **Point source** - model with position and color
    * **Directional source** - source that is infinite distance away (parallel)
    * **Ambient light** - same amount of light everywhere. Models the contribution of many sources and reflecting surfaces

### Types of surfaces
    * smooth surface (mirror)
    * rough (paper)
### Reflection models
* **Phong reflection model** -8m in Shading section
    * 3 components of light -  ambient, diffuse, specular
    * 4 vectors - light source, normal, viewer, perfect reflection
* **Blinn-Phong** - uses halfway vector instead of perfect reflection (saves on computation)
(sometimes distance is calculated to dim lights over distance but not always)
### Shading models
* **Flat shading** - average normal @ each vertex, fill color for whole polygon
* **Gouraud Shading** - average normal @ each vertex, compute shade, interporlate vertex shades accross polygon
* **Phong Shading** - average normal @ each vertex, interpolate verex normals across edges, interpolate edge normals across polygon, compute shade at each fragment
## Rendering and Visualization
3D surfaces are modeled with triangle meshes
each triangle is projected to 2D
each triangle is rasterized into pixels
each pixel is shadded according to some model

### Performance
**TLDR** - Fewer triangles => faster rendering
**Projections and distortion
*** I.e. Mercator Projection - good for navigtion, bad for comparing relative sizes
* Perspecive Projectsion - objects appear smaller as the get further away
* Othrographic projection - objects has the same apparent size regardless of distance from the eye
    * Foreshortening can still occur (related to angels)
    * good for comparing relative sizes (engineering documents)
* Isometric Projection - Engineering diagrams ( x,y,z are 120deg away from each other on a 2d plane)

**Shading and Visualization**
* was non white light used?
* too much/too little ambient light?

**Hidden surface removal and Z-Fighting**
* each fragment/pixel has a z value (depth from camera)
* on overlap of fragments, keep only the smallest z value 
    * Bucketing and rounding errors can make this nondeterministic if not careful
