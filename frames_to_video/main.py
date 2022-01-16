# based on: https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481
import argparse
import os
from os.path import abspath, isfile, join

import cv2


def run():
    parser = argparse.ArgumentParser(
        description="Converts a directory of frames to a video."
    )
    parser.add_argument(
        "path", metavar="path", type=str, help="The path to the frames directory."
    )
    parser.add_argument(
        "--outpath",
        dest="outpath",
        nargs=1,
        type=str,
        default=".",
        help="The path to the directory where the video should be saved.",
    )
    parser.add_argument(
        "--fps",
        dest="fps",
        nargs=1,
        default=30.0,
        type=float,
        help="The frames per second to use.",
    )

    args = parser.parse_args()

    path_in = abspath(args.path)
    print(f"Reading frames from directory: {path_in}")
    path_out = abspath(args.outpath) + "/video.mp4"
    print(f"Saving video to: {path_out}")

    fps = args.fps
    print(f"Using FPS: {fps}")

    frame_array = []
    files = [f for f in os.listdir(path_in) if isfile(join(path_in, f))]

    # for sorting the file names properly
    files.sort(key=lambda x: int(x[:-4]))

    for i in range(len(files)):
        filename = path_in + "/" + files[i]
        # reading each files
        img = cv2.imread(filename)
        try:
            height, width, _ = img.shape
            size = (width, height)

            # inserting the frames into an image array
            frame_array.append(img)
        except:
            break

    out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*"MP4V"), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])

    out.release()

    print("done")
