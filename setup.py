from setuptools import setup, find_packages
from pathlib import Path

# La descripción larga va a ser el mismo fichero README.md
long_desc = Path("README.md").read_text()

# Datos del paquete
setup(
    name="outputstyles",
    version="0.1.2",
    author="Duniesky Salazar Pérez",
    author_email="<duniesky.salazar@gmail.com>",
    description="Applying styles to CLI output",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/dunieskysp/output_styles',
    packages=find_packages(),
    keywords=['python', 'output styles'],
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
    ]

)
