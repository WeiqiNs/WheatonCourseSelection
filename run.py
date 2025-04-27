"""Run the app."""

from app.application import app

if __name__ == "__main__":
    app.run(threaded=True)
