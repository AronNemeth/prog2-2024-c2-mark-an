# 2024-04-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.685569 |       1.009    |   0.065313 |
| solution-pl        |     5.88441  |       0.11372  |   0.165542 |
| solution-aron-mark |     0.683789 |       0.115219 |   0.172103 |
| solution-1-flask   |     1.51464  |       1.08999  |   0.262874 |
| solution-1         |     8.31319  |       1e-06    |   0.784554 |
| solution-2         |     0.667531 |       0.449163 |   0.791016 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661878 |       1.00883  |   0.160609 |
| solution-pl        |     0.667103 |       0.119117 |   0.256153 |
| solution-aron-mark |     0.655514 |       0.117785 |   0.256799 |
| solution-1-flask   |     0.679724 |       1.00913  |   0.771852 |
| solution-2         |     0.695364 |       0.444851 |  13.3562   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658791 |       1.00917  |   0.753866 |
| solution-aron-mark |     0.663105 |       0.126037 |   0.842021 |
| solution-pl        |     0.660293 |       0.12712  |   0.846241 |
| solution-1-flask   |     0.671464 |       1.00952  |   5.67285  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668161 |       1.00913  |    2.58105 |
| solution-aron-mark |     0.670985 |       0.164649 |    3.30715 |
| solution-pl        |     0.659241 |       0.165797 |    3.3992  |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.661504 |        1.00907 |    17.1493 |