# 2025-07-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.40494  |       1.2125   |   0.105824 |
| solution-pl        |     0.530468 |       0.160358 |   0.248845 |
| solution-aron-mark |     4.70878  |       0.159127 |   0.249844 |
| solution-1-flask   |     0.527554 |       1.00953  |   0.275954 |
| solution-1         |     7.66714  |       1e-06    |   0.717418 |
| solution-2         |     0.53726  |       0.628798 |   1.13732  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534338 |       0.164545 |   0.373913 |
| solution-pl        |     0.518853 |       0.159091 |   0.386811 |
| solution-flask     |     0.526417 |       1.00948  |   0.395743 |
| solution-1-flask   |     0.524768 |       1.00914  |   0.822978 |
| solution-2         |     0.521904 |       0.523904 |   3.73553  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.539364 |       0.174158 |    1.11699 |
| solution-aron-mark |     0.528856 |       0.171373 |    1.12733 |
| solution-flask     |     0.52104  |       1.00931  |    1.63781 |
| solution-1-flask   |     0.519778 |       1.00985  |    5.97882 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.532202 |       0.205967 |    3.48358 |
| solution-aron-mark |     0.561915 |       0.204086 |    3.49206 |
| solution-flask     |     0.5658   |       1.01007  |    5.62517 |