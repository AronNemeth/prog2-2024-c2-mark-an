# 2025-05-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.461963 |       1.00865  |   0.083311 |
| solution-pl        |     0.470983 |       0.120313 |   0.192351 |
| solution-aron-mark |     1.772    |       0.121379 |   0.194659 |
| solution-1-flask   |     1.08928  |       1.0746   |   0.267629 |
| solution-1         |     7.64106  |       1e-06    |   0.633818 |
| solution-2         |     4.61782  |       0.647431 |   1.09266  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482319 |       0.124898 |   0.295141 |
| solution-aron-mark |     0.475343 |       0.12216  |   0.295175 |
| solution-flask     |     0.46741  |       1.0085   |   0.31873  |
| solution-1-flask   |     0.47761  |       1.00881  |   0.802333 |
| solution-2         |     0.464987 |       0.507518 |  12.7647   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.483668 |       0.12908  |   0.891263 |
| solution-pl        |     0.469799 |       0.130441 |   0.898488 |
| solution-flask     |     0.466789 |       1.00878  |   1.24788  |
| solution-1-flask   |     0.476776 |       1.0093   |   5.47412  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.474947 |       0.164556 |    2.85157 |
| solution-aron-mark |     0.478423 |       0.16094  |    2.85176 |
| solution-flask     |     0.467963 |       1.00955  |    4.24003 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.487517 |       0.267824 |    15.9538 |
| solution-aron-mark |     0.476583 |       0.270262 |    16.224  |