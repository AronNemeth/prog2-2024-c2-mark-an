# 2025-06-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.50127  |       1.00813  |   0.097913 |
| solution-pl        |     0.492741 |       0.146513 |   0.22976  |
| solution-aron-mark |     5.70768  |       0.189473 |   0.231196 |
| solution-1-flask   |     1.11329  |       1.0425   |   0.263882 |
| solution-1         |     7.50156  |       1e-06    |   0.604621 |
| solution-2         |     0.500527 |       0.744824 |   1.05028  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.504351 |       0.150809 |   0.357166 |
| solution-flask     |     0.499644 |       1.00828  |   0.367668 |
| solution-pl        |     0.501587 |       0.160363 |   0.392921 |
| solution-1-flask   |     0.52203  |       1.00851  |   0.785234 |
| solution-2         |     0.497673 |       0.509376 |   3.1989   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.503431 |       0.158894 |    1.05256 |
| solution-pl        |     0.498683 |       0.158027 |    1.05805 |
| solution-flask     |     0.500669 |       1.00842  |    1.55727 |
| solution-1-flask   |     0.506652 |       1.00849  |    5.34455 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.498967 |       0.187209 |    3.17854 |
| solution-pl        |     0.496225 |       0.187098 |    3.20994 |
| solution-flask     |     0.498684 |       1.00847  |    5.03696 |