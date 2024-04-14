# 2024-04-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671363 |       1.00917  |   0.06394  |
| solution-aron-mark |     0.651432 |       0.112674 |   0.165072 |
| solution-pl        |     5.83286  |       0.11384  |   0.168791 |
| solution-1-flask   |     1.44653  |       1.05129  |   0.271412 |
| solution-1         |     7.98642  |       1e-06    |   0.702535 |
| solution-2         |     0.6484   |       0.416148 |   1.24429  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656681 |       1.00892  |   0.161538 |
| solution-pl        |     0.668543 |       0.118121 |   0.258049 |
| solution-aron-mark |     0.660082 |       0.11784  |   0.261783 |
| solution-1-flask   |     0.66747  |       1.00869  |   0.781006 |
| solution-2         |     0.659791 |       0.42775  |   3.01857  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67883  |       1.00908  |   0.697309 |
| solution-aron-mark |     0.650756 |       0.12512  |   0.81144  |
| solution-pl        |     0.65682  |       0.123619 |   0.831027 |
| solution-1-flask   |     0.669365 |       1.0088   |   5.64942  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.651567 |       1.00901  |    2.43426 |
| solution-aron-mark |     0.653451 |       0.160265 |    3.16904 |
| solution-pl        |     0.663758 |       0.162941 |    3.20245 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.656255 |         1.0089 |    15.5952 |