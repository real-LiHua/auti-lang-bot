import fasttext


model = fasttext.load_model()
print(model.predict("Hello, world!"))
