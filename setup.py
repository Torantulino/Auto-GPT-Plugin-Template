from setuptools import setup, find_packages

setup(
    name='your_plugin_name',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',  # Add any other dependencies your plugin needs
    ],
    entry_points={
        'auto_gpt_plugins': [
            'your_plugin_name = auto_gpt_plugin_template.your_plugin_module:MaterialsProjectPlugin',
        ],
    },
    description='A plugin for AutoGPT to interact with the Materials Project API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/your_plugin_name',  # Update with your repository URL
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
