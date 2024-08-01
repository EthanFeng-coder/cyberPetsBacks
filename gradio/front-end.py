import gradio as gr


def greet(your_input):
    return "Hello " + your_input + "!"


if __name__ == "__main__":
    with gr.Blocks() as demo:
        video_output = gr.Video(label="Processed Image")
        audio_input = gr.Audio(type="numpy", label="Input", autoplay=True)
        audio_output = gr.Audio(type="filepath", label="output", value='../Recording.m4a')
        submit_button = gr.Button("Submit").click(
            inputs=[audio_input],
            outputs=[video_output, audio_output], )
    demo.launch(share=True)
