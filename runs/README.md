# 2025-05-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.05338  |       1.00827  |   0.099557 |
| solution-aron-mark |     0.519191 |       0.152865 |   0.233358 |
| solution-pl        |     0.535449 |       0.167761 |   0.234421 |
| solution-1-flask   |     5.22435  |       1.19568  |   0.272989 |
| solution-1         |     7.91818  |       1e-06    |   0.747966 |
| solution-2         |     0.515073 |       0.72531  |   0.796347 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512023 |       0.153847 |   0.356164 |
| solution-flask     |     0.516426 |       1.00844  |   0.377317 |
| solution-aron-mark |     0.510221 |       0.175905 |   0.378184 |
| solution-1-flask   |     0.523844 |       1.00884  |   0.792892 |
| solution-2         |     0.511062 |       0.536697 |   4.15798  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528494 |       0.173958 |    1.05664 |
| solution-pl        |     0.516083 |       0.166175 |    1.06034 |
| solution-flask     |     0.52509  |       1.00855  |    1.55624 |
| solution-1-flask   |     0.526665 |       1.00862  |    5.43901 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.516317 |       0.190794 |    3.29713 |
| solution-pl        |     0.511512 |       0.193311 |    3.30269 |
| solution-flask     |     0.533305 |       1.00858  |    5.13222 |