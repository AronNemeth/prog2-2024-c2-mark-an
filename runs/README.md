# 2024-04-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.705972 |       1.00945  |   0.068873 |
| solution-aron-mark |     0.691856 |       0.12055  |   0.185284 |
| solution-pl        |     6.48203  |       0.15817  |   0.188565 |
| solution-1-flask   |     1.59896  |       1.09552  |   0.276781 |
| solution-1         |     8.66332  |       1e-06    |   0.646493 |
| solution-2         |     0.703028 |       0.449708 |   1.21772  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.716147 |       1.00945  |   0.165376 |
| solution-aron-mark |     0.706211 |       0.132908 |   0.280723 |
| solution-pl        |     0.689657 |       0.129333 |   0.281037 |
| solution-1-flask   |     0.698768 |       1.00913  |   0.781976 |
| solution-2         |     0.691175 |       0.473078 |  14.6339   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.70269  |       1.00922  |   0.737485 |
| solution-pl        |     0.705033 |       0.137662 |   0.832698 |
| solution-aron-mark |     0.706113 |       0.138532 |   0.8559   |
| solution-1-flask   |     0.725626 |       1.00938  |   5.67038  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664256 |       1.00896  |    2.54198 |
| solution-aron-mark |     0.676361 |       0.172345 |    2.66127 |
| solution-pl        |     0.68472  |       0.172029 |    2.68209 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.665467 |       0.295049 |    16.7662 |
| solution-flask     |     0.664376 |       1.0087   |    17.2204 |
| solution-pl        |     0.665999 |       0.297009 |    17.3067 |