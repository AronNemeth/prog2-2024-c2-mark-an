# 2026-03-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67048  |       1.11959  |   0.101958 |
| solution-pl        |     4.69561  |       0.147138 |   0.231338 |
| solution-aron-mark |     0.41602  |       0.148023 |   0.23142  |
| solution-1-flask   |     0.425045 |       1.00817  |   0.268781 |
| solution-1         |     9.07517  |       1e-06    |   0.886622 |
| solution-2         |     0.412772 |       0.764348 |   1.20747  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.419938 |       0.149848 |   0.359333 |
| solution-pl        |     0.418718 |       0.150485 |   0.362071 |
| solution-flask     |     0.420744 |       1.00834  |   0.380779 |
| solution-1-flask   |     0.425011 |       1.00845  |   0.804088 |
| solution-2         |     0.437772 |       0.528094 |   2.55796  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.421977 |       0.153471 |    1.09134 |
| solution-aron-mark |     0.41627  |       0.153025 |    1.0922  |
| solution-flask     |     0.422611 |       1.00844  |    1.59423 |
| solution-1-flask   |     0.444403 |       1.00857  |    5.7734  |
| solution-2         |     0.416374 |       0.601464 |   41.1646  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429585 |       0.182345 |    4.00179 |
| solution-aron-mark |     0.43694  |       0.180851 |    4.00705 |
| solution-flask     |     0.42557  |       1.00876  |    5.27141 |