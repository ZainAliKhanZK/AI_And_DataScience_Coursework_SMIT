import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Fashion MNIST Classifier",
    page_icon="👕"
)

st.title("👕 Fashion-MNIST Classifier")

class_names = [
    "T-shirt / Top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle Boot"
]


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "mnist_fashion_model.keras"
    )


model = load_model()


from PIL import Image, ImageOps
import numpy as np


def preprocess_image(image):

    # 1. Convert to grayscale
    image = image.convert("L")

    # 2. Convert to numpy
    img = np.array(image)

    # 3. Detect non-white pixels
    mask = img < 240

    # If foreground exists
    if np.any(mask):

        rows = np.any(mask, axis=1)
        cols = np.any(mask, axis=0)

        ymin, ymax = np.where(rows)[0][[0, -1]]
        xmin, xmax = np.where(cols)[0][[0, -1]]

        # 4. Crop around object
        image = image.crop(
            (xmin, ymin, xmax + 1, ymax + 1)
        )

    # 5. Resize while maintaining aspect ratio
    image.thumbnail((20, 20))

    # 6. Create 28x28 black canvas
    canvas = Image.new(
        "L",
        (28, 28),
        0
    )

    # 7. Center object
    x = (28 - image.width) // 2
    y = (28 - image.height) // 2

    canvas.paste(image, (x, y))

    # 8. Convert to numpy
    img_array = np.array(
        canvas
    ).astype("float32")

    # 9. Normalize
    img_array = img_array / 255.0

    # 10. Flatten
    img_array = img_array.reshape(
        1, 784
    )

    return img_array



uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image, width=300)

    # Let user choose inversion
    invert = st.checkbox(
        "Invert image",
        value=False
    )

    image_array = preprocess_image(image)

    st.subheader("What the Model Sees")

    st.image(
    image_array.reshape(28, 28),
    width=250
    )


    # Show exactly what model sees
    st.subheader("Image Given to Model")

    model_image = image_array.reshape(28, 28)

    st.image(
        model_image,
        width=200,
        clamp=True
    )

    # Prediction
    prediction = model.predict(
        image_array,
        verbose=0
    )

    probabilities = prediction[0]

    predicted_index = np.argmax(probabilities)

    predicted_class = class_names[predicted_index]

    confidence = probabilities[predicted_index] * 100

    st.subheader("Prediction")

    st.success(
        f"### {predicted_class}"
    )

    st.write(
        f"Confidence: **{confidence:.2f}%**"
    )

    # All predictions
    st.subheader("All Class Probabilities")

    for i in np.argsort(probabilities)[::-1]:

        probability = probabilities[i] * 100

        st.write(
            f"{class_names[i]}: **{probability:.2f}%**"
        )

        st.progress(
            min(int(probability), 100)
        )
