# Spike-Classifier

### Introduction
When the Hubble Space Telescope take an image of space, it does so at a specific angle that telescope is currently positioned. When the telescope returns to take a picture, or if it uses a different camera, that picutre might be at a different angle. Usually this doesn't matter-- you can focus your science on the area that has overlapping coverage and make fantastic colorful images. But the different roll angles can also cause us issues in the form of "diffraction spikes". 

### What are diffraction spikes?
Diffraction spikes beautiful, but completely artificial. When the light of a star or object is bright enough, like for a star, light diffracted off the support beams holding up the secondary mirror will fall onto the detector, creating "spikes" in the image. These spikes are annoying artifacts in images that can be confused with other, real astronomical sources. Moreover, the different roll angles of Hubble can make it non-trivial to identify the spikes compared to very distant galaxies. 

### Solving with Machine Learning
In the following notebooks, I try two approaches to identift artifacts in the catalogs of image sources. 

1. **Classic Machine Learning:** Apply decision tree and random forests to the full catalog data. It's possible that the computer can find a hidden set of relations within the catalog that will allow it to correctly determine spikes vs galaxies. 
2. **Neural Network:** Use a neural net on the actual images themselves. This is the slower, more complex approach that I would take if the machine learning way fails. We will use the actual astronomical images to build a convolutional neural net capable of making the spike/galaxy judgement. 
