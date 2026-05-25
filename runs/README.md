# 2026-05-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.3631   |       1.06501  |   0.107377 |
| solution-1-flask   |     0.430508 |       1.00863  |   0.226647 |
| solution-aron-mark |     6.06578  |       0.166628 |   0.231272 |
| solution-pl        |     0.424928 |       0.150408 |   0.232867 |
| solution-1         |     8.30296  |       1e-06    |   0.551646 |
| solution-2         |     0.432499 |       0.576072 |   0.889055 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.43024  |       0.14936  |   0.359257 |
| solution-pl        |     0.430261 |       0.151607 |   0.359463 |
| solution-flask     |     0.430762 |       1.00967  |   0.409864 |
| solution-1-flask   |     0.434938 |       1.00868  |   0.713499 |
| solution-2         |     0.428386 |       0.505995 |   2.72044  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431678 |       0.159729 |    1.06384 |
| solution-aron-mark |     0.423804 |       0.156432 |    1.06698 |
| solution-flask     |     0.423089 |       1.00872  |    1.68081 |
| solution-1-flask   |     0.429368 |       1.00873  |    5.52306 |
| solution-2         |     0.433532 |       0.580559 |  179.506   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422417 |       0.182404 |    3.79845 |
| solution-aron-mark |     0.444524 |       0.184125 |    3.80518 |
| solution-flask     |     0.42492  |       1.00892  |    5.28511 |