# 2026-09-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.5611   |       1.13694  |   0.105622 |
| solution-pl        |     2.38531  |       0.156389 |   0.23218  |
| solution-aron-mark |     0.424008 |       0.153338 |   0.232557 |
| solution-1-flask   |     0.428818 |       1.00878  |   0.234581 |
| solution-1         |     8.37591  |       1e-06    |   0.600762 |
| solution-2         |     4.78919  |       0.578892 |   0.813387 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.426077 |       0.153523 |   0.351435 |
| solution-pl        |     0.42226  |       0.154245 |   0.353162 |
| solution-flask     |     0.423091 |       1.0091   |   0.396301 |
| solution-1-flask   |     0.422828 |       1.00891  |   0.748076 |
| solution-2         |     0.420011 |       0.50282  |   5.18895  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420301 |       0.16027  |    1.02915 |
| solution-pl        |     0.4208   |       0.159987 |    1.05934 |
| solution-flask     |     0.423615 |       1.00918  |    1.63601 |
| solution-1-flask   |     0.42909  |       1.00902  |    6.31663 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.417652 |       0.184412 |    3.43395 |
| solution-pl        |     0.422533 |       0.184193 |    3.45154 |
| solution-flask     |     0.419554 |       1.00896  |    5.22157 |