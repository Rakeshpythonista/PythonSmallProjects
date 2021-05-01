import os

path = "D:/Rakesh_GIT/PythonSmallProjects/FacebookGIETImages/"

i = 0
for filename in os.listdir(path):
    new_name = "GIET{i}.jpg".format(i)
    os.rename(filename , new_name)
    i += 1


