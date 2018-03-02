# Find Intersection with Ray Marching

```cpp
float tmin; // minimal step size
float tmax; // maximal step size
float eps; // a given threshold for checking whether the surface is considered as intersected

float intersect(vec3 ray_origin, vec3 ray_direction) {
  float t = tmin;

  while (t <= tmax) {
    float d = sceneDistance(ray_origin + t * ray_direction);

    if (d < eps) return t;

    t += d;
  }

  // no intersection found
  return tmax;
}
```
