# 2026-02-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.71017  |       1.07473  |   0.105143 |
| solution-aron-mark |     0.463813 |       0.146843 |   0.240817 |
| solution-pl        |     5.04507  |       0.152444 |   0.242133 |
| solution-1-flask   |     0.46064  |       1.00902  |   0.272563 |
| solution-1         |     8.67705  |       1e-06    |   0.733837 |
| solution-2         |     0.445149 |       0.666194 |   1.35056  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.458852 |       0.151211 |   0.370068 |
| solution-pl        |     0.461489 |       0.15078  |   0.374551 |
| solution-flask     |     0.452733 |       1.00919  |   0.39453  |
| solution-1-flask   |     0.472961 |       1.00901  |   0.819865 |
| solution-2         |     0.439728 |       0.525097 |   2.98891  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.450176 |       0.1535   |    1.12025 |
| solution-pl        |     0.445793 |       0.158272 |    1.12443 |
| solution-flask     |     0.457695 |       1.00883  |    1.64018 |
| solution-1-flask   |     0.459511 |       1.00885  |    5.6688  |
| solution-2         |     0.453098 |       0.582141 |  167.209   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.458122 |       0.185064 |    3.99569 |
| solution-aron-mark |     0.448775 |       0.179383 |    4.02555 |
| solution-flask     |     0.465239 |       1.00908  |    5.25137 |