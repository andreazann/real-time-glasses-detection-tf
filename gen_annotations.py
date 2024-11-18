import os
import subprocess

WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = os.path.join(WORKSPACE_PATH, 'annotations')
IMAGE_PATH = os.path.join(WORKSPACE_PATH, 'images')
MODEL_PATH = os.path.join(WORKSPACE_PATH, 'models')
PRETRAINED_MODEL_PATH = os.path.join(WORKSPACE_PATH, 'pre-trained-models')
CONFIG_PATH = os.path.join(MODEL_PATH, 'my_ssd_mobnet', 'pipeline.config')
CHECKPOINT_PATH = os.path.join(MODEL_PATH, 'my_ssd_mobnet')

labels = [{'name': 'Glasses', 'id': 1}, {'name': 'NoGlasses', 'id': 2}]

# Creazione del file label_map.pbtxt
with open(os.path.join(ANNOTATION_PATH, 'label_map.pbtxt'), 'w') as f:
    for label in labels:
        f.write('item {\n')
        f.write('\tname: \'{}\'\n'.format(label['name']))
        f.write('\tid: {}\n'.format(label['id']))
        f.write('}\n')

# Comandi per eseguire gli script Python esterni
subprocess.run(['python', os.path.join(SCRIPTS_PATH, 'generate_tfrecord.py'),
                '-x', os.path.join(IMAGE_PATH, 'train'),
                '-l', os.path.join(ANNOTATION_PATH, 'label_map.pbtxt'),
                '-o', os.path.join(ANNOTATION_PATH, 'train.record')])

subprocess.run(['python', os.path.join(SCRIPTS_PATH, 'generate_tfrecord.py'),
                '-x', os.path.join(IMAGE_PATH, 'test'),
                '-l', os.path.join(ANNOTATION_PATH, 'label_map.pbtxt'),
                '-o', os.path.join(ANNOTATION_PATH, 'test.record')])
