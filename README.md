# Curve Fit Assignment — Research and Development 

## Final Parameter Values
- θ = 0.4908 radians  
- M = 0.0214  
- X = 54.9008  

## Parametric Equation (LaTeX)
\[
\left(
t \cdot \cos(0.4908) - e^{0.0214|t|} \cdot \sin(0.3t)\sin(0.4908) + 54.9008,\;
42 + t \cdot \sin(0.4908) + e^{0.0214|t|} \cdot \sin(0.3t)\cos(0.4908)
\right)
\]

## Desmos Equation

```
(t*cos(0.4908) - e^(0.0214*abs(t))*sin(0.3*t)*sin(0.4908) + 54.9008, 
 42 + t*sin(0.4908) + e^(0.0214*abs(t))*sin(0.3*t)*cos(0.4908))
```


Domain: 6 ≤ t ≤ 60

## Methodology
1. The given dataset 'xy_data.csv' was used for the curve fitting task.  
2. I generated equal intervals of 't' between 6 and 60.  
3. The provided parametric equations were used with unknown parameters θ, M, and X.  
4. I applied the L-BFGS-B optimization method to minimize the L1 distance between actual and predicted points.  
5. The optimized values of θ, M, and X were recorded.  
6. The fitted curve was plotted and verified with the given data.

## Files Included
- 'xy_data.csv' — given dataset  
- 'fit_curve.py' — Python program used for optimization  


## Submitted by
**Rayapu Varshitha**

