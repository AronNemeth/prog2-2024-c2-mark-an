# 2026-06-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19267  |       1.07586  |   0.104901 |
| solution-pl        |     6.76729  |       0.174772 |   0.231612 |
| solution-aron-mark |     0.483866 |       0.192672 |   0.238285 |
| solution-1-flask   |     0.433645 |       1.00811  |   0.266372 |
| solution-1         |     7.85085  |       1e-06    |   0.66497  |
| solution-2         |     0.902642 |       0.632619 |   1.47941  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430889 |       0.151896 |   0.365233 |
| solution-pl        |     0.440946 |       0.15627  |   0.368032 |
| solution-flask     |     0.44087  |       1.00876  |   0.401601 |
| solution-1-flask   |     0.452502 |       1.00838  |   0.806762 |
| solution-2         |     0.429577 |       0.5103   |   2.69513  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426129 |       0.156256 |    1.10092 |
| solution-aron-mark |     0.428766 |       0.15584  |    1.10395 |
| solution-flask     |     0.426929 |       1.00848  |    1.66764 |
| solution-1-flask   |     0.430386 |       1.00848  |    5.71793 |
| solution-2         |     0.426092 |       0.572097 |   38.7937  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436489 |       0.180479 |    3.9056  |
| solution-pl        |     0.433224 |       0.182199 |    3.96908 |
| solution-flask     |     0.430173 |       1.00852  |    5.38565 |