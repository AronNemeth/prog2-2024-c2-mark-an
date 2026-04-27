# 2026-04-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.50744  |       1.06708  |   0.098442 |
| solution-aron-mark |     4.29152  |       0.141922 |   0.225283 |
| solution-pl        |     0.405819 |       0.144215 |   0.228363 |
| solution-1-flask   |     0.410209 |       1.00792  |   0.261012 |
| solution-1         |     7.11204  |       1e-06    |   0.698936 |
| solution-2         |     0.407736 |       0.655788 |   1.64759  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.406378 |       0.146209 |   0.354002 |
| solution-aron-mark |     0.408656 |       0.146469 |   0.355489 |
| solution-flask     |     0.408289 |       1.00804  |   0.386472 |
| solution-1-flask   |     0.413644 |       1.00797  |   0.789429 |
| solution-2         |     0.407789 |       0.503215 |   9.81593  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.405622 |       0.15115  |    1.06119 |
| solution-aron-mark |     0.410639 |       0.152058 |    1.08885 |
| solution-flask     |     0.410111 |       1.00857  |    1.6027  |
| solution-1-flask   |     0.409989 |       1.00837  |    5.57339 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.407581 |       0.174766 |    3.65124 |
| solution-aron-mark |     0.408332 |       0.174382 |    3.7787  |
| solution-flask     |     0.404088 |       1.00857  |    5.18154 |