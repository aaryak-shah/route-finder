# calculation logging flag
log = False

# available city/station codes
cities = [
  'MUM',
  'DEL',
  'GWL',
  'CHN',
  'KLK',
  'BLR',
  'AMD',
  'HYD',
  'JPR',
  'GWT',
  'VKP'
]

# path costs
costs = [
# JOURNEY TIME IN HOURS:
#----------------------#
#   MUM  DEL  GWL  CHN  KLK  BLR  AMD  HYD  JPR  GWT  VKP
  [   0,  -1,  16,  -1,  -1,  20,   7,  13,  -1,  -1,  -1], # MUM
  [  -1,   0,   5,  -1,  17,  -1,  -1,  -1,   6,  -1,  -1], # DEL
  [  16,   5,   0,  -1,  21,  -1,  -1,  17,  -1,  -1,  -1], # GWL
  [  -1,  -1,  -1,   0,  -1,   6,  -1,  -1,  -1,  -1,  12], # CHN
  [  -1,  17,  21,  -1,   0,  -1,  -1,  -1,  -1,  15,  -1], # KLK
  [  20,  -1,  -1,   6,  -1,   0,  -1,  12,  -1,  -1,  18], # BLR
  [   7,  -1,  -1,  -1,  -1,  -1,   0,  -1,  10,  -1,  -1], # AMD
  [  13,  -1,  17,  -1,  -1,  12,  -1,   0,  -1,  -1,  -1], # HYD
  [  -1,   6,  -1,  -1,  -1,  -1,  10,  -1,   0,  -1,  -1], # JPR
  [  -1,  -1,  -1,  -1,  15,  -1,  -1,  -1,  -1,   0,  -1], # GWT
  [  -1,  -1,  -1,  12,  -1,  18,  -1,  -1,  -1,  -1,   0]  # VKP
]

# heuristic values
heuristics = [
# ESTIMATED HOURS REQUIRED TO COVER STRAIGHT LINE DISTANCE:
#---------------------------------------------------------#
#   MUM  DEL  GWL  CHN  KLK  BLR  AMD  HYD  JPR  GWT  VKP
  [   0,  19,  13,  20,  24,  18,   5,  10,  12,  29,  22], # MUM
  [  19,   0,   4,  30,  11,  22,  10,  19,   4,  18,  37], # DEL
  [  13,   4,   0,  24,  19,  18,  10,  15,   6,  22,  29], # GWL
  [  20,  30,  24,   0,  40,   5,  27,  15,  31,  43,   9], # CHN
  [  24,  11,  19,  40,   0,  29,  24,  22,  20,   9,  41], # KLK
  [  18,  22,  18,   5,  29,   0,  24,  10,  29,  37,  14], # BLR
  [   5,  10,  10,  27,  24,  24,   0,  15,   7,  29,  30], # AMD
  [  10,  19,  15,  15,  22,  10,  15,   0,  19,  32,  18], # HYD
  [  12,   4,   6,  31,  20,  29,   7,  19,   0,  21,  33], # JPR
  [  29,  18,  22,  43,   9,  37,  29,  32,  21,   0,  38], # GWT
  [  22,  37,  19,   9,  41,  14,  30,  18,  33,  38,   0]  # VKP
]

# schedule table
departures = [
# HOURS OF THE DAY WHEN A TRAIN DEPARTS, IN RANGE [0, 24):
#--------------------------------------------------------#
#                 MUM             DEL                     GWL               CHN          KLK                 BLR                  AMD              HYD           JPR      GWT          VKP
  [                (),             (),       (10, 12, 17, 20),               (),          (),     (6, 9, 14, 16), (6, 10, 13, 18, 23),     (2, 17, 19),           (),      (),          ()], # MUM
  [                (),             (), (5, 8, 11, 14, 20, 22),               (), (6, 12, 18),                 (),                  (),              (), (11, 13, 19),      (),          ()], # DEL
  [(3, 6, 10, 15, 23), (6, 7, 12, 17),                     (),               (), (1, 15, 18),                 (),                  (),     (5, 14, 20),           (),      (),          ()], # GWL
  [                (),             (),                     (),               (),          (), (2, 7, 11, 13, 14),                  (),              (),           (),      (), (5, 15, 23)], # CHN
  [                (), (1, 5, 13, 19),             (6, 8, 13),               (),          (),                 (),                  (),              (),           (), (5, 21),          ()], # KLK
  [    (4, 8, 13, 18),             (),                     (), (11, 14, 15, 21),          (),                 (),                  (), (9, 12, 16, 22),           (),      (), (1, 12, 17)], # BLR
  [    (1, 8, 12, 19),             (),                     (),               (),          (),                 (),                  (),              (),  (9, 13, 15),      (),          ()], # AMD
  [       (5, 10, 15),             (),            (6, 15, 23),               (),          (),   (11, 13, 16, 18),                  (),              (),           (),      (),          ()], # HYD
  [                (), (6, 8, 13, 17),                     (),               (),          (),                 (),         (7, 11, 15),              (),           (),      (),          ()], # JPR
  [                (),             (),                     (),               (),    (12, 20),                 (),                  (),              (),           (),      (),          ()], # GWT
  [                (),             (),                     (),      (6, 14, 17),          (),        (7, 14, 16),                  (),              (),           (),      (),          ()]  # VKP
]

# train map
map = r'''
                  ,---------------17-------------[KLK]---15---[GWT]
          6-----[DEL]                            /
         /       \                              /
      [JPR]       5,                           /
       /      ,---[GWL]----------------------21
      /      /       \
    10      16        \
    /      /          17
   /      /            |
 [AMD]   /             |
   |    /              |
   7   /               |
    \ /                |
   [MUM]----------13   |
     \              \  |
      \            ,[HYD]
       20         /
        \        12
         \      /
          \    /                          |     [STATIONS]
           [BLR]-------18-------[VKP]     |    
             |                   /        |      0 - MUM
             6                  /         |      1 - DEL
             |                 /          |      2 - GWL
             |                /           |      3 - CHN
            [CHN]-----------12            |      4 - KLK
                                          |      5 - BLR
                                          |      6 - AMD
  +--------------------------------+      |      7 - HYD
  |  [ABC] = City                  |      |      8 - JPR
  |  --n-- = Journey Time (Hours)  |      |      9 - GWT
  +--------------------------------+      |     10 - VKP
'''