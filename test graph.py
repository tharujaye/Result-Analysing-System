from graphics import GraphWin, Point, Rectangle

# Function to create a bar graph
def create_bar_graph(data, win):
    n = len(data)
    bar_width = 30
    space_between = 10

    for i in range(n):
        # Calculate bar position and size
        x = i * (bar_width + space_between) + 50
        height = data[i] * 10  # Scale the height for better visualization

        # Create a rectangle for the bar
        bar = Rectangle(Point(x, win.getHeight() - 20), Point(x + bar_width, win.getHeight() - 20 - height))
        bar.setFill("blue")
        bar.draw(win)

# Sample data for the bar graph
data = [3, 7, 2, 5, 8]

# Create a graphics window
win = GraphWin("Bar Graph", 400, 200)

# Create the bar graph
create_bar_graph(data, win)

# Wait for a click before closing the window
win.getMouse()
win.close()
