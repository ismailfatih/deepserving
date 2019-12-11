import uvicorn
import sys
from app import create_app

if __name__ == "__main__":
    if "serve" in sys.argv:
        app = create_app()
        uvicorn.run(app=app, host="0.0.0.0", port=5000, log_level="info")
