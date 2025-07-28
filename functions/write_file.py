import os

def write_file(working_directory, file_path, content):
  wd_abs_path = os.path.abspath(working_directory)
  file_abs_path = os.path.abspath(os.path.join(wd_abs_path, file_path))

  if not file_abs_path.startswith(wd_abs_path):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  if not os.path.exists(file_abs_path):
    try:
      dir_name = os.path.dirname(file_abs_path)
      os.makedirs(dir_name, exist_ok=True)
    except Exception as e:
      return f"Error creating files: {e}"
  if os.path.exists(file_abs_path) and os.path.isdir(file_abs_path):
    return f'Error: "{file_path}" is a directory, not a file'

  try:
    with open(file_abs_path, "w") as f:
      f.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
      return f"Error writing to file: {e}"