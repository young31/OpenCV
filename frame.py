import cv2 as cv
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, default="sample/demo1.mp4", help="path to dataset")
    parser.add_argument('--output_path', type=str, default='output/frame/', help='output path to save')
    parser.add_argument('--sec', '-s', type=float, default=1, help='sec to divide video')
    parser.add_argument('--width', type=int, help='img width to save/show')
    parser.add_argument('--height', type=int, help='img height to save/show')
    opt = parser.parse_args()

    cap = cv.VideoCapture(opt.video_path)
    n_frame = cap.get(cv.CAP_PROP_FPS)
    cut_frame = int(n_frame*opt.sec)
    print(cut_frame)

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
        frame = cv.resize(frame, size)

        if save_frame == cut_frame:
            cv.imwrite(f'{opt.output_path}{idx}.png', frame)
            save_frame=0
            idx += 1

        save_frame += 1

        cv.imshow('cam', frame)

        key = cv.waitKey(10)
        if key & 0xFF == 27: # esc
            break

    cap.release()
    cv.destroyAllWindows()