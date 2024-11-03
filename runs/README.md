# 2024-11-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.21028  |       1.12204  |   0.106972 |
| solution-aron-mark |     0.553854 |       0.108792 |   0.173388 |
| solution-pl        |     5.80378  |       0.107243 |   0.174916 |
| solution-1-flask   |     0.56827  |       1.00894  |   0.257304 |
| solution-1         |     7.6813   |       1e-06    |   0.586952 |
| solution-2         |     0.549989 |       0.492187 |   1.17648  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.584648 |       0.109241 |   0.294811 |
| solution-aron-mark |     0.566918 |       0.109472 |   0.337576 |
| solution-flask     |     0.566357 |       1.01034  |   0.475943 |
| solution-1-flask   |     0.56526  |       1.00894  |   0.770203 |
| solution-2         |     0.554541 |       0.469652 |  12.3385   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.552159 |       0.11729  |    1.01045 |
| solution-pl        |     0.557065 |       0.116953 |    1.02929 |
| solution-flask     |     0.553832 |       1.00905  |    2.12801 |
| solution-1-flask   |     0.565293 |       1.00926  |    5.37485 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.559042 |       0.146614 |    4.16958 |
| solution-aron-mark |     0.556359 |       0.144523 |    4.26265 |
| solution-flask     |     0.560938 |       1.00906  |    8.14093 |