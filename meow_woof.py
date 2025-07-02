import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

@st.cache_resource
def load_my_model():
    return load_model("model.h5")

model = load_my_model()
st.title("Dogs vs Cats Classifier")

_, H, W, C = model.input_shape

color_mode = "rgb" if C == 3 else "grayscale"

uploaded_file = st.file_uploader("Upload an image...", type=["jpg","jpeg","png"])
if uploaded_file:
    
    img = image.load_img(
        uploaded_file,
        target_size=(H, W),
        color_mode=color_mode
    )
    
    x = image.img_to_array(img) / 255.0                     # shape: (H, W, C)
    x = np.expand_dims(x, axis=0)                           # shape: (1, H, W, C)
    
    preds = model.predict(x)[0]
    
    
    if preds.shape == (1,) or np.isscalar(preds):
        score = float(preds)                               
        label = "Dog" if score > 0.5 else "Cat"
        
        st.write(f"**Prediction:** {label}   ({score:.3f})")
    else:
        
        idx = np.argmax(preds)
        st.write(f"**Predicted class #{idx}** (conf={preds[idx]:.3f})")

    st.image(img, caption=label if 'label' in locals() else None, use_container_width=True)
