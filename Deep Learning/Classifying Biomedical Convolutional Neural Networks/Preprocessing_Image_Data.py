from tensorflow.keras.preprocessing.image import ImageDataGenerator

#Creates an ImageDataGenerator:
training_data_generator = ImageDataGenerator(rescale = 1.0 / 255, zoom_range = 0.2, rotation_range = 15, width_shift_range = 0.05, height_shift_range = 0.05)

# rescale: pixel normalisation: CNNs struggle with larger integer values
# A common way to augment image data is to flip or randomly shift each image by small amounts. 


#Prints its attributes:
print(training_data_generator.__dict__)

