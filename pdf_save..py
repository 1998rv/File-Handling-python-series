# Developer Name :- Ravi Kumawat
# Date :- 08-11-2023
# Code :- To write pdf file in our pc

from pathlib import Path # =========== moduls make a file name =============
import requests          # ==================== moduls import request ======

filename = Path('metadata.pdf') #===================== file name ===========
url = 'https://www.kapsarc.org/file-download.php?i=200175.pdf'
response = requests.get(url)
filename.write_bytes(response.content)
