# 2024-06-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.42168  |       1.2266   |   0.10717  |
| solution-aron-mark |     6.47081  |       0.102666 |   0.159279 |
| solution-pl        |     0.663723 |       0.10375  |   0.161918 |
| solution-1-flask   |     0.693212 |       1.0092   |   0.2684   |
| solution-2         |     0.661639 |       0.424049 |   0.795564 |
| solution-1         |     9.07444  |       1e-06    |   0.836959 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664676 |       1.00911  |   0.162487 |
| solution-pl        |     0.673442 |       0.103681 |   0.258368 |
| solution-aron-mark |     0.673097 |       0.104861 |   0.272038 |
| solution-1-flask   |     0.682707 |       1.00948  |   0.841793 |
| solution-2         |     0.66469  |       0.43342  |   3.23286  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.697064 |       1.00944  |   0.707959 |
| solution-pl        |     0.669712 |       0.111818 |   0.82211  |
| solution-aron-mark |     0.670135 |       0.113869 |   0.82496  |
| solution-1-flask   |     0.689475 |       1.00943  |   5.54802  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657978 |       1.00943  |    2.49781 |
| solution-pl        |     0.666744 |       0.15225  |    2.6242  |
| solution-aron-mark |     0.67665  |       0.154548 |    2.65338 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666158 |       1.00936  |    15.8735 |
| solution-aron-mark |     0.666887 |       0.273311 |    20.0901 |
| solution-pl        |     0.663924 |       0.275644 |    21.3085 |