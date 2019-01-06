# Setup
Use Python 3.x.

Install pip3.
```bash
sudo apt-get update
sudo apt-get install python3-pip
```
Install Tensorflow on Raspberry Pi. 
```bash
# https://www.raspberrypi.org/magpi/tensorflow-ai-raspberry-pi/
sudo apt install libatlas-base-dev
pip3 install tensorflow
```
Install dependencies.
```bash
pip3 install -r requirements.txt
```
# Usage
See main.py
```python
from model.serve import load_model, predict

# Load the model and the mapping.
model, mapping = load_model("model/bin")

# Make a prediction on PNG image.
print(predict("input.png", model, mapping)) 
# {'prediction': 'H', 'confidence': '99.755'}
```
# Train
Don't train on the Raspberry Pi. It is too computationally expensive.

Go to https://www.kaggle.com/crawford/emnist.
Download ```emnist-balanced-train.csv``` and ```emnist-balanced-test.csv```.

On your local computer,
```bash
python3 training.py -f path/to/emnist-balanced-train.csv -g path/to/emnist-balanced-test.csv --verbose
```

After successfully training, the newly trained model is saved to the ```bin``` directory.

