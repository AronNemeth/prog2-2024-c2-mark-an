# 2024-03-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.75947  |       1.05301  |   0.086509 |
| solution-aron-mark |     0.675237 |       0.116001 |   0.171852 |
| solution-pl        |     0.677057 |       0.115514 |   0.173373 |
| solution-1-flask   |     0.685255 |       1.00955  |   0.268085 |
| solution-1         |     8.85711  |       2e-06    |   0.804036 |
| solution-2         |     4.88363  |       0.572442 |   0.900624 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665917 |       1.00916  |   0.178293 |
| solution-aron-mark |     0.682225 |       0.119494 |   0.265745 |
| solution-pl        |     0.666016 |       0.119519 |   0.266076 |
| solution-1-flask   |     0.681315 |       1.00874  |   0.809171 |
| solution-2         |     0.679349 |       0.469541 |   2.14066  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.662684 |       0.12604  |   0.830114 |
| solution-pl        |     0.70213  |       0.12925  |   0.837579 |
| solution-flask     |     0.669971 |       1.00907  |   0.959498 |
| solution-1-flask   |     0.692173 |       1.00937  |   5.56244  |
| solution-2         |     0.676702 |       0.550542 | 309.568    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.69514  |       0.158832 |    3.56448 |
| solution-aron-mark |     0.681156 |       0.16251  |    3.65187 |
| solution-flask     |     0.682062 |       1.00977  |    6.75551 |