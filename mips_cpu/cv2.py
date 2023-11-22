import os
import pandas as pd
import matplotlib.pyplot as plt

# Specify the folder path where the text files are located
folder_path = '/home/linux/ieng6/cs148sp23/sbouzikian/baseline/mips_cpu/collectedData/all2'

# Get a list of all the text files in the folder
file_list = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# Define the variables you want to extract
variables = ['Total time', 'Cycle count', 'Instruction count', 'CPI', 'IPC',
             'if_flush', 'dec_stall', 'dec_overload', 'if_stall', 'ic_miss',
             'mem_stall', 'dec_flush', 'dc_miss', 'ex_stall', 'ds_miss',
             'mem_flush', 'ex_overload']

# Create an empty dictionary to store the extracted data
data_dict = {var: [] for var in variables}

# Create a dictionary to store the grouped data
grouped_data = {}

# Iterate over each file
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize default values for each variable
    default_values = {var: None for var in variables}

    # Extract the faulty type from the file name
    faulty_type = file_name.split('_')[1].split('.')[0]

    # Extract the data for each variable
    for line in lines:
        for var in variables:
            if var in line:
                value = line.split(':')[-1].strip()
                if var == 'CPI':
                    # Check if the line contains both CPI and IPC
                    if 'IPC' in value:
                        values = value.split('IPC:')
                        default_values['CPI'] = values[0].strip()
                        default_values['IPC'] = values[1].strip()
                    else:
                        # Set default values if IPC is not found
                        default_values['CPI'] = value
                        default_values['IPC'] = None
                else:
                    default_values[var] = value
                break

    # Append the extracted data to the dictionary
    for var in variables:
        data_dict[var].append(default_values[var])

    # Group the data based on faulty type
    if faulty_type in grouped_data:
        grouped_data[faulty_type].append(file_name)
    else:
        grouped_data[faulty_type] = [file_name]

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data_dict)

# Add the file name as an additional column
df['File'] = [os.path.splitext(file)[0] for file in file_list]

# Save the DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)

# Plot the grouped data
# Plot each variable in a stick shape
for var in variables:
    plt.figure()
    plt.stem(df['File'], df[var])
    plt.xlabel('File')
    plt.ylabel(var)
    plt.title(var + ' for Each File')
    plt.xticks(rotation=90)
    plt.ylim(bottom=0, top=plt.ylim()[1] * 10)  # Set y-axis limits to be 10 times bigger
    plt.tight_layout()
    plt.savefig(f'{var}.png')
    plt.close()
