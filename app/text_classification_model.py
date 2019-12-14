import aiohttp
import asyncio
from io import BytesIO
from interfaces.ml_model import MlModel, Configuration
from injector import Module, provider, Injector, inject, singleton, InstanceProvider
from pathlib import Path

__all__ = ["TextClassificationModelModule"]


class TextClassificationConfiguration(Configuration):
    def __init__(self, config_path):
        """ Configuration class for MLModel """
        self.config_path = config_path


class TextClassificationModel(MlModel):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def setup_model(self):
        self.configuration = self.configuration

    def predict(self, input):
        return {"result": 1, "details": {"0": 1, "1": 0}}


class TextClassificationModelModule(Module):
    def configure(self, binder):
        configuration = TextClassificationConfiguration(Path(__file__).parent)
        binder.bind(Configuration, to=configuration, scope=singleton)

    @singleton
    @provider
    def provide_ml_model(self, configuration: Configuration) -> MlModel:
        model = TextClassificationModel(configuration)
        return model
