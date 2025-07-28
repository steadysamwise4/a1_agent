import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  wd_abs_path = os.path.abspath(working_directory)
  file_abs_path = os.path.abspath(os.path.join(wd_abs_path, file_path))

  if not file_abs_path.startswith(wd_abs_path):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  if not os.path.exists(file_abs_path):
    return f'Error: File "{file_path}" not found.'
  if not os.path.splitext(file_abs_path)[1].lower() == '.py' and os.path.isfile(file_abs_path):
    return f'Error: "{file_path}" is not a Python file.'
  try:
    commands = ["python", file_path]
    if args:
      commands.extend(args)
    completed_process = subprocess.run(
      commands, 
      capture_output=True, 
      text=True,
      cwd=wd_abs_path, 
      timeout=30)
    rtncode_msg = ""
    output = []
    if completed_process.stdout:
      output.append(f"STDOUT:\n{completed_process.stdout}")
    if completed_process.stderr:
      output.append(f"STDERR:\n{completed_process.stderr}")

    if completed_process.returncode != 0:
      output.append(f"Process exited with code {completed_process.returncode}")

    return "\n".join(output) if output else "No output produced."
  except Exception as e:
      return f"Error running file: {e}"