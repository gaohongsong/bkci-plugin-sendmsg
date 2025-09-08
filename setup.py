# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

BASE_DIR = os.path.realpath(os.path.dirname(__file__))


def parse_requirements():
    """
    @summary: 获取依赖
    """
    reqs = []
    if os.path.isfile(os.path.join(BASE_DIR, "requirements.txt")):
        with open(os.path.join(BASE_DIR, "requirements.txt"), "r") as fd:
            for line in fd.readlines():
                line = line.strip()
                if line:
                    reqs.append(line)
    return reqs


if __name__ == "__main__":
    setup(
        version="7.0.0",
        name="sendmsg",
        description="",
        cmdclass={},
        packages=find_packages(),
        package_data={"": ["*.txt", "*.TXT", "*.JS", "test/*"]},
        install_requires=parse_requirements(),
        entry_points={"console_scripts": ["sendmsg = sendmsg.command_line:main"]},
        author="ghs1",
        author_email="ghs1@meitu.com",
        license="Copyright(c)2025-2035 ghs1 All Rights Reserved.",
    )
