# 2026-06-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.37515  |       1.15518  |   0.107095 |
| solution-1-flask   |     0.436088 |       1.00875  |   0.229516 |
| solution-aron-mark |     0.431514 |       0.152176 |   0.234547 |
| solution-pl        |     7.41623  |       0.240121 |   0.234766 |
| solution-2         |     0.421772 |       0.759458 |   1.03732  |
| solution-1         |     8.39709  |       1e-06    |   1.08249  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424643 |       0.149778 |   0.3497   |
| solution-pl        |     0.444126 |       0.156161 |   0.355613 |
| solution-flask     |     0.426105 |       1.00883  |   0.395345 |
| solution-1-flask   |     0.425134 |       1.00884  |   0.723612 |
| solution-2         |     0.423133 |       0.505274 |   1.86637  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420248 |       0.157326 |    1.03079 |
| solution-aron-mark |     0.422151 |       0.157253 |    1.03314 |
| solution-flask     |     0.421799 |       1.00891  |    1.64196 |
| solution-1-flask   |     0.424836 |       1.00879  |    5.63995 |
| solution-2         |     0.421028 |       0.567746 |   40.2077  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422044 |       0.183411 |    3.73468 |
| solution-pl        |     0.422302 |       0.182795 |    3.79236 |
| solution-flask     |     0.422245 |       1.00883  |    5.18476 |