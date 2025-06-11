import os

def get_file_content(working_directory, file_path):
    abs_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    try:
        if not abs_file_path.startswith(abs_work_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        MAX_CHARS = 10001

        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) > 10000:
            return f'{file_content_string[:10000]}[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_string
        
    except Exception as e:
        return f'Error: {e}'

