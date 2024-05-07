# 2024-05-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66113  |       1.00924  |   0.066574 |
| solution-aron-mark |     0.663917 |       0.119325 |   0.174543 |
| solution-pl        |     5.91008  |       0.1205   |   0.176192 |
| solution-1-flask   |     1.33134  |       1.11246  |   0.264165 |
| solution-1         |     8.46786  |       1e-06    |   0.605262 |
| solution-2         |     0.657623 |       0.412749 |   1.09119  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.650972 |       1.00894  |   0.204086 |
| solution-pl        |     0.653478 |       0.123389 |   0.26539  |
| solution-aron-mark |     0.665604 |       0.126159 |   0.282124 |
| solution-1-flask   |     0.675474 |       1.00898  |   0.789963 |
| solution-2         |     0.667895 |       0.431488 |   5.12233  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.680854 |       1.00901  |   0.722072 |
| solution-aron-mark |     0.664216 |       0.13324  |   0.831247 |
| solution-pl        |     0.696511 |       0.139631 |   0.962979 |
| solution-1-flask   |     0.71338  |       1.00954  |   5.5666   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662491 |       1.00903  |    2.61035 |
| solution-aron-mark |     0.664323 |       0.170565 |    2.65162 |
| solution-pl        |     0.66108  |       0.17055  |    2.72978 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666342 |       1.01314  |    16.156  |
| solution-aron-mark |     0.657215 |       0.302538 |    16.2344 |
| solution-pl        |     0.66511  |       0.305678 |    17.0565 |