# 2024-11-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.44293  |       1.11306  |   0.110207 |
| solution-aron-mark |     0.554179 |       0.106678 |   0.190504 |
| solution-pl        |     5.72995  |       0.109844 |   0.191355 |
| solution-1-flask   |     0.55692  |       1.00898  |   0.266886 |
| solution-1         |     7.96647  |       1e-06    |   0.792178 |
| solution-2         |     0.547189 |       0.736702 |   0.912279 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.553686 |       0.10831  |   0.297557 |
| solution-pl        |     0.555922 |       0.10837  |   0.318886 |
| solution-flask     |     0.558465 |       1.00872  |   0.476137 |
| solution-1-flask   |     0.556295 |       1.00943  |   0.775089 |
| solution-2         |     0.552968 |       0.470953 |   3.53152  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.55076  |       0.115902 |    1.01091 |
| solution-pl        |     0.557553 |       0.116696 |    1.01604 |
| solution-flask     |     0.571859 |       1.00898  |    2.1178  |
| solution-1-flask   |     0.559048 |       1.00897  |    5.4357  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.552114 |       0.146924 |    4.17715 |
| solution-aron-mark |     0.552671 |       0.145129 |    4.21691 |
| solution-flask     |     0.552215 |       1.00947  |    8.33451 |