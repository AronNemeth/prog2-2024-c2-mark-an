# 2024-11-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2538   |       1.09762  |   0.11299  |
| solution-pl        |     5.93714  |       0.110953 |   0.180038 |
| solution-aron-mark |     0.558999 |       0.109791 |   0.192649 |
| solution-1-flask   |     0.579506 |       1.00955  |   0.262714 |
| solution-1         |     7.84795  |       1e-06    |   0.604463 |
| solution-2         |     0.563841 |       0.524221 |   0.932543 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.577342 |       0.110205 |   0.328443 |
| solution-aron-mark |     0.559865 |       0.109721 |   0.33559  |
| solution-flask     |     0.591092 |       1.00905  |   0.49021  |
| solution-1-flask   |     0.56775  |       1.00909  |   0.768881 |
| solution-2         |     0.569998 |       0.488286 |   2.76266  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.563591 |       0.118137 |    1.01196 |
| solution-pl        |     0.560367 |       0.12012  |    1.02041 |
| solution-flask     |     0.559799 |       1.00908  |    2.13931 |
| solution-1-flask   |     0.571813 |       1.00929  |    5.38842 |
| solution-2         |     0.567621 |       0.529123 |  160.851   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.56042  |       0.145609 |    4.50687 |
| solution-pl        |     0.557439 |       0.1491   |    4.53267 |
| solution-flask     |     0.555831 |       1.0092   |    8.58756 |