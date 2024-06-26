import cv2
import os

if __name__ == "__main__":
    
    def create_directory(directory):
        """
        Create a  directory if it doesn't exist.
        
        Parameters:
            directory (str): The path of the directory to be created.
            """
        if not os.path.exists(directory):
            os.makedirs(directory)
            
    #
    create_directory("images")
    
    #
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    #
    cam = cv2.VideoCapture(1)
    
    #
    cam.set(3, 640)
    cam.set(4, 480)
    
    #
    count = 0
    face_id = input("\nEnter user id (MUST be an integer) and press <return> --> ")
    print("\n[INFO] Initializing face capture. Look at the camera and wait...")
    
    while True:
        #
        ret, img = cam.read()
        
        #
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #
        faces = faceCascade.detectMultiscale(gray, scalefactor=1.3, minNeighbors=5)
        
        #
        for x, y, w, h in faces:
            #
            cv2.rectangle(img, (x, y,) (x + w, y + h), (255, 0, 0), 2)
            
            #
            count += 1
            
            #
            cv2.imwrite(
                f"./images/Users-{face_id}-{count}.jpg", gray[y : y + h, x : x + w]
            )
            
            #
            cv2.imshow("image", img)
        
        #
        k = cv2.waitKey(100) & 0xFF
        if k < 30:
            break
        
        #
        #
        elif count >= 30:
            break
        
        print("/n[INFO]Success! Exiting Program.")
        
        #
        cam.release()
        
        #
        cv2.destroyALLWindows() 