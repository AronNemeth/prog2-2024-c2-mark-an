# 2026-07-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.60426  |       1.00857  |   0.106555 |
| solution-aron-mark |     0.431155 |       0.15041  |   0.23802  |
| solution-pl        |     0.434938 |       0.151609 |   0.239414 |
| solution-1-flask   |     1.46223  |       1.12936  |   0.274929 |
| solution-1         |     8.03963  |       1e-06    |   0.733196 |
| solution-2         |     4.6061   |       0.707501 |   0.942292 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431222 |       0.154917 |   0.366255 |
| solution-aron-mark |     0.440808 |       0.156652 |   0.371868 |
| solution-flask     |     0.432323 |       1.0087   |   0.392372 |
| solution-1-flask   |     0.446156 |       1.00886  |   0.822801 |
| solution-2         |     0.427757 |       0.521244 |   4.6389   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4338   |       0.160007 |    1.10528 |
| solution-aron-mark |     0.436112 |       0.158982 |    1.11293 |
| solution-flask     |     0.431667 |       1.00874  |    1.67413 |
| solution-1-flask   |     0.43493  |       1.00862  |    5.78046 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429293 |       0.185741 |    3.62178 |
| solution-aron-mark |     0.433362 |       0.185412 |    3.63744 |
| solution-flask     |     0.434397 |       1.00849  |    5.40778 |