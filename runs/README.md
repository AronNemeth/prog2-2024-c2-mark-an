# 2024-12-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.69372  |       1.00845  |   0.100968 |
| solution-aron-mark |     0.518157 |       0.106489 |   0.184677 |
| solution-pl        |     0.526647 |       0.112612 |   0.184916 |
| solution-1-flask   |     4.64656  |       1.06566  |   0.261141 |
| solution-1         |     7.25163  |       1e-06    |   0.569389 |
| solution-2         |     0.516131 |       0.476943 |   0.910194 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534931 |       0.109567 |   0.312014 |
| solution-aron-mark |     0.520559 |       0.109571 |   0.316807 |
| solution-flask     |     0.520434 |       1.00879  |   0.47928  |
| solution-1-flask   |     0.531076 |       1.00864  |   0.79815  |
| solution-2         |     0.519495 |       0.466098 |   2.17955  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.518736 |       0.116772 |    1.06461 |
| solution-aron-mark |     0.520276 |       0.115584 |    1.06904 |
| solution-flask     |     0.522393 |       1.00871  |    2.11622 |
| solution-1-flask   |     0.525975 |       1.00887  |    5.73315 |
| solution-2         |     0.520812 |       0.517613 |  171.19    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527221 |       0.14562  |    4.34252 |
| solution-pl        |     0.52433  |       0.143718 |    4.36269 |
| solution-flask     |     0.523277 |       1.00908  |    8.33341 |