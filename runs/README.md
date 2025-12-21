# 2025-12-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.56632  |       1.05761  |   0.097673 |
| solution-aron-mark |     0.471018 |       0.160298 |   0.243774 |
| solution-pl        |     0.475452 |       0.160645 |   0.245126 |
| solution-1-flask   |     0.473794 |       1.00838  |   0.272487 |
| solution-1         |     8.20495  |       1e-06    |   0.797894 |
| solution-2         |     4.54566  |       0.752697 |   1.03275  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.482658 |       0.182291 |   0.366498 |
| solution-pl        |     0.47487  |       0.165336 |   0.373734 |
| solution-flask     |     0.469926 |       1.00866  |   0.374238 |
| solution-1-flask   |     0.476492 |       1.00837  |   0.807866 |
| solution-2         |     0.474879 |       0.510648 |   6.26409  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477536 |       0.168261 |    1.07715 |
| solution-aron-mark |     0.470375 |       0.168144 |    1.07877 |
| solution-flask     |     0.482737 |       1.00868  |    1.57765 |
| solution-1-flask   |     0.471454 |       1.0084   |    5.59828 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470519 |       0.19377  |    3.48508 |
| solution-pl        |     0.471969 |       0.191705 |    3.51274 |
| solution-flask     |     0.472532 |       1.00844  |    5.03706 |