# 2026-08-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     6.68496  |       1.13171  |   0.09485  |
| solution-pl        |     0.378317 |       0.13677  |   0.202952 |
| solution-aron-mark |     4.35026  |       0.135417 |   0.203068 |
| solution-1-flask   |     0.382967 |       1.00661  |   0.216977 |
| solution-2         |     0.378494 |       0.818974 |   0.676884 |
| solution-1         |     6.96554  |       1e-06    |   0.77337  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.380018 |       0.139672 |   0.307979 |
| solution-aron-mark |     0.381041 |       0.138927 |   0.313774 |
| solution-flask     |     0.380918 |       1.00678  |   0.364089 |
| solution-1-flask   |     0.388256 |       1.00697  |   0.689407 |
| solution-2         |     0.383042 |       0.465417 |   4.6509   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.382042 |       0.144225 |   0.969008 |
| solution-pl        |     0.381819 |       0.142418 |   0.974837 |
| solution-flask     |     0.378071 |       1.00703  |   1.5657   |
| solution-1-flask   |     0.381768 |       1.00676  |   5.51075  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.383451 |       0.166842 |    3.81048 |
| solution-pl        |     0.378364 |       0.164793 |    3.84648 |
| solution-flask     |     0.380136 |       1.00688  |    5.13299 |