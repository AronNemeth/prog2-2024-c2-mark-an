# 2024-11-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.70263  |       1.07727  |   0.120093 |
| solution-pl        |     7.47506  |       0.135179 |   0.210835 |
| solution-aron-mark |     0.668394 |       0.129449 |   0.22149  |
| solution-1-flask   |     0.700802 |       1.01089  |   0.273984 |
| solution-1         |     9.2216   |       2e-06    |   0.939867 |
| solution-2         |     0.724282 |       0.770709 |   1.56623  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.686205 |       0.135595 |   0.334846 |
| solution-pl        |     0.671359 |       0.136003 |   0.335683 |
| solution-flask     |     0.681101 |       1.01107  |   0.540534 |
| solution-1-flask   |     0.720028 |       1.01094  |   0.833972 |
| solution-2         |     0.677161 |       0.562022 |   3.33191  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.700848 |       0.143488 |    1.15824 |
| solution-aron-mark |     0.698896 |       0.147092 |    1.19558 |
| solution-flask     |     0.736001 |       1.01086  |    2.34399 |
| solution-1-flask   |     0.721247 |       1.01131  |    5.88624 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.684078 |       0.181509 |    7.14768 |
| solution-pl        |     0.686312 |       0.17962  |    7.37643 |
| solution-flask     |     0.681439 |       1.01168  |   12.6229  |