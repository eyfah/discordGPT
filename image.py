import base64
import aiohttp
import ollama
from eventhandler import info, memory
from eventhandler import prompt_logic


async def image_handler(image_url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status == 200:
                    image_data = await resp.read()
                    encoded_image = base64.b64encode(image_data).decode('utf-8')

                    if encoded_image:
                        response = analyze(encoded_image)
                        return response


    except Exception as e:
        return e


def analyze(image):
    try:

        output = ollama.generate(
            model=info["vmodel"],
            prompt="what do you see",
            images=[str(image)]
        )

        caption = output.get('response', 'content')

        print(f"{info["vmodel"]}: {caption}")
        return f"**{info["vmodel"]}**\n\n{caption}"
    except Exception as e:
        print(e)
        return e
