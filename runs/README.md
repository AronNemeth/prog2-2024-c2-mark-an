# 2026-09-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.07859  |       1.05487  |   0.084388 |
| solution-1-flask   |     0.332892 |       1.00762  |   0.178235 |
| solution-pl        |     1.91208  |       0.124063 |   0.1824   |
| solution-aron-mark |     0.324225 |       0.119899 |   0.18457  |
| solution-1         |     6.08638  |       1e-06    |   0.585026 |
| solution-2         |     4.21304  |       0.573168 |   0.799423 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.327421 |       0.121251 |   0.283005 |
| solution-aron-mark |     0.333405 |       0.122443 |   0.285074 |
| solution-flask     |     0.329749 |       1.00767  |   0.306179 |
| solution-1-flask   |     0.335237 |       1.0077   |   0.558202 |
| solution-2         |     0.33117  |       0.397449 |   1.70948  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.331955 |       0.127826 |   0.817186 |
| solution-aron-mark |     0.332846 |       0.126858 |   0.830887 |
| solution-flask     |     0.331158 |       1.00792  |   1.27506  |
| solution-1-flask   |     0.3347   |       1.00781  |   4.37005  |
| solution-2         |     0.332099 |       0.441648 |  29.4915   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.332007 |       0.163838 |    2.72714 |
| solution-aron-mark |     0.332417 |       0.154054 |    2.7364  |
| solution-flask     |     0.328213 |       1.0078   |    4.03857 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.330094 |       0.227831 |    15.6408 |
| solution-pl        |     0.331628 |       0.278856 |    15.6554 |