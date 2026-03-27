# 2026-03-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.44494  |       1.10991  |   0.104543 |
| solution-aron-mark |     0.407561 |       0.144033 |   0.226491 |
| solution-pl        |     4.18766  |       0.143457 |   0.230056 |
| solution-1-flask   |     0.414397 |       1.00792  |   0.262515 |
| solution-1         |     7.80095  |       1e-06    |   0.845069 |
| solution-2         |     0.400874 |       0.624413 |   0.892745 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.408401 |       0.146356 |   0.363258 |
| solution-pl        |     0.414982 |       0.157986 |   0.366921 |
| solution-flask     |     0.405236 |       1.0081   |   0.422332 |
| solution-1-flask   |     0.413521 |       1.0081   |   0.790444 |
| solution-2         |     0.40839  |       0.500621 |   3.10608  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.403895 |       0.149973 |    1.09872 |
| solution-pl        |     0.395207 |       0.149804 |    1.11455 |
| solution-flask     |     0.407659 |       1.00797  |    1.58257 |
| solution-1-flask   |     0.410651 |       1.00812  |    5.87722 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.403624 |       0.177116 |    3.84159 |
| solution-pl        |     0.411408 |       0.176377 |    3.92333 |
| solution-flask     |     0.406384 |       1.00792  |    5.13454 |