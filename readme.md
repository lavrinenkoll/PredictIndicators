# Project Title: Mortgage Data Analysis and Prediction Tool

## Overview

This project is designed to analyze and visualize mortgage sales data from a dataset. It also incorporates predictive analysis using machine learning techniques to forecast future trends. The tool processes multiple mortgage-related metrics and presents the results in graphical form, making it a valuable asset for data analysts working in the real estate or financial sectors.

## Key Features

- **Data Parsing**: Utilizes `pandas` to read and process data from Excel sheets, extracting relevant information such as sales by loan amount, income multipliers, property values, and more.
- **Data Visualization**: Generates stacked bar charts and trend graphs using `matplotlib` to display insights from the dataset, making it easier to understand complex mortgage-related data.
- **Predictive Modeling**: Leverages `Keras` and `LSTM` neural networks to forecast future mortgage sales, providing valuable predictive insights for stakeholders.
- **Data Smoothing**: Uses `scipy` interpolation to create smoothed trend lines for a better visual understanding of long-term trends in mortgage sales data.

## Technologies Used

- **Python**: Main programming language used for data processing and visualization.
- **Pandas**: For reading and manipulating data from Excel sheets.
- **Matplotlib**: For generating visualizations, including bar charts and line plots.
- **Scipy**: For data smoothing using interpolation techniques.
- **Keras and TensorFlow**: For building and training LSTM models to predict future trends in mortgage sales.

## How to Use

1. **Install Required Libraries**:
   Install the necessary Python libraries by running:
   ```
   pip install pandas matplotlib scipy keras tensorflow
   ```

2. **Prepare Data**:
   Ensure that the input dataset (`Data_Set_14.xlsx`) is placed in the same directory as the script. The dataset should have multiple sheets, each containing structured mortgage-related data.

3. **Run the Script**:
   Execute the `main.py` file to start the analysis and visualization:
   ```bash
   python main.py
   ```

4. **View Results**:
   The script will display several graphs representing various mortgage data segments, including sales by loan amount, income multipliers, and property value. It will also generate predictions for the next four quarters based on the historical data.
