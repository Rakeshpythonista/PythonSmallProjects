import os

os.chdir('D:/Data/PostgreSQL_EssT')

for f in os.listdir():
    filename,filext = os.path.splitext(f)
    file_no,fName = filename.split(' - ')
    RepName = f'{file_no}.{fName}{filext}'
    os.replace(f,RepName)


