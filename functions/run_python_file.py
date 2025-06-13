import os
import subprocess


def run_python_file(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run(
            args=["python3", abs_file_path],
            timeout=30,
            stdout=True,
            stderr=True,
            cwd=working_directory,
            check=True,
        )

        if not completed_process:
            return "No output produced"

        formatted_stdout = f"STDOUT: {completed_process.stdout}"
        formatted_stderr = f"STDERR: {completed_process.stderr}"

        return f"{formatted_stdout}\n{formatted_stderr}"

    except subprocess.CalledProcessError as e:
        return f"Process exited with code X {e}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

