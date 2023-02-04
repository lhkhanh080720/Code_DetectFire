from libs import *
import multiprocessing

# Real Camera
camera_id = "/dev/video1"
videoCapture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
# Zoom Camera
camID = "/dev/video2"
cam = cv2.VideoCapture(camID)
# Wait a second to let the port initialize
time.sleep(1)

def process_frame(cap, window_name, indx):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(window_name, frame)
        cv2.moveWindow(window_name, indx, 0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()

if __name__ == '__main__':
    camera_ids = [cam, videoCapture]
    window_names = ['Zoom Cam', 'Real Cam']
    window_index = [0, 650]

    processes = [multiprocessing.Process(target=process_frame, args=(camera_ids[i],  window_names[i][0], window_index[i], )) for i in range(2)]
    [process.start() for process in processes]
    [process.join() for process in processes]