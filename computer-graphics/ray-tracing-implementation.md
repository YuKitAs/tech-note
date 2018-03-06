# Ray Tracing Implementation

When a ray from the camera/eye hits a surface, it can generate three types of new rays: reflection, refraction and shadow rays. Basically, a ray tracing process consists of three steps: ray generation, ray casting (ray intersection) and shading.  Some processes like Whitted-style ray tracing check secondary rays.

## Ray Generation

A ray can be described as a vector function of t: **r**(t) = **e** + t**d**. **e** is the start position of the ray (for primary rays, position of the camera/eye) and **d** is the normalized direction vector.

We generate rays from the camera to the middle of each pixel on the screen. The center of screen is at the origin of the *uvw*-coordinate used by the camera. The left, right, top and bottom boundaries of the screen are given as l, r, t and b. Every `(u, v)` position on the screen that each ray hits, starting from the top-left `(l, t)`, is computed as follows:

```cpp
for (float y = 0; y < SCREEN_H; y++) {
  for (float x = 0; x < SCREEN_W; x++) {
    u = l + (r - l) * (x + 0.5) / SCREEN_W;
    v = t + (t - b) * (y + 0.5) / SCREEN_H;
  }
}
```

## Ray Casting

Given a ray and objects, we can compute if the ray intersects the object surface. An intersection that we consider as valid should be in front of the camera (t' > 0), and the distance to the camera shouldn't be greater than a known intersection (t' < t) because in the same direction we only want the nearest intersection.

The following is just pseudocode:

```
intersection = NULL;
float t = FLOAT_MAX;

for (each object) {
  t' = intersect(object, e, d);
  if (t' > 0 && t' < t) {
    intersection = object;
    t = t';
  }
}
```

The ray-triangle intersection can be determined with the help of the [barycentric coordinate](https://en.wikipedia.org/wiki/Barycentric_coordinate_system). We can also compute intersection with ray marching and distance fields, see the implementation [here](https://github.com/YuKitAs/tech-note/blob/master/computer-graphics/find-intersection-with-ray-marching.md).

## Shading

In the shading step we calculate lighting and shadow for a found intersection `i` (i != NULL) with a point light source `l`.

At first, we will check whether the intersection is in the shadow, which means there is at least one other object between the intersection and the light source. In that case we don't calculate the lighting for it.

For lighting we will use the [Phong reflection model](https://en.wikipedia.org/wiki/Phong_reflection_model) to calculate the ambient term, diffuse term and specular term.

Suppose we already have structs like `Material`, `Intersection` and `PointLight` with all the information that we need.

```cpp
// ambient term
vec3 I = i.material->k_a * l.intensity;

// shadow ray
vec3 L = l.pos - i.pos;
float dist2Light = length(l);

// check if the intersection is in the shadwow (pseudocode)
for (each object) {
  t = intersect(object, i.pos, L);
  if (t > 0 && t < dist2Light)  return I;
}

float NdotL = dot(i.n, normalize(L));
// for point source in reality, the intensity of light decreases as the distance grows
float dist = length(l.pos - i.pos);

if (NdotL > 0) {
  // diffuse term
  I += i.material->k_d * l.intensity * NdotL / (dist * dist);

  // specular term
  vec R = 2.0f * i.n * NdotL - L;
  float RdotV = dot(R, V);
  if (Rdotv > 0) {
    I += i.material->k_s * l.intensity * powf(RdotV, i.material->n);
  }
}
```

Lighting can be calculated using different kinds of normals, which are called different shading methods, like Flat shading, Gouraud shading and Phong shading. The implementation of Gouraud shading and Phong shading can be found [here](https://github.com/YuKitAs/tech-note/blob/master/programming-language/c%2B%2B/opengl/gouraud-and-phong-shading.md).

## Tracing Secondary Rays

As mentioned above, Whitted-style ray tracing is a recursive algorithm used to determine the summed light intensity (color) of the surface.

Pseudocode:

```
vec3 raytrace(Ray, *ray, ...) {
  vec3 color = 0.0f;

  Intersection i;
  // use `cast` method to check if an intersection exists
  if (!cast(ray, FLOAT_MAX, &i)) return color;

  for (each light source) {
    // use `computeDirectLight` method defined above
    color += computeDirectLight(ray, i, ...);
  }

  if (surface is specular) {
    Ray reflect = ...;
    color += i.material->k_r * raytrace(reflect, ...);
  }

  if (surface is (semi-)transparent) {
    Ray refract = ...;
    if (total-reflection) {
      color += i.material->k_r * raytrace(reflect, ...);
    } else {
      color += i.material->k_t * raytrace(refract, ...);
    }
  }

  return color;
}
```
