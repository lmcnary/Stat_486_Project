# Working Investigation

**Checkpoint:** November 12, 2026, by 11:59 PM Mountain Time  
**Team:** Jane Gustafson, Lindsay McNary
**Route:** C  
**Date:** November 12, 2026

Use the prompts for your chosen route to describe what is working now and what you learned from a first check. Add a new, dated entry for the working investigation to the root `README.md` of your team's GitHub repository and link the relevant code and output there. Keep earlier entries, commit the update, and submit the repository URL with that commit in Canvas. This file is optional supporting material; it does not replace the README entry. Preliminary or negative results are welcome when you explain what they show.

## Working code and evidence

- What part of your investigation runs now? Link the code, configuration, and an output it produced.
Our current investigation includes a data cleaning and integration pipeline and an initial machine learning model to predict vehicle mileage. We have created a cleaned dataset called car_pricing_final.csv that combines vehicle specifications with additional vehicle characteristics extracted from trim descriptions. We have also started building a Decision Tree regression model using the cleaned dataset to predict mileage for gas vehicles. (linked in README.md)
- What inputs and steps does the run use? Give the command to reproduce the first check if available, and note any data access or setup needed.
Our pipeline uses downloaded vehicle CSV files and historical gasoline and electricity pricing data from the EIA. We use Python, Pandas, and NumPy to clean the data, classify vehicles by fuel type, combine pricing information, extract vehicle characteristics, remove duplicate observations, and handle missing mileage values. To reproduce the initial model, we load the cleaned dataset, filter for gas vehicles, select vehicle characteristics as predictors, and split the data into training and testing sets using an 80/20 split with a random state of 42. We then use a preprocessing pipeline before fitting a Decision Tree regression model.
- What comparison or diagnostic did you run, using which evaluation split, metric, or quality measure? What does the result show so far?
We tested different combinations of maximum tree depth (2, 5, 10, and 20) and minimum samples per leaf (5, 10, 20, and 50). We evaluated the models using Mean Absolute Error (MAE) and R², along with training and testing R² to examine how well the models generalize to unseen data.

## Route-specific progress

Complete the prompts for your chosen route.

### Route C: New dataset and ML pipeline

- Where are the collection, cleaning, and integration scripts that produce the cleaned dataset? Give the run order and record the source dates or versions and any access limits.
clean.py cleans the original gas, electricity, and vehicle data. pipeline.py combines the cleaned data and creates our final dataset. ml-efficiency.ipynb uses the final dataset to train and test our models. Run in that order. Our original CSV files are stored in data/source/.
- What does one cleaned observation represent? Link a permissible sample or summary and report relevant quality checks, such as coverage, duplicates, missingness, or label consistency.
One observation represents one vehicle trim/configuration, including its characteristics and EPA combined mileage. We combined vehicle mileage and trim information, removed duplicate rows, and removed vehicles without mileage data. We also labeled vehicles as gas, hybrid, electric, or diesel and removed diesel vehicles.
- What initial ML result did you obtain **using the cleaned output of this pipeline**? Link its code and output. What do the quality checks and ML result suggest you should investigate next?
We used our cleaned dataset to build a decision tree model that predicts vehicle mileage based on characteristics such as engine size, body type, number of doors, cylinders, and transmission. We split the gas vehicle data into 80% training data and 20% testing data. We tested different tree depths and minimum leaf sizes and evaluated the models using MAE and R². We want to compare how well the model predicts mileage for gas and hybrid vehicles and see which vehicle characteristics are most useful.

## Next question

- If your plan changed since November 5, what evidence or feedback led to the change?
We changed our question from comparing the long-term costs of electric and gas vehicles to predicting mileage for gas and hybrid vehicles. We had trouble finding enough consistent electric vehicle data to make a fair comparison. The new question lets us use more of the vehicle data we already have.
- What is uncertain or blocked now, and how will you adjust the scope if needed?
We still need to check the quality of our dataset, finish the hybrid model, and compare its results with the gas model. If we do not have enough reliable hybrid data, we may need to narrow our comparison or use fewer vehicle characteristics.
