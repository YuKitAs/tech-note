# Calling C Method from Java

1. Declare a native method in Java. Load the shared library (which will be built later) before calling the native method.

  ```java
  public class Main {
      public static void main(String[] args) {
          System.loadLibrary("Hello");
          new Main().greet();
      }

      public native void greet();
  }
  ```

2. Compile Java with `javac Main.java`.

3. Generate JNI-style header file with `javah Main`. The generated `Main.h` looks like:

  ```c
  /* DO NOT EDIT THIS FILE - it is machine generated */
  #include <jni.h>
  /* Header for class Main */

  #ifndef _Included_Main
  #define _Included_Main
  #ifdef __cplusplus
  extern "C" {
  #endif
  /*
   * Class:     Main
   * Method:    greet
   * Signature: ()V
   */
  JNIEXPORT void JNICALL Java_Main_greet
    (JNIEnv *, jobject);

  #ifdef __cplusplus
  }
  #endif
  #endif
  ```

4. Create `Main.c` and implement the method (remember to fix the method signature by adding parameter names):

  ```c
  #include <jni.h>
  #include "Main.h"
  #include <stdio.h>

  JNIEXPORT void JNICALL Java_Main_greet(JNIEnv *env, jobject obj) {
    printf("Hello world!\n");
    return;
  }
  ```

5. Build shared library `libHello.so` (on Ubuntu in this example) with `gcc`.

  ```console
  gcc -shared -fpic -o libHello.so -I${JAVA_HOME}/include -I${JAVA_HOME}/include/linux Main.c
  ```

  `${JAVA_HOME}/include` is where `jni.h` is located. The descriptive part in the library name (soname) should map the name in the Java code.

6. Run Java with explicitly specified library path:

  ```console
  java -Djava.library.path=. Main
  ```

  Output:

  ```
  Hello world!
  ```
