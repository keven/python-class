import time
import webbrowser

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=zqE-ultsWt0")
    break_count = break_count + 1
