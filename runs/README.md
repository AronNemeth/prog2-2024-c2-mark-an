# 2024-10-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2783   |       1.17375  |   0.157292 |
| solution-aron-mark |     0.554477 |       0.107406 |   0.181907 |
| solution-pl        |     5.79068  |       0.107993 |   0.203124 |
| solution-1-flask   |     0.571645 |       1.00896  |   0.256439 |
| solution-1         |     7.94719  |       1e-06    |   0.83868  |
| solution-2         |     0.569306 |       0.738176 |   1.2186   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.562996 |       0.110445 |   0.295265 |
| solution-pl        |     0.57032  |       0.109524 |   0.295595 |
| solution-flask     |     0.572496 |       1.00904  |   0.484197 |
| solution-1-flask   |     0.567875 |       1.0088   |   0.765005 |
| solution-2         |     0.562837 |       0.47275  |   3.25076  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.558276 |       0.115653 |    1.00503 |
| solution-pl        |     0.566181 |       0.11656  |    1.01131 |
| solution-flask     |     0.567425 |       1.00913  |    2.1101  |
| solution-1-flask   |     0.587082 |       1.00916  |    5.34743 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.566271 |       0.149058 |    4.28742 |
| solution-aron-mark |     0.562791 |       0.14554  |    4.28833 |
| solution-flask     |     0.565556 |       1.00905  |    8.36267 |