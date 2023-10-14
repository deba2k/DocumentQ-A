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
print('#'*100)

os.system('python doc.py')



