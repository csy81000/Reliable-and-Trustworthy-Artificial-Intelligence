# Reliable and Trustworthy Artificial Intelligence - Assignment #3

## Overview
This repository contains the setup and execution code for verifying a small Convolutional Neural Network (CNN) trained on the MNIST dataset using the **Marabou** verification framework.

## Project Structure
- `requirements.txt` : Required Python packages (excluding Marabou).
- `test.py` : The main script to run the verification query on the external ONNX model.
- `report.pdf` : Analysis report including model details, verification results (SAT/UNSAT), and evaluation of Marabou.
- `README.md` : Installation and execution guide.


```
# 1. Install Python dependencies
pip install numpy onnx torch torchvision

# 2. Install system build tools
sudo apt-get update
sudo apt-get install -y cmake build-essential python3-dev

# 3. Clone and Build Marabou from Source
git clone [https://github.com/NeuralNetworkVerification/Marabou.git](https://github.com/NeuralNetworkVerification/Marabou.git)
cd Marabou
mkdir build && cd build
# Use CMAKE_POLICY_VERSION_MINIMUM=3.5 to resolve pybind11 compatibility issues
cmake .. -DBUILD_PYTHON=ON -DCMAKE_POLICY_VERSION_MINIMUM=3.5
cmake --build . -j 2
cd ../..

# 4. Run Verification Script
python test.py
```
