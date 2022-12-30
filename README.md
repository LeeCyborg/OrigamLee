# OrigamLee

This is for creating basic origami tesselation patterns that can be laser cut or creased.

+ Custom width/height of tesselation
+ Gradient X and Y axis
+ Grids
+ Linear folds
+ Radial folds

## use

Uses DrawSVG and Python 3 to create and export SVG files. Saves them out as Pattern.svg.

```bash
pip3 install drawSvg
python3 draw.py
```

.svg can be opened in web browser or vector program.

To make a simple waterbomb pattern, use makeSimple
Params are: width, height, fold, Pieces.FOLDNAME
Fold is a boolean for toggling mountain or valley

```python
t.makeSimple(100, 100, 0, Pieces.waterbombTwo)
```

To make a complex grid
Params are: width, height, fold, first pattern, second pattern

```python
t.makeComplex(100, 100, 0, Pieces.waterbombOneA, Pieces.waterbombOneB)
```

To make a gradient in X and Y
Params are: width, height, factor, iterations, piece

```python
t.makeGradientXY(100, 100, 5, 10, Pieces.waterbombTwo)
```

To make a complex grid with gradient in X and Y
Params are: width, height, fold, first pattern, second pattern

```python
t.makeComplexGradientXY(50, 50, 5, Pieces.waterbombOneA, Pieces.waterbombOneB)
```

## current patterns

+ 3 waterbomb grids
+ 2 linear point variations
+ basic radial fan fold
