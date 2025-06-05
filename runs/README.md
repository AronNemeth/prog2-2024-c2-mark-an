# 2025-06-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.9266   |       1.00843  |   0.10098  |
| solution-aron-mark |     0.498715 |       0.145489 |   0.229402 |
| solution-pl        |     0.509157 |       0.146546 |   0.232991 |
| solution-1-flask   |     5.40919  |       1.09342  |   0.265745 |
| solution-1         |     7.95838  |       1e-06    |   0.724335 |
| solution-2         |     0.49556  |       0.694432 |   0.744212 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.497998 |       0.150153 |   0.351803 |
| solution-pl        |     0.495154 |       0.147888 |   0.356593 |
| solution-flask     |     0.499409 |       1.00852  |   0.373082 |
| solution-1-flask   |     0.510856 |       1.0085   |   0.783758 |
| solution-2         |     0.493121 |       0.497102 |   3.82603  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506154 |       0.159739 |    1.05072 |
| solution-aron-mark |     0.496416 |       0.154609 |    1.05349 |
| solution-flask     |     0.49924  |       1.00832  |    1.55526 |
| solution-1-flask   |     0.500097 |       1.00855  |    5.36047 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.500337 |       0.1879   |    3.21241 |
| solution-aron-mark |     0.498147 |       0.192609 |    3.21406 |
| solution-flask     |     0.495416 |       1.00846  |    5.03167 |