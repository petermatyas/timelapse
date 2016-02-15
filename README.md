# timelapse

I make a time lapse video based on Raspberry pi cam and raspberry pi.

The hardware is a Raspberry pi B and a Raspbery pi camera in a waterproof box. The cron execute the *cam.sh* script what take a picture in every 10 minutes and save in the SD card in YYYYmmDDHHMMSS.png format ( **Y**ear **m**onth **D**ay **H**our **M**inute **S**ecundum ).
I can log in the Raspi via serail SSH and download the pictures to USB drive.

I collect the pictures in a portable hard drive. The camera is working all day even in night I have to separate the the night pictures with the *night.py* script. After that I manually select dark and wrong pictures.

If I have the finally pictures I execute the *video.py* script to convert the pictures to video. It is working always one day pictures because in this way I need less storage and easyest to correct the errors. The script copy one day pictures to *workingFolder* resize and crop it, and write the date to the picture with **imagemagic**. After that the **ffmpeg** convert the pictures to *.mp4* format. If all days ready the ffmpeg convert to one video. The advantage of this way that I don't need to convert all picture every week. 
I can set the start and end date in the *video.py* and I can set the frame rate what define the length of final video. 












