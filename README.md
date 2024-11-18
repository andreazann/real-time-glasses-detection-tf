# real-time-glasses-detection-tf

# Instructions for use
## Environment Setup

1. Create a conda environment with `conda create --name [env_name] -r [requirements.txt]`. Download here the requirements.txt
2. Enable CUDA and CuDNN for faster training

## Generating custom images and labels for training

1. Produce at least 40-50 images. Half of them wearing something (such as sunglasses, face masks, hats) and the other half removing it.
2. Open /Tensorflow/labelImg/labelImg.py with `python /Tensorflow/labelImg/labelImg.py`
3. Once the program opens, click on the "Open dir" button and selected the folder where all the images producted are located
4. Click on "Change Save dir" and make sure it's the same directory as "Open dir"
5. Click on View -> Auto Save Mode
6. Press "W" and draw a label on top of the area where the object needs to be detected
7. Name the label, accordignly. In my case, naming it "Glasses" if the glasses are on, or "NoGlasses" if they aren't
8. Go to the next image pressing "D" and repat point 7 until all images are marked with labels
9. Close the application
10. Select the couples of images and labels produced as xml files. Move approx 90% of them in `\Tensorflow\workspace\images\train` folder and the remaining 10% in the `\Tensorflow\workspace\images\test` folder. Making sure there is a good mix of "with and without object" images in both folders

## Training the model

1. Open `gen_annotation.py` in the root of the repo. Replace in line 14 "Glasses" and "NoGlasses" with the names of your labels. Save it.
2. Run `gen_annotation.py` with `python gen_annotation.py`
3. Run `update_config.py` with `python update_config.py`
4. Train the model with `python Tensorflow/models/research/object_detection/model_main_tf2.py --model_dir=Tensorflow/workspace/models/my_ssd_mobnet --pipeline_config_path=Tensorflow/workspace/models/my_ssd_mobnet/pipeline.config --num_train_steps=10000` where in num_train_steps you can choose how many timesteps train the model

## Run the model

1. Go to the `Tensorflow/workspace/models/my_ssd_mobnet/` folder. Check which one is the last checkpoint saved. For example `ckpt-10.index`
2. Open `detect_real_time.py` and replace line 28 `ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-11')).expect_partial()` with `ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-10')).expect_partial()`. Save the file.
3. Run `detect_real_time.py` with `python detect_real_time.py`. Wait for the webcam to open. And enjoy!
4. To close press "q"

## Extra

1. To run the model I've trained with images of myself with sunglasses (it's probably not going to work with you), use model with ckpt-11 already present in Tensorflow/workspace/models/my_ssd_mobnet/
