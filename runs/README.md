# 2026-08-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.76916  |       1.07656  |   0.109065 |
| solution-aron-mark |     4.3199   |       0.152944 |   0.238228 |
| solution-pl        |     0.430643 |       0.156212 |   0.251608 |
| solution-1-flask   |     0.43309  |       1.00849  |   0.272976 |
| solution-1         |     7.69284  |       1e-06    |   0.685381 |
| solution-2         |     0.425857 |       0.698937 |   0.963202 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.425967 |       0.151793 |   0.373435 |
| solution-aron-mark |     0.42987  |       0.155074 |   0.378686 |
| solution-flask     |     0.428991 |       1.00856  |   0.410185 |
| solution-1-flask   |     0.429796 |       1.00875  |   0.809674 |
| solution-2         |     0.426501 |       0.498551 |   2.7262   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429358 |       0.157238 |    1.14169 |
| solution-pl        |     0.430494 |       0.15963  |    1.14968 |
| solution-flask     |     0.425802 |       1.00844  |    1.67525 |
| solution-1-flask   |     0.437485 |       1.00893  |    5.81135 |
| solution-2         |     0.42532  |       0.561283 |  462.708   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.450838 |       0.209437 |    3.84993 |
| solution-aron-mark |     0.454363 |       0.192737 |    3.87305 |
| solution-flask     |     0.45972  |       1.01019  |    5.68075 |