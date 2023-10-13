import torch

from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
prompt = "An image of a squirrel in Picasso style"
image = pipeline(prompt).images[0]
image.save("test.png")
