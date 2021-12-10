from setuptools import setup, find_packages

VERSION = '1.0.1' 
DESCRIPTION = 'PyWapp : Automate sending messages and images for whatsapp'
LONG_DESCRIPTION = 'PyWapp : Automate sending messages and images for whatsapp'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pywapp", 
        version=VERSION,
        author="Md. Zarif Ul Alam",
        author_email="zarif98sjs@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['selenium'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'whatsapp'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)