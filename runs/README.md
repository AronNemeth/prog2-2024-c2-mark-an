# 2025-04-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.03352 |       1.00964  |   0.087994 |
| solution-pl        |      1.03479 |       0.125997 |   0.191222 |
| solution-aron-mark |      2.28941 |       0.140273 |   0.207648 |
| solution-1-flask   |      5.52402 |       1.1075   |   0.28494  |
| solution-1         |      7.94995 |       1e-06    |   0.810011 |
| solution-2         |      1.04834 |       0.696423 |   1.10472  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.55307  |       0.13075  |   0.300976 |
| solution-aron-mark |     0.542666 |       0.128716 |   0.301461 |
| solution-flask     |     0.566787 |       1.00994  |   0.315322 |
| solution-1-flask   |     0.918413 |       1.00929  |   0.823033 |
| solution-2         |     0.569565 |       0.576288 |   4.19616  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.58129  |       0.155121 |   0.935594 |
| solution-pl        |     0.551228 |       0.141188 |   0.968213 |
| solution-flask     |     0.584614 |       1.01014  |   1.33726  |
| solution-1-flask   |     0.552292 |       1.00968  |   5.90432  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.549693 |       0.171877 |    3.17448 |
| solution-aron-mark |     0.583146 |       0.17045  |    3.22106 |
| solution-flask     |     0.567031 |       1.00983  |    4.63638 |