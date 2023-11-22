#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
  echo "Usage: ./run_benchmark.sh <output_file_prefix>"
  exit 1
fi

# Assign the first argument to the variable output_prefix
output_prefix=$1

# Run Vmips_core with the "nqueens" benchmark and store the output in a text file
./obj_dir/Vmips_core -b nqueens > "./collectedData/${output_prefix}_nqueens.txt"
  echo "nqueens done"
# Run Vmips_core with the "coin" benchmark and store the output in a text file
./obj_dir/Vmips_core -b coin > "./collectedData/${output_prefix}_coin.txt"
  echo "coin done"
# Run Vmips_core with the "qsort" benchmark and store the output in a text file
./obj_dir/Vmips_core -b qsort > "./collectedData/${output_prefix}_qsort.txt"
  echo "qsort done"
# Run Vmips_core with the "esift" benchmark and store the output in a text file
./obj_dir/Vmips_core -b esift > "./collectedData/${output_prefix}_esift.txt"
  echo "esift done"
# Run Vmips_core with the "esift2" benchmark and store the output in a text file
./obj_dir/Vmips_core -b esift2 > "./collectedData/${output_prefix}_esift2.txt"
  echo "esift2 done"


# #!/bin/bash

# # Check if an argument is provided
# if [ $# -eq 0 ]; then
#   echo "Usage: ./sako.sh <output_file_prefix>"
#   exit 1
# fi

# # Assign the first argument to the variable output_prefix
# output_prefix=$1

# # Array of branch predictor names
# predictor_names=("branch_predictor_gshare" "branch_predictor_gshare_loop" "branch_predictor_gshare_loop_2" "branch_predictor_always_taken" "branch_predictor_always_not_taken" "branch_predictor_2bit")

# # Iterate over each predictor name
# for name in "${predictor_names[@]}"; do
#   # Change line 28 in branch_controlle.sv with the new predictor name
#   sed -i "28s/.*/$name PREDICTOR (/" ./mips_core/branch_controller.sv
#   echo "$name started"
#   # Make
#   make verilate
#   echo "$name make done"
#   # Run Vmips_core with the "nqueens" benchmark and store the output in a text file
#   ./obj_dir/Vmips_core -b nqueens > "./collectedData/${name}_nqueens.txt"
#   echo "nqueens done"

#   # Run Vmips_core with the "coin" benchmark and store the output in a text file
#   ./obj_dir/Vmips_core -b coin > "./collectedData/${name}_coin.txt"
#   echo "coin done"

#   # Run Vmips_core with the "qsort" benchmark and store the output in a text file
#   ./obj_dir/Vmips_core -b qsort > "./collectedData/${name}_qsort.txt"
#   echo "qsort done"

#   # Run Vmips_core with the "esift" benchmark and store the output in a text file
#   ./obj_dir/Vmips_core -b esift > "./collectedData/${name}_esift.txt"
#   echo "esift done"

#   # Run Vmips_core with the "esift2" benchmark and store the output in a text file
#   ./obj_dir/Vmips_core -b esift2 > "./collectedData/${name}_esift2.txt"
#   echo "esift2 done"
#   echo "$name done"
# done