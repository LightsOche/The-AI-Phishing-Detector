# The AI Phishing Detector

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)

## 🔍 Overview

**The AI Phishing Detector** is an AI-powered project that helps identify whether a given URL is legitimate or a phishing attempt. It leverages machine learning (Logistic Regression) and Natural Language Processing (TF-IDF Vectorization) to analyze URLs and classify them as safe or malicious.

Designed as part of the **3MTT Knowledge Showcase (Cybersecurity Track)**, this tool aims to demonstrate how machine learning can contribute to cybersecurity by preventing phishing attacks.

---

## 🚀 Features

* Accepts raw URLs or data from `.csv` files
* Preprocesses and vectorizes input using TF-IDF
* Trains a Logistic Regression classifier
* Predicts whether a URL is phishing or legitimate
* Includes a web UI built with Streamlit for easy interaction

---

## 🧰 Tools & Technologies

* Python 3.10+
* Scikit-learn
* Pandas & NumPy
* Streamlit
* Git & GitHub

---

## 📁 Project Structure

```
AI-Phishing-Detection/
├── app.py                      # Streamlit web app
├── phishing_data.csv          # Dataset used
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
├── .gitignore
├── scripts/
│   ├── load_data.py           # Load data functions
│   ├── preprocess_data.py     # TF-IDF and preprocessing
│   ├── train_model.py         # Train and save model
│   └── test_model.py          # Evaluate/test model
└── data/
    └── phishing_data.csv      # Dataset folder
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/LightsOche/The-AI-Phishing-Detector.git
cd The-AI-Phishing-Detector
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📊 Model Training

To train or retrain the model, use the `scripts/train_model.py` file.

```bash
python scripts/train_model.py
```

This will train a Logistic Regression model and save it as `phishing_model.pkl` for future use in the app.

---

## 🧪 Testing

The `scripts/test_model.py` file contains code to load the saved model and test it against new or test URLs.

```bash
python scripts/test_model.py
```

---

## 🖥️ Web UI with Streamlit

Launch the Streamlit app using:

```bash
streamlit run app.py
```

* Paste a URL into the input box
* Click **"Check URL"**
* Instantly see if it’s **legitimate** or **phishing**

---

## 📸 Screenshots

> *(Add screenshots of the Streamlit interface and results after launching the app)*

---

## 📚 Dataset Source

* [Open Phishing Datasets](https://data.world/datasets/phishing) *(or indicate your own curated CSV)*

---

## 📌 Future Improvements

* Use more advanced models like Random Forest or XGBoost
* Add live URL scraping for real-time predictions
* Deploy on cloud using Streamlit Cloud, Heroku, or AWS

---

## 🤝 Contributions

Pull requests are welcome! If you’d like to contribute, please fork the repo and submit a PR.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🧠 Author & Acknowledgements

**Project by:** [Lights Oche](https://github.com/LightsOche)

## 📽️ Demo Video

Watch the full demo of the AI Phishing Detection project:

👉 [Click here to watch on Google Drive](https://drive.google.com/file/d/1sLjLej_zu8LCpXsTsZQ3qbHl4fnKmvXO/view?usp=sharing)

Special thanks to:

* 3MTT Cybersecurity Track
* Python and Open Source community

---

> 🚀 Ready to stop phishing in its tracks with AI!
