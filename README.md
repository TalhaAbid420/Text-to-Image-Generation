# 🎨 FLUX Fast Studio

A high-performance Text-to-Image generation application built with Python and Gradio. This app leverages the **FLUX.1-schnell** model via the Hugging Face Inference API (Router) to deliver professional-grade AI artwork in seconds.

---

## 🚀 Live Demo
Experience the application live on Hugging Face Spaces:
**[👉 View Live App on Hugging Face](https://talhabid420-image-generation-app.hf.space)**

---

## 🌟 Features

* **Ultra-Fast Generation:** High-quality images in 2–5 seconds using FLUX.1-schnell.
* **Artistic Style Presets:** Choose from Cinematic, Anime, Cyberpunk, Oil Painting, or Sketch.
* **Modern UI:** A clean, responsive interface built with Gradio Blocks.
* **API-Driven:** Offloads heavy computation to the Hugging Face Inference Router.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend:** [Gradio](https://gradio.app/)
* **AI Model:** [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
* **Backend:** Hugging Face Inference API (`huggingface_hub`)

## 📋 Prerequisites

To run this project locally, you need:
1.  A [Hugging Face](https://huggingface.co/) account.
2.  A Hugging Face **Access Token** (Inference permissions enabled).

## ⚙️ Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    Create a `.env` file in the root directory:
    ```env
    HF_TOKEN=your_huggingface_token_here
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

## 📝 License
Distributed under the MIT License.
