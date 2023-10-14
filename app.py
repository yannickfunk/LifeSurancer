import gradio as gr
import numpy as np
import random

from logo import logo

INSURANCES = [
    "Kfz-Versicherung",
    "Haftpflichtversicherung",
    "Hausratversicherung",
    "Rechtsschutzversicherung",
    "Unfallversicherung",
    "Berufsunfähigkeitsversicherung",
    "Lebensversicherung",
    "E-Scooter-Versicherung",
    "Fahrradversicherung",
    "Hundehaftpflichtversicherung",
    "Pferdehaftpflichtversicherung",
    "Auslandskrankenversicherung",
    "E-Bike-Versicherung",
    "Oldtimer-Versicherung",
    "Zahnzusatzversicherung",
    "Verkehrs-Rechtsschutzversicherung",
    "Wohngebäudeversicherung",
    "Tierkrankenversicherung",
    "Bauherren-Rechtsschutzversicherung",
]
LINKS = ["https://www.check24.de/suche/?q=" + e for e in INSURANCES]

TAGS = list(
    {
        "Haustiere",
        "Reisen",
        "Essen",
        "Natur",
        "Architektur",
        "Kunst",
        "Mode",
        "Sport",
        "Menschen",
        "Technologie",
        "Geschäft",
        "Gesundheit",
        "Wissenschaft",
        "Bildung",
        "Spiritualität",
        "Geschichte",
        "Musik",
        "Bücher",
        "Filme",
        "Fernsehen",
        "Gaming",
        "Komödie",
        "Autos",
        "Motorräder",
        "Design",
        "Fotografie",
        "Schönheit",
        "DIY",
        "Gartenarbeit",
        "Fitness",
        "Zuhause",
        "Elternschaft",
        "Humor",
        "Kunst",
        "Handwerk",
        "Berühmtheiten",
        "Marketing",
        "Filme",
    }
)

css = """
body {
    overflow-y: scroll;
}

body::-webkit-scrollbar {
    width: 7px;
}
body::-webkit-scrollbar-thumb {
    background-color: rgba(0,0,0,0.4);
    border-radius: 10rem;
    border: 1px solid #fff;
}


body::-webkit-scrollbar-track-piece:start {
    background: transparent;
}

body::-webkit-scrollbar-track-piece:end {
    background: transparent;
}

gradio-app {
    background-image: url("https://i.postimg.cc/QMsSKndk/06-2023-Header-Website-Idea-Spark-SVInformatik-03-svg.png") !important;
    background-repeat: no-repeat !important;
    background-size: 1920px 600px !important;
}

.gradio-container > *:first-child {
    margin-top: 50px;
}
footer {visibility: hidden}
.comp, .form {
    box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px !important;
}

#ourlogo {
    height: 10%;
    width: 10%;
    margin: auto;
    margin-bottom: 20px;
}

#platformlogo {
    margin: auto;
}

"""


def get_relevant_images(query):
    dummy_urls = [
        "https://dummyimage.com/600x400/000/fff",
        "https://dummyimage.com/600x400/00ff00/fff",
        "https://dummyimage.com/600x400/0000ff/fff",
        "https://dummyimage.com/600x400/ff0000/fff",
        "https://dummyimage.com/600x400/ff00ff/fff",
    ]
    return dummy_urls


dummy_data = {
    "realsophiegrace": {
        "profile": "resources/sophie_pp.jpg",
        "images": [
            "resources/sophie_2.jpg",
            "resources/sophie_1.jpg",
            "resources/sophie_3.jpg",
            "resources/sophie_4.jpg",
        ],
        "tags": ["Haustiere", "Reisen", "Essen", "Natur", "Strand"],
        "recommendations": {
            "Hundeversicherung": 0.98,
            "Pferdeversicherung": 0.9,
            "Reiseversicherung": 0.7,
            "Hausratversicherung": 0.4,
        },
    },
    "mariusquast": {
        "profile": "resources/marius_pp.jpg",
        "images": [
            "resources/marius_1.jpg",
            "resources/marius_2.jpg",
            "resources/marius_3.jpg",
            "resources/marius_4.jpg",
        ],
        "tags": ["Ski", "E-Bike", "Natur", "Reisen"],
        "recommendations": {
            "Auslandskrankenversicherung": 0.88,
            "E-Bike Versicherung": 0.70,
            "Reiseversicherung": 0.63,
        },
    },
}

dummy_tiktok_data = {
    "@mathisox": {
        "profile": "resources/mathis_pp.jpg",
        "images": [
            "resources/mathis_1.jpg",
            "resources/mathis_2.jpg",
            "resources/mathis_3.jpg",
            "resources/mathis_4.jpg",
        ],
        "tags": ["Auto", "Motorrad", "Reisen", "DIY"],
        "recommendations": {
            "Oldtimer-Versicherung": 0.93,
            "KFZ-Versicherung": 0.82,
            "Hausratversicherung": 0.4,
        },
    }
}


def get_recommendations():
    # random numpy array of shape 5
    x = np.random.rand(5)
    scores = np.exp(x) / np.sum(np.exp(x))
    insurances = random.choices(INSURANCES, k=5)

    return dict(zip(insurances, scores))


def get_tags():
    # choose one to 8 tags
    num_tags = random.randint(1, 8)
    tags = list(set(random.choices(TAGS, k=num_tags)))
    return tags


def on_click(text, platform):
    d = dummy_data if platform == "Instagram" else dummy_tiktok_data
    if text in d.keys():
        images = d[text]["images"]
        tags = d[text]["tags"]
        recommendations = d[text]["recommendations"]
        checked_tags = gr.CheckboxGroup(choices=tags, value=tags)
        return recommendations, checked_tags, images, d[text]["profile"]

    images = get_relevant_images(text)
    recommendations = get_recommendations()

    tags = get_tags()
    checked_tags = gr.CheckboxGroup(choices=tags, value=tags)

    return (
        recommendations,
        checked_tags,
        images,
        "https://dummyimage.com/600x400/000/fff",
    )


def on_platform_change(platform):
    if platform == "Instagram":
        return (
            gr.Image("instagram_logo.webp"),
            gr.Textbox(placeholder="https://www.instagram.com/mariusquast/"),
            gr.Dropdown(
                value="mariusquast",
                choices=["realsophiegrace", "mariusquast"],
            ),
        )
    elif platform == "TikTok":
        return (
            gr.Image("tiktok_logo.webp"),
            gr.Textbox(placeholder="https://www.tiktok.com/@h3llomarc"),
            gr.Dropdown(
                value="@mathisox",
                choices=["@mathisox"],
            ),
        )


theme = gr.themes.Soft(
    primary_hue="lime",
    secondary_hue="green",
)
with gr.Blocks(theme=theme, css=css) as demo:
    # row for logogra
    with gr.Row():
        gr.HTML(logo)

    # row of left and right column
    with gr.Row():
        # left column (inputs)
        with gr.Column():
            disp_radio = gr.Radio(
                label="Wähle deine Social Media Plattform:",
                value="Instagram",
                elem_classes=["comp"],
                choices=["Instagram", "TikTok"],
            )
            # disp_text_input = gr.Textbox(
            #     label="Gib deinen Profillink ein:",
            #     placeholder="https://www.instagram.com/mariusquast/",
            #     elem_classes=["comp"],
            # )
            disp_text_input = gr.Dropdown(
                label="Wähle dein Profil aus:",
                value="mariusquast",
                choices=["realsophiegrace", "mariusquast"],
                elem_classes=["comp"],
            )
            disp_platform_preview = gr.Image(
                "instagram_logo.webp",
                label="Vorschau",
                elem_classes=["comp"],
                elem_id="platformlogo",
                show_label=False,
                show_download_button=False,
                height=160,
                width=160,
            )
            disp_radio.change(
                fn=on_platform_change,
                inputs=[disp_radio],
                outputs=[disp_platform_preview, disp_text_input, disp_text_input],
            )
        inputs = [disp_text_input, disp_radio]

        # right column (outputs)
        with gr.Column():
            disp_recommends = gr.Label(
                label="Wir empfehlen dir:", elem_classes=["comp"], num_top_classes=5
            )
            disp_tags = gr.CheckboxGroup(
                label="Dein Lifestyle-Profil:", elem_classes=["comp"]
            )

            with gr.Accordion(
                "Deine relevanten Beiträge", open=False, elem_classes=["comp"]
            ):
                disp_gallery = gr.Gallery(preview=True, label="Images")
        outputs = [disp_recommends, disp_tags, disp_gallery, disp_platform_preview]

    # submit button
    with gr.Row():
        gr.Button("Submit", variant="primary").click(
            fn=on_click, inputs=inputs, outputs=outputs
        )

    demo.launch()
