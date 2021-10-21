 # Distance Between two city (ϕ and λ)
from math import radians, asin, cos, sin, sqrt

radius = 6371
ϕ1, λ1 = radians(59.9), radians(10.8)
ϕ2, λ2 = radians(49.3), radians(-123.1)

print("Distance=",distance:= 2*radius*asin(
        sqrt(
            ϕ_hav := sin((ϕ2-ϕ1) /2 ) ** 2
            + cos(ϕ1) * cos(ϕ2) * sin((λ2 - λ1) /2) **2
        )
    )
)

# Can assign value and run command
print("ϕ_hav=",ϕ_hav,"distance:",distance)
