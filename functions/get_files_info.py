import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # Check that target_dir falls withing absolute path of working_directory
        try:
            valid_target_path = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        except ValueError:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not valid_target_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        files = os.listdir(target_dir)
        files_metadata = []
        for file in files:
            abs_file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(abs_file_path)
            is_dir = os.path.isdir(abs_file_path)
            files_metadata.append(
                f'- {file}: file_size={file_size} bytes, is_dir={is_dir}'
                )
            
        return "\n".join(files_metadata)
    
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"