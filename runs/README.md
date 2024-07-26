# 2024-07-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496978 |       1.00905  |   0.090685 |
| solution-pl        |     5.79576  |       0.10298  |   0.165873 |
| solution-aron-mark |     0.498637 |       0.10298  |   0.169861 |
| solution-1-flask   |     1.18945  |       1.12161  |   0.255935 |
| solution-1         |     7.79787  |       1e-06    |   0.574926 |
| solution-2         |     0.502527 |       0.571762 |   1.34577  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.501639 |       1.00936  |   0.223859 |
| solution-aron-mark |     0.499637 |       0.102664 |   0.28451  |
| solution-pl        |     0.498442 |       0.102605 |   0.296011 |
| solution-1-flask   |     0.503662 |       1.00928  |   0.778376 |
| solution-2         |     0.517133 |       0.485319 |   4.60268  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.497726 |       1.00899  |   0.896384 |
| solution-aron-mark |     0.495039 |       0.113428 |   1.00016  |
| solution-pl        |     0.50656  |       0.110105 |   1.00487  |
| solution-1-flask   |     0.499879 |       1.00917  |   5.57859  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.503526 |       0.148674 |    4.24008 |
| solution-flask     |     0.500144 |       1.00895  |    4.26416 |
| solution-aron-mark |     0.498353 |       0.147185 |    4.28617 |