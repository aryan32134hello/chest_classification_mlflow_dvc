import os
import urllib.request as requests
from zipfile import ZipFile
import tensorflow as tf
import keras
from CNNChestClassifier.entity.config_entity import BaseModelConfig
from pathlib import Path

class PrepareBaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config = config
        
    @staticmethod
    def save_model(path:Path,model:keras.Model):
        model.save(path)

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(include_top=self.config.params_include_top,
        weights=self.config.params_weight,
        input_shape=self.config.params_image_size
        )
        self.save_model(path = self.config.base_model_path,model=self.model)
    @staticmethod
    def _prepare_full_model(base_model,classes,learning_rate):
        base_model.trainable = False
        model = keras.Sequential()
        model.add(base_model)
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(units=classes,activation='softmax'))
        
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        metrics=['accuracy'],
        loss=tf.losses.CategoricalCrossentropy())

        model.summary()

        return model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(base_model=self.model,
        classes=self.config.params_classes,
        learning_rate = self.config.params_learning_rate
        )

        self.save_model(path=self.config.base_updated_model_path,model=self.full_model)