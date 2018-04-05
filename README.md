# fractales

This little program generates fractals, which is cool. 
You can also zoom into the fractal by selecting the zone ur interested in zooming into.

The file is called mandelbrot.py but is not limited to the mandelbrot set.
You can tune the algorithm in the "iter" function to show different fractals especially the ones from the famous julia set.
:)
by default it's in black and white but you can set the color mode by changing these lines :

newGrid[i][j] = map(grid[i][j], 0, max_iters, 0, 255) => colors
newGrid[i][j] = 255 => black and white
(put a # before the mode you don't want)

![alt text](https://github.com/Smirkey/fractales/edit/master/output.png)
