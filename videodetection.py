import matplotlib.pyplot as plt
import numpy as np
import mxnet as mx
from mxnet import gluon, nd, image
from mxnet.gluon.data.vision import transforms
from gluoncv.data.transforms import video
from gluoncv import utils
from gluoncv.model_zoo import get_model
from gluoncv import data
import gluoncv
from gluoncv.data import mscoco
from gluoncv.model_zoo import get_model
from gluoncv.data.transforms.pose import detector_to_simple_pose, heatmap_to_coord
from gluoncv.utils.viz import cv_plot_image, cv_plot_keypoints
from main import VideoDecord
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required = True, help = "path to where the image file resides")
args = vars(ap.parse_args())
vr = VideoDecord(args["video"])
ci = vr.detect()
model_name = 'slowfast_4x16_resnet50_kinetics400'
net = get_model(model_name, nclass=400, pretrained=True)
print('%s model is successfully loaded.' % model_name)
pred = net(nd.array(ci))
allval=[]
classes = net.classes
topK = 5
ind = nd.topk(pred, k=topK)[0].astype('int')
print('The input video clip is classified to be')
for i in range(topK):
    val=(classes[ind[i].asscalar()], nd.softmax(pred)[0][ind[i]].asscalar())
    allval.append(val)
print(allval[0][0])



