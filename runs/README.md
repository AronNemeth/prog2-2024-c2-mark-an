# 2024-03-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.56937  |       1.04651  |   0.065342 |
| solution-aron-mark |     0.670707 |       0.110062 |   0.16234  |
| solution-pl        |     0.682705 |       0.110975 |   0.166232 |
| solution-1-flask   |     0.685669 |       1.00868  |   0.260983 |
| solution-1         |     8.31283  |       1e-06    |   0.857583 |
| solution-2         |     4.66512  |       0.594131 |   1.0194   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674093 |       1.00855  |   0.178941 |
| solution-aron-mark |     0.687529 |       0.116878 |   0.25595  |
| solution-pl        |     0.686824 |       0.116571 |   0.258132 |
| solution-1-flask   |     0.677354 |       1.00883  |   0.793531 |
| solution-2         |     0.684146 |       0.472503 |   3.44168  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.661323 |       0.121717 |   0.806438 |
| solution-aron-mark |     0.674698 |       0.123421 |   0.807912 |
| solution-flask     |     0.675945 |       1.00879  |   0.921668 |
| solution-1-flask   |     0.680854 |       1.00879  |   5.4714   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.676385 |       0.156786 |    3.3081  |
| solution-pl        |     0.677996 |       0.157711 |    3.32488 |
| solution-flask     |     0.665375 |       1.00857  |    5.56518 |