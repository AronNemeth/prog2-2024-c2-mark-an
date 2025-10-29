# 2025-10-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.92805  |       1.095    |   0.102342 |
| solution-aron-mark |     0.496259 |       0.163039 |   0.246297 |
| solution-pl        |     0.514369 |       0.164841 |   0.248438 |
| solution-1-flask   |     0.499694 |       1.00856  |   0.267723 |
| solution-1         |     8.31369  |       1e-06    |   0.696352 |
| solution-2         |     5.0873   |       0.631358 |   0.99762  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499625 |       0.161751 |   0.373679 |
| solution-aron-mark |     0.497232 |       0.164089 |   0.376719 |
| solution-flask     |     0.505152 |       1.00847  |   0.382087 |
| solution-1-flask   |     0.507051 |       1.00864  |   0.833188 |
| solution-2         |     0.51739  |       0.572462 |   2.25491  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507859 |       0.171676 |    1.0785  |
| solution-pl        |     0.515083 |       0.172767 |    1.08781 |
| solution-flask     |     0.502174 |       1.0089   |    1.5782  |
| solution-1-flask   |     0.526531 |       1.00878  |    5.68524 |
| solution-2         |     0.501073 |       0.578637 |   38.1036  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500182 |       0.203075 |    3.40634 |
| solution-pl        |     0.514028 |       0.210552 |    3.45103 |
| solution-flask     |     0.517657 |       1.00915  |    5.20045 |