# STAT 486 Project Plan

**Due:** Tuesday, October 27, 2026, at 11:59 PM Mountain Time  
**Team:** Jane Gustafson, Lindsay McNary  
**Repository:** [[GitHub URL]](https://github.com/lmcnary/Stat_486_Project.git )  
**Date updated:** 10/27/26

Use these prompts to plan your investigation. Keep the answers focused; revise the plan when evidence or instructor feedback changes your direction. The Oct. 27 checkpoint still requires a new, dated project-plan entry in the root `README.md` of your team's GitHub repository. Link this document there if you use it; this document does not replace that entry.

## Project question and purpose

- What specific question do you want to investigate?
  - Are electric cars worth it? 
    - Are electric vehicles less expensive to own than comparable gas-powered vehicles over a five year period? Over a ten year period? What characteristics influence total ownership cost? When does it become more cost effective to purchase an electric car as opposed to a gas car?
- Why does this question interest your team, and what might someone learn from answering it?
  - We are interested in this topic because electric cars are becoming increasingly more popular. As young adults, we want to know whether it would be worth it in the long run to invest in a more expensive electric car as opposed to a cheaper gas powered car.
- What claim or expectation could your evidence support, challenge, or leave uncertain?
  - We expect that electric cars will be more cost-effective over time because of the price of electricity and less need for routine maintenance, specifically for drivers who travel greater distances each year.
- What does one observation represent in the data you expect to use?
  - One observation would be an individual vehicle (make, model, year)

## Chosen route

Choose one route and explain why it fits your question and available time.

- [ ] **C. Build a dataset** and use it in a reproducible ML pipeline

**Why this route:** [How does the route support the question and the team's intended contribution?]
We chose route C because it will help us strengthen our skills as analysts to collect, clean, and assemble data. We also want to use our dataset to develop machine learning models that can predict 5 and 10 year ownership costs and identify which factors have the most impact on those costs.
## Data source and access

- What data will you use? Give the dataset, competition, API, or source name and a direct link if available.
   - We will use data from alternative fuels data center – Fuel Economy Web Services 
Possible other sources: https://afdc.energy.gov/, https://www.kaggle.com/search?q=electric+vs+gas+cars,
- What does each row or record represent, and which fields are relevant to the question?
  - Each row represents a car. Features relevant to our question would be mpg, electricity consumption per 100 miles, price of fuel
- How will the team obtain the data? Note access requirements, collection dates or versions, and any expected size or compute needs.
  - Downloading a csv 
- What license, competition rules, privacy, ethical, or other use limits apply? Could any data be restricted or identifying?
  - The data from the alternative fuels data center is free to be distributed for non-commercial, scientific, and educational uses
- What data quality issues might affect the investigation (for example, missingness, duplicates, labels, coverage, or changes over time)?
  - There is some missing data. The dataset contains a lot of different vehicle types like dual-fuel, diesel, hybrids, etc.

## Route-specific plan

Complete the subsection for your chosen route. For a different route, remove the unused subsections.

### Route C: New dataset and ML pipeline

- What useful dataset will you create, and what question will the ML analysis investigate?
  - The dataset will include information about electric and gas powered cars - specifically prices new/used, fuel efficiency, miles per gallon, and maintenance costs
- What source or sources will you combine or collect? Are collection and redistribution permitted?
  - There are a few options (listed above) but we haven’t decided fully yet.
- What does one observation represent, and what will the dataset schema contain?
- How will you collect, integrate, clean, or label the data? Which scripts will reproduce these steps?
  - We will standardize things like vehicle names and dates, identify and deal with missing data values, and ensure consistent measurements throughout.
  - We plan to create python scripts to automate data collection, cleaning, and integration processes so that our results can be reproduced
- How will you record source locations, access or license terms, collection dates or versions, and transformations?
- What quality checks will you run (such as join coverage, duplicates, missingness, label consistency, or source changes)?
- Can you preserve a permitted snapshot or small fixture? If raw data cannot be shared, how can an authorized reader rebuild or verify the cleaned data?
  - We plan to preserve a copy of the cleaned dataset in the github repository and if that isn’t permitted then we will provide links to the original datasets
- What reference ML method will use the cleaned dataset, and what evidence will show both dataset fitness and ML usefulness?
  - Our original thought is to use linear regression as the baseline model to predict cost efficiency over 5 and 10 year time periods.

## Initial reference and proposed contribution

- What is the simplest credible baseline, reference method, or comparison for your question?
  - The baseline would be a gas-powered car of similar model years and vehicle class to the electric car
- What will your team design, build, collect, or investigate beyond that reference?
  - We will design a model to compare the electric and gas cars
- Which choices, code, data, papers, notebooks, packages, or pretrained models will come from others, and how will you credit them?
  - We will cite our data sources in the README

## Evaluation and evidence

- What evaluation design fits the question and how the data were collected (for example, a split, cross-validation, control, stability check, or data-quality diagnostic)?
  - A matched pairs design with data-quality diagnostics
- What metric or diagnostic will you use, and why does it match the question?
  - Mean difference at a 95% confidence interval
- How will you compare your work with a baseline or other reference? What would count as evidence against your initial expectation?
  - mean difference
- What informative error, failure, uncertainty, tradeoff, or limitation will you inspect?
  - One limitation may be a lack of a directly comparable gasoline-powered vehicle for some electric vehicles. For example, a Tesla may not have a gasoline counterpart with the same size, performance, and model year, because they only manufacture EVs.
- What figures, tables, examples, or other outputs could make the results understandable?
  - side -by-side boxplots comparing the range in price of EVs and gas-powered cars. A confidence interval.

## Risks and backup scope

- What could prevent the plan from working (for example, access, collection, compute, time, data quality, or competition constraints)?
  - If we cannot match up the EVs to equivalent gas powered cars, then we will not be able to compare with matched pairs mean difference
- What smaller version would still let you answer a useful question if a risk occurs?
  - We could group together the EVs and then group together the gas powered cars and compare that way
- What evidence or feedback would lead you to pivot, and how would you document the reason?
  - If we find in the dataset the EVs do not have an equivalent gas-powered match. We could mention it in the readme

## Reproducibility and team contributions

- Where will code, configuration, data instructions, and results live in the repository?
  - Code.ipynb, instructions.md
- What is the first small runnable result you aim to produce, and what will a reader need to reproduce it?
  - The first runnable will be a streamlit app showing some plots comparing EVs to gas powered cars.
- How will team members contribute substantively and review one another's work?
  - We will assign tasks and complete them by the morning of the specified day then review each other's same day.
- What support, approval, or early instructor feedback would help you proceed?
  - We would love feedback affirming we are on the right track and ways we could improve our project.

## Sources

List initial data sources, papers, competition pages, public notebooks, software, and other materials relevant to the plan. Include links and access or license details when known.

- [Source or material, link, and relevant note]
