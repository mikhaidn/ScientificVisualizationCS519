# Perceptually-Defined Color Spaces
## Perceptual Color Spaces
### Most important fact
Color is percepted, it is not a physical property of light or a material

High wavelength is percepted as red
Low is percepted as magenta

Three cone cells, L (~yellow) M (~green) S (~blue)
Rods give more information, they provide details on intensity

We can determine which wavelength we'd percieve as the "brightest" given the same luminosity

### Human visual system

Light is a mix of wavelengths
**metamers** Different light distributions that can produce the same stimulus

The RGB basis vectors don't map to the LMS cones in our eyes. We can make a basis out of that concept, however.

### CIE RGB colorspace
* French abbreviation
* defined in 1931 by the international commission on Illumination

Primary wavelengths are as follows:
* 435.8 nm
* 546.1 nm
* 700 nm

### Color Matching Experiments -13 minutes
* confusing go back

### CIE xy Chromaticity Diagram ~19:45
* Diagram of all colors visible to average human
* Curved boundary is the spectral locus 
    * one wavelength "rides" accross it.
    * Points not on the curved boundary are a mixture of multiple wavelengths
* Standard sRGB color space is defined by three points R G B.
   * set of all producible colors in a space is the **gamut**
### Standard Illuminants
* Perfectly white light occurs at (1/3,1/3) on the Chromaticity Diagram
* This is called Standard Illuminant E
* Illuminant D65 - a precise approximation of sunlight "white"

## The sRGB Color Space
(xr,yr)(xg,yg)(xb,yb)
white = D65

Requirements:
* Sum of primaries to D65 with y65 =1 

### Convert from XYZ to sRGB 3:48

### gamma correction -brightness conversion  5 m
gamma=2.2 usually
Gamma correction has to do with brightness
make sure that the pixels you're computing have "undid" the gamma correction befor processing