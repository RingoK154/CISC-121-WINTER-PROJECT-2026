import gradio as gr

# ============================ Quick Sort FUNCTION ============================
def quicksort(a):
  smaller =[] # Setting up 3 stacks to store the numbers
  equal = []
  larger = []

  if len(a) < 2: # Restraint to pause the process
    return a
    print(a)

  mid = a[len(a)//2] #To get the index/ the position of the middle number of the list
  for number in a:
    if number < mid:
      smaller.append(number) #Selecting and putting numbers in each stack based on the requirement 
    if number == mid:
      equal.append(number)
    if number > mid:
      larger.append(number)
  # Putting together a sorted list when the process finishes
  decend_a = quicksort(smaller) #Samaller stack put first 
  decend_a += equal
  decend_a += quicksort(larger) #Larger Stack put last in order
  # Both smaller and larger stacks will go through the quicksort function again 
  return decend_a

def sort_numbers(input_string):
    try:
        a = list(map(int, input_string.split()))
        result = quicksort(a)
        return result
    except:
        return "Please enter numbers separated by spaces and no comma (,) "

# ============================ USER INTERFACE ============================
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

               """) as demo: # I am using CSS due to the limited editing detail of the user interface in Gradio to get a better experience for users.
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
