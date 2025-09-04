import pandas as pd 
from ast import literal_eval
import numpy as np

data = pd.read_csv('/Users/Programmieren/LLM_apps/Arbeitsbereich/ProofofConcept-directory/Processed results/processed_results_real_data2.csv')

# Display column names
print("Column names:", data.columns.tolist())

#---------------### Interest Enjoyment ###---------------------------
def extract_InterestEnjoyment(row):
    try:
        # literal_eval is used to tell python that the dataset needs to be read as a dict
        nested = literal_eval(row)
        # Correctly access the 'Interest_enjoyment' key with [0] here
        if 'Interest_enjoyment' in nested[0]:
            return nested[0]['Interest_enjoyment']
        else:
            return None  
    except Exception as e:
        # Return None if parsing fails 
        print(f"Error processing row: {e}")
        return None

# Apply the function to each row and create a new DataFrame
data['interest enjoyment'] = data['interest enjoyment'].apply(extract_InterestEnjoyment)
dataIE = pd.DataFrame(data['interest enjoyment'].tolist())

if not dataIE.empty:
    dataIE['mean_Interest_Enjoyment'] = round(dataIE.mean(axis=1), 3) # calculate the mean per row + round to three digits
    round(dataIE, 3)
    print(dataIE.head()) # print the row 
else:
    print("No valid data to display.") #! if it works for one it will work for all 

#---------------### Perceived competence ###---------------------------
def extract_PerceivedCompetence(row):
    try:
        nested = literal_eval(row)
        # Correctly access the 'Pco' key
        if 'Perceived competence' in nested[0]:
            return nested[0]['Perceived competence']
        else:
            return None  
    except Exception as e:
        # Return None if parsing fails or data is not as expected
        print(f"Error processing row: {e}")
        return None

data['perceived competence'] = data['perceived competence'].apply(extract_PerceivedCompetence)
dataPCo = pd.DataFrame(data['perceived competence'].tolist())

# calculate the mean
if not dataPCo.empty:
    dataPCo['mean_perceived_competence'] = round(dataPCo.mean(axis=1), 3)
    print(dataPCo.head())
else:
    print("No valid data to display.")

#---------------### Effort Importance ###---------------------------
def extract_EffortImportance(row):
    try:
        nested = literal_eval(row)
        # Correctly access the 'Effort importance' key
        if 'Effort importance' in nested[0]:
            return nested[0]['Effort importance']
        else:
            return None  
    except Exception as e:
        print(f"Error processing row: {e}")
        return None


data['Effort importance'] = data['Effort importance'].apply(extract_EffortImportance)
dataEI = pd.DataFrame(data['Effort importance'].tolist())


if not dataPCo.empty:
    dataEI['mean_effort_importance'] = round(dataEI.mean(axis=1), 3)
    print(dataEI.head())
else:
    print("No valid data to display.")

#---------------### Pressure tension ###---------------------------
def extract_PressureTension(row):
    try:
        nested = literal_eval(row)
        # Correctly access the 'Pressure tension' key
        if 'Pressure tension' in nested[0]:
            return nested[0]['Pressure tension']
        else:
            return None  
    except Exception as e:
        # Return None if parsing fails or data is not as expected
        print(f"Error processing row: {e}")
        return None

data['Pressure Tension'] = data['Pressure Tension'].apply(extract_PressureTension)
dataPT = pd.DataFrame(data['Pressure Tension'].tolist())

if not dataPT.empty:
    dataPT['mean_pressure_tension'] = round(dataPT.mean(axis=1),3)
    print(dataPT.head())
else:
    print("No valid data to display.")

#---------------### Perceived choice ###---------------------------
def extract_PerceivedChoice(row):
    try:
        nested = literal_eval(row)
        # Correctly access the 'Perceived choice' key
        if 'Perceived choice' in nested[0]:
            return nested[0]['Perceived choice']
        else:
            return None  
    except Exception as e:
        
        print(f"Error processing row: {e}")
        return None

data['Perceived choice'] = data['Perceived choice'].apply(extract_PerceivedChoice)
dataPC = pd.DataFrame(data['Perceived choice'].tolist())

if not dataPC.empty:
    dataPC['mean_perceived_choice'] = round(dataPC.mean(axis=1), 3)
    print(dataPC.head())
else:
    print("No valid data to display.")

#---------------### Value Usefulness ###---------------------------
def extract_ValueUsefulness(row):
    try:
        nested = literal_eval(row)
        if 'Value Usefulness' in nested[0]:
            return nested[0]['Value Usefulness']
        else:
            return None  
    except Exception as e:
        print(f"Error processing row: {e}")
        return None

data['Value Usefulness'] = data['Value Usefulness'].apply(extract_ValueUsefulness)
dataVU = pd.DataFrame(data['Value Usefulness'].tolist())

if not dataVU.empty:
    dataVU['mean_value_usefulness'] = round(dataVU.mean(axis=1), 3)
    print(dataVU.head())
else:
    print("No valid data to display.")

def create_summary_dataframe(data):
    # List of subscale names and their respective dataframes e.g. mean_interest_enjoyment = key of the dataIE dict
    subscales = [
        ('Interest Enjoyment', dataIE, 'mean_Interest_Enjoyment'),
        ('Perceived Competence', dataPCo, 'mean_perceived_competence'),
        ('Effort Importance', dataEI, 'mean_effort_importance'),
        ('Pressure Tension', dataPT, 'mean_pressure_tension'),
        ('Perceived Choice', dataPC, 'mean_perceived_choice'),
        ('Value Usefulness', dataVU, 'mean_value_usefulness')
    ]

    # Iempty DataFrame
    summary_df = pd.DataFrame()

    # Loop through each subscale and its dataframe
    for name, df, mean_col in subscales: # for the name of the subscale, the different dict and the value
        if not df.empty:
            if mean_col in df.columns:
                # Add the mean column to the summary dataframe with the name of the subscale
                summary_df[name] = df[mean_col]
            else:
                # fill with NaNs
                summary_df[name] = pd.NA
        else:
            # If dataframe is empty, also fill with NaNs
            summary_df[name] = pd.NA

    return summary_df

# Create the summary DataFrame using the function
summary_data = create_summary_dataframe(data)
summary_data.to_csv('ProofofConcept-directory/Computed_averages/computed_averages_real2.csv')
print(summary_data.head())
