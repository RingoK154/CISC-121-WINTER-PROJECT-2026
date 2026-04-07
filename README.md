# CISC-121-WINTER-PROJECT-2026
Winter 2026 CISC 121 FINAL PROJECT
## Quick Sort
https://github.com/user-attachments/assets/2a578270-0fe2-4d8f-b7bb-80da709a0030

I decided to choose Quick Sorting as an application to help with sorting numbers in ascending order (small to large).

Quick Sort an unsorted list of numbers/integers by choosing a number from the list (usually the middle index of the list), then assign the rest of the numbers into stacks of larger than, smaller than and equal to the middle number. Then put the smaller stack first in order, then the equal stack and last is the larger stack. Then repeat the same process for smaller and larger stacks until the total number within a stack is less than 2. The result would be a sorted list of input numbers in ascending order. 

The Quick sorting process can be described as:
1) Choosing the middle number/ pivot by dividing the total number of indexes within the list to get the middle number's index.
2) For each number in the list:
   1) If the number is larger than the pivot, put in the stack "Larger"
   2) If the number is smaller than the pivot, put in the stack "Smaller"
   3) If the number is equal to the pivot, put in the stack "Equal"
3) Put the smaller stack first, then Equal and last is Larger to form a sorted list in ascending order. 
4) Repeat step 2'sprocess for Smaller and Larger's stack until the total numbers in each stack are less than 2.

## Design and Goal
The application can help users sort a list of numbers (grades, credit scores, bills, etc.), especially in larger quantities, and can assist the user in getting a sorted list without manually selecting and putting the numbers in the right order, which consumes too much time and could be done incorrectly. 

Using Gradio can generrate User Interfacew application quickly, but is limited in editing details like HTML and CSS. The user can enter the numbers/integers into the input field and will get a Sorted list of numbers in ascending order. 

Users don't have to put commas between numbers in the input to save time, and will let out a message if there is any comma within the input ("Please enter numbers separated by spaces and no comma (,)")
## Testing 

## Hugging Face Link
To check the application, use the Hugging Face link: https://huggingface.co/spaces/RingVN/CISC121_PROJECT_WINTER2026_QUICK_SORT

## Author & Acknowledgment
The code was in part/ assisted by ChatGPT LLM using prompts based on this README.
