import gradio as gr
import os
from huggingface_hub import InferenceClient

# Initialize the client - the library now handles the new router URLs automatically
client = InferenceClient(
    model="black-forest-labs/FLUX.1-schnell",
    token=os.getenv("HF_TOKEN")
)

# Style Dictionary (Restored)
STYLE_PROMPTS = {
    "No Style": "{}",
    "Cinematic": "{}, cinematic lighting, highly detailed, 8k resolution, masterpiece, dramatic atmosphere",
    "Anime": "{}, anime style, vibrant colors, clean lines, high quality, aesthetic",
    "Cyberpunk": "{}, cyberpunk aesthetic, neon lights, futuristic, high contrast, rainy street",
    "Oil Painting": "{}, classic oil painting, thick brushstrokes, textured canvas, artistic",
    "Sketch": "{}, pencil sketch, charcoal, hand-drawn, minimalist, paper texture"
}

def generate_image(prompt, style):
    if not prompt or prompt.strip() == "":
        raise gr.Error("Please enter a description.")
    
    # Apply style to the prompt
    final_prompt = STYLE_PROMPTS[style].format(prompt)
    
    try:
        # The text_to_image method is optimized for the new Hugging Face router
        image = client.text_to_image(final_prompt)
        return image
    except Exception as e:
        # Improved error handling to catch API changes
        raise gr.Error(f"API Error: {str(e)}")

# --- Professional UI ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# ⚡ FLUX Fast Studio")
    gr.Markdown("Using the latest Hugging Face Inference Router for high-speed generation.")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="Prompt", 
                placeholder="A lion chilling with his kids...",
                lines=3
            )
            
            style_dropdown = gr.Dropdown(
                label="Choose Style",
                choices=list(STYLE_PROMPTS.keys()),
                value="No Style"
            )
            
            generate_btn = gr.Button("Generate ⚡", variant="primary")
            
        with gr.Column(scale=1):
            output_image = gr.Image(label="Result")

    # Connect UI elements
    generate_btn.click(
        fn=generate_image,
        inputs=[input_text, style_dropdown],
        outputs=output_image
    )

if __name__ == "__main__":
    demo.launch(share=True)