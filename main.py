import speaker
import time

def main():
    i=1
    said = False
    while True:
        localtime = time.asctime(time.localtime(time.time())).split(' ')[4]
        print(localtime)
        hours = int(localtime.split(":")[0])
        minutes = int(localtime.split(":")[1])
        seconds = int(localtime.split(":")[2])
        if(minutes == 00 and said==False):
            said = True
            i=i+1
            fileName = 'logs/'+str(i)+'.mp3'
            sayit = "Hello Sir, Its me, Zira, girlfriend of Jarvis, at your service sir. Its been "+localtime+" and You should probably take a break"
            speaker.convertTTS(sayit, fileName)
            speaker.speak(fileName)

main()
