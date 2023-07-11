# Iris Scan
## Made with Django Python

## Reuirements for Image Processing
* scikit-image - http://scikit-image.org/

### ORB feature detector and binary descriptor
Unlike BRIEF, ORB is comparatively scale and rotation invariant while still employing the very efficient Hamming distance metric for matching. 
As such, it is preferred for real-time applications.
> http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_orb.html

Displays/Returns similarity match in percentage %
* Extract ORB Features and Compare the ORB Descriptors, Calulate the similarity index.
