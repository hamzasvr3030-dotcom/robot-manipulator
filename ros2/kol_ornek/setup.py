from glob import glob
from setuptools import setup

paket = "kol_ornek"
setup(
    name=paket,
    version="0.1.0",
    packages=[paket],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + paket]),
        ("share/" + paket, ["package.xml"]),
        ("share/" + paket + "/launch", glob("launch/*.launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Robot kol ekibi",
    description="O5 alıştırması: yayıncı/abone ve launch dosyası",
    license="MIT",
    entry_points={
        "console_scripts": [
            "yayinci = kol_ornek.yayinci:main",
            "abone = kol_ornek.abone:main",
        ],
    },
)