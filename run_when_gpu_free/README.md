# run_when_gpu_free
This script checks whether GPUs are free (the occupied memory is less than or equal to `idle_threshold`) every `busy_sleep` second, and if they are, runs the command(s) you specify.

## Usage

Specify the command(s) you would like to run in the script, and run the script.

The arguments `idle_threshold` and `busy_sleep` can be modified at the top of the script.

