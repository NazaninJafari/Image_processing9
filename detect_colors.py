import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)

#width  = int(video_cap.get(3))
#height = int(video_cap.get(4))

#save_video = cv2.VideoWriter('video_detectColors.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, (width,height), 0)
#cv2.VideoWriter(file path, fourcc, fps, (w,h))

while True:
    
    ret, frame = video_cap.read()
    color = (0,0,0)

    width, height, _ = frame.shape
    frame_size = (width,height)
    #RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    not_blur = frame[190:290, 270:370]
        
    if not ret:
        break
    
    
    # Using cv2.blur() method 
    frame_blur = cv2.blur(frame, frame_size)
    frame_blur[190:290, 270:370] = not_blur
    Blue,Green,Red = cv2.split(frame_blur[190:290, 270:370])
    
    alpha = 3
    beta = 0
    
    #red_avg = round(np.average(Red))
    #green_avg = round(np.average(Green))
    #blue_avg = round(np.average(Blue))
    
    red_avg = np.mean(Red)
    green_avg = np.mean(Green)
    blue_avg = np.mean(Blue)
    
    #detect colors
    if red_avg>150 and green_avg<70 and blue_avg<70 :
        cv2.putText(frame_blur , 'Red', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )
    
    elif red_avg<100 and green_avg>200 and blue_avg<100 :
        cv2.putText(frame_blur , 'Green', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )
    
    elif red_avg<100 and green_avg<100 and blue_avg>130 :
        cv2.putText(frame_blur , 'Blue', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )
    
    elif red_avg>200 and green_avg>200 and blue_avg<90 :
        cv2.putText(frame_blur , 'Yellow', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )   
    
    elif red_avg>225 and green_avg<23 and blue_avg>145 :
        cv2.putText(frame_blur , 'Pink', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 ) 

    elif red_avg==0 and green_avg>230 and blue_avg>230 :
        cv2.putText(frame_blur , 'Turquoise', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )

    elif red_avg>190 and green_avg>190 and blue_avg>190 :
        cv2.putText(frame_blur , 'White', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )

    elif red_avg<60 and green_avg<60 and blue_avg<60 :
        cv2.putText(frame_blur , 'Black', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )

    elif 100<red_avg<200 and 100<green_avg<200 and 100<blue_avg<200 :
        cv2.putText(frame_blur , 'Gray', (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )
    

    key = cv2.waitKey(1)
    if key == 27: #Esc
        break

    cv2.imshow('detect colors', frame_blur)

video_cap.release()
cv2.destroyAllWindows()  