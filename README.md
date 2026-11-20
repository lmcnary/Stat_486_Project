# Gas and Hybrid Mileage
### Stats 486 -- Jane Gustafson and Lindsay McNary
###
---

## Introduction

**Question**

## Findings?

## Repository Mapping

## Setup and Run Instructions

## Data Access and Sources

## Data Schema

## Project Development 

| Date | Checkpoint | README entry |
| --- | --- | --- |
| **Oct 20** | Team and directions | Name the team and describe two possible questions, routes, and data sources. Start the repository. If you need help finding a team, contact the instructor. |
| **Oct 27** | Project plan | Are electric cars worth it? , [data](https://www.fueleconomy.gov/feg/ws/), he baseline would be a gas-powered car of similar model years and vehicle class to the electric car, We will use a matched pairs design with data-quality diagnostics measuring the Mean difference at a 95% confidence interval. |
| **Nov 5** | Data and reference result | Our initial dataset consists of vehicle information from the downloaded CSV files, historical electricity pricing information from the EIA, and an average annual mileage estimate. The dataset will allow us to calculate estimated energy costs for both types of vehicles and begin comparing the cost of operating them. We plan to calculate the average annual energy cost associated with each vehicle over the span of a five year period using average annual mileage, vehicle efficiency, and the corresponding electricity or gasoline price. We will then compare the estimated costs between electric and gas-powered vehicles to determine how much a driver could potentially save in the long run by choosing an electric vehicle. We will compare vehicles with similar characteristics, such as model year and vehicle size, to make the comparison more meaningful and avoid comparing vehicles that serve very different purposes. We want to know at what point (if ever) does it become more financially beneficial to buy a more expensive electric car. We ran our initial data transformation and cleaning process in Python using Pandas and Numpy. We combined the vehicle specifications, fuel pricing, and mileage information into a dataset that can be used for our cost comparisons |
| **Nov 12** | Working investigation |  Our original question focused on comparing the long-term costs of electric and gas-powered vehicles, however, due to difficulty finding enough relevant electric vehicle data, we decided to change our research question to focus instead on predicting vehicle mileage using vehicle characteristics and comparing gas and hybrid vehicles. We developed a data cleaning and integration pipeline in Python using Pandas and NumPy to combine vehicle specifications with historical gasoline and electricity pricing data (found in [clean.py](https://github.com/lmcnary/Stat_486_Project/blob/main/src/clean.py) and [pipeline.py](https://github.com/lmcnary/Stat_486_Project/blob/main/src/pipeline.py)). Our pipeline classifies vehicles by fuel type, removes diesel vehicles, extracts characteristics such as number of doors, body type, engine size, cylinders, turbo status, and transmission, and handles missing mileage values and duplicate observations. We then created a cleaned dataset (car_pricing_final.csv) to use for our machine learning analysis. We have started building a Decision Tree regression model to predict mileage for gas vehicles using an 80/20 training and testing split [ml-efficiency.ipynb](https://github.com/lmcnary/Stat_486_Project/blob/main/ml-efficiency.ipynb). We tested different tree depths and minimum samples per leaf and evaluated performance using Mean Absolute Error (MAE) and R². Our next step is to complete the same process for hybrid vehicles and compare how accurately mileage can be predicted for each vehicle type. We evaluated our clean data using duplicate checks, missingness checks, fuel type counts, and descriptive statistics. You can look at ([one-clean-observation.ipynb](https://github.com/lmcnary/Stat_486_Project/blob/e3898d1fdc3c8475fecb806a72d01907a573497f/one-clean-observation.ipynb)) to see the dataset's structure and consistency for every one clean observation and the data quality.There are no duplicates or missing values for mileage |
| **Nov 19** | Evidence and interpretation | The cleaned dataset contains 11,839 gas vehicles and 777 hybrids. After removing all incomplete rows, the one-clean-observation notebook show no missing values or duplicate rows. Mean EPA combined mileage is about 22.75 MPG for gas vehicle and 34.31 MPG for hybrids. The summaries shown in the notebook just describe the dataset. See [one-clean-observation](https://github.com/lmcnary/Stat_486_Project/blob/main/one-clean-observation.ipynb) and [the cleaning pipeline](https://github.com/lmcnary/Stat_486_Project/tree/main/src) for more details. Our Decision tree Model shows the gas cars have an MAE of about 2.25 MPG and R^2 of about 0.619. The Decision tree model for the hybrids the MAE was about 2.82MPG and the R^2 score was about 0.843 as shown in [ml-efficiency](https://github.com/lmcnary/Stat_486_Project/blob/main/ml-efficiency.ipynb).after dropping the missing values instead of using the simple imputer our accuracy decreased a lot it went from around 0.9 to 0.69. I have been testing different decision tree models and random forest models to see if the validation score increases, but I may need to try a different model. |
| **Dec 3** | Reproduction draft | Link the code-and-results-complete draft, identify the main result and known gaps, and give exact setup and run commands using the committed `uv` environment files. B teams should link both valid Kaggle submissions and the commands that generated them. |
| **Dec 8 or 10** | Presentation | Link the presentation materials and state the main findings before your assigned class meeting. Present during that meeting. |
| **Dec 10** | Final submission | Identify the final commit or tag and link the completed `report.md`, main results, and presentation materials. Submit the repository URL and commit or tag in Canvas by 11:59 PM Mountain Time. |
