# Autoencoders homework

Autoencoders homework consisted of several tasks devoted to the implementation and some pracitcal uses of autoencoders. Overall, two main approaches were used: fully-connected (__autoencoders_fc_out.ipynb__) and a convolutional one (__autoencoders_conv_out.ipynb__). The latter used a network architecture similar to the [UNET](https://arxiv.org/pdf/1505.04597.pdf) with transpose convolutions in the decoder part.

The tasks were mostly implemented on the ["Labeled Faces in the Wild" (LFW)](http://vis-www.cs.umass.edu/lfw/) images. Dataset download and processing code is located in __get_dataset.py__. For conditional VAE (CVAE) part, the MNIST dataset was used.

All the pretrained models can be found [here](https://drive.google.com/drive/folders/1Q7_QauAFNQJGl8OlM9pt5LAWSqFDr0RD?usp=sharing)

Some of the results of the homework are shown below (for full code and tasks, pls see notebooks):

## Image reconstruction
Basic example of image reconstruction using the convolutional autoencoder looks like this:
![ini](output/conv_vanilla/conv_example_0.png)
![reconstruction](output/conv_vanilla/conv_example_0.png)  
