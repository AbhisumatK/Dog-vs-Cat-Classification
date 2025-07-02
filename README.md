# Dog vs Cat  Classification

---

## 🚀 Live Demo

Try it out live here: [**Streamlit App**](https://abhisumat-dog-vs-cat-classification.streamlit.app/)

---

Kaggle Dataset used - https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset

---

## Table of Contents

1. [What It Does](#what-it-does)  
2. [How It Works](#how-it-works)  
3. [Quickstart](#quickstart)   
4. [Model & Performance](#model--performance)  
5. [Contributing](#contributing)  
6. [Credits](#credits)  
7. [License & Disclaimer](#license--disclaimer)

---

## What It Does

-  Classifies images as **Dog** or **Cat** with a custom CNN model.
-  Built into a slick Streamlit UI—just drag, drop, and get results.

---

## How It Works

1. **Data**: Trained on Kaggle’s Dogs vs Cats dataset (~25,000 labeled images).  
2. **Pre‑processing**: Resize to a consistent input size (e.g. 224×224), normalize pixel values, apply light augmentations.  
3. **Model**: Sequential CNN—stacked `Conv2D → MaxPool → Flatten → Dense → Sigmoid` layers.  
4. **Deployment**: Streamlit front‑end for instant inference.

---

## Quickstart

```bash
git clone https://github.com/AbhisumatK/Dog-vs-Cat-Classification.git
cd Dog-vs-Cat-Classification

python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

## Model & Performance

- **Architecture**: Custom-built **Sequential CNN**.
- **Performance**: Consistently delivers in the **near‑90 % accuracy** on validation/test datasets.  

---

## Contributing

Your ideas, pull requests, bug reports = ❤️

1. Fork → branch → build → open PR  
2. Keep commits scoped (“Add Grad‑CAM” beats “fix stuff”)  
3. Verify that `pip install -r requirements.txt` installs everything

---

## Credits

- Inspired by classic CNN tutorials (e.g., Hackers Realm’s Dogs vs Cats video guide)  
- Dataset courtesy of **Kaggle - Dogs vs Cats**  
- Built with 💻 **TensorFlow/Keras** and **Streamlit**

---

## License & Disclaimer

**MIT License**

**Disclaimer**: Educational/demo use only. Not for real-world veterinary diagnosis—consult a professional vet.
