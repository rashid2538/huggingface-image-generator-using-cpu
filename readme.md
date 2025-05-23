# 🔮 Local Image Generator using Hugggin Face Diffusers

Generate AI images locally on a CPU-only Mac (e.g., MacBook 2017) using the [`OFA-Sys/small-stable-diffusion-v0`](https://huggingface.co/OFA-Sys/small-stable-diffusion-v0) model from Hugging Face.

---

## ✅ Features

- Runs fully offline (after initial model download)
- CPU-compatible (no GPU or CUDA needed)
- Generates one or multiple images per prompt
- Custom resolution (16:9 for YouTube supported)
- Easy to modify and expand

---

## 💻 System Requirements

- macOS with Python 3.10.12
- At least 8 GB RAM (more is better)
- No GPU required

Tested on: **MacBook 13-inch, 2017, Intel i5, 8GB RAM**

---

## 🧪 Setup Instructions

### 1. Clone the repo (or create your project folder)
```bash
git clone https://github.com/rashid2538/huggingface-image-generator-using-cpu
cd huggingface-image-generator-using-cpu
```

---

### 2. Create and activate virtual environment (optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install numpy==1.26.4
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu
pip install diffusers==0.20.2 transformers==4.31.0 huggingface_hub==0.17.3 accelerate==0.21.0 safetensors
```

---

## 🚀 Usage

### 1. Run the script:

```bash
python main.py prompts.txt ./outputs
```

**"Kick Back, Grab a Coffee ☕, and Chill—This Ain’t a Netflix Series! �🎬"**  

Relax, my impatient friend! This won’t take **a full day** ⏳🗓️ (unlike your last Windows update 💻😤). Just:  

1. **Sit down** 🪑 (or lie down, no judgment 🛋️💤).  
2. **Order that fancy latte** ☕✨ (extra foam, because you *deserve it* 💅).  
3. **Blink twice** 👀… and *BOOM!* 💥 **Done!** Faster than your Wi-Fi buffering. 📶🐢  

No all-nighters here! **Unless you *want* to stare at the screen for fun.** (Weird flex, but okay. 🤷‍♂️😂)

Now **stop stressing**—your computer’s working *harder than your ex’s therapist*. 😏🔥 **Let’s go!** 🚀

---

### 2. Output

Images will be saved in the current directory as:

```
./outputs/image_0.png
./outputs/image_1.png
...
```

**"Okay, So These Ain’t Picasso Masterpieces… But Cut Your Machine Some Slack! 🎨🤖💻"**  

Look, I get it—these images might not be **Mona Lisa-level** 🖼️✨ or make your eyeballs weep with joy 😭🎨. But hey! **Your computer and You** teamed up like two sleep-deprived interns ☕👾, scrambling to make art happen!

**Give us a high-five!** ✋ Because:  
- **We tried.** (Unlike your ex. 😏)
- **Pixels were harmed** in the making. (RIP, perfect shading. 🪦)
- **This is AI art, not magic!** (Unless you count "turning code into a blob monster" as magic. 🧙‍♂️👾)

So yeah, **applaud the effort** 👏, laugh at the wonky details 🤪, and remember: **Even Van Gogh started with stick figures.** (Probably. 🖍️🌻)

**Now go generate something weirder.** I dare you. 😈🔥

---

## ✍️ Options & Customization

Edit the `main.py` script to change the following:

Replace this with your own creative prompt.

---

### 🔹 Image Count

```python
num_images = 3
```

---

### 🔹 Dimensions (width and height)

```python
width = 640
height = 360
```

*Note: Width and height should be a multiple of 8*
---

### 🔹 Inference Steps (Quality vs Speed)

```python
num_inference_steps = 25  # Increase to 40–50 for better quality
```

---

## 🧠 Notes

* First run will download model weights (\~1.3GB).
* Execution is slow on CPU (1–5 minutes per image).
* Avoid high batch sizes or too-large resolutions to prevent memory errors.

---

## 📷 Example Prompt Ideas (prompts.txt)

| A futuristic city skyline at night, in cinematic lighting | A traditional Indian bride in red saree, beautiful lighting | A sci-fi soldier in neon armor, concept art style |
|---|---|---|
| ![A futuristic city skyline at night, in cinematic lighting](https://github.com/rashid2538/huggingface-image-generator-using-cpu/blob/main/outputs/image_0.png?raw=true) | ![A traditional Indian bride in red saree, beautiful lighting](https://github.com/rashid2538/huggingface-image-generator-using-cpu/blob/main/outputs/image_1.png?raw=true) | ![A sci-fi soldier in neon armor, concept art style](https://github.com/rashid2538/huggingface-image-generator-using-cpu/blob/main/outputs/image_2.png?raw=true) |

---

## 🧰 Credits

* [Lykon/dreamshaper-6](https://huggingface.co/Lykon/dreamshaper-6)
* [OFA-Sys/small-stable-diffusion-v0](https://huggingface.co/OFA-Sys/small-stable-diffusion-v0)
* Hugging Face Diffusers
* PyTorch (CPU build)

---

## 🗂 License

MIT License — feel free to modify, remix, and share.
