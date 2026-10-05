import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path='p:/P/Projects/CropApp/cropapp/assets/model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print('--- INPUT ---')
for i in input_details:
    print(f"Name: {i['name']}, Shape: {i['shape']}, Type: {i['dtype']}")

print('\n--- OUTPUT ---')
for o in output_details:
    print(f"Name: {o['name']}, Shape: {o['shape']}, Type: {o['dtype']}")
