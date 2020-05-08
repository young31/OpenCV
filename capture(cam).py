import cv2 as cv
import datetime
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', type=str, default='output/capture/', help='output path to save')
    parser.add_argument('--width', type=int, help='img width to save/show')
    parser.add_argument('--height', type=int, help='img height to save/show')
    opt = parser.parse_args()

    cap = cv.VideoCapture(0) # to use cam
    n_frame = cap.get(cv.CAP_PROP_FPS)

    height, width = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    if opt.height!=None:
        height = opt.height
    if opt.width!=None:
        width = opt.width
    size = (width, height)

    print(f'''############\nvideo info\nsize = {size}\nfps = {n_frame}\n############''')
    n_frame=0
    idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv.resize(frame, size)

        cv.imshow('cam', frame)

        key = cv.waitKey(10)
        if key & 0xFF == 27: # esc
            break
        elif key==32: #space
            fname = opt.output_path + datetime.datetime.now().strftime('%m%d%H%M%S') + '.jpg'
            cv.imwrite(fname, frame)

    cap.release()
    cv.destroyAllWindows()