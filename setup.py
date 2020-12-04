import setuptools

setuptools.setup(
    name='controllermodel',
    version='0.1',
    description='A simple controller-model implementation.',
    url='',
    author='Aadam Zocolo',
    author_email='azocolo@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False)