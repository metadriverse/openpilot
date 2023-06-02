from tools.streamer.tasks import Camerad, NavCamerad
import struct
import numpy as np
import zmq
import cv2
from selfdrive.test.helpers import set_params_enabled
from common.params import Params
#import cereal.messaging as messaging

def nav_streamer():
  set_params_enabled()
  nav_H, nav_W = 256, 256
  _nav_camerad = NavCamerad(nav_H, nav_W)
  while True:
    img = cv2.imread("/home/liuzhi/moretore/openpilot/nu_scene_test.png", cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (nav_H, nav_W), interpolation = cv2.INTER_AREA)
    _nav_camerad.cam_callback_nav(img)
    #cv2.imshow('wide_img', wide_img)
    #cv2.imshow("cropped", cropped_img)
    #cv2.imshow('road_img', road_img)
    #cv2.waitKey(1)


def main():
  nav_streamer()

if __name__ == "__main__":
  main()