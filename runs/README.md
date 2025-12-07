# 2025-12-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.63352  |       1.1986   |   0.102499 |
| solution-aron-mark |     0.47124  |       0.156336 |   0.245492 |
| solution-pl        |     0.470433 |       0.159491 |   0.246853 |
| solution-1-flask   |     0.478613 |       1.00837  |   0.264623 |
| solution-1         |     7.46978  |       1e-06    |   0.593097 |
| solution-2         |     4.53541  |       0.604255 |   0.900748 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473944 |       0.163133 |   0.376581 |
| solution-pl        |     0.470398 |       0.165733 |   0.379158 |
| solution-flask     |     0.48323  |       1.00829  |   0.383091 |
| solution-1-flask   |     0.472059 |       1.00845  |   0.799515 |
| solution-2         |     0.465396 |       0.504005 |   6.50542  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.468858 |       0.165438 |    1.08913 |
| solution-aron-mark |     0.476407 |       0.164779 |    1.09521 |
| solution-flask     |     0.470193 |       1.0086   |    1.5735  |
| solution-1-flask   |     0.47117  |       1.00861  |    5.55871 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468062 |       0.196601 |    3.2276  |
| solution-pl        |     0.468933 |       0.193977 |    3.23953 |
| solution-flask     |     0.484022 |       1.0086   |    5.05335 |