#!/bin/bash
libcamera-vid -t 0 --inline --vflip=1 --hflip=1 --width 640 --height 360 --framerate 20 -o - | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264




