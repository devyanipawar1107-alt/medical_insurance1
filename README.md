# Medical Insurance Cost Prediction

## Project Overview
This project predicts medical insurance costs using a machine learning model. It is designed to help users estimate insurance charges based on personal and health-related information. The project includes a trained linear regression model, data preprocessing utilities, and a simple web interface for user interaction.

## Features
- Predicts insurance costs using a trained linear regression model
- Handles categorical variables with label encoding
- Modular codebase for easy maintenance
- Jupyter notebooks for model training and testing
- Web interface with HTML templates for user input and results

## Directory Structure
```
medical_insurance1/
│   interface.py
│   label_enc_data.json
│   linear_regression.pkl
│   README.md
│   test.txt
│   utils.py
│
└───project_app/
	 │   __init__.py
	 │   config.py
	 │   label_enc_data.json
	 │   linear_regression.pkl
	 │   medical insurance.ipynb
	 │   model testing med.ipynb
	 │   utils.py
	 │
	 └───__pycache__/
	 └───templates/
		  │   demo.html
		  │   index.html
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
	```sh
	git clone <repository-url>
	```
2. Navigate to the project directory:
	```sh
	cd medical_insurance1
	```
3. (Optional) Create and activate a virtual environment:
	```sh
	python -m venv venv
	.\venv\Scripts\activate
	```
4. Install dependencies:
	```sh
	pip install -r requirements.txt
	```

### Running the Application
1. Ensure `linear_regression.pkl` and `label_enc_data.json` are present in the correct directories.
2. Run the main interface:
	```sh
	python interface.py
	```
3. For the web interface, open the HTML files in the `templates` folder.

## Usage
- Enter user data as prompted.
- The model will output the predicted insurance cost.

## Notebooks
- `medical insurance.ipynb`: Data exploration and model training
- `model testing med.ipynb`: Model evaluation and testing

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please contact the project maintainer.