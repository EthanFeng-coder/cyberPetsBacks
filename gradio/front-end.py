import gradio as gr


def greet(your_input):
    return "Hello " + your_input + "!"


demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch(share=True)
