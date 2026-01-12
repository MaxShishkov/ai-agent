import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Check that target_file falls withing absolute path of working_directory
        try:
            valid_target_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        except ValueError:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        
        if args:
            command.extend(args)
            
        completed_process = subprocess.run(
            args=command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )
        
        output_string = ""
        
        if completed_process.returncode:
            output_string += f"Process exited with code {completed_process.returncode}\n"
            
        if completed_process.stdout:
            output_string += f"STDOUT: {completed_process.stdout}\n"
        elif completed_process.stderr:
            output_string += f"STDERR: {completed_process.stderr}\n"
        else:
            output_string += "No output produced\n"
        
        return output_string
    
    except Exception as e:
        return f"Error: executing Python file: {type(e).__name__}: {e}"