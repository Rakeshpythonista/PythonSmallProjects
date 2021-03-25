import os

def main():
    i = 0
    path = "D:/Rakesh_GIT/PythonSmallProjects/FacebookGIETImages/"
    for filename in os.listdir(path):
        new_name = "GIET" + str(i) + ".jpg"
        my_source =path + filename
        new_name =path + new_name
        os.rename(my_source , new_name)
        i += 1

if __name__ == '__main__':
    main()

