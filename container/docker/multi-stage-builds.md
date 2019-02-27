# Multi-stage Builds

This feature was introduced since Docker 17.05 with the idea to define multiple stages in one Dockerfile in order to reduce intermediate artifacts in the final image.

For example, using `COPY` with the flag `--from=0` will just copy the built artifact from the previous stage, or we can name a build stage with `FROM <image> as <stage-name>` and then use `COPY --from=<stage-name>` to refer to a specific stage.
