import gradio as gr

# ============================ Quick Sort FUNCTION ============================
def quicksort(a):
  smaller =[]
  equal = []
  larger = []

  if len(a) < 2:
    return a
    print(a)

  mid = a[len(a)//2]
  for number in a:
    if number < mid:
      smaller.append(number)
    if number == mid:
      equal.append(number)
    if number > mid:
      larger.append(number)
  decend_a = quicksort(smaller)
  decend_a += equal
  decend_a += quicksort(larger)
  
  return decend_a


# ============================ USER INTERFACE ============================
def sort_numbers(input_string):
    try:
        a = list(map(int, input_string.split()))
        result = quicksort(a)
        return result
    except:
        return "Please enter numbers separated by spaces and no comma (,) "


with gr.Blocks(title="Quicksort App", theme=gr.themes.Glass(), css="""
#input_box, #output_box {
    max-width: 500px;
    margin: auto;
}
#btn {
    width: 200px;
    margin: auto;
    display: block;
    text-align: center;
}
#title {
    text-align: center;
}
               """) as demo:
    gr.Markdown("### Quicksort Number Sorter ",
                elem_id="title"
    )

    input_box = gr.Textbox(
        label="Enter numbers (space separated)",
        placeholder="e.g. 5 2 9 1 7",
        elem_id="input_box"
    )

    output_box = gr.Textbox(label="Sorted Output",
                            elem_id="output_box"
    )

    btn = gr.Button("Sort", elem_id="btn")

    btn.click(
        fn=sort_numbers,
        inputs=input_box,
        outputs=output_box
    )

demo.launch()
