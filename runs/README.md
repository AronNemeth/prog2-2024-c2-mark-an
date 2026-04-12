# 2026-04-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.44058  |       1.05918  |   0.094005 |
| solution-aron-mark |     4.60858  |       0.144909 |   0.221087 |
| solution-pl        |     0.407397 |       0.145003 |   0.221504 |
| solution-1-flask   |     0.421796 |       1.00869  |   0.225942 |
| solution-1         |     8.10598  |       1e-06    |   0.569874 |
| solution-2         |     0.408486 |       0.53474  |   0.935984 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.406519 |       0.148202 |   0.327697 |
| solution-pl        |     0.409658 |       0.151271 |   0.337801 |
| solution-flask     |     0.411088 |       1.00867  |   0.374877 |
| solution-1-flask   |     0.428599 |       1.00867  |   0.712464 |
| solution-2         |     0.406516 |       0.507396 |  11.4321   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.409917 |       0.153238 |   0.987824 |
| solution-aron-mark |     0.432369 |       0.153312 |   1.001    |
| solution-flask     |     0.420083 |       1.00906  |   1.53509  |
| solution-1-flask   |     0.413921 |       1.00872  |   5.55488  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.408674 |       0.178899 |    3.54644 |
| solution-aron-mark |     0.405466 |       0.179877 |    3.5558  |
| solution-flask     |     0.40749  |       1.00878  |    4.87984 |