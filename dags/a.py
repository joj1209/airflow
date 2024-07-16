import os
from pathlib import Path

# print(os.urandom(16))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR1 = Path(__file__).resolve()
BASE_DIR2 = Path(__file__).resolve().parent
BASE_DIR3 = Path(__file__).resolve().parent.parent
BASE_DIR4 = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR1)
print(BASE_DIR2)
print(BASE_DIR3)
print(BASE_DIR4)