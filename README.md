# Computer Graphics Algorithms

This repository contains Python implementations of classic computer graphics algorithms for drawing lines and circles using the DDA (Digital Differential Analyzer) and parametric methods. The algorithms are visualized using Matplotlib.

## Folder Structure

- `DDA_LINE/dda_matplotlib.py`  
  Draws a line using the DDA line drawing algorithm.
- `DDA_CIRCLE/dda_matplotlib.py`  
  Draws a circle using the DDA (midpoint) circle algorithm.
- `DDA_CIRCLE/theta_Circle.py`  
  Draws a circle using the parametric (theta) method.

## Algorithms Explained

### DDA Line Drawing Algorithm
- Calculates the intermediate points between two endpoints using floating-point increments.
- Plots each calculated point to form a straight line.

### DDA Circle Drawing Algorithm
- Uses symmetry and a decision parameter to plot points around a center, forming a circle.
- Efficiently calculates all points using integer arithmetic.

### Parametric (Theta) Circle Method
- Uses the parametric equations:
  - `x = xc + r * cos(theta)`
  - `y = yc + r * sin(theta)`
- Plots points for theta from 0 to 2π to form a circle.

## Requirements
- Python 3.x
- Matplotlib
- Numpy (for parametric circle)

Install dependencies:
```bash
pip install matplotlib numpy
```

## Usage

### DDA Line
Run the line drawing script and enter coordinates:
```bash
python DDA_LINE/dda_matplotlib.py
```

### DDA Circle
Run the circle drawing script and enter center and radius:
```bash
python DDA_CIRCLE/dda_matplotlib.py
```

### Parametric Circle
Run the parametric circle script and enter center and radius:
```bash
python DDA_CIRCLE/theta_Circle.py
```

## License
This project is for educational purposes.
