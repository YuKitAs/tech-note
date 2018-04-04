# Gouraud and Phong Shading

Input variables for both shadings in Vertex Shader:

```glsl
uniform mat4 MVP; // Transformation matrix for vertex to clip space
uniform mat4 MV; // Transformation matrix for vertex to camera space
uniform mat4 N; // Transformation matrix for normal to camera space
uniform vec3 lightSourcePos;

in vec4 in_position;
in vec3 in_normal;
```

[Gouraud shading](https://en.wikipedia.org/wiki/Gouraud_shading) computes the color at each vertex, so the output variable of Vertex Shader is the vertex color. Later the fragment color will be interpolated from the color of vertices.

```glsl
out vec4 color;

void main() {
  gl_Position = MVP * in_position;

  vec3 P = vec3(MV * in_position);
  vec3 N = vec3(N * vec4(in_normal, 0.0));
  vec3 L = lightsourcePos - P;
  color = vec4(max(0.0, dot(normalize(L), normalize(N)));
}
```

[Phong shading](https://en.wikipedia.org/wiki/Phong_shading) computes the color of each fragment, the output variables of Vertex Shader are N and L of the vertex, which are computed the same way as above, unnormalized. N and L of each fragment will be interpolated from N and L of vertices, then the fragment color can be computed.
