# Facial Emotion Recognition (FER) oTree app

## Introduction

Emotion detection already plays a relevant role in experimental economics, providing insights into participants’ psychological reality while making decisions and interacting with other agents. The development of advanced tools, such as emotion recognition from face images, aims to address these shortcomings. The current project "FER" for Facial Expressions Recognition incorporates an open source, popular engine into a package usable with oTree, one of the most popular frameworks for developing experiment interfaces.

The initial iteration of the project is on this repo. The following are still under development. 

## Code Overview

This is an oTree app that can use the user webcam to take snapshots and predict the dominant emotions displayed on the picture.
It can be be used as a template for developing more advanced experiments based on FER or other visual analysis.

The software used in this version, [FER](https://pypi.org/project/fer/), detects the following emotional states

- E1: Anger
- E2: Disgust
- E3: Fear
- E4: Happiness
- E5: Sadness
- E6: Surprise
- E7: Neutral

In this version, the predictions take place on the backend of the server hosting the web application with the experiment. In our following iterations, two servers are required: one to host the web application and another one to handle the predictions. Currently, we are focusing both on (1) finding a way to seamlessly integrate the prediction software on an oTree experiment and (2) improve the performance of the emotion prediction models.

## Requirements

- Python 3.7.x
- Nvidia CUDA Toolkit 10.1
- The required packages can be found on the `requirements.txt` file from this repo
- A ton of patience (configuring your pc to run this project might take a while)

## Deployment

- Create an environment to run the scripts
    - If you are using anaconda, install it using environment.yml
    - Else, create the environment using runtime.txt to find the right Python version and requirements.txt for the packages
- Open a terminal and move to the directory of your repo
- Run `otree devserver` for deploying it locally in development mode
