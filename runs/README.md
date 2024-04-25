# 2024-04-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.6936   |       1.00944  |   0.06927  |
| solution-pl        |     6.14946  |       0.114931 |   0.17381  |
| solution-aron-mark |     0.709896 |       0.116935 |   0.177235 |
| solution-1-flask   |     1.55591  |       1.07998  |   0.261548 |
| solution-1         |     8.56742  |       1e-06    |   0.636215 |
| solution-2         |     0.684173 |       0.443893 |   1.53538  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.709192 |       1.00958  |   0.162332 |
| solution-aron-mark |     0.705178 |       0.126273 |   0.276362 |
| solution-pl        |     0.716186 |       0.126285 |   0.290419 |
| solution-1-flask   |     0.733252 |       1.00928  |   0.819313 |
| solution-2         |     0.737054 |       0.475229 |   3.45578  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.690418 |       1.00975  |   0.732638 |
| solution-aron-mark |     0.699769 |       0.131337 |   0.830371 |
| solution-pl        |     0.69579  |       0.131115 |   0.88226  |
| solution-1-flask   |     0.73737  |       1.00936  |   5.81474  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.684464 |       1.00953  |    2.70673 |
| solution-pl        |     0.686607 |       0.170871 |    2.79424 |
| solution-aron-mark |     0.787001 |       0.179428 |    3.10426 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.70027  |       1.00989  |    19.3195 |
| solution-pl    |     0.776315 |       0.297423 |    19.5072 |