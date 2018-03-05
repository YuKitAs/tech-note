# Draw (Semi-)Transparent Objects

## Depth Test

Depth test is one of the most important per-fragment operations performed after the Fragment Shader. If the test fails, the fragment will be discarded, otherwise the depth buffer will be updated with the fragment's output depth.


## Depth Buffer

With depth test enabled and `glDepthMask` on, the depth buffer gets updated every time an object is rendered. However, when drawing a (semi-)transparent object (eg. fire, smoke), if we update the depth buffer, the objects behind the (semi-)transparent object will not be shown, so we should "trick" OpenGL by turning off `glDepthMask` for the moment.

Correct steps to draw opague and (semi-)transparent objects with OpenGL:

```
glEnable(GL_DEPTH_TEST);
glDisable(GL_BLEND);

// Draw opaque objects in any order. if (color.a < 1.0) discard;

glEnable(GL_BLEND);
glBendFunc(sfactor, dfactor);

glDepthMask(GL_FALSE);

// Draw (semi-)transparent objects from furthest to nearest.

glDepthMask(GL_TRUE);
```
