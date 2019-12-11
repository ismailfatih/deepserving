import uvicorn
import sys
from classification_model import inference_model
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse, PlainTextResponse
from starlette.staticfiles import StaticFiles


def create_app():
    app = Starlette()
    app.add_middleware(CORSMiddleware,
                       allow_origins=["*"],
                       allow_headers=["X-Requested-With", "Content-Type"])

    @app.route("/")
    async def homepage(request):
        return PlainTextResponse("Server")

    @app.route("/predic/{input}", methods=["GET"])
    async def analyze(request):
        sentence = request.path_params["input"]
        prediction = inference_model.predict(sentence)[0]
        return JSONResponse(prediction)

    @app.route("/predict-details/{input}", methods=["GET"])
    async def analyze_details(request):
        sentence = request.path_params["input"]
        prediction = inference_model.predict_detailed(input)
        return JSONResponse(prediction)

    return app
