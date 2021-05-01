import os

os.chdir('D:/Data/PostgreSQL_EssT')

for f in os.listdir():
    file_name,file_ext = os.path.splitext(f)
    file_ext = '.mp4'
    new_name = f'{file_name}{file_ext}'
    os.rename(f,new_name)


