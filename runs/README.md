# 2025-05-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.95949  |       1.00845  |   0.080719 |
| solution-pl        |     0.493981 |       0.119885 |   0.189826 |
| solution-aron-mark |     0.498856 |       0.1193   |   0.190163 |
| solution-1-flask   |     4.98008  |       1.05339  |   0.270839 |
| solution-1         |     7.47659  |       1e-06    |   0.873571 |
| solution-2         |     0.492421 |       0.729893 |   1.1048   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.49963  |       0.122195 |   0.288227 |
| solution-pl        |     0.493    |       0.122013 |   0.293406 |
| solution-flask     |     0.495358 |       1.00829  |   0.293666 |
| solution-1-flask   |     0.513276 |       1.00848  |   0.794744 |
| solution-2         |     0.50054  |       0.508264 |   4.27614  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494879 |       0.127935 |   0.883923 |
| solution-pl        |     0.497006 |       0.129037 |   0.886806 |
| solution-flask     |     0.50184  |       1.00862  |   1.23247  |
| solution-1-flask   |     0.50032  |       1.00841  |   5.43754  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512005 |       0.161033 |    2.80444 |
| solution-aron-mark |     0.496475 |       0.159998 |    2.81273 |
| solution-flask     |     0.501982 |       1.00842  |    4.25472 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.493809 |       0.268445 |    16.2581 |
| solution-pl        |     0.497964 |       0.267371 |    16.4048 |