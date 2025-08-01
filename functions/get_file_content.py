import os
from config import MAX_CHARS
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
  parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
          "file_path": types.Schema(
              type=types.Type.STRING,
              description="The path to the file whose content should be read, relative to the working directory.",
          ),
      },
  ),
)
