from website import create_app
import socket
import os

flask_env = os.getenv("FLASK_ENV", "development")

if flask_env == "deployment":
    port = int(os.getenv("PORT", 5000))

    app = create_app()

    if __name__ == '__main__':
        print(f"Website is live at: https://geosenseassist-3f7440326683.herokuapp.com/")
        app.run(host='0.0.0.0', port=port, debug=True) 
else:
    # Local Development Configuration
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"Your local IP: {local_ip}")

    app = create_app()

    if __name__ == '__main__':
        print(f"Access the app at: http://{local_ip}:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
