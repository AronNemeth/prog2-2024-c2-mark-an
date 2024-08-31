# 2024-08-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.558526 |       1.00912  |   0.092604 |
| solution-pl        |     0.5913   |       0.104137 |   0.169301 |
| solution-aron-mark |     1.87128  |       0.104007 |   0.170263 |
| solution-1-flask   |     1.19461  |       1.03963  |   0.262361 |
| solution-1         |     7.61164  |       1e-06    |   0.600818 |
| solution-2         |     4.51612  |       0.557572 |   1.09108  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.578293 |       1.00945  |   0.22603  |
| solution-aron-mark |     0.56137  |       0.106033 |   0.298857 |
| solution-pl        |     0.554455 |       0.107308 |   0.332932 |
| solution-1-flask   |     0.568674 |       1.00904  |   0.779283 |
| solution-2         |     0.567715 |       0.483633 |   3.3995   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.560858 |       1.00889  |   0.897147 |
| solution-aron-mark |     0.600842 |       0.115794 |   0.989963 |
| solution-pl        |     0.577539 |       0.115223 |   1.00008  |
| solution-1-flask   |     0.579125 |       1.00942  |   5.5485   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.59899  |       0.143511 |    4.41955 |
| solution-flask     |     0.568148 |       1.00944  |    4.53497 |
| solution-aron-mark |     0.580196 |       0.144682 |    4.83876 |