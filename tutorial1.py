from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(500, 500, thinline, blue)
circle = EllipseAsset(200, 200, thinline, red)
scircle = EllipseAsset(50, 40, thinline, Color(0x073d91, 1.0))
# Now display a rectangle
Sprite(rectangle, (100,50))
Sprite(circle, (300, 250))
Sprite(scircle, (240, 200))
Sprite(scircle, (370, 200))
ImageAsset(self, a1.mzstatic.com/us/r30/Purple5/v4/5a/2e/e9/5a2ee9b3-8f0e-4f8b-4043-dd3e3ea29766/icon256.png, frame=None, qty=1, direction='horizontal', margin=0)
myapp = App()
myapp.run()