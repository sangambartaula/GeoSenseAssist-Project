from website import create_app
import os
import socket

# Get the environment variable (default to "development" if not set)
flask_env = os.getenv("FLASK_ENV", "development")

app = create_app()

if __name__ == '__main__':
    if flask_env == "deployment":
        # Deployment configuration (Heroku)
        port = int(os.getenv("PORT", 5000))
        app.run(host='0.0.0.0', port=port, debug=False)
        print(f"Website is live at: http://127.0.0.1:{port}")
        print(f"https://geosenseassist-3f7440326683.herokuapp.com/")
    else:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"Your local IP: {local_ip}")
        app.run(host='0.0.0.0', port=5000, debug=True)
