# import the necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the data from the Mouse_metadata.csv and Study_results.csv files into two separate data frames
mouse_metadata_path = "./Resources/Mouse_metadata.csv"
study_results_path = "./Resources/Study_results.csv"

mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Merge the two data frames into a single data frame and drop any duplicate rows
study_data_complete = pd.merge(study_results, mouse_metadata, how = "left", on = "Mouse ID")
study_data_complete = study_data_complete.drop_duplicates(subset=["Mouse ID", "Timepoint"], keep="last")

# Define a function to calculate the summary statistics for each drug regimen and display the results in a table
def drug_summary_stats(data):
    means = data.groupby("Drug Regimen").mean()["Tumor Volume (mm3)"]
    medians = data.groupby("Drug Regimen").median()["Tumor Volume (mm3)"]
    variances = data.groupby("Drug Regimen").var()["Tumor Volume (mm3)"]
    sds = data.groupby("Drug Regimen").std()["Tumor Volume (mm3)"]
    sems = data.groupby("Drug Regimen").sem()["Tumor Volume (mm3)"]
    summary_table = pd.DataFrame({"Mean Tumor Volume":means,
                                  "Median Tumor Volume":medians,
                                  "Tumor Volume Variance":variances,
                                  "Tumor Volume Std. Dev.":sds,
                                  "Tumor Volume Std. Err.":sems})
    return summary_table

# Define a function to create a bar plot showing the total number of timepoints for all mice tested for each drug regimen using Pandas

def create_bar_plot(data):
    counts = data['Drug Regimen'].value_counts()
    counts.plot(kind="bar")
    plt.xlabel("Drug Regimen")
    plt.xticks(rotation=90)
    plt.ylabel("Number of Mice Tested")
    st.pyplot()

    
# Define a function to create a pie plot showing the distribution of female versus male mice using Pandas:
def create_pie_plot(data):
    counts = data.Sex.value_counts()
    counts.plot(kind="pie",autopct='%1.1f%%')
    st.pyplot()
    
# Define a function to calculate the final tumor volume of each mouse across four of the treatment regimens (Capomulin, Ramicane, Infubinol, and Ceftamin) and display the results in a table

def final_tumor_volume(data):
    treatment_list = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]
    max_tumor = data.groupby(["Mouse ID"])["Timepoint"].max()
    max_tumor = max_tumor.reset_index()
    merged_data = max_tumor.merge(data, on = ["Mouse ID", "Timepoint"], how = "left")
    final_tumor_vol = merged_data[merged_data["Drug Regimen"].isin(treatment_list)]
    final_tumor_vol = final_tumor_vol.loc[:, ["Mouse ID", "Drug Regimen", "Tumor Volume (mm3)"]]
    return final_tumor_vol

# Define a function to create a box plot of the final tumor volume of each mouse across four of the treatment regimens (Capomulin, Ramicane, Infubinol, and Ceftamin) using Matplotlib
def create_box_plot(data):
    treatment_list = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]
    final_tumor_vol = final_tumor_volume(data)
    final_tumor_vol = final_tumor_vol.groupby("Drug Regimen")["Tumor Volume (mm3)"].apply(list)
    final_tumor_vol_df = pd.DataFrame(final_tumor_vol)
    final_tumor_vol_df = final_tumor_vol_df.reindex(treatment_list)
    fig, ax = plt.subplots()
    ax.boxplot(final_tumor_vol_df["Tumor Volume (mm3)"], sym="o")
    ax.set_xlabel("Drug Regimen")
    ax.set_ylabel("Final Tumor Volume (mm3)")
    ax.set_xticklabels(treatment_list)
    st.pyplot(fig)

# Define a function to calculate the correlation coefficient and linear regression model for mouse weight and average tumor volume for the Capomulin treatment regimen, and plot the linear regression model on top of the scatter plot
def plot_regression(data):
    capomulin_data = data[data["Drug Regimen"] == "Capomulin"]
    weight_vs_tumor = capomulin_data.loc[:, ["Mouse ID", "Weight (g)", "Tumor Volume (mm3)"]]
    avg_tumor_by_weight = pd.DataFrame(weight_vs_tumor.groupby("Mouse ID")["Weight (g)", "Tumor Volume (mm3)"].mean()).rename(columns={"Weight (g)":"Average Weight (g)","Tumor Volume (mm3)":"Average Tumor Volume (mm3)"})
    x_values = avg_tumor_by_weight["Average Weight (g)"]
    y_values = avg_tumor_by_weight["Average Tumor Volume (mm3)"]
    correlation = stats.pearsonr(x_values,y_values)
    st.write(f"The correlation between mouse weight and the average tumor volume is {round(correlation[0],2)}")
    slope, intercept, rvalue, pvalue, stderr = stats.linregress(x_values, y_values)
    regression_line = slope * x_values + intercept
    plt.scatter(x_values,y_values)
    plt.plot(x_values,regression_line,"r-")
    plt.xlabel("Average Weight (g)")
    plt.ylabel("Average Tumor Volume (mm3)")
    st.pyplot()
    # return correlation[0]


# Calculate and display the average tumor volume for the Capomulin treatment regimen
capomulin_data = study_data_complete[study_data_complete["Drug Regimen"] == "Capomulin"]
avg_tumor_vol = capomulin_data.groupby("Mouse ID").mean()["Tumor Volume (mm3)"].mean()

# st.title("Average Tumor Volume for Capomulin Treatment Regimen")
# st.subheader(round(avg_tumor_vol, 2))

def app():
    # Add a title and description to the app
    st.title("Cancer Treatment Study Data")
    st.markdown("This app provides an interactive dashboard for exploring the Cancer Treatment Study data.")

    # Create a sidebar with options for exploring the data
    st.sidebar.header("Explore the Data")
    options = ["Drug Summary Statistics", "Number of Mice Tested per Drug Regimen", "Distribution of Mice Sex", 
               "Final Tumor Volume across Four Treatment Regimens", "Mouse Weight vs. Average Tumor Volume for Capomulin Treatment Regimen"]
    selection = st.sidebar.selectbox("Select an option", options)

    # Display the appropriate plot or table based on the user's selection
    if selection == "Drug Summary Statistics":
        st.subheader("Drug Summary Statistics")
        st.write(drug_summary_stats(study_data_complete))

    elif selection == "Number of Mice Tested per Drug Regimen":
        st.subheader("Number of Mice Tested per Drug Regimen")
        create_bar_plot(study_data_complete)

    elif selection == "Distribution of Mice Sex":
        st.subheader("Distribution of Mice Sex")
        create_pie_plot(study_data_complete)

    elif selection == "Final Tumor Volume across Four Treatment Regimens":
        st.subheader("Final Tumor Volume across Four Treatment Regimens")
        create_box_plot(study_data_complete)

    elif selection == "Mouse Weight vs. Average Tumor Volume for Capomulin Treatment Regimen":
        st.subheader("Mouse Weight vs. Average Tumor Volume for Capomulin Treatment Regimen")
        plot_regression(study_data_complete)

app()