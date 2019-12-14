from injector import Injector
from text_classification_model import *
from interfaces.ml_model import MlModel

injector = Injector([TextClassificationModelModule()])
inference_model = injector.get(MlModel)
inference_model.setup_model()