# TimeSeriesRNN
**Udacity - Artificial Intelligence Nanodegree Program**   
AI -  RNNs that can generate sequences based on input data

# RNN

This project is part of **Udacity´s Artificial Intelligence Nanodegree Program**. Here you will find my personal solution to the challenge. The following project can be run using a Local Machine or using an external GPU (Solution provided by **Amazon Web Services** is recommended). Next, you can follow Udacitys instructions to install the necessary dependencies on a local machine or on AWS.

In this project, we train a **Recurrent Neural Network** to predict the future outcome of an input data.

Follow the instructions to install the required environment and check the jupyter notebook files:

    (pmaienv)$ jupyter notebook RNN_project.ipynb
    
Alternative. You can open on a browser opening the file:
    
    RNN_project.html

--------------------------------------------------------------------------------------------------------

## Main Instructions
Follow the **Udacity instructions** to launch an EC2 GPU instance . Make sure you have installed the modules described in the instructions, including the correct version of tensorflow & the udacity-pa module.

Steps 2-4 should be executed in the EC2 instance.
Clone the RNN project GitHub repository, and navigate to the downloaded folder:

    $ git clone https://github.com/pablomateo/TimeSeriesRNN.git
    $ cd TimeSeriesRNN
    
Start Jupyter: 
     
     $ jupyter notebook --ip=0.0.0.0 --no-browser

Look at the output in the window, and find the line that looks like the following:
Copy/paste this URL into your browser when you connect for the first time to login with a token: 
http://0.0.0.0:8888/?token=3156e...

Copy and paste the complete URL into the address bar of a web browser (Firefox, Safari, Chrome, etc). Before navigating to the URL, replace 0.0.0.0 in the URL with the "IPv4 Public IP" address from the EC2 Dashboard. Press Enter.
Click on RNN_project.ipynb. Follow the instructions in the notebook.

--------------------------------------------------------------------------------------------------------

### Instructions - Udacity Project

1. Clone the repository and navigate to the downloaded folder.
	
```	
    $ git clone https://github.com/pablomateo/TimeSeriesRNN.git
    $ cd TimeSeriesRNN
```

2. (Optional) __If you plan to install TensorFlow with GPU support on your local machine__, follow [the guide](https://www.tensorflow.org/install/) to install the necessary NVIDIA software on your system.  If you are using an EC2 GPU instance, you can skip this step.

3. (Optional) **If you are running the project on your local machine (and not using AWS)**, create (and activate) a new environment.

	- __Linux__ (to install with __GPU support__, change `requirements/pmaienv-linux.yml` to `requirements/pmaienv-linux-gpu.yml`): 
	```
	  $ conda env create -f requirements/pmaienv-linux.yml
    $ source activate pmaienv-project
	```  
	- __Mac__ (to install with __GPU support__, change `requirements/pmaienv-mac.yml` to `requirements/pmaienv-mac-gpu.yml`): 
	```
    $ conda env create -f requirements/pmaienv-mac.yml
    $ source activate pmaienv-project
	```  
	- __Windows__ (to install with __GPU support__, change `requirements/pmaienv-windows.yml` to `requirements/pmaienv-windows-gpu.yml`):  
	```
    $ conda env create -f requirements/pmaienv-windows.yml
    $ activate pmaienv-project
	```
	
4. (Optional) **If you are running the project on your local machine (and not using AWS)** and Step 6 throws errors, try this __alternative__ step to create your environment.

	- __Linux__ or __Mac__ (to install with __GPU support__, change `requirements/requirements.txt` to `requirements/requirements-gpu.txt`): 
	```
    $ conda create --name pmaienv-project python=3.5
    $ source activate pmaienv-project
    (pmaienv)$ pip install -r requirements/requirements.txt
	```  
	- __Windows__ (to install with __GPU support__, change `requirements/requirements.txt` to `requirements/requirements-gpu.txt`):  
	```
    $ conda create --name pmaienv-project python=3.5
    $ activate pmaienv-project
    (pmaienv)$ pip install -r requirements/requirements.txt
	```
	
5. (Optional) **If you are using AWS**, install Tensorflow.
```
    (pmaienv)$ sudo python3 -m pip install -r requirements/requirements-gpu.txt
```
	
6. Switch [Keras backend](https://keras.io/backend/) to TensorFlow.
	- __Linux__ or __Mac__: 
		```
    (pmaienv)$ KERAS_BACKEND=tensorflow python -c "from keras import backend"
		```
	- __Windows__: 
		```
    (pmaienv)$ set KERAS_BACKEND=tensorflow
		python -c "from keras import backend"
		```

7. (Optional) **If you are running the project on your local machine (and not using AWS)**, create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `pmaienv-project` environment. 
```
    (pmaienv)$ python -m ipykernel install --user --name pmaienv-project --display-name "pmaienv-project"
```

8. Follow the **Main Instructions** at the top of this file

9. (Optional) **If you are running the project on your local machine (and not using AWS)**, before running code, change the kernel to match the pmaienv-project environment by using the drop-down menu (**Kernel > Change kernel > pmaienv-project**). 
