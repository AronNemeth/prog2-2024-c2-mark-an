# 2026-04-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.52631  |       1.02999  |   0.100384 |
| solution-aron-mark |     4.72357  |       0.148023 |   0.230569 |
| solution-pl        |     0.4256   |       0.146462 |   0.233159 |
| solution-1-flask   |     0.41658  |       1.00792  |   0.295906 |
| solution-1         |     8.11552  |       1e-06    |   0.693037 |
| solution-2         |     0.415111 |       0.587351 |   0.937998 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.428776 |       0.146535 |   0.354428 |
| solution-pl        |     0.420074 |       0.149164 |   0.35528  |
| solution-flask     |     0.424588 |       1.00844  |   0.377364 |
| solution-1-flask   |     0.417308 |       1.00837  |   0.795534 |
| solution-2         |     0.413048 |       0.531125 |   2.49347  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431381 |       0.159055 |    1.07355 |
| solution-pl        |     0.417093 |       0.150709 |    1.07726 |
| solution-flask     |     0.421855 |       1.00861  |    1.58043 |
| solution-1-flask   |     0.420813 |       1.00829  |    5.66783 |
| solution-2         |     0.411923 |       0.572543 |   39.5053  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.434266 |       0.177789 |    3.72603 |
| solution-pl        |     0.415281 |       0.178109 |    3.81206 |
| solution-flask     |     0.416818 |       1.00828  |    5.05064 |