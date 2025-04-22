# 2025-04-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.540816 |       1.00898  |   0.085679 |
| solution-aron-mark |     1.96871  |       0.1246   |   0.191241 |
| solution-pl        |     0.535561 |       0.1278   |   0.194576 |
| solution-1-flask   |     5.46232  |       1.09638  |   0.275956 |
| solution-1         |     7.78246  |       1e-06    |   0.795625 |
| solution-2         |     0.527754 |       0.689483 |   1.27329  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.539703 |       1.0097   |   0.300803 |
| solution-pl        |     0.556155 |       0.129948 |   0.303219 |
| solution-aron-mark |     0.542269 |       0.127839 |   0.304218 |
| solution-1-flask   |     0.552751 |       1.00914  |   0.809798 |
| solution-2         |     0.549589 |       0.567997 |   3.81487  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543712 |       0.133337 |   0.923071 |
| solution-aron-mark |     0.548638 |       0.135293 |   0.934498 |
| solution-flask     |     0.55004  |       1.00953  |   1.26521  |
| solution-1-flask   |     0.55233  |       1.00914  |   5.5825   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529744 |       0.166748 |    3.04851 |
| solution-aron-mark |     0.535805 |       0.166203 |    3.07142 |
| solution-flask     |     0.549295 |       1.00909  |    4.53045 |