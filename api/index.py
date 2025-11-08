import subprocess
subprocess.Popen(["streamlit", "run", "demo.py", "--server.port", "8000", "--server.headless", "true"])
