import os

# Path to the input folder containing .txt files
input_folder = "/home/linux/ieng6/cs148sp23/sbouzikian/baseline/mips_cpu/collectedData/all"

# Path to the output folder where modified files will be saved
output_folder = "/home/linux/ieng6/cs148sp23/sbouzikian/baseline/mips_cpu/collectedData/all2"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r') as file:
            lines = file.readlines()

        # Find the line with the CPI and IPC values
        for i, line in enumerate(lines):
            if "CPI:" in line and "IPC:" in line:
                cpi_index = line.index("CPI:")
                ipc_index = line.index("IPC:")

                # Insert a new line before the IPC value
                lines[i] = line[:ipc_index] + '\n' + line[ipc_index:]

                break

        # Save the modified content to the output file
        with open(output_path, 'w') as file:
            file.writelines(lines)

        print(f"Modified file saved: {output_path}")
