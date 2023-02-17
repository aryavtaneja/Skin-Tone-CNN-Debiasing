# Skin Tone Incorporation in Convolutional Neural Network Training forAmerican Sign Language to Debias Datasets

This repository contains the code used for the paper Skin Tone Incorporation in Convolutional Neural Network Training forAmerican Sign Language to Debias Datasets. It contains the models, Jupyter notebooks and augmentation and debiasing methods used in the paper. The data is available separately [on Kaggle.](https://www.kaggle.com/datasets/aryavtaneja/skin-tone-cnn-debiasing)

# File Structure

The `models` folder contains the two Keras models tested in the paper. The `notebooks` folder contains Jupyter notebooks for training new models based on the data and for testing their accuracy against the validation datasets. The `utils` folder contains the image augmentation pipeline used to generate the initial dataset of 84,000 images in `augment.py`, and the method used to generate the debiased dataset in `debias_method.py`. Both of these require the Pillow library to be installed.

# Requirements

To run the code in this repository, you will need a Jupyter Notebook setup with the following libraries

- Tensorflow
- scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn
- VisualKeras
- Pillow

# Acknowledgements

The initial datasets were generated using data from [a repository by Sreehari Srijith](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn).
