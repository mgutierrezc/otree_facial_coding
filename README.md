# Facial Emotion Recognition (FER) oTree app

## Introduction

Emotion detection already plays a relevant role in experimental economics, providing insights into participants’ psychological reality while making decisions and interacting with other agents. The development of advanced tools, such as emotion recognition from face images, aims to address these shortcomings. The current project "FER" for Facial Expressions Recognition incorporates an open source, popular engine into a package usable with oTree, one of the most popular frameworks for developing experiment interfaces.

The initial iteration of the project is on this repo. The following are still under development. 

## Code Overview

This is an oTree app that can use the user webcam to take snapshots and predict the dominant emotions displayed on the picture.
It can be be used as a template for developing more advanced experiments based on FER or other visual analysis.

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
