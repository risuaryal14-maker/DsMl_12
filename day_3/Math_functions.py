"""MATH FUNCTIONS
1. ABS()--> RETURN THE ABSOLUTE VALUE OF A NUMBER
2. ROUND()--> RETURN A NUMBER ROUNDED TO A SPECIFIED NUMBER OF DECIMALS
3. POW()--> RETURN THE VALUE OF A NUMBER RAISED TO A POWER
4. MAX()--> RETURN THE LARGEST NUMBER IN A LIST OR TUPLE
5. MIN()--> RETURN THE SMALLEST NUMBER IN A LIST OR TUPLE
6. SUM()--> RETURN THE SUM OF ALL NUMBERS IN A LIST OR TUPLE
7. LOG()--> RETURN THE NATURAL LOGARITHM OF A NUMBER
8. SQRT()--> RETURN THE SQUARE ROOT OF A NUMBER
9. GCD()--> RETURN THE GREATEST COMMON DIVISOR OF TWO NUMBERS"""

#ABSOLUTE VALUE
number=-10
absolute_value=abs(number)
print("Absolute Value:", absolute_value)

#ROUND
number2=3.14159
rounded_value=round(number2,2)
print("Rounded Value:", rounded_value)

#POW
base=2
exponent=3
power_value=pow(base, exponent)
print("Power Value:", power_value)

#MAX
numbers=[1,2,3,4,5]
max_value=max(numbers)
print("Max Value:", max_value)

#MIN
numbers2=[1,2,3,4,5]
min_value=min(numbers2)
print("Min Value:", min_value)

#SUM
numbers3=[1,2,3,4,5]
sum_value=sum(numbers3)
print("Sum Value:", sum_value)

#LOG
import math
number3=10
log_value=math.log(number3)
print("Log Value:", log_value)

#SQRT
number4=16
sqrt_value=math.sqrt(number4)
print("Square Root Value:", sqrt_value) 

#GCD
number5=12
number6=18
gcd_value=math.gcd(number5, number6)
print("GCD Value:", gcd_value)