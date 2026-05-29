# 2026-05-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.84943  |       1.14071  |   0.103562 |
| solution-1-flask   |     0.45033  |       1.00905  |   0.231933 |
| solution-pl        |     0.459944 |       0.155238 |   0.234608 |
| solution-aron-mark |     0.436382 |       0.154343 |   0.235658 |
| solution-1         |     7.74425  |       1e-06    |   0.618856 |
| solution-2         |     4.60968  |       0.660314 |   0.816323 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445448 |       0.15631  |   0.352866 |
| solution-pl        |     0.440581 |       0.157599 |   0.355249 |
| solution-flask     |     0.441811 |       1.00894  |   0.402213 |
| solution-1-flask   |     0.459939 |       1.00925  |   0.717089 |
| solution-2         |     0.452213 |       0.532795 |   4.23359  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.443864 |       0.162703 |    1.03167 |
| solution-aron-mark |     0.46737  |       0.163269 |    1.03361 |
| solution-flask     |     0.445115 |       1.00909  |    1.64901 |
| solution-1-flask   |     0.450149 |       1.00903  |    5.64496 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.440047 |       0.187243 |    3.96501 |
| solution-pl        |     0.453483 |       0.191589 |    4.12011 |
| solution-flask     |     0.465619 |       1.0089   |    5.46674 |