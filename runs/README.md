# 2024-04-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656954 |       1.00906  |   0.075228 |
| solution-pl        |     5.69289  |       0.126272 |   0.17553  |
| solution-aron-mark |     0.654775 |       0.115139 |   0.181153 |
| solution-1-flask   |     1.40173  |       1.07257  |   0.258949 |
| solution-1         |     8.0295   |       1e-06    |   0.582817 |
| solution-2         |     0.659022 |       0.413697 |   1.17154  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.654664 |       1.00887  |   0.163815 |
| solution-aron-mark |     0.652656 |       0.122338 |   0.289026 |
| solution-pl        |     0.659739 |       0.123788 |   0.29057  |
| solution-1-flask   |     0.672378 |       1.00912  |   0.784783 |
| solution-2         |     0.667794 |       0.424383 |   3.33738  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.652379 |       1.00866  |   0.733047 |
| solution-aron-mark |     0.669751 |       0.129312 |   0.827961 |
| solution-pl        |     0.660471 |       0.129802 |   0.832853 |
| solution-1-flask   |     0.680871 |       1.0091   |   5.56772  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.652396 |       1.00874  |    2.43247 |
| solution-pl        |     0.658896 |       0.164653 |    2.59792 |
| solution-aron-mark |     0.654811 |       0.1648   |    2.60099 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.655632 |       0.293736 |    15.2525 |
| solution-flask     |     0.646092 |       1.00897  |    15.3626 |
| solution-aron-mark |     0.657872 |       0.289964 |    15.5    |