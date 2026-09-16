# 👗 Fashion MNIST Image Classification

A deep learning project that classifies grayscale images of clothing items into 10 categories using a fully connected (Dense) neural network built with TensorFlow/Keras.

## 📌 Overview

This project trains a neural network on the **Fashion MNIST** dataset to recognize 10 types of clothing items from 28x28 grayscale images. It covers the complete ML workflow — data preprocessing, model building, training, evaluation, and single/batch prediction checks.

## 📊 Dataset

- **Source:** [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) (via `tf.keras.datasets.fashion_mnist`)
- **Size:** 60,000 training images + 10,000 test images
- **Image dimensions:** 28x28 pixels, grayscale
- **Classes (10):**

| Label | Class |
|-------|-------|
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

## 🧠 Model Architecture

A simple **Dense (fully connected) Neural Network**:

- Input layer — flattened 28x28 pixel image (784 input features)
- One or more hidden Dense layers with ReLU activation
- Output layer — 10 units with Softmax activation (one probability per class)

Trained using the Adam optimizer with sparse categorical crossentropy loss.

## 📈 Results

- **Test Accuracy:** ~89%

The model correctly classifies the majority of clothing items, with most confusion occurring between visually similar classes (e.g., Shirt vs. T-shirt/top vs. Pullover/Coat).

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib (for visualizing predictions)

## 🚀 Getting Started

### Prerequisites
```bash
pip install tensorflow numpy matplotlib
```

### Run the notebook
1. Clone this repository
   ```bash
   git clone https://github.com/ZainAliKhanZK/<repo-name>.git
   cd <repo-name>
   ```
2. Open `MNIST_Fashion_Dataset.ipynb` in Jupyter Notebook or Google Colab
3. Run all cells to train the model and view predictions

## 🔍 Making Predictions

The notebook includes code to run predictions on the test set and compare predicted labels against actual labels, both for a single image and in batch, along with visual output using Matplotlib.

## 📁 Project Structure

```
├── MNIST_Fashion_Dataset.ipynb   # Main notebook: preprocessing, model, training, evaluation
├── README.md                     # Project documentation
```

## 🔮 Future Improvements

- [ ] Experiment with a CNN architecture to improve accuracy
- [ ] Add dropout/batch normalization for better generalization
- [ ] Hyperparameter tuning (learning rate, hidden units, epochs)
- [ ] Deploy as an interactive Streamlit app for live predictions
- [ ] Add a confusion matrix and per-class precision/recall report

## 👤 Author

**Zain Ali Khan**
AI Student | Building an ML Portfolio
- GitHub: [@ZainAliKhanZK](https://github.com/ZainAliKhanZK)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
