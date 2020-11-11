from Preprocessing_Image_Data import training_data_generator


DIRECTORY = "data/train"
CLASS_MODE = "categorical"
COLOR_MODE = "grayscale"
TARGET_SIZE = (256,256)
BATCH_SIZE = 32

#Creates a DirectoryIterator object using the above parameters:

training_iterator = training_data_generator.flow_from_directory(DIRECTORY, class_mode = CLASS_MODE, color_mode = COLOR_MODE, target_size = TARGET_SIZE, batch_size = BATCH_SIZE)

# iterate over the training batches 
sample_batch_input, sample_batch_labels  = training_iterator.next()

# display its dimensions
print(sample_batch_input.shape, sample_batch_labels.shape)

# sample_batch_input = (32, 256, 256, 1):
# 32 images in a batch, each is a 256x256 pixel grayscale image

# sample_batch_labels = (32, 2): 2 for # of classes: labelled Normal [1, 0] or Pneumonia [0, 1]
