import gradio as gr

def image_search(query):
    dummy_urls = [
        "https://dummyimage.com/600x400/000/fff",
        "https://dummyimage.com/600x400/00ff00/fff",
        "https://dummyimage.com/600x400/0000ff/fff",
        "https://dummyimage.com/600x400/ff0000/fff",
        "https://dummyimage.com/600x400/ff00ff/fff",
    ]
    return dummy_urls


def recommendation(tags):
    # Your recommendation algorithm here
    return "Based on your tags, we recommend...."


def image_search_interface(query):
    images = image_search(query)
    recommendation = {"D": 1, "E": 0.8, "F": 0.5}
    tags = ["A", "B", "C"]
    return images, gr.update(choices=tags), recommendation


demo = gr.Interface(

    fn=image_search_interface,
    inputs=gr.Textbox(placeholder="Enter a instagram username"),
    outputs=[
        gr.Gallery(preview=True, label="Images"),
        gr.CheckboxGroup(["A", "B"], label="Travelling with (select all)"),
        gr.Label(label="Recommendations"),
    ],
    title="Image Search",
    description="Enter a instagram username to search for recommended insurance products.",
    allow_flagging="never",
    layout="vertical",
    thumbnail=None
)

demo.launch()
