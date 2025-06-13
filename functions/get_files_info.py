import os
def get_files_info(working_directory, directory=None):
    try:
        abs_working_path = os.path.abspath(working_directory)
        if directory is None:
            directory = ""
        abs_path = os.path.abspath(os.path.join(working_directory, directory))

        # print(abs_working_path)
        # print(abs_path)

        if not os.path.isdir(abs_path): 
            return f'Error: "{directory}" is not a directory'
        if not abs_path.startswith(abs_working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        content_list = os.listdir(abs_path)

        result_list = []
    
        for content in content_list:
            # 파일 경로 
            content_path = os.path.join(abs_path, content)
            # 파일 크기
            content_size = os.path.getsize(content_path)
            # 파일 정보
            content_is_dir = os.path.isfile(content_path)
        
            result_list.append(f"{content}: file_size={content_size} bytes, is_dir={not content_is_dir}")
        

        if len(result_list) > 0:
            result_str = "\n".join(result_list)
            return result_str

    except Exception as e:
        return f"Error: {e}"
    # - 이런 포맷으로 리턴
    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False
    



    