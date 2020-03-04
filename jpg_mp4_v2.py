
# coding: utf-8

## Ensure files abide by a filename pattern, in this case "img-%05d.jpg"
## This will mean filenames should be "img-00001", "img-00002", etc.

## To do this in UI, highlight files, Settings->Rename "x" Items, use dropdown 
## bar to "Format", "Name Format" bar to "Name and Counter", "custom Format" to "img-"
## Set "Where" to "after name" and "Start numbers at:" to "1"
## Then hit "Rename"

## Navigate to directory in terminal where images and script are stored
## `jpg_mp4_v2.py`

get_ipython().system('pip install ffmpeg')
get_ipython().system('pip install ffmpy')

import os
from os import path
import ffmpeg
import ffmpy
import subprocess

def get_codecs():
    cmd = "ffmpeg -codecs"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)


def get_formats():
    cmd = "ffmpeg -formats"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)

def convert_seq_to_mov():
    input = 'images_rando1/img-%05d.jpg'
    output = 'output9.mp4'
    frame_rate = 5
    cmd = f'ffmpeg -framerate {frame_rate} -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)
    
convert_seq_to_mov()






