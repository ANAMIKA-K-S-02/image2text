import os
import streamlit as st
from gradio_client import Client
import shutil
import time

save_dir=r"C:\Users\anami\OneDrive\Documents\Desktop\image2text"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
client=Client("black-forest-labs/FLUX.1-schnell")

st.sidebar.title("IMAGE GENERATION PROMPT")
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            min-width: 400px;
            max-width: 400px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
prompt=st.sidebar.text_area('Enter Your Prompt:',"")

generate_image=st.sidebar.button("Generate Image")

if generate_image:
    if prompt:
        progress_bar=st.progress(0)
        st.info("Generating your image,please wait...")

        for percent_complete in range(0,100,20):
            time.sleep(0.5)
            progress_bar.progress(percent_complete)

        result=client.predict(
            prompt=prompt,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            num_inference_steps=4,
            api_name="/infer"
        )

        progress_bar.progress(100)

        image_path=result[0]

        save_path=os.path.join(save_dir,"generated_image.webp")

        shutil.move(image_path,save_path)

        st.image(save_path,caption="Generated Image",use_container_width=True)

        #provide the edownload link

        with open(save_path,"rb")as file:
            st.download_button(
                label="Download Image",
                data=file,
                file_name="generated_image.webp",
                mime="image/webp"
             )
        st.success(f"Image Successfully Generated and Saved at:{save_path}")
            
    else:
        st.error("Please enter a prompt to generate the image.")