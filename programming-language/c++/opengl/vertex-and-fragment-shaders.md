# Vertex and Fragment Shaders

The following are examples of simple vertex shader and fragment shader using [GLSL](https://www.opengl.org/sdk/docs/tutorials/ClockworkCoders/glsl_overview.php)（OpenGL Shader Language).

Input variables for vertex shader are vertex position and normal in object space. Output variables are vertex position and interpolated normal in world space.

```glsl
#version 330 // same as #version 330 core

layout(location = 0) in vec3 POSITION;
layout(location = 1) in vec3 NORMAL;

uniform mat4 MVP; // model-view-projection matrix
uniform mat4 M; // transformation matrix for vertices from object to world space
uniform mat4 N; // transformation matrix for normals from object to world space

out vec3 world_position;
out vec3 world_normal_interpolated;

void main(void)
{
    gl_Position = MVP * vec4(POSITION, 1.0); // build-in variable: vertex position in clip space
    
    world_position = vec3(M * vec4(POSITION, 1.0));
    world_normal_interpolated = N * NORMAL;
}
```

Input variables for fragment shader are vertex position and interpolated normal in world space from vertex shader. Output variable is the final color of the fragment.

```glsl
#version 330

in vec3 world_position;
in vec3 world_normal_interpolated;

out vec4 frag_color;

void main(void)
{
    vec3 world_normal = normalize(world_normal_interpolated);
    
    vec3 color = 0.5 * world_normal + vec3(0.5, 0.5, 0.5);
    
    frag_color = vec4(color, 1.0);
}
```

Read texture with sampler{1,2,3}D in fragment shader:

```glsl
in vec2 texCoord;

uniform sampler2D sam;

out vec4 frag_color:

void main() {
    frag_color = texture(sam, texCoord); // if frag_color is vec3 then frag_color = texture(sam, texCoord).rgb
}
```
