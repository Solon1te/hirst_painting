# Damien Hirst Painting with Python

## About The Project
This project is a part of my learning journey through the "100 Days of Code" class on Udemy. It focuses on using Python to generate a vibrant dot art. The project utilizes libraries such as `turtle` for drawing and `colorgram` for extracting color palettes from images. This creative endeavor not only reinforced my understanding of Python basics but also introduced me to working with external libraries and manipulating images and graphics in Python.

### Built With
- Python
- Turtle Graphics
- Colorgram

## What I Learned

### Color Extraction with Colorgram
- **Colorgram's Power:** I learned how to use `colorgram` to extract colors from an image. This was fascinating as it allowed me to dynamically choose a color palette based on any image, opening up endless possibilities for automated art creation.
- **Handling Colors:** Extracting colors as RGB tuples and storing them in a list was a great practice in working with data structures.

### Graphics with Turtle
- **Basics of Turtle Graphics:** I got hands-on experience with the `turtle` module, learning how to create a window, draw on it, and customize aspects like color mode and speed.
- **Creating Dot Art:** The project taught me how to systematically place dots on the canvas to create a coherent piece of art. This involved iterating over positions on the canvas and drawing filled circles with colors from the extracted palette.
- **Optimizing Movement:** I learned to optimize the turtle's movement across the canvas, minimizing the drawing time by hiding the turtle during drawing and moving it strategically.

### Programming Concepts
- **Iterative Development:** The project reinforced the importance of breaking down a problem into smaller, manageable tasks (like drawing a single dot, moving to the next position, etc.) and iterating over these tasks.
- **Working with External Libraries:** I gained experience in integrating and utilizing external libraries (`colorgram` and `turtle`) in a project, which is a crucial skill in software development.
- **Creativity in Code:** This project was a great reminder of how creative coding can be. It was thrilling to see how a few lines of code could transform into a beautiful piece of art.

## How to Run
Ensure you have Python installed on your system. This project was developed using Python 3.8. You'll also need to install the `colorgram` library if you haven't already.

1. Clone the repo:
   ```sh
   git clone https://https://github.com/Solon1te/hirst_painting.git

2. install the required libraries:
   colorgram
   
4. run the script
   python hirst_painting
