# Data and Reference Result 

**Checkpoint**: November 5, 2026, by 11:59 PM Mountain Time 
**Team**: Jane Gustafson, Lindsay McNary
**Date**: Nov 5, 2026

Use any prompts that help you describe your progress. Add a dated entry to the root README.md of your team's repository and link the relevant code and output there; this file is optional supporting material. 

## Data 
- Where did the data come from, and how did you obtain or prepare them?
  - We collected data from three primary sources to support our comparison of long term costs of gas vs electric powered cars. 
    - API Dashboard - U.S. Energy Information Administration (EIA) (https://www.eia.gov/opendata/browser/electricity/retail-sales?frequency=monthly&data=price;&start=2015-01&end=2020-12&sortColumn=period;&sortDirection=desc;)
      - We used this API to obtain historically accurate electricity price data. This information will provide a way for us to account for changes in electricity prices over time instead of relying on a single fixed value. Overall, it will help us estimate the cost of charging electric vehicles in order to compare the long term costs of electric cars v gas cars.
    - Vehicle CSV/Excel: Year, Make, Model and more | Car API (https://carapi.app/features/vehicle-csv-download/)
      - We downloaded two csv files that contain vehicle information, including model year, make, model, and other vehicle specifications. This will serve as the foundation for comparing gas and electric cars with similar characteristics.
    - Average Annual Miles per Driver by Age Group(https://www.fhwa.dot.gov/ohim/onh00/bar8.htm) 
      - This source gave us the average annual mileage estimate that we then manually incorporated into our dataset. It will allow us to calculate and compare operating costs based on a consistent annual driving distance.
- What data are available to your team now? 
  - All data needed for our initial analysis is currently available. 
- What remains to be collected or cleaned? 
  - Some remaining preparation is needed, for example, ensuring that all data are clean and in a consistent format.

- **Route C**: What does your first collected and cleaned sample contain?
  - Our initial dataset consists of vehicle information from the downloaded CSV files, historical electricity pricing information from the EIA, and an average annual mileage estimate. The dataset will allow us to calculate estimated energy costs for both types of vehicles and begin comparing the cost of operating them.

## Evaluation plan 
- What comparison, split, metric, or diagnostic will help answer your question? Why? 
  - We plan to calculate the average annual energy cost associated with each vehicle over the span of a five year period using average annual mileage, vehicle efficiency, and the corresponding electricity or gasoline price. We will then compare the estimated costs between electric and gas-powered vehicles to determine how much a driver could potentially save in the long run by choosing an electric vehicle. We will compare vehicles with similar characteristics, such as model year and vehicle size, to make the comparison more meaningful and avoid comparing vehicles that serve very different purposes. We want to know at what point (if ever) does it become more financially beneficial to buy a more expensive electric car.
- How will you avoid data leakage or another misleading comparison? 
  - There are many things we plan to do in order to avoid data leakage or other misleading comparisons. We will use the same annual mileage assumption across both vehicle types. We will use electricity and gasoline prices that correspond to the appropriate time periods whenever possible. We will only make conclusions based on comparisons between vehicles with similar characteristics. We will identify assumptions and limitations in our calculations, for example where we use national averages rather than location-specific prices.

## First runnable result 
- What baseline or other reference did you run? What did it produce? 
  - We ran our initial data transformation and cleaning process in Python using Pandas and Numpy. We combined the vehicle specifications, fuel pricing, and mileage information into a dataset that can be used for our cost comparisons.
- Where are the code and output? Link them, and include the command needed to rerun the result if available. 
  - Stat_486_Project/data_transform.ipynb at main · lmcnary/Stat_486_Project 
- What did this first result suggest, and what will you try next? 
  - Our initial data transformation showed that we can combine the different data sources into a usable dataset. This will allow us to long-term energy costs and compare electric and gas-powered vehicles. Next, we will examine the differences between electric vehicles and gas powered cars	
