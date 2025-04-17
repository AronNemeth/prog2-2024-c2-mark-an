# 2025-04-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.503869 |       1.00879  |   0.08432  |
| solution-pl        |     0.506131 |       0.119877 |   0.187614 |
| solution-aron-mark |     1.89762  |       0.119314 |   0.189075 |
| solution-1-flask   |     4.99772  |       1.11343  |   0.269448 |
| solution-1         |     7.5532   |       1e-06    |   0.745821 |
| solution-2         |     0.49832  |       0.707417 |   0.79613  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.507946 |       0.120789 |   0.293207 |
| solution-aron-mark |     0.511258 |       0.120607 |   0.296098 |
| solution-flask     |     0.506035 |       1.00869  |   0.309207 |
| solution-1-flask   |     0.512351 |       1.00886  |   0.811389 |
| solution-2         |     0.5056   |       0.498082 |   4.1113   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507953 |       0.128516 |   0.916913 |
| solution-pl        |     0.522701 |       0.131507 |   0.92873  |
| solution-flask     |     0.523835 |       1.00882  |   1.2574   |
| solution-1-flask   |     0.512324 |       1.00929  |   5.41852  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.507129 |       0.160555 |    2.82962 |
| solution-aron-mark |     0.506805 |       0.16015  |    2.83966 |
| solution-flask     |     0.509727 |       1.00887  |    4.22486 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.503629 |       0.268612 |    17.1152 |
| solution-pl        |     0.516516 |       0.263675 |    17.2601 |