# Curve Fit Assignment — Research & Development 

## Final parameter values
- θ = 0.4908 (radians)
- M = 0.0214
- X = 54.9008

## Parametric equation (LaTeX)
\[
\left(
t \cdot \cos(0.4908) - e^{0.0214|t|} \cdot \sin(0.3t)\sin(0.4908) + 54.9008,\;
42 + t \cdot \sin(0.4908) + e^{0.0214|t|} \cdot \sin(0.3t)\cos(0.4908)
\right)
\]

## Desmos equation (paste this into Desmos)

(tcos(0.4908) - e^(0.0214abs(t))sin(0.3t)sin(0.4908) + 54.9008, 42 + tsin(0.4908) + e^(0.0214*abs(t))sin(0.3t)*cos(0.4908))

Set domain: '6 ≤ t ≤ 60'

## Methodology
1. Loaded the provided dataset 'xy_data.csv'
2. Created evenly spaced 't' values between 6 and 60
3. Defined the given parametric equations with unknowns θ, M, and X
4. Used optimization (L-BFGS-B) minimizing L1 distance to fit the curve
5. Obtained the optimized parameters shown above
6. Plotted and verified the fitted curve visually

## Files included
- 'xy_data.csv'
- 'fit_curve.py'
