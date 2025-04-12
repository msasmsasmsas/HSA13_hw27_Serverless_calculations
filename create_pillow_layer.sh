#!/bin/bash

LAYER_DIR="python"

rm -rf $LAYER_DIR
mkdir -p $LAYER_DIR

pip install -r requirements.txt -t $LAYER_DIR

zip -r pillow_layer.zip $LAYER_DIR
rm -rf $LAYER_DIR

echo "Lambda Layer pillow_layer.zip готов к загрузке в AWS"
