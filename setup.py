from setuptools import setup, find_packages

setup(name='ofxhome',
      version="0.2",
      description="ofxhome.com financial institution lookup REST client",
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='ofx, Open Financial Exchange, bank search, ofxhome, ofxhome.com',
      author='David Bartle',
      author_email='captindave@gmail.com',
      url='https://github.com/captin411/ofxhome',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[ ],
      test_suite = 'tests',
      entry_points="""
      """,
      )
