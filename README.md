#                       Model description
![unnamed](https://github.com/quantumArise/blue_point_predicted_all/assets/162140361/92f7bc31-1cd5-49fa-9e6f-f2835705be89)

##                        Prediction of thermoelectric material properties in D2

**Linear regression on cluster D2:** Figure 7 illustrates the relationship between the true and the predicted value of the Seebeck coefficient, power factor, electrical conductivity of n type doping material given p type doping material properties. We applied a linear regression fitting on material in D2, and we found a relationship as in equation 9 for the Seebeck coefficient, equation 10 for the power factor, and finally equation 11 for the electrical conductivity using dataset D2 as illustrated in figure 7 -(a), (b), (c) along with the respective r-square value and the mean absolute error.

Using these equations, one can very accurately predict with a very high R-square the value of the electrical conductivity, Seebeck coefficient and thermoelectric power factor of n doping material given the value of p doping material properties and vice versa. This thorough analysis underscores the equation’s accuracy in precisely estimating the Seebeck coefficient, power factor, and
electrical conductivity of n-doped materials, particularly when we possess information about the power factor of p-doped materials and vice versa. The small mean absolute error and the high R-squared value validate the model’s reliability, establishing it as a valuable tool for predicting these thermometric properties.
![unname](https://github.com/quantumArise/blue_point_predicted_all/assets/162140361/fa792ff6-85e4-493b-90c4-4a9506911bad)

![image](https://github.com/quantumArise/blue_point_predicted_all/assets/162140361/4b2097d2-1ffd-439d-8801-09b16d33d460)




**Random Forest on cluster D1:** Figure 8 is the result of the prediction of the seebeck coefficient. 
![image](https://github.com/quantumArise/blue_point_predicted_all/assets/162140361/937e67fa-cb46-484b-ae5a-ce31c490e910)

This consist of using material 

The second group consists of magpie featurization with effective mass and the result of the prediction using those features are represented in figure 8-(a), (b) for the whole dataset. The model without magpie featurization performs with an R-square of 0.76 and a MAE of 45.70. However with magpie featurization as one can see in 8-(b), the R-square is improved to 0.79 and the MAE as well. Figure 8-(c), (d) represented
