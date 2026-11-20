## Project Development 

| Date | Checkpoint | Required README entry |
| --- | --- | --- |
| **Oct 20** | Team and directions | Name the team and describe two possible questions, routes, and data sources. Start the repository. If you need help finding a team, contact the instructor. |
| **Oct 27** | Project plan | Are electric cars worth it? , [data](https://www.fueleconomy.gov/feg/ws/), he baseline would be a gas-powered car of similar model years and vehicle class to the electric car, We will use a matched pairs design with data-quality diagnostics measuring the Mean difference at a 95% confidence interval. |
| **Nov 5** | Data and reference result | Our initial dataset consists of vehicle information from the downloaded CSV files, historical electricity pricing information from the EIA, and an average annual mileage estimate. The dataset will allow us to calculate estimated energy costs for both types of vehicles and begin comparing the cost of operating them. We plan to calculate the average annual energy cost associated with each vehicle over the span of a five year period using average annual mileage, vehicle efficiency, and the corresponding electricity or gasoline price. We will then compare the estimated costs between electric and gas-powered vehicles to determine how much a driver could potentially save in the long run by choosing an electric vehicle. We will compare vehicles with similar characteristics, such as model year and vehicle size, to make the comparison more meaningful and avoid comparing vehicles that serve very different purposes. We want to know at what point (if ever) does it become more financially beneficial to buy a more expensive electric car. We ran our initial data transformation and cleaning process in Python using Pandas and Numpy. We combined the vehicle specifications, fuel pricing, and mileage information into a dataset that can be used for our cost comparisons |
| **Nov 12** | Working investigation |  Our original question focused on comparing the long-term costs of electric and gas-powered vehicles, however, due to difficulty finding enough relevant electric vehicle data, we decided to change our research question to focus instead on predicting vehicle mileage using vehicle characteristics and comparing gas and hybrid vehicles. We developed a data cleaning and integration pipeline in Python using Pandas and NumPy to combine vehicle specifications with historical gasoline and electricity pricing data (found in [clean.py](https://github.com/lmcnary/Stat_486_Project/blob/main/src/clean.py) and [pipeline.py](https://github.com/lmcnary/Stat_486_Project/blob/main/src/pipeline.py)). Our pipeline classifies vehicles by fuel type, removes diesel vehicles, extracts characteristics such as number of doors, body type, engine size, cylinders, turbo status, and transmission, and handles missing mileage values and duplicate observations. We then created a cleaned dataset (car_pricing_final.csv) to use for our machine learning analysis. We have started building a Decision Tree regression model to predict mileage for gas vehicles using an 80/20 training and testing split [ml-efficiency.ipynb](https://github.com/lmcnary/Stat_486_Project/blob/main/ml-efficiency.ipynb). We tested different tree depths and minimum samples per leaf and evaluated performance using Mean Absolute Error (MAE) and R². Our next step is to complete the same process for hybrid vehicles and compare how accurately mileage can be predicted for each vehicle type. We evaluated our clean data using duplicate checks, missingness checks, fuel type counts, and descriptive statistics. You can look at ([one-clean-observation.ipynb](https://github.com/lmcnary/Stat_486_Project/blob/e3898d1fdc3c8475fecb806a72d01907a573497f/one-clean-observation.ipynb)) to see the dataset's structure and consistency for every one clean observation and the data quality.There are no duplicates or missing values for mileage |
| **Nov 19** | Evidence and interpretation | The cleaned dataset contains 11,839 gas vehicles and 777 hybrids. After removing all incomplete rows, the one-clean-observation notebook show no missing values or duplicate rows. Mean EPA combined mileage is about 22.75 MPG for gas vehicle and 34.31 MPG for hybrids. The summaries shown in the notebook just describe the dataset. See [one-clean-observation](https://github.com/lmcnary/Stat_486_Project/blob/main/one-clean-observation.ipynb) and [the cleaning pipeline](https://github.com/lmcnary/Stat_486_Project/tree/main/src) for more details. Our Decision tree Model shows the gas cars have an MAE of about 2.25 MPG and R^2 of about 0.619. The Decision tree model for the hybrids the MAE was about 2.82MPG and the R^2 score was about 0.843 as shown in [ml-efficiency](https://github.com/lmcnary/Stat_486_Project/blob/main/ml-efficiency.ipynb).after dropping the missing values instead of using the simple imputer our accuracy decreased a lot it went from around 0.9 to 0.69. I have been testing different decision tree models and random forest models to see if the validation score increases, but I may need to try a different model. |
| **Dec 3** | Reproduction draft | Link the code-and-results-complete draft, identify the main result and known gaps, and give exact setup and run commands using the committed `uv` environment files. B teams should link both valid Kaggle submissions and the commands that generated them. |
| **Dec 8 or 10** | Presentation | Link the presentation materials and state the main findings before your assigned class meeting. Present during that meeting. |
| **Dec 10** | Final submission | Identify the final commit or tag and link the completed `report.md`, main results, and presentation materials. Submit the repository URL and commit or tag in Canvas by 11:59 PM Mountain Time. |


## The final GitHub repository

The repository is the main project artifact. Organize it in a way that fits your work. It should contain:

- a **README** that introduces the question and main finding, maps the repository, and gives exact setup, data-access, and run instructions;
- the code and configuration used for the main analysis, plus a **reproducible `uv` environment**: commit `pyproject.toml` and `uv.lock`, and state the required Python version in the README or a committed `.python-version` file;
- saved figures, tables, outputs, or examples to support the report and presentation; and
- a completed `report.md` based on the [Markdown report template](report-template.md), linked from the repository README, and the presentation materials.

For route C, also include a short description of the dataset's schema, sources, collection date or version, permitted access, cleaning decisions, and quality checks. The repository must contain the scraping or collection scripts used for the reported dataset, even if the raw data cannot be shared. Document the commands that run those scripts and build the cleaned data from accessible inputs; include a shareable data snapshot or small fixture when source terms permit it. The ML run should use the cleaned output produced by this pipeline.

For route B, include the code, configurations, and run commands for **both** pipelines. Link each valid Kaggle submission to the pipeline and commit that produced it, and record its local validation and Kaggle result. A reader should be able to regenerate each submission file from the documented data access steps.

## The written project report

Copy the [report template](report-template.md) into the root of your team's repository as `report.md`, fill it in with your own writing, commit it, and link it from the root README. Submit the completed report in your repository. This is an account of your project experience, not a publication-style technical paper. This is an opportunity to explain your understanding of the project and your outcomes. It is expected that you do **not** use AI for this part, other than for grammatical polishing. Tell readers why you chose the question, the main steps you took, the choices and challenges that shaped the work, and the final outcomes. Explain what worked, what did not, what you learned, and what remains uncertain. Include enough detail and links to code, data, figures, or results for a reader to follow your account, along with each teammate's contributions and your sources. The README carries the exact setup and run instructions, so the report can link to them.

There is **no page or word limit**. Use the length needed to fully describe your project, without padding it with raw logs or a list of every minor experiment. You may adapt the template headings to fit your story as long as the report covers the substance above.

## Verify the environment

Before the December 3 review and again before final submission, **verify the environment from a fresh clone**. Run `uv sync`, then use `uv run` to execute your documented test, small demonstration, or representative-result command. Confirm that it finishes and produces the expected output; record the command and outcome in the corresponding dated README entry. The committed environment files recreate the local `.venv/` directory; do not commit that directory itself. A reader should be able to obtain permitted data and rerun a representative result without hidden notebook state or personal file paths. If the full run is costly, provide a small runnable path and record the configuration and provenance of the full result. Do not commit credentials, restricted data, or unnecessary large files. If data cannot be shared, explain how an authorized reader can access them and provide a small permissible example when possible.

## Presentation and collaboration

Plan for about **12 - 15 minutes** for the presentation. Slides, a live demonstration, or both are welcome. Focus on the question, the choices that mattered, the evidence, and what you learned. Every member should present a meaningful part and be able to discuss the shared project. Have your presentation materials ready for your assigned class meeting and add them to the final repository.

All teammates should make substantive technical or analytical contributions. You may divide tasks, but review each other's work and keep the main decisions understandable to the whole team. Cite datasets, papers, public notebooks, packages, and pretrained models. Follow data licenses and competition rules. If your idea involves collecting new information from people or using private or identifying data, discuss it with the instructor before proceeding.

## AI use

AI tools may help you conceive project ideas, write or debug code, and polish work your team has already created. **Your team must create the final report and presentation slides, including their outlines, interpretation, and conclusions. Do not use AI to generate those deliverables.** I want to hear your own take on what happened in the project. Verify AI-assisted code and claims, and briefly disclose material AI help in `report.md`.

## Grading

The project is worth **100 points**:

| Component | Points |
| --- | ---: |
| Checkpoints | 30 |
| Reproducible workflow | 20 |
| Presentation | 20 |
| Written project report | 30 |
| **Total** | **100** |

The [rubric](rubric.md) explains how these points are judged; the [presentation scoring sheet](presentation-rubric.md) gives the detailed 20-point presentation criteria. The workflow score covers the working code, data-to-result path, and fresh-clone setup. The presentation and report scores reward your team's own account of its choices, evidence, challenges, and outcomes. Quality of reasoning and clear communication matter more than model count, compute spent, or leaderboard position.
