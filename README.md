# Semantic Segmentation
### Introduction
In this project, I label the pixels of a road in images using a Fully Convolutional Network (FCN).

### Setup
##### Frameworks and Packages
I used the community ami `udacity-carnd-advanced-deep-learning - ami-3e6c7547`, update of all packages and h\
ad to re-install `tensorflow-gpu`.
I had to add the package `tqdm`.

The one problem I had was that the first virtial machine I used was one with the K520 processor. This had to\
 little memory so I had to switch to a machine with a tesla k80 processor.

##### Dataset
I downloaded the [Kitti Road dataset](http://www.cvlibs.net/datasets/kitti/eval_road.php).

### Implementation
I saw the project walkthrough video with Aaron and Brok, and my implementations follow the template provided\
 in the video.

All my code is in the `main.py` file indicated by the "TODO" comments.
I did not do the "OPTIONAL" tasks.

I ended out with 60 Epochs and a batch size of 32.

