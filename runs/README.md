# 2025-11-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.97262  |       1.04267  |   0.103336 |
| solution-aron-mark |     0.49354  |       0.163058 |   0.248402 |
| solution-pl        |     0.484038 |       0.15949  |   0.250781 |
| solution-1-flask   |     0.491466 |       1.00829  |   0.265985 |
| solution-1         |     8.12727  |       1e-06    |   0.713319 |
| solution-2         |     4.9748   |       0.646155 |   0.822953 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.483519 |       0.162425 |   0.370154 |
| solution-pl        |     0.512876 |       0.162691 |   0.375077 |
| solution-flask     |     0.52192  |       1.00858  |   0.377556 |
| solution-1-flask   |     0.482229 |       1.00873  |   0.798633 |
| solution-2         |     0.48684  |       0.526274 |   2.66873  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475979 |       0.164622 |    1.06911 |
| solution-aron-mark |     0.475177 |       0.167286 |    1.07407 |
| solution-flask     |     0.482268 |       1.00886  |    1.57746 |
| solution-1-flask   |     0.477548 |       1.00857  |    5.56192 |
| solution-2         |     0.485856 |       0.58506  |   44.9172  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.495242 |       0.196337 |    3.27566 |
| solution-aron-mark |     0.477183 |       0.196197 |    3.28719 |
| solution-flask     |     0.479517 |       1.00847  |    5.13587 |