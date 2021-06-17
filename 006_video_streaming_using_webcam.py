from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('indexvideo.html')

def generate_frames():
    while True:
        success,frame = camera.read()
        # read() returns two values
        # a boolean value to indicate if the video capture was successful or not
        # The frame

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg',frame)
            # We have to encode the frame into jpg or img or png format
            # imencode() returns
            frame = buffer.tobytes()
            # Have to convert the frame from compressed buffer memory into bytes

        yield(b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        # This yield() is an alterntive to return without breaking the loop

@app.route('/video')
def video():
    # Response is some kind of response we want to send in a continuous manner
    # This function will take all the frames from our webcam
    # and send them to "indexvideo.html" as response
    # since "indexvideo.html" is calling "video" route
    return Response(generate_frames(),mimetype="multipart/x-mixed-replace; boundary=frame")
    # Whenever we are passing a function we need to set some mimetype

if __name__ == "__main__":
    app.run(debug=True)