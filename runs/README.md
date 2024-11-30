# 2024-11-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.13308  |       1.04454  |   0.108366 |
| solution-aron-mark |     0.557408 |       0.107158 |   0.184177 |
| solution-pl        |     5.77351  |       0.109665 |   0.185357 |
| solution-1-flask   |     0.591414 |       1.00898  |   0.255343 |
| solution-1         |     7.56482  |       1e-06    |   0.905561 |
| solution-2         |     0.556806 |       0.637785 |   1.66456  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.564664 |       0.111504 |   0.300497 |
| solution-aron-mark |     0.56212  |       0.110893 |   0.302192 |
| solution-flask     |     0.570664 |       1.00871  |   0.520684 |
| solution-1-flask   |     0.565094 |       1.00903  |   0.755975 |
| solution-2         |     0.557794 |       0.473778 |   2.48348  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.564171 |       0.116032 |    1.01543 |
| solution-aron-mark |     0.557183 |       0.116216 |    1.0166  |
| solution-flask     |     0.560486 |       1.00953  |    2.21151 |
| solution-1-flask   |     0.569144 |       1.00912  |    5.30251 |
| solution-2         |     0.599305 |       0.525168 |   43.3587  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.563087 |       0.148886 |    4.29602 |
| solution-aron-mark |     0.555808 |       0.150619 |    4.31863 |
| solution-flask     |     0.555823 |       1.00926  |    8.64422 |