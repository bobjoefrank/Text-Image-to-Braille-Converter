from model.serve import load_model, predict

# Load the model and the mapping.
model, mapping = load_model("model/bin")

# Make a prediction on PNG image.
print(predict("input.png", model, mapping))

