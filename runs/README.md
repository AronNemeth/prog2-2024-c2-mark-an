# 2025-02-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.531504 |       1.00876  |   0.081545 |
| solution-pl        |     0.541411 |       0.143431 |   0.20594  |
| solution-aron-mark |     1.78636  |       0.156607 |   0.206182 |
| solution-1-flask   |     5.33005  |       1.05173  |   0.27543  |
| solution-1         |     7.73964  |       1e-06    |   0.605096 |
| solution-2         |     0.534777 |       0.559822 |   1.36464  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.534081 |       1.00904  |   0.28668  |
| solution-aron-mark |     0.536076 |       0.14367  |   0.308163 |
| solution-pl        |     0.530948 |       0.144802 |   0.308368 |
| solution-1-flask   |     0.563794 |       1.00932  |   0.788904 |
| solution-2         |     0.540445 |       0.51125  |  13.7728   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535433 |       0.150734 |   0.903258 |
| solution-pl        |     0.535538 |       0.150953 |   0.905363 |
| solution-flask     |     0.540914 |       1.00893  |   1.24541  |
| solution-1-flask   |     0.550588 |       1.00891  |   5.69326  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.536877 |       0.175029 |    2.8335  |
| solution-aron-mark |     0.535315 |       0.17815  |    2.8605  |
| solution-flask     |     0.53206  |       1.00911  |    4.20419 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529948 |       0.278472 |    17.0661 |
| solution-pl        |     0.528068 |       0.277705 |    17.4968 |