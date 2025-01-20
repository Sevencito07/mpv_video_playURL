from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  

channels = {
    3:"https://www.youtube.com/live/jfKfPfyJRdk?si=O0XZjQ0O06Q2_tVa",
    4: "https://www.youtube.com/live/41o_tcuJLXc?si=kd039fyFPzbn4kZR",
    5: "https://www.youtube.com/live/erUTqlcsDJI?si=3-felkBAFs_jxYp-",
    6: "https://www.youtube.com/watch?v=xRQnJyP77tY",
    7: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    8: "https://www.youtube.com/live/qguK2VjyiGc?si=-z-wBCeVfAeFt2n-",
    9: "https://www.youtube.com/live/fNjQBXADm44?si=4pjgc-Ma652psCAN",
    10: "https://www.youtube.com/live/2WKf5DkLjz4?si=STB8HeaPPFdPHO-X",
    11: "https://www.youtube.com/live/0zMi6kHo19o?si=_g3uqTHseRuNEQBh",
    12:"https://www.youtube.com/live/V4C7VNfRATA?si=2jC3jbOIA3bYfnhx",
    13:"https://www.youtube.com/live/6PUEYnYDE-A?si=CDQzk3zZ7lGVeHYv",
    14:"https://la12hd.com/vivo/canales.php?stream=foxsports",
}

@app.route('/ch', methods=['POST'])
def handle_ch():
    print("running")
    data = request.get_json()
    print("data client:", data)
    
   # chanel_number = data.get("chanel_number")
    chanel_number = data;
    if chanel_number is None:
        return "error", 400
    
    try:
        chanel_number = int(chanel_number)
        if chanel_number in channels:
            print("executing video")
            print(channels[chanel_number])
            os.system(f"pkill mpv")
            os.system(f"mpv {channels[chanel_number]}")
        else:
            return "not chanel found", 404
    except ValueError:
        return "invalid number", 400
    
    return "executing function", 200







@app.route('/url', methods=['POST'])
def handle_url():
    print("prueba function")
    data = request.get_json()
    print("Data recived:", data)
   # chanel_number = data.get("chanel_number")
    url_video = data.get("url");
    if url_video is None:
        return "Número de canal no proporcionado", 400

    try:
        url_video = str(url_video)
        if url_video.startswith("http"):
            os.system(f"pkill mpv")
            os.system(f"mpv {url_video}")
        else:
            return "Chanel not found", 404
    except ValueError:
        return "invalid number", 400

    return "executing function", 200




@app.route('/volumen_up', methods=['POST'])
def  volumen_up():
    try:
            os.system(f"pactl set-sink-volume @DEFAULT_SINK@ +20%")
    except ValueError:
        return "invalid post", 400

    return "executing function", 200


@app.route('/volumen_down', methods=['POST'])
def  volumen_down():
    try:
            os.system(f"pactl set-sink-volume @DEFAULT_SINK@ -20%")
    except ValueError:
        return "invalid post", 400

    return "executing function", 200





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
