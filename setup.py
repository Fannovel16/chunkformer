from setuptools import setup, find_packages

setup(
    name='chunkformer',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'regex',
        'Pillow',
        'pyyaml',
        'sentencepiece',
        'textgrid',
        'pandas',
        'jiwer',
        'huggingface_hub',
        'colorama',
        'pydub'
    ],
    python_requires='>=3.7',
    author='khanld',
    author_email='',
    description='ChunkFormer: Masked Chunking Conformer For Long-Form Speech Transcription',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/khanld/chunkformer',
    license='Apache 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)