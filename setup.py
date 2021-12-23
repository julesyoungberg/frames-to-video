from setuptools import find_packages, setup

setup(
    name="frames-to-video",
    version="0.1.0",
    packages=find_packages(
        include=["frames-to-video", "frames_to_video.*"]),
    entry_points={
        "console_scripts": [
            "frames-to-video = frames_to_video.main:run",
        ],
    },
    install_requires=["opencv-python"],
    python_requires=">=3.6",
)
