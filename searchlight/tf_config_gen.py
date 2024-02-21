import sys
import subprocess
import os


def config_gen(tf_import_blocks_file):
    terraform_directory, import_blocks = tf_import_blocks_file.rsplit('/', 1)
    input_file_name = import_blocks.split('_')[0]
    tf_config_output = f"{terraform_directory}/{input_file_name}_generated_config.tf"

    # Change to the specified directory
    os.chdir(terraform_directory)

    # Run the Terraform command
    terraform_command = f'terraform plan -generate-config-out={tf_config_output}'

    # Use subprocess to run the command
    process = subprocess.Popen(terraform_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture and print the output
    stdout, stderr = process.communicate()
    print("Terraform Output:", stdout.decode('utf-8'))

    # Check for errors
    if process.returncode != 0:
        print("Error:", stderr.decode('utf-8'))
        sys.exit(1)
    else:
        print("Terraform command executed successfully.")
        return tf_config_output
