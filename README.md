Text-to-Image Generation using Streamlit & Gradio

🚀 Project Overview
This project is a Text-to-Image Generator that transforms textual descriptions into AI-generated images using Streamlit and Gradio API. The user provides a text prompt, and the application generates an image based on that prompt. The generated image can be saved and downloaded for further use.

🛠 Tech Stack
Python: Main programming language
Streamlit: For building the interactive web application
Gradio API (FLUX.1 Model): For text-to-image generation
OS & Shutil: For file handling and image management
Time: For progress bar simulation

🔹 Features
✅ User-Friendly Interface: Streamlit-powered UI for seamless interaction✅ AI-Powered Image Generation: Uses Gradio’s FLUX.1 model for fast and high-quality outputs✅ Progress Feedback: Progress bar to indicate image generation status✅ Image Saving & Downloading: Saves generated images and allows downloading

📥 Installation & Setup
To run the project locally, follow these steps:

1️⃣ Clone the Repository
git clone https://github.com/your-username/text-to-image.git
cd text-to-image

2️⃣ Install Dependencies
Make sure you have Python installed (preferably 3.8+). Then, install the required libraries:
pip install streamlit gradio-client

3️⃣ Run the Application
streamlit run app.py

🖼️ How It Works

Open the app using Streamlit.
Enter a descriptive text prompt in the sidebar.
Click Generate Image.
The app calls the Gradio API to create the image.
The progress bar shows the image generation status.
The generated image is displayed, saved, and can be downloaded.

🔗 API Details

This project uses the Gradio FLUX.1 Model:

API Client: black-forest-labs/FLUX.1-schnell
