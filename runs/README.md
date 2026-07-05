# 2026-07-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.66     |       1.04697  |   0.112685 |
| solution-aron-mark |     0.437544 |       0.152819 |   0.250233 |
| solution-pl        |     6.45564  |       0.178065 |   0.270062 |
| solution-1-flask   |     0.457286 |       1.00828  |   0.274215 |
| solution-1         |     8.08867  |       1e-06    |   0.661376 |
| solution-2         |     0.420654 |       0.663108 |   1.19913  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.449678 |       0.15533  |   0.377358 |
| solution-aron-mark |     0.431035 |       0.15628  |   0.377501 |
| solution-flask     |     0.435331 |       1.00853  |   0.404445 |
| solution-1-flask   |     0.444058 |       1.00845  |   0.825848 |
| solution-2         |     0.434883 |       0.518858 |   5.64332  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432314 |       0.158827 |    1.14604 |
| solution-aron-mark |     0.448159 |       0.159681 |    1.15183 |
| solution-flask     |     0.439743 |       1.00861  |    1.72287 |
| solution-1-flask   |     0.437494 |       1.00886  |    5.86447 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434526 |       0.189341 |    4.14457 |
| solution-aron-mark |     0.445846 |       0.192294 |    4.16424 |
| solution-flask     |     0.444093 |       1.0086   |    5.502   |