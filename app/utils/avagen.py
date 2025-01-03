from PIL import Image
import random
import io

def avatar_gen(size=16):
  ava = Image.new("RGB", (size, size), "white")
  pixels = ava.load()

  for y in range(size):
    for x in range(size):
      pixels[x, y] = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
      )
  ava_bytes = io.BytesIO()
  ava.save(ava_bytes, format="PNG")
  return ava_bytes.getValue()
