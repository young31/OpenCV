import cv2 as cv
import glob
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, default="./video/", help="path to dataset")
    parser.add_argument('--output_path', type=str, default='output/', help='output path to save')
    parser.add_argument('--sec', '-s', type=float, default=10, help='sec to divide video')
    parser.add_argument('--width', type=int, help='img width to save/show')
    parser.add_argument('--height', type=int, help='img height to save/show')
    parser.add_argument('--verbose', type=int, default=0, help='whether see video or not')
    opt = parser.parse_args()

    files = glob.glob(opt.video_path+'*.mp4')
    for file in files:
        _, fname = file.split('\\')
        fname = fname[:-4]
        cap = cv.VideoCapture(file)
        n_frame = cap.get(cv.CAP_PROP_FPS)
        cut_frame = int(n_frame*opt.sec)

        height, width = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        if opt.height!=None:
            height = opt.height
        if opt.width!=None:
            width = opt.width
        size = (width, height)

        print(f'''############\nvideo info\nsize = {size}\nfps = {n_frame}\n############''')
        save_frame=0
        idx = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if frame is None:
                break
            frame = cv.resize(frame, size)
            # print(frame.shape)

            if save_frame == cut_frame:
                cv.imwrite(f'{opt.output_path}{fname}_{idx}.jpg', frame)
                save_frame=0
                idx += 1

            save_frame += 1

            if opt.verbose==1:
                cv.imshow('cam', frame)

            key = cv.waitKey(1)
            if key & 0xFF == 27: # esc
                break

        cap.release()
        cv.destroyAllWindows()
