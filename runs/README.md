# 2025-07-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.30932  |       1.05307  |   0.101239 |
| solution-aron-mark |     4.36829  |       0.147773 |   0.234863 |
| solution-pl        |     0.494173 |       0.150038 |   0.2359   |
| solution-1-flask   |     0.500813 |       1.00824  |   0.270061 |
| solution-2         |     0.49507  |       0.667819 |   0.934855 |
| solution-1         |     7.49515  |       1e-06    |   1.01455  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.50004  |       0.150444 |   0.359964 |
| solution-pl        |     0.497284 |       0.14899  |   0.363683 |
| solution-flask     |     0.497717 |       1.00836  |   0.37756  |
| solution-1-flask   |     0.502028 |       1.00844  |   0.807095 |
| solution-2         |     0.497406 |       0.498823 |   5.2861   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502751 |       0.156324 |    1.07292 |
| solution-pl        |     0.512636 |       0.157371 |    1.08292 |
| solution-flask     |     0.493028 |       1.00834  |    1.61822 |
| solution-1-flask   |     0.504316 |       1.00849  |    5.72771 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495932 |       0.187295 |    3.20062 |
| solution-pl        |     0.497056 |       0.188484 |    3.20078 |
| solution-flask     |     0.493484 |       1.00838  |    5.11048 |