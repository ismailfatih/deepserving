import aiohttp
import asyncio
from io import BytesIO
from app.ml_model import MlModel, Configuration
from injector import Module, provider, Injector, inject, singleton, InstanceProvider
from pathlib import Path


class ClassificationConfiguration(Configuration):
    def __init__(self, config_path):
        """ Configuration class for MLModel """
        self.config_path = config_path


class ClassificationModel(MlModel):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def setup_model(self):
        pass

    def inference(self, input):
        return {"result": 1}

    def inference_detailed(self, input):
        return {"result": 1, "details": {"0": 1, "1": 0}}


class ClassificationModelModule(Module):
    def configure(self, binder):
        configuration = ClassificationConfiguration(Path(__file__).parent)
        binder.bind(Configuration, to=configuration, scope=singleton)

    @singleton
    @provider
    def provide_inference_model(self, configuration: Configuration) -> MlModel:
        model = ClassificationModel(configuration)
        return model


injector = Injector([ClassificationModelModule()])
inference_model = injector.get(MlModel)
inference_model.setup_model()
