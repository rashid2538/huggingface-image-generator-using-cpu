import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path
import sys

# Set device to CPU (your Mac doesn't have CUDA/GPU support)
device = "cpu" #cpu/xpu

# Load the model - OFA-Sys small Stable Diffusion
model_id = "Lykon/dreamshaper-6" # "OFA-Sys/small-stable-diffusion-v0"

print("Loading the model. This may take a while...")
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    safety_checker=None  # Optional: disable NSFW filter to save resources
)
pipe = pipe.to(device)

def generate_image(prompt, output, steps=25):
    print("Generating image...")
    image = pipe(prompt, num_inference_steps=steps, width=800, height=450).images[0]
    image.save(output)
    print(f"Image saved to {output}")

if len(sys.argv) > 2:
    inputFile = sys.argv[1]
    outputPath = sys.argv[2]
    print(f"Input: {input}")

    if Path(inputFile).is_file():
        Path(outputPath).mkdir(parents=True, exist_ok=True)
        with open(inputFile, 'r') as f:
            for index, line in enumerate(f):
                prompt = line.strip()
                output = f"{outputPath}/image_{index}.png"
                print(f"Prompt: {prompt} - Output: {output}")
                generate_image(prompt, output)
    else:
        print("Input is not a file!")
else:
    print("No input/output path provided!")
