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
    install_requires=["cryptography==35.0.0",
                      "passlib==1.7.4", "pycryptodome==3.11.0"],
    python_requires=">=3.6",
)
