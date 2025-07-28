import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
  wd_abs_path = os.path.abspath(working_directory)
  file_abs_path = os.path.abspath(os.path.join(wd_abs_path, file_path))

  if not file_abs_path.startswith(wd_abs_path):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if not os.path.isfile(file_abs_path):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  try:
    file_content_string = ""
    with open(file_abs_path, "r") as f:
      file_content_string = f.read(MAX_CHARS)
      if os.path.getsize(file_abs_path) > MAX_CHARS:
        file_content_string = file_content_string + f'\n[...File "{file_path}" truncated at 10000 characters]'
    return file_content_string
  except Exception as e:
    return f'Error reading file "{file_path}": {e}'
