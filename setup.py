import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(name='configparsertool',
                 version='1.0.1',
                 author='bjtj',
                 author_email='bjtj10@gmail.com',
                 description='python configparser tool',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/bjtj/python-configparser-tool',
                 packages=setuptools.find_packages(),
                 classifiers=[
                     'Programming Language :: Python :: 3',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                 ],
)
