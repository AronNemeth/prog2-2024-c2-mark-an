# 2024-06-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.5515   |       1.07345  |   0.07103  |
| solution-pl        |     0.65462  |       0.10293  |   0.166209 |
| solution-aron-mark |     6.70713  |       0.104515 |   0.168089 |
| solution-1-flask   |     0.707248 |       1.00911  |   0.269432 |
| solution-1         |     8.15703  |       1e-06    |   0.770943 |
| solution-2         |     0.668511 |       0.437392 |   1.12754  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.675274 |       1.00928  |   0.164414 |
| solution-aron-mark |     0.687268 |       0.107486 |   0.25907  |
| solution-pl        |     0.69422  |       0.107774 |   0.262984 |
| solution-1-flask   |     0.677786 |       1.00912  |   0.824987 |
| solution-2         |     0.675687 |       0.44268  |   4.53636  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663805 |       1.00926  |   0.725317 |
| solution-aron-mark |     0.668447 |       0.113984 |   0.815454 |
| solution-pl        |     0.670477 |       0.115495 |   0.826274 |
| solution-1-flask   |     0.676936 |       1.00893  |   5.63552  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668629 |       1.00934  |    2.49328 |
| solution-pl        |     0.662365 |       0.149123 |    2.61444 |
| solution-aron-mark |     0.6891   |       0.152682 |    2.71215 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663322 |       1.00937  |    16.3363 |
| solution-pl        |     0.67191  |       0.276845 |    21.8917 |
| solution-aron-mark |     0.667435 |       0.280308 |    22.813  |