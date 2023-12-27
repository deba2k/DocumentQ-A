import os
os.mkdir("yourPdf")
"""
python -m venv myvenv 

myvenv\\Scripts\\activate

py pre_req.py

"""

LIBRARIES = ['accelerate', 'transformers', 'tiktoken', 'llama_index', 'pypdf', 'streamlit']

for i in LIBRARIES:
    os.system("pip install "+i)

print("All libraries successfully installed")
os.system('cls')

print("everything installed successfully")
print("now you can execute run.py in your venv")



