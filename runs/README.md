# 2026-05-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67579  |       1.05726  |   0.107034 |
| solution-pl        |     0.453825 |       0.155709 |   0.242306 |
| solution-aron-mark |     4.44534  |       0.15389  |   0.245956 |
| solution-1-flask   |     0.45187  |       1.00951  |   0.274416 |
| solution-1         |     8.03959  |       1e-06    |   0.773869 |
| solution-2         |     0.446139 |       0.758939 |   1.0074   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.454807 |       0.15949  |   0.374384 |
| solution-pl        |     0.450668 |       0.154889 |   0.377317 |
| solution-flask     |     0.45298  |       1.00889  |   0.405164 |
| solution-1-flask   |     0.457099 |       1.00843  |   0.827638 |
| solution-2         |     0.458616 |       0.584826 |   5.1025   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.446087 |       0.166731 |    1.12242 |
| solution-pl        |     0.455206 |       0.162621 |    1.1238  |
| solution-flask     |     0.451611 |       1.0086   |    1.73069 |
| solution-1-flask   |     0.455446 |       1.00867  |    5.88638 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434935 |       0.183766 |    3.99081 |
| solution-aron-mark |     0.433517 |       0.18199  |    3.99165 |
| solution-flask     |     0.441545 |       1.00861  |    5.60063 |