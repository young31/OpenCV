import cv2 as cv
import os
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', type=str, default="output/frame/", help="path to dataset")
    parser.add_argument('--output_path', type=str, default='output/video/sample.avi', help='output path to save')
    parser.add_argument('--width', type=int, help='img width to save/show', required=True)
    parser.add_argument('--height', type=int, help='img height to save/show', required=True)
    opt = parser.parse_args()

    size = (opt.width, opt.height)

    files = os.listdir(opt.img_path)
    idcs = list(map(lambda x: int(x.split('.')[-2]), files))

    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    writer = cv.VideoWriter(opt.output_path, fourcc, 25.0, size)

    for i in sorted(idcs):
        idx = idcs.index(i)

        frame = cv.imread(opt.img_path+files[idx])
        frame = cv.resize(frame, size)
        cv.imshow('img', frame)
        cv.waitKey(10)
        writer.write(frame)
