import os
from google.genai import types

def get_files_info(working_directory, directory="."):
  wd_abs_path = os.path.abspath(working_directory)
  dir_abs_path = os.path.abspath(os.path.join(wd_abs_path, directory))
  is_in_wd = dir_abs_path.startswith(wd_abs_path)
  is_directory = os.path.isdir(dir_abs_path)
  if not is_in_wd:
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  if not is_directory:
    return f'Error: "{directory}" is not a directory'
  try:

    directory_contents_list = os.listdir(dir_abs_path)
  
    result_string = ""
    for item in directory_contents_list:
      item_abspath = os.path.join(dir_abs_path, item)
      is_dir = os.path.isdir(item_abspath)
      file_size = os.path.getsize(item_abspath)
      result_string = result_string + "\n" + f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
    return result_string
  except Exception as e:
    return f"Error listing files: {e}"

schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
          "directory": types.Schema(
              type=types.Type.STRING,
              description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
          ),
      },
  ),
)