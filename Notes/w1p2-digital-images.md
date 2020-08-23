# Digital Images
## (Display-Derived Color Spaces)

Creating a digital image is a fundamental task in viz. Most modern digital displacys rely on a *raster* of *pixels*.

a *raster* is a grid of pixels
A *pixel* is the smallest controllable element of a digital image (Like the atom, before subatomic particles were discovered) 

Types of Displays
* LCD
* OLED

Device derived color space (RGB values)
RGB are **primaries**
The color of a pixel is specefied by a tuple of the values (R,G,B). Each value is referred to as a color channel and the value of the channel is the intensity from [0-1]

Sometimes there is a 4th channel, A, *alpha* is used for opacity

operations are linear combinations of all the forms of the space of all the colors

## Representing Intensity
24 bit color (even if it's a 32 bit storage for "intensity")
8-bit unsigned ints for each color channel
0-255 (0x00,0xFF)
|Byte 0|Byte 1|Byte 2|Byte 3|
|---|---|---|---|---|
|Red|Green|Blue|Alpha|

256 "luminence values" is too few to appear continuous to the human eye so some implementations will use more than 8 bits per channel. (open exr is 16 bit)

At application level, use 32 bits to avoid quantization

**Quantization** - Reduces precision to store values into a data structure. (approximate 100123 to 100000)

### PNG Format
/fill in later 6:03 in Week2 Representing identity
One of the best ones to use, minimizes loss

### Implications for Visualization
* no guarantee that viewers see what is computed
    * quantization or display differences
* Ensure that users can query for the original numerical value

### HSV Color Space
Picking color from RGB is tough to use as an artist
Navigates a color cone (look up color cone)
~3:00 in this section
**Hue** - [0-360]
**saturation**
**Value**
Conversion is easy (programmabble):
RGB -> HSV
S = (maxRGB - minRGB)/maxRGB
V = maxRGB
H =: # look it up
     # in short, start at RGB angle of maxRGB, divide the difference of the other color channels by the delta between max and min. Add {0,2,4} for maxRGB={R,G,B} respectively. Multiply by 60, mod by 360

HSV -> RGB look it up

### Primary Colors
Any set of wavelengths can serve as primaries, but no three wavelengths can produce all the colors a person can see

