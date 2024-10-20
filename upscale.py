import pathlib
from video2x import Video2X

def process_video(input_file: str, output_file: str):
    algorithm = "realcugan"
    width = 0
    height = 720
    noise = 3
    processes = 2
    threshold = 0

    video2x = Video2X()
    video2x.upscale(
        pathlib.Path(input_file),
        pathlib.Path(output_file),
        width,
        height,
        noise,
        processes,
        threshold,
        algorithm,
    )

process_video('onepiece_demo.mp4','onepiece_demo_out.mp4')
