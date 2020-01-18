# Meme_Keyboard
Python Script that will play a vine or meme video related to the key that was pressed. Put it on a friends computer and see the chaos that comes. For HackWPI best meme category. 


# Installation

```bash
pip3 install opencv-python
pip3 install ffpyplayer
pip3 install keyboard
```
# Usage

Download memekeyboard.py and the download the memes and then place the memes in the same directory as the .py file. If you want to use your own videos at the top of the program just change the name of the .mp4 file that is in the differnt key variables.

# Issues

If the video resolution is too large the video and the audio come out of sync. It is apparently hard to play a video from python so we had to use opencv and ffpyplayer to sync the audio and video. It is still choppy at times.
Another issue is that on mac the cv2.destroyAllWindows has a bug where is does not close the window when used in certain applications. This happens to be one of those applications because whenever we used that line it would crash the program so we removed it and just reused the window that was already open for the previous video played. If you really wanted to be evil you could have it spawn new windows whenever a new video is played to slow down the persons computer but its up to you. 
