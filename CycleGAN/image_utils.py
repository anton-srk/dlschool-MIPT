#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:15:00 2020

@author: anton
"""

import os
import glob

import numpy as np
from PIL import Image
from tqdm import tqdm
from os import listdir
from keras.preprocessing.image import load_img, img_to_array

# Some of the following code was shamelessly borrowed from
# https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


def image_process(src_dir, dst_dir, crop_size):
    
    files = glob.glob(os.path.join(src_dir, '*.jpg'))
    
    for f in tqdm(files):
        im = Image.open(f)
        im_thumb = crop_max_square(im).resize((crop_size, crop_size),
                                              Image.LANCZOS)
        ftitle, fext = os.path.splitext(os.path.basename(f))
        im_thumb.save(os.path.join(dst_dir, ftitle + '_thumbnail' + fext),
                      quality=95)


def load_images(path, size=(256,256)):
  data_list = list()
  # enumerate filenames in directory, assume all are images
  for filename in listdir(path):
    # load and resize the image
    pixels = load_img(path + filename, target_size=size)
    # convert to numpy array
    pixels = img_to_array(pixels)
    # store
    data_list.append(pixels)
  return np.asarray(data_list)


def compress_img_dataset(path_a_0, path_a_1, path_b_0, path_b_1,
                         output_filename):
    
    data_a_0 = load_images(path_a_0)
    data_a_1 = load_images(path_a_1)
    data_a = np.vstack((data_a_0, data_a_1))
    print( "Loaded dataA:" , data_a.shape)
    data_b_0 = load_images(path_b_0)
    data_b_1 = load_images(path_b_1)
    data_b = np.vstack((data_b_0, data_b_1))
    print( "Loaded dataB:", data_b.shape)
    # save as compressed numpy array
    filename = output_filename
    np.savez_compressed(filename, data_a, data_b)
    print( "Saved dataset:" , filename)
    
    return None
