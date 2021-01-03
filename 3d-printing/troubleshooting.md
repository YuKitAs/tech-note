# Troubleshooting

## Print Warping

**Problem**: the first layer curls up at corners

**Cause**: the prints cool unevenly, which leads to different tensions

**Solutions**:

1. Improve bed adhesion:

  * Use a heated bed

  * Use adhesives like hair spray or glue stick

2. Adjust slicer's settings:

  * Decrease the print speed

  * Increase temperature for the first layer

  * Turn off or lower the speed of the fan for the first layer

  * Add brim or raft or mouse ears under the print


## Stringing

**Problem**: thin strands between printed parts

**Cause**: FDM printer nozzle oozes melted plastic material when traveling through open spaces, especially with PETG due to its liquidity

**Solutions**:

1. Enable retraction (default for Ender 3) and tune retraction settings:

  * Adjust retraction distance up/down by 1mm increments

  * Increase retraction speed

  * Decrease maximum retraction count to 10

  * Set minimum extrusion distance window the same as retraction distance

  * Change `Combing Mode` to `Within Infill`

  Try with [retraction test print](https://www.thingiverse.com/thing:909901).

2. Lower print temperature

3. Increase nozzle travel speed

4. Clean the nozzle before printing

5. Keep filaments dry
