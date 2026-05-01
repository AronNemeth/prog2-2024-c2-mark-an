# 2026-05-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.85224  |       1.04741  |   0.104321 |
| solution-aron-mark |     4.90745  |       0.150643 |   0.229605 |
| solution-pl        |     0.437191 |       0.151144 |   0.23046  |
| solution-1-flask   |     0.419661 |       1.00802  |   0.269255 |
| solution-1         |     8.06772  |       2e-06    |   0.680626 |
| solution-2         |     0.419078 |       0.659323 |   0.894292 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.418873 |       0.146668 |   0.356063 |
| solution-aron-mark |     0.413361 |       0.148725 |   0.360934 |
| solution-flask     |     0.422713 |       1.00829  |   0.397093 |
| solution-1-flask   |     0.417764 |       1.0083   |   0.837041 |
| solution-2         |     0.414025 |       0.509536 |   5.36563  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.43302  |       0.154349 |    1.07513 |
| solution-aron-mark |     0.419569 |       0.154161 |    1.0802  |
| solution-flask     |     0.427628 |       1.00861  |    1.65941 |
| solution-1-flask   |     0.418548 |       1.00831  |    5.55369 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.414834 |       0.176709 |    3.79593 |
| solution-pl        |     0.423463 |       0.176911 |    3.85065 |
| solution-flask     |     0.41908  |       1.00872  |    5.31784 |