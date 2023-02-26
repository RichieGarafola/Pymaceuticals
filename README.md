# Pymaceuticals

Deploayable Dashboard:
https://pymaceuticals.streamlit.app/
---

## Background

You've just joined Pymaceuticals, Inc., a new pharmaceutical company that specializes in anti-cancer medications. Recently, it began screening for potential treatments for squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.

As a senior data analyst at the company, you've been given access to the complete data from their most recent animal study. In this study, 249 mice who were identified with SCC tumors received treatment with a range of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals’ drug of interest, Capomulin, against the other treatment regimens.

The executive team has tasked you with generating all of the tables and figures needed for the technical report of the clinical study. They have also asked you for a top-level summary of the study results.

---

## Overview
This project is a data analysis of mouse tumor growth in response to various drug regimens. The data comes from a study in which mice were treated with different drugs and their tumor volumes were measured over time. The goal of this project is to analyze the data and determine which drugs are most effective at reducing tumor growth.

---

## Features

- Summary statistics for each drug regimen
- Bar plot showing the total number of timepoints for all mice tested for each drug regimen
- Pie plot showing the distribution of female versus male mice
- Table displaying the final tumor volume of each mouse across four of the treatment regimens
- Box plot of the final tumor volume of each mouse across four of the treatment regimens
- Scatter plot with linear regression model showing the correlation between mouse weight and average tumor volume for the Capomulin treatment regimen

---

## Instructions
This assignment is broken down into the following tasks:

Prepare the data.

Generate summary statistics.

Create bar charts and pie charts.

Calculate quartiles, find outliers, and create a box plot.

Create a line plot and a scatter plot.

Calculate correlation and regression.

---

## Installation
To use this project, you will need to have Python installed on your computer. You will also need to install the following libraries:

Streamlit
Matplotlib
Pandas
Scipy

You can install these libraries using pip by running the following command in your terminal:

    pip install streamlit matplotlib pandas scipy

---

## Prepare the Data

- Run the provided package dependency and data imports, and then merge the mouse_metadata and study_results DataFrames into a single DataFrame.

- Display the number of unique mice IDs in the data, and then check for any mouse ID with duplicate time points. Display the data associated with that mouse ID, and then create a new DataFrame where this data is removed. Use this cleaned DataFrame for the remaining steps.

- Display the updated number of unique mice IDs.

---

## Generate Summary Statistics

Create a DataFrame of summary statistics. Remember, there is more than one method to produce the results you're after, so the method you use is less important than the result.

Your summary statistics should include:

- A row for each drug regimen. These regimen names should be contained in the index column.

- A column for each of the following statistics: mean, median, variance, standard deviation, and SEM of the tumor volume.

---

## Create Bar Charts and Pie Charts
- Generate two bar charts. Both charts should be identical and show the total number of time points for all mice tested for each drug regimen throughout the study.

    - Create the first bar chart with the Pandas DataFrame.plot() method.

    - Create the second bar chart with Matplotlib's pyplot methods.

- Generate two pie charts. Both charts should be identical and show the distribution of female versus male mice in the study.

    - Create the first pie chart with the Pandas DataFrame.plot() method.

    - Create the second pie chart with Matplotlib's pyplot methods.

---

## Calculate Quartiles, Find Outliers, and Create a Box Plot

- Calculate the final tumor volume of each mouse across four of the most promising treatment regimens: Capomulin, Ramicane, Infubinol, and Ceftamin. Then, calculate the quartiles and IQR, and determine if there are any potential outliers across all four treatment regimens. Use the following substeps:

    - Create a grouped DataFrame that shows the last (greatest) time point for each mouse. Merge this grouped DataFrame with the original cleaned DataFrame.

    - Create a list that holds the treatment names as well as a second, empty list to hold the tumor volume data.

    - Loop through each drug in the treatment list, locating the rows in the merged DataFrame that correspond to each treatment. Append the resulting final tumor volumes for each drug to the empty list.

    - Determine outliers by using the upper and lower bounds, and then print the results.

Using Matplotlib, generate a box plot that shows the distribution of the final tumor volume for all the mice in each treatment group. Highlight any potential outliers in the plot by changing their color and style.

hint: All four box plots should be within the same figure. Use this Matplotlib documentation pageLinks to an external site. for help with changing the style of the outliers.

---

## Create a Line Plot and a Scatter Plot
    - Select a mouse that was treated with Capomulin, and generate a line plot of tumor volume versus time point for that mouse.

    - Generate a scatter plot of tumor volume versus mouse weight for the Capomulin treatment regimen.

---

## Calculate Correlation and Regression
- Calculate the correlation coefficient and linear regression model between mouse weight and average tumor volume for the Capomulin treatment.

- Plot the linear regression model on top of the previous scatter plot.

---

To run the project, navigate to the project directory in your terminal and run the following command:

    streamlit run app.py
    
---

# KPI Dashboard

The KPI Dashboard is a data visualization tool that displays key performance indicators (KPIs) for a business or organization. It allows users to easily monitor their progress towards goals, identify trends, and make data-driven decisions.

## Features

- Customizable dashboard layout: Users can choose which KPIs to display and how to arrange them on the dashboard.
- Real-time data updates: The dashboard automatically refreshes to show the latest data from the underlying data source.
- Interactive charts and graphs: Users can click on different parts of the charts to see more detailed information and drill down into the data.
- Mobile-friendly design: The dashboard is optimized for viewing on mobile devices, making it easy to access important data on the go.

---

## Installation

The KPI Dashboard is a web-based application that runs in a web browser. There is no need to install any software on your computer or server.

To use the KPI Dashboard, simply open the dashboard URL in your web browser and log in with your credentials. The dashboard can be accessed from anywhere with an internet connection.

---

## Configuration

The KPI Dashboard is designed to be easily configurable by non-technical users. Administrators can use the web-based dashboard configuration tool to:

- Add, edit, or remove KPIs
- Choose the data source for each KPI
- Customize the dashboard layout and appearance
- Set user permissions and access controls
