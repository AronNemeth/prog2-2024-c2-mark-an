# 2026-11-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.42005  |       1.0105   |   0.09657  |
| solution-pl        |     5.75883  |       0.164773 |   0.247765 |
| solution-aron-mark |     0.415177 |       0.164645 |   0.250097 |
| solution-1-flask   |     1.04606  |       1.20579  |   0.269617 |
| solution-1         |     7.20437  |       1e-06    |   0.583263 |
| solution-2         |     0.412512 |       0.531949 |   0.750164 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.425353 |       1.01065  |   0.231332 |
| solution-aron-mark |     0.418177 |       0.166186 |   0.387578 |
| solution-pl        |     0.425099 |       0.168442 |   0.389811 |
| solution-1-flask   |     0.423569 |       1.01073  |   0.797047 |
| solution-2         |     0.419431 |       0.50857  |   4.43759  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.448241 |       1.01075  |    1.02185 |
| solution-aron-mark |     0.419124 |       0.178842 |    1.13838 |
| solution-pl        |     0.418402 |       0.179197 |    1.14173 |
| solution-1-flask   |     0.429576 |       1.01084  |    5.44446 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420878 |       0.210244 |    3.52111 |
| solution-pl        |     0.420882 |       0.20697  |    3.53423 |
| solution-flask     |     0.419986 |       1.0127   |    4.30435 |