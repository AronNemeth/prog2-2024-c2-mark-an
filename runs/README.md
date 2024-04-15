# 2024-04-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.719223 |       1.0092   |   0.066344 |
| solution-pl        |     5.98207  |       0.117623 |   0.174179 |
| solution-aron-mark |     0.6945   |       0.115179 |   0.175699 |
| solution-1-flask   |     1.39464  |       1.10481  |   0.272306 |
| solution-2         |     0.699366 |       0.459059 |   0.807693 |
| solution-1         |     8.34116  |       1e-06    |   1.02722  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.706009 |       1.00892  |   0.184122 |
| solution-aron-mark |     0.707439 |       0.122726 |   0.263584 |
| solution-pl        |     0.705501 |       0.121124 |   0.263754 |
| solution-1-flask   |     0.723632 |       1.00972  |   0.807452 |
| solution-2         |     0.7031   |       0.474534 |   4.86728  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.703716 |       0.129031 |   0.833646 |
| solution-pl        |     0.714103 |       0.126444 |   0.834134 |
| solution-flask     |     0.708286 |       1.00943  |   0.959658 |
| solution-1-flask   |     0.712743 |       1.00926  |   5.88804  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.705117 |       0.163205 |    3.47743 |
| solution-pl        |     0.702835 |       0.165518 |    3.52249 |
| solution-flask     |     0.706128 |       1.00937  |    6.42884 |