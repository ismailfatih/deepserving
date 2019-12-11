import uvicorn
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

    @app.route("/{data}")
    async def homepage(request):
        data = request.path_params["data"]
        prediction = inference_model.predict_detailed(input)
        return JSONResponse(prediction)

    @app.route("/predict/{data}", methods=["GET"])
    async def analyze(request):
        data = request.path_params["data"]
        prediction = inference_model.predict(data)
        return JSONResponse(prediction)

    return app
