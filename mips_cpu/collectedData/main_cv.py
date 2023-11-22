# import os

# # Specify the folder path where the text files are located
# folder_path = 'path/to/folder'

# # Get a list of all the text files in the folder
# file_list = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# common_data = []  # List to store the common data from each file

# # Iterate over each file
# for file_name in file_list:
#     file_path = os.path.join(folder_path, file_name)
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     # Extract the common data from the last line of the file
#     last_line = lines[-1]
#     # Assuming the common data is the last space-separated element
#     data = last_line.split(' ')[-1].strip()

#     common_data.append(data)

# # Print the common data from each file
# for i, data in enumerate(common_data, start=1):
#     print(f"Data from file{i}: {data}")
# import pandas as pd
# import matplotlib.pyplot as plt

# # Assuming you have your data stored in a variable called 'data'

# # Create a DataFrame from your data
# df = pd.DataFrame(data)

# # Save the DataFrame to an Excel file
# df.to_excel('data.xlsx', index=False)

# # Plot the data
# plt.plot(data)

# # Save the plot as a PNG image
# plt.savefig('plot.png')

import os
import pandas as pd
import matplotlib.pyplot as plt

folder_path = '/home/linux/ieng6/cs148sp23/sbouzikian/baseline/mips_cpu/collectedData'  # Specify the folder path where the text files are located

# Get a list of all the text files in the folder
file_list = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# Define the variables you want to extract
variables = ['Total time', 'Cycle count', 'Instruction count', 'CPI', 'IPC',
             'if_flush', 'dec_stall', 'dec_overload', 'if_stall', 'ic_miss',
             'mem_stall', 'dec_flush', 'dc_miss', 'ex_stall', 'ds_miss',
             'mem_flush', 'ex_overload']

# Create an empty dictionary to store the extracted data
data_dict = {var: [] for var in variables}

# Iterate over each file
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract the data for each variable
    for var in variables:
        for line in lines:
            if line.startswith(var):
                value = line.split(':')[-1].strip()
                data_dict[var].append(value)
                break

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data_dict)

# Add the file name as an additional column
df['File'] = [os.path.splitext(file)[0] for file in file_list]

# Save the DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)

# Plot each variable in a stick shape
for var in variables:
    plt.figure()
    plt.stem(df['File'], df[var])
    plt.xlabel('File')
    plt.ylabel(var)
    plt.title(var + ' for Each File')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'{var}.png')
    plt.close()
