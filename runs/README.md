# 2024-09-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19894  |       1.05048  |   0.08421  |
| solution-aron-mark |     1.80014  |       0.10291  |   0.176763 |
| solution-pl        |     0.558622 |       0.103039 |   0.177994 |
| solution-1-flask   |     0.568948 |       1.00818  |   0.266418 |
| solution-1         |     7.50189  |       1e-06    |   0.684329 |
| solution-2         |     4.40807  |       0.657788 |   1.01304  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.559937 |       1.00857  |   0.208647 |
| solution-pl        |     0.566133 |       0.104409 |   0.305315 |
| solution-aron-mark |     0.56112  |       0.105202 |   0.312449 |
| solution-1-flask   |     0.572838 |       1.0087   |   0.781021 |
| solution-2         |     0.58214  |       0.485651 |   2.41858  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568256 |       1.00832  |    0.93721 |
| solution-aron-mark |     0.571894 |       0.112177 |    1.04768 |
| solution-pl        |     0.570673 |       0.111378 |    1.04875 |
| solution-1-flask   |     0.575702 |       1.0087   |    5.50955 |
| solution-2         |     0.567581 |       0.537126 |  297.102   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.571474 |       1.00865  |    4.44197 |
| solution-pl        |     0.567923 |       0.138768 |    4.59679 |
| solution-aron-mark |     0.569623 |       0.140343 |    4.60388 |