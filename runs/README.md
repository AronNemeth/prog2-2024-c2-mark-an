# 2024-11-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30943  |       1.06394  |   0.10672  |
| solution-pl        |     5.65295  |       0.106183 |   0.176017 |
| solution-aron-mark |     0.547632 |       0.103278 |   0.191005 |
| solution-1-flask   |     0.554523 |       1.00878  |   0.256735 |
| solution-1         |     7.54847  |       1e-06    |   0.776205 |
| solution-2         |     0.544422 |       0.643161 |   1.65843  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.551342 |       0.106244 |   0.316925 |
| solution-pl        |     0.547245 |       0.108561 |   0.320985 |
| solution-flask     |     0.564195 |       1.00867  |   0.486735 |
| solution-1-flask   |     0.557966 |       1.00873  |   0.773891 |
| solution-2         |     0.551518 |       0.464526 |   4.17332  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.556006 |       0.122393 |    1.01458 |
| solution-aron-mark |     0.554023 |       0.113062 |    1.01503 |
| solution-flask     |     0.547264 |       1.00879  |    2.14168 |
| solution-1-flask   |     0.561198 |       1.00885  |    5.37856 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.554068 |       0.145809 |    4.13687 |
| solution-aron-mark |     0.549878 |       0.144894 |    4.18726 |
| solution-flask     |     0.548535 |       1.00923  |    8.43592 |