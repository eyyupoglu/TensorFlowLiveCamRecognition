import subprocess

def pushPictureToGithub(fileName):
    try:
        subprocess.call("(git pull)", shell=True)
        subprocess.call("(git add )" + fileName, shell=True)
        subprocess.call("(git commit -m \"asdasd\")", shell=True) 
        subprocess.call("(git push)", shell=True)
    except:
        print("could not push picture")

pushPictureToGithub("frame10.jpg")
