import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(name='pyramid_jinja2_alchemy',
      version='0.3',
      author='Andrew Kou',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points = """\
        [pyramid.scaffold]
        jinja2_alchemy=pyramid_jinja2_alchemy.scaffolds:Jinja2AlchemyProjectTemplate
      """
     )
