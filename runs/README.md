# 2025-02-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.14344  |       1.06672  |   0.080178 |
| solution-aron-mark |     0.544184 |       0.140741 |   0.201327 |
| solution-pl        |     4.60668  |       0.140118 |   0.206555 |
| solution-1-flask   |     0.560024 |       1.00865  |   0.261468 |
| solution-1         |     7.42221  |       1e-06    |   0.593623 |
| solution-2         |     0.533808 |       0.547621 |   1.48038  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554708 |       1.00913  |   0.292589 |
| solution-aron-mark |     0.545612 |       0.138925 |   0.304034 |
| solution-pl        |     0.536793 |       0.140688 |   0.306332 |
| solution-1-flask   |     0.548338 |       1.00931  |   0.794967 |
| solution-2         |     0.545739 |       0.501372 |  12.4916   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.544019 |       0.153244 |   0.90207  |
| solution-pl        |     0.533851 |       0.146651 |   0.907833 |
| solution-flask     |     0.545147 |       1.00913  |   1.23742  |
| solution-1-flask   |     0.55065  |       1.00921  |   5.71129  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.537768 |       0.180107 |    2.86468 |
| solution-pl        |     0.542102 |       0.177319 |    2.88775 |
| solution-flask     |     0.548393 |       1.00917  |    4.2275  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53927  |       0.306412 |    17.4878 |
| solution-aron-mark |     0.568973 |       0.281849 |    17.8302 |