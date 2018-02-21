# Vertex and Fragment Shaders

The following are examples of simple vertex shader and fragment shader using [OpenGL Shader Language](https://www.opengl.org/sdk/docs/tutorials/ClockworkCoders/glsl_overview.php).

Input variables for vertex shader are vertex position in object space and texture coordinates (uv coordinates) of the vertex. Output variables are interpolated vertex color and texture coordinates.

```cpp
#version 330 // same as #version 330 core

layout(location = 0) in vec3 POSITION;
layout(location = 2) in vec2 TEXCOORD;

uniform mat4 MVP; // model-view-projection matrix

out vec3 color;
out vec2 tex_coord;

void main(void)
{
    tex_coord = TEXCOORD;
    gl_Position = MVP * vec4(POSITION, 1.0);
    color = 0.5 * POSITION + vec3(0.5, 0.5, 0.5);
}
```

Input variables for fragment shader are interpolated vertex color and texture coordinates from vertex shader. Output variable is the final color of the fragment.

```cpp
#version 330

in vec3 color;
in vec2 tex_coord;

out vec4 frag_color;

void main(void)
{
    frag_color = vec4(color, 1.0);
}
```
