# Project Setup

This project uses Python and several libraries. Follow the steps below to set up the project:

1. Install Python: Download and install Python from https://www.python.org/downloads/. This project was developed using Python 3.8, but it should work with other versions as well.

2. Clone the project: Clone the project from its repository to your local machine.

3. It's generally a good practice to use a virtual environment for Python projects to isolate the dependencies. Here's how you can set it up:

	-Install virtualenv if you haven't already: pip install virtualenv
	-Navigate to your project directory: cd project_directory
	-Create a virtual environment: virtualenv venv
	-Activate the virtual environment:
		On Windows: venv\Scripts\activate
		On Unix or MacOS: source venv/bin/activate
	-Now you can install your dependencies: 
		pip install opencv-python gaze-tracking
		pip install -r requirements.txt


4. Run the project: Navigate to the project directory in your terminal and run `python example.py` to start the project.

Please note that this project uses webcam input. Ensure that a webcam is connected to your machine and is working properly.

If you encounter any issues during setup, please refer to the documentation of the respective libraries or Python itself.