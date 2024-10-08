# 2024-10-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.36498  |       1.0663   |   0.083909 |
| solution-pl        |     0.54884  |       0.101213 |   0.175049 |
| solution-aron-mark |     1.90783  |       0.10155  |   0.176006 |
| solution-1-flask   |     0.562648 |       1.00811  |   0.260205 |
| solution-1         |     7.61221  |       1e-06    |   0.68429  |
| solution-2         |     4.43761  |       0.612689 |   1.04445  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.559566 |       1.00822  |   0.230583 |
| solution-pl        |     0.555622 |       0.102379 |   0.30411  |
| solution-aron-mark |     0.554079 |       0.10207  |   0.304844 |
| solution-1-flask   |     0.560037 |       1.0079   |   0.778093 |
| solution-2         |     0.551119 |       0.474106 |   2.61453  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553845 |       1.00796  |   0.933796 |
| solution-aron-mark |     0.550945 |       0.107728 |   1.03344  |
| solution-pl        |     0.549023 |       0.109206 |   1.0398   |
| solution-1-flask   |     0.568698 |       1.00807  |   5.45213  |
| solution-2         |     0.556185 |       0.524277 | 280.516    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55073  |       1.00824  |    4.1081  |
| solution-aron-mark |     0.546339 |       0.137686 |    4.18581 |
| solution-pl        |     0.549557 |       0.138457 |    4.20009 |