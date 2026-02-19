# 2026-02-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.339    |       1.08471  |   0.104607 |
| solution-aron-mark |     0.440503 |       0.147442 |   0.228459 |
| solution-pl        |     0.438426 |       0.145367 |   0.234063 |
| solution-1-flask   |     0.482218 |       1.0082   |   0.264871 |
| solution-1         |     9.13235  |       1e-06    |   0.607548 |
| solution-2         |     5.97925  |       0.565656 |   0.958109 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.443279 |       0.147615 |   0.360194 |
| solution-pl        |     0.434372 |       0.145739 |   0.360737 |
| solution-flask     |     0.437896 |       1.00838  |   0.380751 |
| solution-1-flask   |     0.444924 |       1.00839  |   0.791196 |
| solution-2         |     0.439162 |       0.493984 |   2.64859  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.43511  |       0.152284 |    1.085   |
| solution-pl        |     0.443205 |       0.153482 |    1.09289 |
| solution-flask     |     0.438363 |       1.00843  |    1.56234 |
| solution-1-flask   |     0.44315  |       1.00824  |    5.50096 |
| solution-2         |     0.435847 |       0.557635 |   34.1537  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.442039 |       0.178681 |    3.68056 |
| solution-aron-mark |     0.439784 |       0.178887 |    3.77521 |
| solution-flask     |     0.433214 |       1.00851  |    5.06711 |